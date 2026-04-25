# 初始化 routes 模組
from .book import bp as book_bp
from .search import bp as search_bp

def register_routes(app):
    """
    提供給 app.py 呼叫以統一註冊所有的 Blueprints
    """
    app.register_blueprint(book_bp)
    app.register_blueprint(search_bp)
