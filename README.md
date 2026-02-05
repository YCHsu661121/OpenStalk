# OpenStalk

## **項目介紹**
`OpenStalk` 是一個基於 Docker 打包的股票掃描工具，其核心功能包括：
- 接口 `/stock`：查詢股票數據，支持 `yfinance`。
- 接口 `/ollama`：利用 Ollama 容器執行命令並返回結果。
- 預設通過 Docker 與其他容器交互。

---

## **系統需求**
- **Python**: 3.9 或更高版本
- **Docker**: 已安裝並啟用

---

## **安裝步驟**

### 1. **克隆倉庫**
```bash
git clone https://github.com/YCHsu661121/OpenStalk.git
cd OpenStalk
```

### 2. **構建 Docker 映像**
```bash
docker-compose build
```

### 3. **啟動服務**
```bash
docker-compose up
```

這將啟動應用，並將服務暴露在 `http://localhost:5000`。

---

## **使用說明**

### 1. 獲取股票數據
- 請求類型：`GET`
- 地址：`http://localhost:5000/stock`
- 範例請求：
  ```bash
  curl "http://localhost:5000/stock?ticker=AAPL"
  ```
- 返回示例：
  ```json
  {
    "company": "Apple Inc.",
    "current_price": 150.0,
    "market_cap": 2500000000000,
    "sector": "Technology"
  }
  ```

### 2. 調用 Ollama 容器
- 請求類型：`POST`
- 地址：`http://localhost:5000/ollama`
- 範例請求：
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"command": "docker ps"}' \
  http://localhost:5000/ollama
  ```
- 返回示例：
  ```json
  {
    "output": "CONTAINER ID   IMAGE     COMMAND                  ...",
    "error": ""
  }
  ```

---

## **文件結構説明**
- `OpenStalk.py`：主要功能實現，包括所有 API 接口。
- `Dockerfile`：構建服務所需的配置。
- `docker-compose.yml`：定義服務和容器的協調方式。
- `requirements.txt`：列出所有 Python 依賴。

---

## **貢獻指南**
歡迎提交 Issues 或 Pull Requests，如果有任何想法或建議，請聯繫我！