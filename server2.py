# -- coding: utf-8 --
#从deeseek的代码测试
#有一个巨大的细节，在云上不能使用debug模式，仅限这个代码。
from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np
from ultralytics import YOLO
import io

app = Flask(__name__)
model = YOLO("yolov8n.pt")  # 加载YOLO模型
@app.route('/detect', methods=['POST'])
def detect():
  # 1. 接收上传的图像
  if 'file' not in request.files:
    return jsonify({"error": "No file uploaded"}), 400

  file = request.files['file']
  if file.filename == '':
    return jsonify({"error": "Empty filename"}), 400

  # 2. 转换为OpenCV格式
  img_bytes = file.read()#读的是二进制
  img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)#这里也是一个重要的节点，如果视pin，需要检查数据
#上面的是8位无符号整数，所以需要在RGB编码时更改
  # 3. YOLO检测
  results = model(img)
  annotated_img = results[0].plot()  # 绘制检测框

  #4. 返回JSON结果
  detections = []
  for box in results[0].boxes:
    detections.append({
      "class": model.names[int(box.cls)],
      "confidence": float(box.conf),
      "bbox": box.xyxy.tolist()[0]  # [x1, y1, x2, y2]
    })

  # # 5. 返回方式（二选一）
  # # 方式1：返回JSON数据
  # return jsonify({
  #   "detections": detections,
  #   "image_size": {"width": img.shape[1], "height": img.shape[0]}
  # })

  #方式2：返回标注后的图像（Bytes）
  _, img_encoded = cv2.imencode('.jpg', annotated_img)
  return send_file(
      io.BytesIO(img_encoded.tobytes()),
      mimetype='image/jpeg'
  )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)






