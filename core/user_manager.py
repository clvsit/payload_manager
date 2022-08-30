import uuid

from loguru import logger

from core.utils.mongo_helper import MongoHelper


class UserManager():

    def __init__(self, account_dict: dict, db_config: dict):
        self.__root_account = account_dict
        self.__mongo_helper = MongoHelper(url=db_config["url"], db_name=db_config["db"])
        self.__session_pool = {}  # 会话池：记录当前的登录信息

    def login(self, username: str, password: str) -> dict:
        token = str(uuid.uuid4())

        if username == self.__root_account["username"] and password == self.__root_account["password"]:
            self.__session_pool[token] = {"role": "root", "token": token}
            return {"code": 1, "msg": "", "data": {"role": "root", "token": token}}

        try:
            self.__mongo_helper.choose_collection("user", is_force=True)
            resp = self.__mongo_helper.find({"data.username": username, "data.password": password}, {"_id": 0}, "date")

            if resp["code"] != 1:
                raise Exception(resp["msg"])
            
            if len(resp["data"]["list"]) > 0:
                self.__session_pool[token] = {"role": "user", "token": token, "user": resp["data"]["list"][0]["data"]}
                return {"code": 1, "msg": "", "data": {"role": "user", "token": token, "user": resp["data"]["list"][0]}}
            else:
                return {"code": 0, "msg": "账号或密码验证失败 ，请重新输入"}
        except Exception as error:
            raise Exception(str(error))
    
    def logout(self, token: str) -> bool:
        """
        注销当前账号
        :param token: str 待注销账号的 token 信息
        :return bool 注销操作的执行情况
        """
        try:
            del self.__session_pool[token]
            return True
        except Exception as error:
            raise Exception(str(error))

    def check_login(self, token: str) -> dict:
        """
        检查登录状态
        :param token: str token 信息
        :return dict 检查结果字典
        """
        if token not in self.__session_pool:
            return {"code": 0, "msg": "当前用户未登录，请重新登录", "data": {"status": 0}}
        
        print(self.__session_pool[token])
        return {"code": 1, "msg": "", "data": {**self.__session_pool[token], "status": 1}}