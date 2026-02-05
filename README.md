# OpenStalk

## **項目介紹**
`OpenStalk` 是一個基於 Docker 打包的股票掃描工具，其核心功能包括：
- 通過 `/stock` API 獲取實時股票數據。
- 通過 `/ollama` API 調用 Ollama 容器執行命令。
- 適用於 OpenClaw 平台進行擴展。

---

## **如何給 OpenClaw 使用？**

### **步驟 1：安裝 Docker 環境**
確保 Docker 已安裝，並啟用了服務。

### **步驟 2：克隆倉庫**
將 `OpenStalk` 倉庫克隆至本地的 OpenClaw `skills/` 目錄下：
```bash
git clone https://github.com/YCHsu661121/OpenStalk.git skills/OpenStalk
```

### **步驟 3：構建與啟動 Docker 容器**
在克隆的目錄下構建容器並啟動：
```bash
cd skills/OpenStalk
sudo docker-compose build
sudo docker-compose up -d
```

### **步驟 4：編輯 OpenClaw 配置**
在 OpenClaw 主配置文件中啟用此技能：
```yaml
skills:
  - path: skills/OpenStalk
```

### **步驟 5：重啟 OpenClaw**
執行以下命令以重新加載技能：
```bash
openclaw restart
```

---

## **技能功能介紹**

### **1. 呼叫股票 API**
方法 `GET /stock`：
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

### **2. 調用 Ollama API**
方法 `POST /ollama`：
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