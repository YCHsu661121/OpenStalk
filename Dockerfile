# 基礎映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 安裝依賴包
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製主程式
COPY OpenStalk.py .

# 啟動服務
CMD ["python", "OpenStalk.py"]