import mysql.connector
import time
from Helpers.Settings import Settings

print("DB起動待ち....")
time.sleep(10) # MySQL起動待ち

# 設定取得
try:
    db_host = Settings.get("DATBASE_HOST")
    db_user = Settings.get('DATABASE_USER')
    db_password = Settings.get('DATABASE_PASSWORD')
    db_port = Settings.get_int("DATABASE_PORT")
    db_name = Settings.get("DATABASE_NAME")
except Exception as e:
    print("設定取得エラー：" , e)
    exit()

# DB接続・SQL
try:
    cnx = mysql.connector.connect(
        user = db_user,
        password = db_password,
        host = db_host,
        port = db_port
    )

    cursor = cnx.cursor()
    cursor.execute(f'SELECT * FROM {db_name}.users')

    for id, name in cursor:
        print(f'{id}, {name}')
except Exception as e:
    print("DBエラー:" , e)

