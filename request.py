# -- coding: utf-8 --
#这是最初版本的传输，其中，请求和响应之间的格式有点问题
import requests
url ="http://i-1.gpushare.com:21533/detect"
image_path ="C:/Users/49860/Desktop/yymm.jpg"
with open(image_path, "rb") as image_file:
    # 构造表单数据
    files = {"image": (image_path, image_file,"image/jpg")}
    # 发送 POST 请求
    response = requests.get(url, files=files)
    image_file.close()  # 记得关闭文件
print(response.status_code)  # 打印状态码
print(response.json())       # 打印 JSON 响应
print(response)

