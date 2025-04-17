# -- coding: utf-8 --
#multipart/form-data 格式传图像，json传文本
#本地图像
import requests
url = "http://i-1.gpushare.com:21533/detect"
urllocal = "http://127.0.0.1:5000/detect"
file_path = "C:/Users/49860/Desktop/yymm.jpg"

response = requests.post(url, files={'file': open(file_path, 'rb')})
#print(response.json())

if response.status_code == 200:
    # 保存图像到本地
    with open('C:/Users/49860/Desktop/yymm2.jpg', 'wb') as f:
        f.write(response.content)
    print("Image saved as output.jpg")
else:
    print("Error:", response.text)
#print(response.json())  # 打印检测结果
