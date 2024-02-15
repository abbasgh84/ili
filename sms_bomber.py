import requests
import time
number =input("Enter The NUmber : ")

url ='https://ws.alibaba.ir/api/v3/account/mobile/otp'
json ={"phoneNumber":number}


for i in range(10):
    a =requests.post(url=url , json=json)
    print(a)
    time.sleep(5)