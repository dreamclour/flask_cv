#直接使用照相机的图像，循环发送
import cv2
import time
from ultralytics import YOLO
from cv2 import getTickCount, getTickFrequency
from io import BytesIO
import requests
from PIL import Image

url = "网址"
urllocal = "本地测试"
file_path = "图片路径"

# 获取摄像头内容，参数 0 表示使用默认的摄像头
cap = cv2.VideoCapture(0)

interval = 2 #间隔时间
while True:
  start_time = time.time()  # 记录开始时间

  success, frame = cap.read()  
  _, img_encoded = cv2.imencode('.jpg', frame)
  img_bytes = img_encoded.tobytes()

  files = {'file': ('image.jpg', BytesIO(img_bytes), 'image/jpeg')}
  response = requests.post(url, files=files)

  if response.status_code == 200:
      # 保存图像到本地
      with open('file_path', 'wb') as f:
          f.write(response.content)
      print("Image saved as output.jpg")
  else:
      print("Error:", response.text)
  #print(response.json())  # 打印检测结果
  elapsed = time.time() - start_time
  time.sleep(max(0, interval - elapsed))  # 确保不会负延迟








