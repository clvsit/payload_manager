from typing import List
from loguru import logger

from core.utils.mongo_helper import MongoHelper


class DataManager:

    def __init__(self):
        self.__mongo_helper = MongoHelper()

    def get_data_list(self, table: str, query_param: dict, offset: int, limit: int) -> List[dict]:
        try:
            self.__mongo_helper.choose_collection(table)
            resp = self.__mongo_helper.find(query_param, {"_id": 0,}, "date", offset=offset, limit=limit)

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            return resp["data"]["list"]
        except Exception as error:
            logger.error(f"Failed to get data_list! reason: {error}.")
            return []
