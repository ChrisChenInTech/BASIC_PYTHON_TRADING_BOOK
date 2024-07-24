#################################
# 登入Shioaji
####################################
import shioaji as sj
import pandas as pd
from time import sleep
import datetime
import sqlite3

api = sj.Shioaji(simulation=False)
person_id = ''  # 你的身分證字號
passwd = ''  # 你的永豐證券登入密碼
if (person_id == ''):
    person_id = input("Please input ID:\n")
if (passwd == ''):
    passwd = input("Please input PASSWORD:\n")
api.login(
    person_id=person_id,
    passwd=passwd,
    contracts_timeout=10000,
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)
