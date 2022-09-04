import traceback
import uuid
import json
from loguru import logger

from core.utils.mongo_helper import MongoHelper
from core.utils.date_helper import DateHelper


class DataManager:

    def __init__(self, db_config: dict):
        self.__mongo_helper = MongoHelper(url=db_config["url"], db_name=db_config["db"])

    def get_data_list(self, table: str, query_param: dict, offset: int, limit: int) -> dict:
        try:
            query_param = json.loads(query_param)
            self.__mongo_helper.choose_collection(table, is_force=True)
            resp = self.__mongo_helper.find(query_param, {"_id": 0}, "date", offset=offset, limit=limit)

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return resp["data"]
        except Exception as error:
            logger.error(f"Failed to get data_list! reason: {error}.")
            return []
    
    def get_data(self, table: str, data_id: str) -> dict:
        try:
            self.__mongo_helper.choose_collection(table, is_force=True)
            resp = self.__mongo_helper.find({"id": data_id}, {"_id": 0}, "date")

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return {"detail": resp["data"]["list"][0]}
        except Exception as error:
            logger.error(f"Failed to get data_list! reason: {error}.")
            return {}

    def add_data(self, table: str, data: dict, config_dict: dict, user: dict) -> dict:
        """
        添加数据到数据库
        :param table:       str  数据表名
        :param data:        dict 存入数据库的数据字典
        :param config_dict: dict 存入数据库的配置字典
        :param user:        dict 用户信息
        :return dict 添加操作的返回结果字典
        """
        try:
            self.__mongo_helper.choose_collection(table, is_force=True)
            date = DateHelper.get_today2string()
            new_id = str(uuid.uuid4())
            resp = self.__mongo_helper.insert({
                "id": new_id,
                "date": {
                    "create": date,
                    "modify": date
                },
                "user": {
                    "create": user["name"],
                    "modify": user["name"]
                },
                "data": data,
                "config": config_dict
            })

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return {"code": 1, "id": new_id}
        except Exception as error:
            logger.error(traceback.format_exc())
            logger.error(f"Failed to add data! reason: {error}.")

    def update_data(self, table: str, data_id: str, data: dict, config_dict: dict, user: dict) -> bool:
        """
        修改数据
        :param table:       str  数据表名
        :param data_id:     str  当前数据的 ID
        :param data:        dict 存入数据库的数据字典
        :param config_dict: dict 存入数据库的配置字典
        :param user:        dict 用户信息
        :return dict 添加操作的返回结果字典
        """
        try:
            self.__mongo_helper.choose_collection(table)
            resp = self.__mongo_helper.update({"id": data_id}, {
                "date.modify": DateHelper.get_today2string(),
                "user.modify": user["name"],
                "data": data,
                "config": config_dict
            })

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return True
        except Exception as error:
            logger.error(traceback.format_exc())
            logger.error(f"Failed to update data! reason: {error}.")

    def copy_data(self, table: str, data_id: str) -> dict:
        """
        拷贝数据
        """
        try:
            data = self.get_data(table, data_id).get("detail", {})
            self.__mongo_helper.choose_collection(table, is_force=True)
            date = DateHelper.get_today2string()
            new_id = str(uuid.uuid4())
            resp = self.__mongo_helper.insert({
                "id": new_id,
                "date": {
                    "create": date,
                    "modify": date
                },
                "data": data.get("data", {})
            })

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return {"code": 1, "id": new_id}
        except Exception as error:
            logger.error(traceback.format_exc())
            logger.error(f"Failed to copy data! reason: {error}.")

    def delete_data(self, table: str, data_id: str) -> bool:
        try:
            self.__mongo_helper.choose_collection(table)
            resp = self.__mongo_helper.delete({"id": data_id})

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return True
        except Exception as error:
            logger.error(traceback.format_exc())
            logger.error(f"Failed to delete data! reason: {error}.")
