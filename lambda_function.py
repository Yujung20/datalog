from bs4 import BeautifulSoup
import mysql.connector
import requests as req
import json

def lambda_handler(event, context):
    db_config = {
        "user": "admin",
        "password": "tada1212!",
        "host": "tada-db.cbq46w2gwwum.ap-northeast-2.rds.amazonaws.com",
        "database": "yu-lgu8-master",
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    url = "https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade?"

    for pageNo in range(1, 5):

        params = {
            "serviceKey": "1734045136945fd09f5d1ab9cc5a652b6c4b01c6c6205ffaa3a6acbb55376a05",
            "LAWD_CD": "11110",
            "DEAL_YMD": "202501",
            "pageNo": str(pageNo),
            "num0fRows": "20",

        }
        resp = req.get(url, params=params)

        decoded_data = resp.content.decode("utf-8")  # 한글 안 깨지게 함

        # decoded_data에 대한 parser 만들기
        # - 특정 Tag값을 추출
        # - DB에 저장

        # 1. Dom tree 구성하기
        soup = BeautifulSoup(decoded_data, "xml")

        # "<item>" 태그들만 모두 찾기
        items = soup.find_all("item")

        for index, item in enumerate(items):
            try:
                apt_name = item.find("aptNm").text
                # item.find("aptNm")은 object형태임
                build_year = item.find("buildYear").text
                deal_amount = item.find("dealAmount").text
                deal_day = item.find("dealDay").text
                deal_month = item.find("dealMonth").text
                deal_year = item.find("dealYear").text
                exclu_usearea = item.find("excluUseAr").text
                floor = item.find("floor").text
                land_leaseholdgbn = item.find("landLeaseholdGbn").text
                sgg_cd = item.find("sggCd").text
                umd_nm = item.find("umdNm").text
                try:
                    # DB입력
                    strSql = """
                                    INSERT INTO apt_cost (apt_name, build_year, deal_amount, deal_day, deal_month, deal_year, exclu_usearea, floor, land_leaseholdgbn, sgg_cd, umd_nm)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);         
                                """
                    data = (
                        apt_name, build_year, deal_amount, deal_day, deal_month, deal_year, exclu_usearea, floor,
                        land_leaseholdgbn, sgg_cd, umd_nm
                    )

                    cursor.execute(strSql, data)
                    connection.commit()
                    print("Success save")
                except mysql.connector.Error as e:
                    print(e)
            except Exception as err:
                print(err)

    if connection.is_connected():
        cursor.close()
        connection.close()


    return {
            "status_code" : 200,
            "body":json.dumps("open api : finish apt_cost lambda function!!!")
        }



