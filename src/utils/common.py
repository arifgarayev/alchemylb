import time
import json
from datetime import datetime as dt
import datetime
import os


class Utils:
    @staticmethod
    def get_json_to_dict(path):
        file = open(os.getcwd() + path)
        return json.load(file)

    @staticmethod
    def get_date_today():
        return dt.now().strftime("%d-%m-%Y")

    @staticmethod
    def get_time_now():
        return dt.now().strftime("%H:%M")

    @staticmethod
    def last_checked(file, mode="r", data=None):
        if mode == "r":
            file = open(os.getcwd() + file, "r")
            return file.readline()

        if mode == "w" and data:
            file = open(os.getcwd() + file, "w")
            file.write(data)

    # Add db stuff here
