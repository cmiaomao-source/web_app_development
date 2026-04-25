# 讀書筆記本專案 - 流程圖 (FLOWCHART)

## 1. 使用者流程圖 (User Flow)

此流程圖描述使用者進入網站後的各種操作路徑，包含瀏覽筆記列表、新增筆記、搜尋與留言評論的互動流程。

```mermaid
flowchart LR
    A([使用者進入網站]) --> B[首頁 - 筆記列表]
    
    B --> C{選擇欲執行的操作}
    
    C -->|新增筆記| D[點擊「新增筆記」]
    D --> E[填寫書名、心得與評分表單]
    E -->|送出表單| F[儲存成功，返回首頁]
    F --> B
    
    C -->|搜尋筆記| G[在搜尋框輸入書名或關鍵字]
    G -->|點擊搜尋| H[顯示過濾後的搜尋結果列表]
    H -->|點擊特定筆記| I
    
    C -->|查看詳情| I[進入筆記詳細頁面]
    I --> J{詳細頁操作}
    
    J -->|瀏覽內容| K[閱讀詳細心得與歷史評論]
    J -->|發表評論| L[在下方填寫評論表單]
    L -->|送出評論| M[儲存並顯示新留言]
    M --> I
    
    J -->|返回列表| B
```

## 2. 系統序列圖 (Sequence Diagram)

此序列圖以「新增讀書筆記」為情境，展示從使用者操作到資料存入資料庫的完整技術流程：

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route
    participant Model as Model (資料處理)
    participant DB as SQLite

    User->>Browser: 在新增頁面填寫書名與心得並點擊「送出」
    Browser->>Flask: POST /create (傳送表單資料)
    Flask->>Model: 驗證資料並呼叫 create_note(data)
    Model->>DB: 執行 INSERT INTO notes ...
    DB-->>Model: 寫入成功
    Model-->>Flask: 回傳執行結果
    Flask-->>Browser: 重新導向 (Redirect) 至首頁 /
    Browser->>Flask: GET / (重新請求首頁)
    Flask->>Model: 呼叫 get_all_notes()
    Model->>DB: 執行 SELECT * FROM notes ...
    DB-->>Model: 回傳所有筆記資料
    Model-->>Flask: 回傳筆記列表
    Flask-->>Browser: 渲染 index.html 並顯示更新後的列表
```

## 3. 功能清單對照表

以下表格整理了系統中各個主要功能、對應的 URL 路徑以及 HTTP 請求方法，供後續 API 設計與前端開發時對齊介面：

| 功能名稱 | 描述 | URL 路徑 | HTTP 方法 |
| --- | --- | --- | --- |
| **筆記列表 (首頁)** | 顯示所有使用者的讀書筆記清單 | `/` | GET |
| **搜尋筆記** | 根據書名或內容關鍵字過濾筆記 | `/search` | GET |
| **新增筆記頁面** | 顯示用於新增筆記的表單頁面 | `/create` | GET |
| **儲存新筆記** | 接收表單資料，寫入資料庫並導回首頁 | `/create` | POST |
| **筆記詳細頁** | 顯示單一筆記的完整內容、評分與評論區 | `/note/<int:id>` | GET |
| **發表評論** | 接收評論表單資料，寫入資料庫並重新載入頁面 | `/note/<int:id>/comment` | POST |
