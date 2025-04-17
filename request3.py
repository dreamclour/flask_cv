#直接使用照相机的图像
import cv2
from ultralytics import YOLO
from cv2 import getTickCount, getTickFrequency
from io import BytesIO
import requests
from PIL import Image
# 加载 YOLOv8 模型

url = "网址"
urllocal = "本地测试"
file_path = "图片路径"
model = YOLO("weights/yolov8s.pt")
# 获取摄像头内容，参数 0 表示使用默认的摄像头
cap = cv2.VideoCapture(0)
success, frame = cap.read()  # 读取摄像头的一帧图像
_, img_encoded = cv2.imencode('.jpg', frame)
img_bytes = img_encoded.tobytes()

files = {'file': ('image.jpg', BytesIO(img_bytes), 'image/jpeg')}
response = requests.post(url, files=files)
print(response.content)

if response.status_code == 200:
    # 保存图像到本地
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print("Image saved as output.jpg")
else:
    print("Error:", response.text)
#print(response.json())  # 打印检测结果

