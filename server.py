import numpy as np
#这个是保存在jupter中的程序，用于服务器的创建
#返回的是图片的类别
#云端运行不用debug模式
from ultralytics import YOLO
model = YOLO("yolov8s.pt")
from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义API端点
@app.route('/predict', methods=['POST','GET'])
def predict():
  data = request.json.post("image")
  results = model.predict(source=data)  # 对当前帧进行目标检测并显示结果
  detection_results = []
  for result in results:
        for box in result.boxes:
            detection_results.append({
                "class": model.names[int(box.cls)],  # 类别名称
                "confidence": float(box.conf),       # 置信度
                "bbox": box.xyxy.tolist()[0]        # 边界框坐标 [x1, y1, x2, y2]
                            })

  # 返回预测结果
  return jsonify({'prediction':detection_results})
  #return "Hello, World!"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)















