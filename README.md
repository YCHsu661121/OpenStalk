# OpenStalk

## **版本**
- **1.0**: 完成基本功能分離，將伺服器與技能邏輯進行整合分開。

## **項目介紹**
`OpenStalk` 包含以下兩大部分：
1. **OpenStalkServer**: 處理股票數據查詢與執行 Ollama 指令的 Docker 化服務。
2. **OpenStalkClient**: 作為 OpenClaw 技能，與伺服器進行互動。

---

## **使用說明**

### **伺服器部署**
1. **進入伺服器目錄**:
   ```bash
   cd skills/OpenStalkServer
   ```
2. **構建與啟動容器**:
   ```bash
   sudo docker-compose build
   sudo docker-compose up -d
   ```
3. **伺服器功能**:
   - **/stock API**: 提供股票數據。
   - **/ollama API**: 支援命令執行。

### **技能啟用**
1. **啟用技能設置**:
   在 OpenClaw 配置文件中加入：
   ```yaml
   skills:
     - path: skills/OpenStalkClient
   ```
2. **重新啟動 OpenClaw**:
   ```bash
   openclaw restart
   ```

---
