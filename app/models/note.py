from app.models.database import get_db_connection

class Note:
    @staticmethod
    def create(book_title, content, rating):
        """新增一筆筆記"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO notes (book_title, content, rating) VALUES (?, ?, ?)',
            (book_title, content, rating)
        )
        conn.commit()
        note_id = cursor.lastrowid
        conn.close()
        return note_id

    @staticmethod
    def get_all():
        """取得所有筆記，依建立時間由新到舊排序"""
        conn = get_db_connection()
        notes = conn.execute(
            'SELECT * FROM notes ORDER BY created_at DESC'
        ).fetchall()
        conn.close()
        return [dict(note) for note in notes]

    @staticmethod
    def get_by_id(note_id):
        """根據 ID 取得單筆筆記"""
        conn = get_db_connection()
        note = conn.execute(
            'SELECT * FROM notes WHERE id = ?',
            (note_id,)
        ).fetchone()
        conn.close()
        return dict(note) if note else None

    @staticmethod
    def search(keyword):
        """根據書名或內容關鍵字搜尋筆記"""
        conn = get_db_connection()
        like_pattern = f"%{keyword}%"
        notes = conn.execute(
            'SELECT * FROM notes WHERE book_title LIKE ? OR content LIKE ? ORDER BY created_at DESC',
            (like_pattern, like_pattern)
        ).fetchall()
        conn.close()
        return [dict(note) for note in notes]
        
    @staticmethod
    def delete(note_id):
        """刪除筆記"""
        conn = get_db_connection()
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()
