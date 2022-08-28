from flask import Flask, render_template, request
from flask_cors import CORS
from loguru import logger

from core.config_manager import ConfigManager
from core.data_manager import DataManager


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app, resources=r'/*')
config_manager = ConfigManager()
data_manager = DataManager()


@app.route('/', methods=['GET'])
def page_index():
    return render_template("index.html")


@app.route("/config/list", methods=["GET"])
def get_config_list():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    config_manager.refresh()
    return {"code": 1, "msg": "获取配置文件内容成功！", "data": {"list": config_manager.get_all_config_title()}}


@app.route("/config/get", methods=["GET"])
def get_special_config():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    title = request.args.get("title")
    config_dict = config_manager.get_special_config(title=title)
    return {"code": 1, "msg": "获取配置文件内容成功！", "data": {"detail": config_dict}}


@app.route("/data/list", methods=["GET"])
def get_data_list():
    if request.method != "GET":
        return {"code": 0, "msg": "请求的方法有误！", "data": {}}

    try:
        table = request.args.get("table")
        query_param = request.args.get("query", {})
        offset = request.args.get("offset", 0)
        limit = request.args.get("limit", 10)
        data_list = data_manager.get_data_list(table, query_param, offset, limit)
        return {"code": 1, "msg": "获取数据列表成功！", "data": {"list": data_list}}
    except Exception as error:
        logger.error(f"Failed to get_data_list! reason: {error}")
        return {"code": 0, "msg": "获取数据列表失败！", "data": {"list": []}}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6869, debug=True, use_reloader=True)
