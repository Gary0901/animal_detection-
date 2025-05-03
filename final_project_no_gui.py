# -*- coding: utf-8 -*-
import cv2
import numpy as np
import torch
import sys
import urllib.request
import bs4
import ssl
from PIL import Image

def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    return cv_img

def crawl(animal_det):
    DET = str(animal_det)
    DET = DET.strip()
    
    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen("https://hiking.biji.co/index.php?q=news&act=info&id=1458")
    
    data = r.read().decode("utf-8")
    
    root = bs4.BeautifulSoup(data, "html.parser")
    
    animals_topic = []
    animals_detail = []

    animals_top = root.find_all("p")
    for i in range(2, 11):
        for animal in animals_top[i].contents:
            animals_topic.append(animal.string)

    animals_topic[7] += animals_topic[8]
    del animals_topic[8]

    for i in range(0, 9):
        del animals_topic[i]

    animals_del = root.find("div", class_="fr-view")

    for i in animals_del.find_all('li'):
        animals_detail.append(i.string)

    for i in range(1, 14, 6):
        del animals_detail[i]

    for i in range(18, 50, 6):
        del animals_detail[i]

    while(len(animals_detail) > 53):
        del animals_detail[53]

    animals = []

    for i in range(0, 17, 6):
        a = ""
        for j in range(i, i+6):
            b = str(animals_detail[j])
            b = b.strip()
            a = a + '\n' + b
        a = a.strip()
        animals.append(a)

    str123 = ""

    for i in range(18, 23):
        b = str(animals_detail[i])
        str123 = str123 + '\n' + b

    str123 = str123.strip()
    animals.append(str123)

    for i in range(23, 52, 6):
        a = ""
        for j in range(i, i+6):
            b = str(animals_detail[j])
            b = b.strip()
            a = a + '\n' + b
        a = a.strip()
        animals.append(a)

    str_all = ""

    if (DET == "Cervus unicolor swinhoei"):
        str_all += animals_topic[0] 
        str_all += '\n'
        str_all += animals[0]
    elif(DET == "Ursus thibetanus formosanus"):
        str_all += animals_topic[1] 
        str_all += '\n'
        str_all += animals[1]
    elif(DET == "Naemorhedus swinhoei"):
        str_all += animals_topic[2] 
        str_all += '\n'
        str_all += animals[2]
    elif(DET == "Mustela sibirica taivana"):
        str_all += animals_topic[3] 
        str_all += '\n'
        str_all += animals[3]
    elif(DET == "Martes flavigula chrysospila"):
        str_all += animals_topic[4] 
        str_all += '\n'
        str_all += animals[4]
    elif(DET == "Pholidota"):
        str_all += animals_topic[5] 
        str_all += '\n'
        str_all += animals[5]
    elif(DET == "Petaurista alborufus lena"):
        str_all += animals_topic[6] 
        str_all += '\n'
        str_all += animals[6]
    elif(DET == "Macaca cyclopis"):
        str_all += animals_topic[7] 
        str_all += '\n'
        str_all += animals[7]
    elif(DET == "Muntiacus reevesi"):
        str_all += animals_topic[8] 
        str_all += '\n'
        str_all += animals[8]
    
    return str_all

def detect_animal(image_path):
    # 讀取圖片
    img = cv_imread(image_path)
    
    # 載入模型
    print("載入模型中...")
    model = torch.hub.load('ultralytics/yolov5', 'custom', 
                          path='yolov5-master/runs/train/exp2/weights/best.pt', 
                          force_reload=True)
    
    # 進行偵測
    print("進行動物偵測...")
    results = model(img)
    
    # 取得偵測結果
    animals_name = results.pandas().xyxy[0].name.to_string()
    name = ""
    for i in range(5, len(animals_name)):
        name = name + animals_name[i]
    
    print("偵測到的動物:", name)
    
    # 取得動物資訊
    info = crawl(name)
    print("\n動物資訊:")
    print(info)
    
    # 儲存結果圖片
    results.save()
    print("\n結果圖片已儲存到runs/detect/exp/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = input("請輸入圖片路徑: ")
    
    detect_animal(image_path)
