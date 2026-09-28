"""
    1) mesajları saklamak için tablo oluştur
    2) kaydet: kullanıcı mesajı ve asistan cevabı
    3) liste: kayıtlı tüm mesajları listele
"""
import sqlite3

DB_NAME = "assistant.db"

#Bu fonksiyon mesajları saklayan tabloyu oluşturur
def create_table():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                assistant_response TEXT NOT NULL
            )
        """
        
    )
    
    conn.commit()
    conn.close()
    
# Bu fonksiyon kullanıcı mesajını ve asistan cevabını dbye kaydeder
def save_message(user_message:str, assistant_response:str):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
            INSERT INTO messages (user_message, assistant_response)
            VALUES (?, ?)
        """,  (user_message, assistant_response)
        
    )
    
    conn.commit()
    conn.cursor()
    
# Bu fonksiyon veritabanında ki tüm mesajları getirir

def get_all_messages():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
            SELECT id, user_message, assistant_response
            FROM message
            ORDER BY id ASC
        """
        
    )
    
    rows = cursor.fetchall()
    conn.close()
    
    messages = []
    for row in rows:
        messages.append(
            {
                "id": row[0],
                "user_message": row[1],
                "assistant_response": row[2]
            }
        )
        
    return messages

if __name__ == "__main__":
    
    create_table()
    save_message(
        "Merhaba, nasılsın",
        "Merhaba, size nasıl yardımcı olabilirim"
    )