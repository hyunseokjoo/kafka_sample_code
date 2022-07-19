"""
@author : 주현석
@date : 2022.07.18
@description : Order에 dummy 데이터 보내는 producer입니다.
"""

from kafka import KafkaProducer 
import datetime, pytz, time, random, json 

TOPIC_NAME = "order"
brokers = ["localhost:9092"]
producer = KafkaProducer(bootstrap_servers=brokers)

def get_time_date():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    kst_now = utc_now.astimezone(pytz.timezone("Asia/Seoul"))
    d = kst_now.strftime("%m/%d/%Y")
    t = kst_now.strftime("%H:%M:%S")
    return d, t

def generate_order_data():
    customer_type = random.choice([0, 1, 2])
    category = random.choice([0, 1, 2])
    menu = random.choice([0, 1, 2])

    dic_customer_type = ["BRONZE", "SILVER", "PLATINUM"]

    dic_menu = [
        ["Classic Burger", "Bigmac Burger", "Sanghai Burger"],
        ["Franch Fries","Coleslaw", "Cheese Sticks"],
        ["McFlurry", "Strawberry Cone", "vanilla shake"]
    ]

    dic_price = [
        [5000, 6000, 7000],
        [3000, 2000, 2000],
        [4000, 2000, 4000]
    ]

    dic_discount = [1.0, 0.9, 0.8]

    choiced_customer_type = dic_customer_type[customer_type]
    choiced_menu = dic_menu[category][menu]
    choiced_price = dic_price[category][menu] * dic_discount[customer_type]

    return choiced_customer_type, choiced_menu, choiced_price


while True:
    d, t = get_time_date()
    choiced_customer_type, choiced_menu, choiced_price  = generate_order_data()
    new_data = {
        "DATE" : d,
        "TIME" : t,
        "CUSTOMER_TYPE" : choiced_customer_type,
        "MENU" : choiced_menu,
        "PRICE" : choiced_price,
    }

    producer.send(TOPIC_NAME, json.dumps(new_data).encode("utf-8"))
    print(new_data)
    time.sleep(1)