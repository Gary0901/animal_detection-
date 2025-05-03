import cv2
import numpy as np
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5-master/runs/train/exp2/weights/best.pt',force_reload=True)
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
#設定多少confidence以上才可以顯示出來
#model.conf = 0.5 

img = cv2.imread('data/test.jpg')
results = model(img)

print("results = "  , results)
print("results1 = "  ,results.xyxy[0])
print("results2 = " ,results.pandas().xyxy[0])
cv2.imshow('YOLO', np.squeeze(results.render()))
cv2.imwrite('result.png',np.squeeze(results.render()))
cv2.waitKey(0)




