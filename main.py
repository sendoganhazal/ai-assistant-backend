"""
    1. fastapi uygulaması oluştur
    2. kullanıcıdan mesaj alan post endpointi
    3. sahte akıllı asistan cevabı
    4. soru ve cevabı database e kaydet
    5. tüm mesajları listeleyen bir get endpointi oluştur

"""

from fastapi import FastAPI
from pydantic import BaseModel
from assistant_logic import fake_assistant
from database import create_table, save_message, get_all_messages

# 1. fastapi uygulaması oluştur
app = FastAPI()

# veritabanı oluştur
create_table()

#base model veri yapısı oluştur
class MessageModal(BaseModel):
    user_message:str
    
# anasayfa endpointi
@app.get("/")
def home():
    return {
        "message": "Akıllı Asistan API Çalışıyor"
    }

# 2. kullanıcıdan mesaj alan post endpointi
@app.post("/chat")
def chat_with_assistant(request:MessageModal):
    
    # kullanıcı mesajı
    user_message = request.user_message
    
    # 3. sahte akıllı asistan cevabı
    assistant_response = fake_assistant(user_message)
    
    #  4. soru ve cevabı database e kaydet
    save_message(user_message, assistant_response)
    
    return {
        "user_message":user_message,
        "assistant_response":assistant_response
    }
    
# 5. tüm mesajları listeleyen bir get endpointi oluştur
@app.get("/messages")
def read_all_messages():
    
    messages = get_all_messages()
    
    return {
        "messages":messages
    }