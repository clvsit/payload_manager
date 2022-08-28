import os
import json
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

    def get_special_config(self, title: str) -> dict:
        for config_item in self.__config_list:
            if config_item["title"] == title:
                return config_item

        return {}

    def get_all_config(self):
        return self.__config_list
    
    def get_all_config_title(self):
        return [{
            "title": item["title"],
            "table": item["table"]
        } for item in self.__config_list if "title" in item and "table" in item]
    


if __name__ == "__main__":
    config_manager = ConfigManager()
    print(config_manager.get_all_config())
    print(config_manager.get_all_config_title())
