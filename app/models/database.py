import sqlite3
import os

# 定義資料庫檔案路徑，確保與專案根目錄相對應
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
DB_PATH = os.path.join(INSTANCE_DIR, 'database.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')

def get_db_connection():
    """取得 SQLite 資料庫連線"""
    # 確保 instance 資料夾存在
    if not os.path.exists(INSTANCE_DIR):
        os.makedirs(INSTANCE_DIR)
        
    conn = sqlite3.connect(DB_PATH)
    # 將回傳結果設定為類似字典的操作模式 (Row)，方便透過欄位名稱取值
    conn.row_factory = sqlite3.Row
    # 啟用 Foreign Key 支援（SQLite 預設可能是關閉的）
    conn.execute('PRAGMA foreign_keys = ON;')
    return conn

def init_db():
    """初始化資料庫與資料表結構"""
    if not os.path.exists(SCHEMA_PATH):
        print(f"Warning: Schema file not found at {SCHEMA_PATH}")
        return

    conn = get_db_connection()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized successfully.")
