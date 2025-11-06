import base64
import json
import mysql.connector

def lambda_handler(event, context):
    db_config = {
        "user":"admin",
        "password":"abcd1234!",
        "host":"lgu8-jjj.cbq46w2gwwum.ap-northeast-2.rds.amazonaws.com",
        "database":"yj_logdata",

    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for record in event["Records"]:
        record_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        data = json.loads(record_data)

        if data["reserv"] == "yes":
            strSql = """
                INSERT INTO saas_log (time, user_id, servicemenu, stars, accesstype, reserv)
                VALUES (%s, %s, %s, %s, %s, %s);            
            """

            values = (
                data["time"],
                data["user_id"],
                data["state"],
                data["stars"],
                data["accesstype"],
                data["reserv"],
            )

            cursor.execute(strSql, values)
            connection.commit()

    cursor.close()
    connection.close()

    return {
        "return_code" : 200,
    }



