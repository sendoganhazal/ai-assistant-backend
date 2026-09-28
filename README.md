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
    .gitignore

    git init
    
    git add .
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/turkiyeyapayzekaakademisi/smart-assistant-backend.git
    git push -u origin main

    https://smart-assistant-backend-u25o.onrender.com