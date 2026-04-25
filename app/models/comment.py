from app.models.database import get_db_connection

class Comment:
    @staticmethod
    def create(note_id, content):
        """為特定筆記新增一則評論"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO comments (note_id, content) VALUES (?, ?)',
            (note_id, content)
        )
        conn.commit()
        comment_id = cursor.lastrowid
        conn.close()
        return comment_id

    @staticmethod
    def get_by_note_id(note_id):
        """取得特定筆記下的所有評論，依建立時間由舊到新排序"""
        conn = get_db_connection()
        comments = conn.execute(
            'SELECT * FROM comments WHERE note_id = ? ORDER BY created_at ASC',
            (note_id,)
        ).fetchall()
        conn.close()
        return [dict(comment) for comment in comments]
