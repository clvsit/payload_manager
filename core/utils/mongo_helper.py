from typing import Union, List

import pymongo
from loguru import logger


class MongoHelper:
    
    def __init__(self):
        user = "root"
        pwd = "admin"
        config = {"host": "124.220.9.36", "port": "27017", "db_name": "admin"}
        client = pymongo.MongoClient(f"mongodb://{user}:{pwd}@{config['host']}:{config['port']}/")
        
        # db_list = client.list_database_names()
        db_name = config["db_name"]
        # self.__db_obj = client[db_name] if db_name in db_list else None
        self.__db_obj = client[db_name]
        self.__col = None

    def list_collection(self) -> List[str]:
        return [item for item in self.__db_obj.list_collection_names()]

    def choose_collection(self, collection_name: str, is_force: bool = False) -> dict:
        """
        选择集合
        :param collection_name: str  集合名称
        :param is_force:        bool 当集合不存在时，是否强制使用（创建）
        :return dict 操作结果字典
        """
        col_list = self.__db_obj.list_collection_names()

        if not is_force and collection_name not in col_list:
            return {"code": 0, "msg": f"The collection {collection_name} is not existed!"}
        
        self.__col = self.__db_obj[collection_name]
        return {"code": 1, "msg": f"choose collection {collection_name} successfully!"}

    def drop_collection(self) -> dict:
        """
        删除集合
        :return dict 删除集合操作的结果字典
        """
        if self.__col is None:
            return {"code": 1, "msg": "Please call choose_collection() to select the collection before deleting."}

        try:
            self.__col.drop()
            return {"code": 1, "msg": "success!"}
        except Exception as error:
            logger.error(f"Failed to drop collection! reason: {error}")
            return {"code": 0, "msg": "failed!"}

    def find(self, param: dict, filter_param: dict, sort_key: str = None, sort_method: int = -1, offset: int = 0,
             limit: int = 10) -> dict:
        """
        检索数据
        :param param:        dict 检索条件字典
        :param filter_param: dict 过滤条件字典
        :param sort_key:     str  排序字段
        :param sort_method:  int  排序方式，1 升序；-1 降序；默认为 -1 降序
        :param offset:       int  起始位置
        :param limit:        int  查询数量
        """
        try:
            """
            limit == -1：查询所有数据
            """

            if limit == -1:
                result_iter = self.__col.find(param, filter_param)
            else:
                result_iter = self.__col.find(param, filter_param).skip(offset).limit(limit)

            if sort_key:
                result_iter = result_iter.sort(sort_key, sort_method)

            count = self.__col.count_documents(param)
            return {"code": 1, "msg": "success!", "data": {"list": [item for item in result_iter], "count": count}}
        except Exception as error:
            logger.error(f"Failed to find data by {param}! reason: {error}")
            return {"code": 0, "msg": "failed!", "data": {}}

    def insert(self, data: Union[dict, List]):
        if type(data) == dict:
            data = [data]

        try:
            result_dict = self.__col.insert_many(data)
            return {"code": 1, "msg": "success!"}
        except Exception as error:
            logger.error(f"Failed to insert data! reason: {error}")
            return {"code": 0, "msg": "failed!", "data": {}}

    def update(self, param: dict, data: dict):
        try:
            self.__col.update_many(param, {"$set": data})
            return {"code": 1, "msg": "success!"}
        except Exception as error:
            logger.error(f"Failed to update data! reason: {error}")
            return {"code": 0, "msg": "failed!", "data": {}}

    def delete(self, param: dict, number: int = -1):
        try:
            if number == -1:
                result = self.__col.delete_many(param)
                return {"code": 1, "msg": "success!", "data": {"count": result.deleted_count}}
            else:
                for idx in range(number):
                    self.__col.delete_one(param)
                return {"code": 1, "msg": "success!", "data": {"count": number}}
        except Exception as error:
            logger.error(f"Failed to delete data by {param}! reason: {error}")
            return {"code": 0, "msg": "failed!", "data": {}}
