import os
import sqlite3
import sys


class Repo:
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    def get_last_log(self):
        res = self.cur.execute("SELECT km FROM last_checked_log WHERE id = 1;")
        return res.fetchall()

    def append_active_log(self, km):
        self.cur.execute(
            f"""
            UPDATE last_checked_log SET km = {float(km)} WHERE id = 1;
        """
        )

        self.con.commit()

        return self

    # self.cur.execute("SELECT km FROM last_checked_log;")


if __name__ == "__main__":
    import sys

    r = Repo(sys.path[1] + "/log/last")

    print(r.append_active_log(float(25.0)))
