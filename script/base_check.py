

from script.abs_check import Checker


class BaseChecker(Checker):

    def __init__(self):
        super(BaseChecker, self).__init__()
    
    def check(input_data: dict) -> dict:
        report_list = []

        for key, value in input_data.items():
            if value == "":
                report_list.append(f"{key} 字段为必填项，不得为空.")
        
        if len(report_list) > 0:
            return {"code": 0, "result": report_list}
