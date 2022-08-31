import os
import json
from tokenize import group
from typing import List


class ConfigManager:

    def __init__(self):
        self.__config_list = self.__read_all_config()

    @staticmethod
    def __read_all_config() -> List[dict]:
        config_list = []
        config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")

        for file_name in os.listdir(config_dir):
            file_type = os.path.splitext(file_name)[1]

            if file_type != ".json":
                continue

            with open(os.path.join(config_dir, file_name), "r", encoding="utf-8") as file:
                config_list.append(json.load(file))
        
        return config_list

    def refresh(self):
        """
        重新读取配置文件
        """
        self.__config_list = self.__read_all_config()

    def get_special_config(self, table: str) -> dict:
        """
        根据表单对应的数据表名来查找表单的配置信息
        :param table: str 数据表名
        :return dict: 表单的配置信息
        """
        if table == "user":
            return self.get_user_config()

        for config_item in self.__config_list:
            if config_item["table"] == table:
                return config_item

        return {}
    
    def get_user_config(self) -> dict:
        return {
            "title": "账号信息",
            "table": "user",
            "show": {
                "param": "name"
            },
            "data": [
                {
                    "name": "姓名",
                    "type": "text",
                    "key": "name",
                    "default": "",
                    "required": True
                },
                {
                    "name": "账号",
                    "type": "text",
                    "key": "username",
                    "default": "",
                    "required": True
                },
                {
                    "name": "密码",
                    "type": "password",
                    "key": "password",
                    "default": "",
                    "required": True
                },
                {
                    "name": "权限",
                    "type": "multiSelect",
                    "key": "auth",
                    "default": [],
                    "optionList": [{
                        "text": item["title"],
                        "value": item["title"]
                    } for item in self.__config_list if "title" in item and "table" in item],
                    "required": True
                }
            ]
        }


    def get_all_config(self):
        return self.__config_list

    def get_all_config_title(self, role: str, auth_list: List[str]):
        
        if role == "root":
            return [
                {
                    "name": "用户管理",
                    "group": [{
                        "name": "账号信息",
                        "url": "/list/user"
                    }]
                },
                {
                    "name": "数据管理",
                    "group": [{
                        "name": item["title"],
                        "url": "/list/" + item["table"]
                    } for item in self.__config_list if "title" in item and "table" in item]
                }
            ]
        elif role == "user":
            return [{
                "name": "数据管理",
                "group": [{
                    "name": item["title"],
                    "url": "/list/" + item["table"]
                } for item in self.__config_list if "title" in item and "table" in item and item["title"] in auth_list]
            }]
    


if __name__ == "__main__":
    config_manager = ConfigManager()
    # print(config_manager.get_all_config())
    print(config_manager.get_user_config())
