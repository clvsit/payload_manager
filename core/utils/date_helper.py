import datetime
from typing import Union


class DateHelper:

    def __init__(self):
        pass

    @staticmethod
    def get_today2string(date_format: str = "%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.now().strftime(date_format)

    @staticmethod
    def convert_datetime2string(date: datetime.datetime, date_format: str = "%Y-%m-%d %H:%M:%S"):
        return date.strftime(date_format)

    @staticmethod
    def convert_string2datetime(date_str: str, date_format: str = "%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.strptime(date_str, date_format)

    @staticmethod
    def change_datetime(date: Union[str, datetime.datetime], date_format: str = "%Y-%m-%d %H:%M:%S") -> str:
        if type(date) == str:
            return datetime.datetime.strptime(date, date_format).strftime(date_format)
        elif type(date) == datetime.datetime:
            return date.strftime(date_format)
        else:
            return date

    @staticmethod
    def date_calculate(date: str or datetime.datetime, days: int):
        if type(date) == str:
            date = DateHelper.convert_string2datetime(date)

        return date + datetime.timedelta(days=days)

    @staticmethod
    def split_date_area_by_interval(start_date: str, end_date: str, interval: int, out_format: str = "str"):
        if type(start_date) == str:
            start_date = DateHelper.convert_string2datetime(start_date)
        if type(end_date) == str:
            end_date = DateHelper.convert_string2datetime(end_date)

        diff_days = (end_date - start_date).days
        area_number, remain_days = divmod(diff_days, interval)
        date_area_list = []

        for idx in range(area_number):
            temp_end_date = DateHelper.date_calculate(start_date, interval)

            date_area_list.append({
                "start_date": start_date,
                "end_date": temp_end_date
            })
            start_date = temp_end_date

        date_area_list.append({
            "start_date": start_date,
            "end_date": end_date
        })

        if out_format == "str":
            for date_area in date_area_list:
                date_area["start_date"] = DateHelper.convert_datetime2string(date_area["start_date"])
                date_area["end_date"] = DateHelper.convert_datetime2string(date_area["end_date"])

        return date_area_list


if __name__ == '__main__':
    date_helper = DateHelper()
    print(date_helper.split_date_area_by_interval("2022-01-01 00:00:00", date_helper.get_today2string(), 30))
