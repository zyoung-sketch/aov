# 傳說對決模擬系統 - Flask Web 版（Railway 部署版）

## 🚀 如何部署到 Railway

1. 建立 GitHub 倉庫，將此專案上傳
2. 前往 [https://railway.app](https://railway.app) 登入帳號（可用 GitHub）
3. 建立新專案 > 連接 GitHub 倉庫
4. 確認以下設定：
   - Python 環境自動辨識
   - 部署指令自動使用 `gunicorn app:app`
5. 點擊部署，幾分鐘內即可取得公開網址！

## 📂 專案結構

- `app.py`: Flask 主程式
- `db.py`: SQLite 資料操作模組
- `aov.db`: 玩家資料
- `templates/`: HTML 模板
- `requirements.txt`: Python 相依套件
- `Procfile`: 啟動 Web 用
- `runtime.txt`: 指定 Python 版本