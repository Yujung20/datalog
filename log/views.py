import datetime
from django.shortcuts import render
import random
import requests as req
import json

# Create your views here.
def get_log(key):
    current_time = datetime.datetime.now()
    #현재날짜를 long type으로 표현
    timestamp = int(current_time.timestamp() * 1000)

    time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    events= {
        1: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-001',
            'bt_desc': '식품-과일', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        2: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-002',
            'bt_desc': '식품-견과/건과', 'access_type': 'web', 'amount': random.randint(1, 5)},
        3: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-003',
            'bt_desc': '식품-채소', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        4: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-004',
            'bt_desc': '식품-쌀/잡곡', 'access_type': 'web', 'amount': random.randint(1, 5)},
        5: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-005',
            'bt_desc': '식품-생수/음료', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        6: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-006',
            'bt_desc': '식품-건강식품', 'access_type': 'web', 'amount': random.randint(1, 5)},
        7: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-007',
            'bt_desc': '식품-간편요리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        8: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-008',
            'bt_desc': '식품-간편식', 'access_type': 'web', 'amount': random.randint(1, 5)},
        9: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-009',
            'bt_desc': '식품-유제품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        10: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-001',
             'bt_desc': '생활용품-헤어', 'access_type': 'web', 'amount': random.randint(1, 5)},
        11: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-002',
             'bt_desc': '생활용품-바디/세안', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        12: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-003',
             'bt_desc': '생활용품-세탁세제', 'access_type': 'web', 'amount': random.randint(1, 5)},
        13: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-004',
             'bt_desc': '생활용품-건강', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        14: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-005',
             'bt_desc': '생활용품-수납/정리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        15: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-006',
             'bt_desc': '생활용품-안전', 'access_type': 'web', 'amount': random.randint(1, 5)},
        16: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-007',
             'bt_desc': '생활용품-생활잡화', 'access_type': 'web', 'amount': random.randint(1, 5)},
        17: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-001',
             'bt_desc': '뷰티-헤어', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        18: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-002',
             'bt_desc': '뷰티-향수', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        19: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-003',
             'bt_desc': '뷰티-남성화장품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        20: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-004',
             'bt_desc': '뷰티-여성화장품', 'access_type': 'web', 'amount': random.randint(1, 5)},
    }
    return events.get(key,"out of bound")

def log_index(request):
    return render(request, "log_index.html")

def log_gen_i(request):
    return render(request, "log_gen_i.html")

def btn_gen_i_click(request, product_id):
    #1~20번 물품을 구매한 정보를 api gw로 전달
    data =get_log(product_id)
    # endpoint_url="https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version1"

    stream_name = "yj_ver2_ki_product"
    endpoint_url=f"https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

    json_data = json.dumps(data)    #dumps() 안에는 딕셔너리 형태가 들어가야 함
    resp = req.post(endpoint_url, data = json_data, headers={"Content-Type":"application/json"})
    print("yj_ver2_ki_product",resp.text)

    #stream_name = "yj_ver2_ki_app"
    #endpoint_url = f"https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

    #json_data = json.dumps(data)  # dumps() 안에는 딕셔너리 형태가 들어가야 함
    #resp = req.post(endpoint_url, data=json_data, headers={"Content-Type": "application/json"})
    #print("yj_ver2_ki_app",resp.text)

    return render(request, "log_gen_i.html")

def log_gen_ii(request):
    return render(request,"log_gen_ii.html")

def btn_gen_ii_click(request):
    if request.method == "POST" :

        current_time = datetime.datetime.now()
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = request.POST["userid"]
        servicemenu=request.POST["servicemenu"]
        stars = request.POST["stars"]
        accesstype= request.POST["accesstype"]
        reserv = request.POST["reserv"]

        form_data={
            "time": str(time),
            "user_id": str(user_id),
            "state": str(servicemenu),
            "stars": str(stars),
            "accesstype": str(accesstype),
            "reserv": str(reserv),
        }

        # Send to API GW
        # Form data : content type(application/x-www-form-urlencoded)
        stream_name = "yj_ver2_ki_saas_stream"
        endpoint_url = f"https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

        resp = req.post(
            endpoint_url,
            data = form_data,
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        )

        print(resp.text)

    return render(request, "log_gen_ii.html")

