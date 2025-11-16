#  Animal Detection 台灣特有動物辨識專案

##  專案簡介 (Introduction)

此專案旨在利用深度學習模型 YOLOv5 實現台灣特有動物的物件偵測（Object Detection）。我們整合了網路爬蟲、資料標註、模型微調（Fine-tuning）與 Python GUI 應用，建立一個從資料獲取到實際推論（Inference）的完整解決方案。

##  專案特色與功能 (Features)

* **多類別動物辨識:** 專注於辨識九種台灣特有動物，實現精確的物件定位與分類。
* **網路資料爬取:** 使用 `crawl.py` 腳本從網頁抓取動物介紹資料。
* **YOLOv5 模型訓練:** 使用手動標註的資料對 YOLOv5 進行 Fine-tuning 訓練。
* **Python GUI 介面:** 提供 `final_project.py` 應用程式，方便使用者上傳圖片進行實時推論（Inference）。
* **無 GUI 模式:** 提供 `final_project_no_gui.py` 腳本，用於命令列下的推論或測試。

## 🛠️ 技術棧 (Technology Stack)

| 類別 | 技術/工具 | 檔案/備註 |
| :--- | :--- | :--- |
| **模型框架** | YOLOv5 (PyTorch) | `yolov5-master/` |
| **程式語言** | Python 3.x | |
| **資料獲取** | 網路爬蟲 | `crawl.py` |
| **GUI 介面** | Python GUI 函式庫 | `final_project.py` |
| **依賴管理** | pip | `requirements.txt` |
