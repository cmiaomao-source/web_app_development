# 讀書筆記本專案 - 路由與頁面設計 (ROUTES)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 筆記列表 (首頁) | GET | `/` | `templates/index.html` | 顯示所有使用者的讀書筆記 |
| 搜尋筆記 | GET | `/search` | `templates/index.html` | 根據關鍵字過濾筆記 (使用 `?q=keyword`) |
| 新增筆記頁面 | GET | `/create` | `templates/create.html` | 顯示供填寫的新增筆記表單 |
| 建立筆記 | POST | `/create` | — | 接收新增表單，存入資料庫並重導向至首頁 |
| 筆記詳情 | GET | `/note/<int:id>` | `templates/detail.html` | 顯示單筆筆記內容與歷史留言 |
| 發表評論 | POST | `/note/<int:id>/comment`| — | 接收評論表單，存入資料庫並重導向回詳情頁 |

## 2. 每個路由的詳細說明

### `GET /` (首頁)
- **輸入**：無。
- **處理邏輯**：呼叫 `Note.get_all()` 取得所有筆記資料。
- **輸出**：將筆記資料傳入並渲染 `index.html`。
- **錯誤處理**：若發生系統異常則顯示通用錯誤畫面。

### `GET /search` (搜尋)
- **輸入**：URL Query Parameter `q` (例如 `?q=Python`)。
- **處理邏輯**：取得參數後，呼叫 `Note.search(keyword)` 進行過濾。
- **輸出**：將過濾後的筆記資料傳入並渲染 `index.html`。
- **錯誤處理**：若未提供參數，則重新導向回首頁 `/`。

### `GET /create` (新增筆記頁面)
- **輸入**：無。
- **處理邏輯**：無特殊邏輯，僅需準備渲染畫面。
- **輸出**：渲染 `create.html` 顯示表單。

### `POST /create` (建立筆記)
- **輸入**：Form Data (`book_title`, `content`, `rating`)。
- **處理邏輯**：呼叫 `Note.create()` 將資料存入 SQLite 資料庫。
- **輸出**：成功後 HTTP Redirect 重新導向至 `/`。
- **錯誤處理**：如果必填欄位遺失，回傳 400 Bad Request 並顯示錯誤提示。

### `GET /note/<int:id>` (筆記詳情頁)
- **輸入**：URL 路徑參數 `id`。
- **處理邏輯**：
  1. 呼叫 `Note.get_by_id(id)` 取得筆記。
  2. 呼叫 `Comment.get_by_note_id(id)` 取得該筆記的所有留言。
- **輸出**：將上述資料傳入並渲染 `detail.html`。
- **錯誤處理**：若筆記 `id` 不存在，回傳 404 Not Found。

### `POST /note/<int:id>/comment` (發表評論)
- **輸入**：URL 路徑參數 `id` 與 Form Data (`content`)。
- **處理邏輯**：呼叫 `Comment.create(id, content)` 寫入留言。
- **輸出**：成功後 HTTP Redirect 重新導向至 `/note/<int:id>`。
- **錯誤處理**：若內容為空，忽略或回傳錯誤；若筆記不存在回傳 404。

## 3. Jinja2 模板清單

以下為前端所需的 HTML 模板設計，所有的頁面都會繼承共用的 `base.html` 以外部引入共用資源：

1. **`base.html`**：全站共用佈局 (Layout)。包含 `<head>`、Navbar、Footer 等共用區塊，並定義 `{% block content %}` 讓其他頁面繼承。
2. **`index.html`**：繼承 `base.html`。用來顯示筆記列表網格或清單，並放置搜尋框。首頁與搜尋結果共用此模板。
3. **`create.html`**：繼承 `base.html`。包含新增讀書筆記的表單 (書名輸入框、心得 Textarea、評分選項)。
4. **`detail.html`**：繼承 `base.html`。顯示某筆筆記的詳細資訊，並在下方列出歷史評論與新增評論的表單。
