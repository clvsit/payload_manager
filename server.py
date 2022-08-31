import json

from flask import Flask, render_template, request
from flask_cors import CORS
from loguru import logger

from core.config_manager import ConfigManager
from core.data_manager import DataManager
from core.user_manager import UserManager


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app, resources=r'/*')


def init():
    with open("system.json", "r", encoding="utf-8") as file:
        config_dict = json.load(file)
    
    if "database" not in config_dict:
        raise Exception("请在 system.json 配置文件中设置 mongodb 数据库的 url 和 db 字段")
    if "account" not in config_dict:
        account_config = {
            "username": "root",
            "password": "admin"
        }
    else:
        account_config = {
            "username": config_dict["account"].get("username", "root"),
            "password": config_dict["account"].get("password", "admin")
        }

    data_manager = DataManager(db_config=config_dict["database"])
    user_manager = UserManager(account_config, db_config=config_dict["database"])
    config_manager = ConfigManager()

    return config_manager, data_manager, user_manager


config_manager, data_manager, user_manager = init()


@app.route('/', methods=['GET'])
def page_index():
    return render_template("index.html")


@app.route("/api/login", methods=["POST"])
def login():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        username = request_json["username"]
        password = request_json["password"]
        resp = user_manager.login(username, password)

        if resp["code"] != 1:
            return {"code": 0, "msg": resp["msg"], "data": {}}
        else:
            return {"code": 1, "msg": "登录成功！", "data": resp["data"]}
    except Exception as error:
        logger.error(f"Failed to login! reason: {error}")
        return {"code": 0, "msg": "登录失败！", "data": {}}


@app.route("/api/logout", methods=["POST"])
def logout():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        token = request_json["token"]
        is_logout = user_manager.logout(token)

        return {"code": 1, "msg": "注销成功！", "data": {}} if is_logout else {"code": 0, "msg": "注销失败", "data": {}}
    except Exception as error:
        logger.error(f"Failed to logout! reason: {error}")
        return {"code": 0, "msg": "注销失败！", "data": {}}


@app.route("/api/config/list", methods=["POST"])
def get_config_list():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}
    
    request_json = request.json
    check_resp = user_manager.check_login(request_json.get("token"))
    
    if check_resp["code"] == 0:
        return {"code": 0, "msg": check_resp["msg"], "data": check_resp["data"]}

    role = check_resp["data"]["role"]
    auth = check_resp["data"].get("user", {}).get("auth", [])
    config_manager.refresh()
    return {"code": 1, "msg": "获取配置文件内容成功！", "data": {"list": config_manager.get_all_config_title(role, auth)}}


@app.route("/api/config/get", methods=["GET"])
def get_special_config():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    table = request.args.get("table")
    config_dict = config_manager.get_special_config(table=table)
    print(config_dict)
    return {"code": 1, "msg": "获取配置文件内容成功！", "data": {"detail": config_dict}}


@app.route("/data/list", methods=["GET"])
def get_data_list():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        table = request.args.get("table")
        query_param = request.args.get("query", {})
        offset = int(request.args.get("offset", 0))
        limit = int(request.args.get("limit", 10))
        resp = data_manager.get_data_list(table, query_param, offset, limit)
        return {"code": 1, "msg": "获取数据列表成功！", "data": resp}
    except Exception as error:
        logger.error(f"Failed to get_data_list! reason: {error}")
        return {"code": 0, "msg": "获取数据列表失败！", "data": {"list": []}}


@app.route("/data/get", methods=["GET"])
def get_data():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        table = request.args.get("table")
        data_id = request.args.get("id")
        resp = data_manager.get_data(table, data_id)
        return {"code": 1, "msg": "获取数据详情成功！", "data": resp}
    except Exception as error:
        logger.error(f"Failed to get_data! reason: {error}")
        return {"code": 0, "msg": "获取数据详情失败！", "data": {"detail": {}}}


@app.route("/api/<table>/<id>", methods=["GET"])
def api_get_data(table, id):
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        resp = data_manager.get_data(table, id)
        return {"code": 1, "msg": "获取数据详情成功！", "data": resp["detail"]}
    except Exception as error:
        logger.error(f"Failed to get_data! reason: {error}")
        return {"code": 0, "msg": "获取数据详情失败！", "data": {"detail": {}}}


@app.route("/data/add", methods=["POST"])
def add_data():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        table = request_json["table"]
        data = request_json.get("data", {})
        resp = data_manager.add_data(table, data)

        if resp["code"] != 1:
            return {"code": 0, "msg": "添加数据失败！", "data": {}}
        else:
            return {"code": 1, "msg": "添加数据成功！", "data": {"id": resp["id"]}}
    except Exception as error:
        logger.error(f"Failed to add_data! reason: {error}")
        return {"code": 0, "msg": "添加数据失败！", "data": {}}


@app.route("/data/update", methods=["POST"])
def update_data():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        table = request_json["table"]
        data_id = request_json["id"]
        data = request_json.get("data", {})
        is_update = data_manager.update_data(table, data_id, data)

        return {"code": 1, "msg": "修改数据成功！", "data": {}} if is_update else {"code": 0, "msg": "修改数据失败！", "data": {}}
    except Exception as error:
        logger.error(f"Failed to update_data! reason: {error}")
        return {"code": 0, "msg": "修改数据失败！", "data": {}}


@app.route("/data/copy", methods=["POST"])
def copy_data():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        table = request_json["table"]
        data_id = request_json["id"]
        resp_dict = data_manager.copy_data(table, data_id)

        if resp_dict["code"] != 0:
            return {"code": 0, "msg": "复制数据失败！", "data": {}}
        else:
            return {"code": 1, "msg": "复制数据成功！", "data": {"id": resp_dict["id"]}}
    except Exception as error:
        logger.error(f"Failed to copy_data! reason: {error}")
        return {"code": 0, "msg": "复制数据失败！", "data": {}}


@app.route("/data/delete", methods=["POST"])
def delete_data():
    if request.method != "POST":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        request_json = request.json
        table = request_json["table"]
        data_id = request_json["id"]
        is_delete = data_manager.delete_data(table, data_id)

        return {"code": 1, "msg": "删除数据成功！", "data": {}} if is_delete else {"code": 0, "msg": "删除数据失败！", "data": {}}
    except Exception as error:
        logger.error(f"Failed to delete_data! reason: {error}")
        return {"code": 0, "msg": "删除数据失败！", "data": {}}



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6869, debug=True, use_reloader=True)
