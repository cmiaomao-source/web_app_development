from flask import Blueprint, render_template, request, redirect, url_for
from app.models.note import Note
from app.models.comment import Comment

# 建立名為 book 的 Blueprint
bp = Blueprint('book', __name__)

@bp.route('/', methods=['GET'])
def index():
    """
    處理首頁請求。
    邏輯：呼叫 Note.get_all() 取得所有筆記，並渲染 index.html。
    """
    pass

@bp.route('/create', methods=['GET'])
def create_page():
    """
    顯示新增筆記頁面。
    邏輯：渲染 create.html 表單。
    """
    pass

@bp.route('/create', methods=['POST'])
def create_note():
    """
    處理新增筆記表單送出。
    邏輯：取得表單資料 (book_title, content, rating)，呼叫 Note.create() 存入資料庫，成功後導向至首頁。
    """
    pass

@bp.route('/note/<int:id>', methods=['GET'])
def note_detail(id):
    """
    顯示特定筆記的詳細內容與評論。
    邏輯：呼叫 Note.get_by_id(id) 與 Comment.get_by_note_id(id)，若找不到回傳 404，否則渲染 detail.html。
    """
    pass

@bp.route('/note/<int:id>/comment', methods=['POST'])
def add_comment(id):
    """
    處理針對特定筆記的評論表單。
    邏輯：取得表單資料 (content)，呼叫 Comment.create() 存入資料庫，成功後導向回該筆記詳細頁。
    """
    pass
