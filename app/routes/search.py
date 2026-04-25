from flask import Blueprint, render_template, request, redirect, url_for
from app.models.note import Note

# 建立名為 search 的 Blueprint
bp = Blueprint('search', __name__)

@bp.route('/search', methods=['GET'])
def search_notes():
    """
    處理搜尋請求。
    邏輯：取得 GET 參數 `q`，呼叫 Note.search(keyword) 進行過濾，並將結果渲染至 index.html。
    """
    pass
