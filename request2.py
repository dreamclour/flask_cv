# -- coding: utf-8 --
#multipart/form-data 格式传图像，json传文本
#本地图像
#传输单张图片，可在本地测试
import requests
url = "网址"
urllocal = "本地测试"
file_path = "图片路径"

response = requests.post(url, files={'file': open(file_path, 'rb')})

if response.status_code == 200:
    # 保存图像到本地
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print("Image saved as output.jpg")
else:
    print("Error:", response.text)
#print(response.json())
