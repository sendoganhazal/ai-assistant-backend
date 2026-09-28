Sahte Akıllı Asistan Fonksiyonun Geliştirilmesi
SQLite ile Database İşlemleri
Fastapi ile Endpoint Oluşturma
    pip install fastapi uvicorn
    uvicorn main:app --reload
    swagger test
Backend Uygulamasını Docker ile Test Et
    requirements.txt
    docker build -t ai-assistant-backend .
    docker run -d -p 8000:8000 --name ai-assistant-container ai-assistant-backend
    http://localhost:8000/docs
Backendi Github'a Yükle ve Render ile Canlıya Al


  https://ai-assistant-backend-4usm.onrender.com