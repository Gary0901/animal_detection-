# -*- coding: utf-8 -*-
import cv2
import numpy as np
import torch
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import urllib.request
import bs4
import pandas as pd
import ssl

root = tk.Tk()
root.title(" Animals Detection")
root.geometry('800x700')

root.configure(background = "black")
background_image = PhotoImage(file = "background.gif")
background = Label(root, image = background_image,bd = 0)
background.place(x = 0,y = 0)

videoFrame = tk.Frame(root).pack()
video = tk.Label(videoFrame)
video.pack()
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img
def upload():
    sfname = filedialog.askopenfilename(title='選擇',
                                        filetypes=[
                                            ('All Files','*'),
                                            ("jpeg files","*.jpg"),
                                            ("png files","*.png"),
                                            ("gif files","*.gif")])

    im = cv_imread(sfname)
    cv2image = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)

    img_width = img.size[0]
    img_height = img.size[1]
    img = img.resize((int(img_width*0.7), int(img_height*0.7)), Image.ANTIALIAS)

    img = image_border(img,'a',20,color = (255,235,205))

    imgtk = ImageTk.PhotoImage(image=img)
    video.imgtk = imgtk
    video.configure(image=imgtk,height= (img_height*0.7),width= int(img_width*0.7))

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5-master/runs/train/exp2/weights/best.pt',force_reload=True)
    results = model(img)
    # print("result = ",results)
    # print("type = ",type(results))
    # print("result1 = ",results.xyxy[0])
    # print("results2 = ",results.pandas().xyxy[0])
    #print("Name = ",results.pandas().xyxy[0].name)
    animals_name = results.pandas().xyxy[0].name.to_string()
    #print(animals_name)
    name = ""
    for i in range(5,len(animals_name)):
        name = name +animals_name[i]
    print("Name =",name)
    #crawl(name)
    TxtMessages.delete(1.0,"end")
    TxtMessages.insert(END,"\n" + crawl(name),'left')

def crawl(animal_det):
    DET = str(animal_det)
    DET = DET.strip()
    #print(len(DET))
    #print("ANIMAL =",DET)
    #print("Type = ",type(DET))

    ssl._create_default_https_context = ssl._create_unverified_context
    r = urllib.request.urlopen("https://hiking.biji.co/index.php?q=news&act=info&id=1458")
    
    data = r.read().decode("utf-8")
    
    root = bs4.BeautifulSoup(data,"html.parser")
    
    animals_topic = []
    animals_detail = []

    animals_top = root.find_all("p")
    for i in range(2,11):
        for animal in animals_top[i].contents:
            animals_topic.append(animal.string)

    animals_topic[7] += animals_topic[8]
    del animals_topic[8]

    for i in range(0,9):
        del animals_topic[i]

    #for i in range(len(animals_topic)):
        #print(animals_topic[i])

    animals_del = root.find("div",class_ = "fr-view")

    for i in animals_del.find_all('li'):
        animals_detail.append(i.string) 

    for i in range(1,14,6):
        del animals_detail[i]

    for i in range(18,50,6):
        del animals_detail[i]

    while(len(animals_detail)  >53):
        del animals_detail[53]

    animals = []

    for i in range(0,17,6):
        a = ""
        for j in range(i,i+6):
            b = str(animals_detail[j])
            b = b.strip()
            a = a + '\n' +b
        #print(a)
        a = a.strip()
        animals.append(a)

    str123 = ""

    for i in range(18,23):
        b = str(animals_detail[j])
        str123 = str123 + '\n' + b

    #print(str123)
    str123 = str123.strip()
    animals.append(str123)

    for i in range(23,52,6):
        a = ""
        for j in range(i,i+6):
            b = str(animals_detail[j])
            b = b.strip()
            a = a + '\n' + b
        #print(a)
        a = a.strip()
        animals.append(a)

    #print(len(animals))

    str_all = ""

    if (DET == "Cervus unicolor swinhoei"):
        #print("1")
        str_all += animals_topic[0] 
        str_all += '\n'
        str_all += animals[0]
    elif(DET == "Ursus thibetanus formosanus"):
        #print("2")
        str_all += animals_topic[1] 
        str_all += '\n'
        str_all += animals[1]
    elif(DET == "Naemorhedus swinhoei"):
        #print("3")
        str_all += animals_topic[2] 
        str_all += '\n'
        str_all += animals[2]
    elif(DET == "Mustela sibirica taivana"):
        #print("4")
        str_all += animals_topic[3] 
        str_all += '\n'
        str_all += animals[3]
    elif(DET == "Martes flavigula chrysospila"):
        #print("5")
        str_all += animals_topic[4] 
        str_all += '\n'
        str_all += animals[4]
    elif(DET == "Pholidota"):
        #print("6")
        str_all += animals_topic[5] 
        str_all += '\n'
        str_all += animals[5]
    elif(DET == "Petaurista alborufus lena"):
        #print("7")
        str_all += animals_topic[6] 
        str_all += '\n'
        str_all += animals[6]
    elif(DET == "Macaca cyclopis"):
        #print("8")
        str_all += animals_topic[7] 
        str_all += '\n'
        str_all += animals[7]
    elif(DET == "Muntiacus reevesi"):
        #print("9")
        str_all += animals_topic[8] 
        str_all += '\n'
        str_all += animals[8]
    #print(str_all)
    return (str_all)

def image_border(img,loc = 'a',width = 10,color = (0, 0, 0,)):
    '''
    src: (str) 需要加边框的图片路径
    dst: (str) 加边框的图片保存路径
    loc: (str) 边框添加的位置, 默认是'a'(
        四周: 'a' or 'all'
        上: 't' or 'top'
        右: 'r' or 'rigth'
        下: 'b' or 'bottom'
        左: 'l' or 'left'
    )
    width: (int) 边框宽度 (默认是3)
    color: (int or 3-tuple) 边框颜色 (默认是0, 表示黑色; 也可以设置为三元组表示RGB颜色)
    '''
    # 读取图片
    #img_ori = Image.open(src)
    img_ori = img
    w = img_ori.size[0]
    h = img_ori.size[1]

    # 添加边框
    if loc in ['a', 'all']:
        w += 2*width
        h += 2*width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (width, width))
    elif loc in ['t', 'top']:
        h += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (0, width, w, h))
    elif loc in ['r', 'right']:
        w += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (0, 0, w-width, h))
    elif loc in ['b', 'bottom']:
        h += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (0, 0, w, h-width))
    elif loc in ['l', 'left']:
        w += width
        img_new = Image.new('RGB', (w, h), color)
        img_new.paste(img_ori, (width, 0, w, h))
    else:
        pass

    return img_ori

    # 保存图片
    # img_new.save(dst)

TxtMessages = Text(root, width = 70,height = 10,font= '標楷體')
TxtMessages.pack()

B1 = tk.Button(root, text = 'SEARCH',command = upload)
B1.config(width = '10',height = '2',background="#FFE4B5",font = 'STHupo')
B1.pack()

# B2 = tk.Button(root,text = 'SEARCH')
# B2.config(width = '10',height = '2',background="#FFE4B5",font = 'STHupo')
# B2.pack(side = 'left',padx = 150)
root.mainloop()