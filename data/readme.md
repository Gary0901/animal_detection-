# 圖像處理與生成作業

本項目包含兩個主要任務：
1. **任務1**：使用不同的模型（BLIP-2和Phi-4）對Flickr30k和MSCOCO數據集進行圖像字幕生成和評估
2. **任務2**：使用多模態大型語言模型和文本到圖像生成模型進行Snoopy風格的圖像轉換

## 環境設置

本項目使用Conda環境開發，您可以按照以下步驟設置環境：

### 系統要求
- Python 3.8+
- CUDA 支持的GPU（用於加速模型運行）
- 至少8GB GPU內存（推薦16GB+）

### 使用Conda設置環境
```bash
# 創建新的conda環境
conda create -n image_processing python=3.8
conda activate image_processing

# 安裝所需依賴
pip install -r requirements.txt
```

requirements.txt已經包含了所有需要的依賴項，包括：
- torch & torchvision
- transformers
- diffusers
- datasets
- nltk
- rouge
- pillow
- tqdm
- 其他必要包

### 模型下載
程式會自動從HuggingFace下載以下模型：
- BLIP-2 圖像字幕模型 (`Salesforce/blip-image-captioning-base`)
- Phi-4多模態指令模型 (`microsoft/Phi-4-multimodal-instruct`)
- Stable Diffusion v1-5 (`sd-legacy/stable-diffusion-v1-5`) 或 Stable Diffusion 3 (`stabilityai/stable-diffusion-3-medium-diffusers`)

首次運行時會需要較長時間下載模型。

## 項目結構
```
hw1/
├── download_data.py          # 數據集下載測試腳本
├── task1_blip2_flickr30k.py          # BLIP-2模型評估Flickr30k
├── task1_blip2_flickr30k_fulldata.py  # BLIP-2模型評估Flickr30k全部數據
├── task1_phi4_flickr30k.py   # Phi-4模型評估Flickr30k
├── task1_phi4_mscoco.py      # Phi-4模型評估MSCOCO
├── task2-1.py               # Snoopy風格轉換 (SD3版本)
├── task2-2.py               # Snoopy風格轉換 (SD1.5版本)
├── checkpoints/             # 檢查點存儲目錄
├── images/                  # 任務2輸入圖像目錄
├── output_stylized/         # 任務2-1輸出圖像目錄
├── my_pic/                  # 任務2-2輸入圖像目錄
├── output/                  # 任務2-2輸出圖像目錄
└── requirements.txt         # 依賴套件清單
```

## 任務1：圖像字幕生成與評估

### 數據集
程式會自動從Hugging Face下載以下數據集：
```bash
python download_data.py
```
- Flickr30k：`nlphuji/flickr30k`
- MSCOCO (Test 5k)：`nlphuji/mscoco_2014_5k_test_image_text_retrieval`

### 運行BLIP-2模型評估Flickr30k測試集（1000個樣本）
```bash
python task1_blip2_flickr30k.py
```

### 運行BLIP-2模型評估Flickr30k全部數據
```bash
python task1_blip2_flickr30k_fulldata.py
```

### 運行Phi-4模型評估Flickr30k
```bash
python task1_phi4_flickr30k.py --batch_size 16 --output_file phi4_flickr30k_results.json
```

### 運行Phi-4模型評估MSCOCO
```bash
python task1_phi4_mscoco.py --batch_size 16 --output_file phi4_mscoco_results.json
```

### 參數調整
對於Phi-4模型，可以調整以下參數：
- `--batch_size`：處理的批次大小（默認16）
- `--output_file`：輸出文件名（可以是.json或.txt）
- `--checkpoint_dir`：檢查點保存目錄（默認為"checkpoints"）
- `--progress_interval`：顯示進度的間隔（默認每20個批次）
- `--subset_size`：指定僅處理部分數據集（僅限phi4_flickr30k.py）

## 任務2：Snoopy風格圖像轉換

本任務有兩個版本的實現，分別使用不同的模型配置。

### 版本1：使用Stable Diffusion 3
```bash
python task2-1.py
```

此版本使用Phi-4多模態模型生成圖像描述，然後使用Stable Diffusion 3 Medium模型生成Snoopy風格的圖像。

需要在當前目錄下創建`images`文件夾，並在其中放入要處理的圖像。生成的圖像將保存在`output_stylized`目錄中。

### 版本2：使用Stable Diffusion v1-5
```bash
python task2-2.py
```

此版本使用Phi-4多模態模型生成圖像描述，然後使用Stable Diffusion v1-5模型生成Snoopy風格的圖像。

需要在當前目錄下創建`my_pic`文件夾，並在其中放入要處理的圖像。生成的圖像將保存在`output`目錄中。

## 輸出說明

### 任務1
- 生成的字幕將保存為JSON或TXT文件
- 評估指標（BLEU-1、BLEU-4、METEOR、ROUGE）結果將被顯示並保存

### 任務2
- 風格化的圖像將被保存在輸出目錄中
- 每個圖像的描述也會被保存在相同目錄中
- 處理日誌將被保存為文本文件

## 故障排除

### 內存問題
如果遇到GPU內存不足的問題：
- 減小批處理大小（使用`--batch_size`參數）
- 對於任務1：使用較少的數據集樣本（使用`--subset_size`參數）
- 對於任務2：處理較少的圖像或減小圖像尺寸

### 下載問題
如果模型或數據集下載失敗：
- 確保您具有穩定的網絡連接
- 嘗試使用VPN或代理服務器
- 手動下載模型文件並放置在適當位置

## 作業說明

本作業實現了兩個主要任務：

1. **圖像描述生成**:
   - 使用BLIP-2和Phi-4多模態模型生成圖像描述
   - 針對Flickr30k和MSCOCO數據集進行評估
   - 計算BLEU、METEOR和ROUGE等評估指標

2. **風格轉換**:
   - 使用多模態模型(Phi-4)分析人臉圖像並生成詳細描述
   - 使用文字到圖像模型(Stable Diffusion)將人臉轉換為Snoopy/花生漫畫風格
   - 提供了兩種實現方式，分別使用SD1.5和SD3

## 資訊

學號：[r13922154]
作業完成日期：[2025/03/28]