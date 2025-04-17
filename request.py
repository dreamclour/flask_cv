# -- coding: utf-8 --
#这是最初版本的传输，传输单张图片
import requests
url ="网址"
image_path ="路径"
with open(image_path, "rb") as image_file:
    files = {"image": (image_path, image_file,"image/jpg")}#multipart/form-data类型
    response = requests.get(url, files=files)
    image_file.close()  
print(response.status_code)  
print(response.json())      
print(response)

