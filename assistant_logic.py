"""
Amaç:
    - gerçek bir yapay zeka modeli kullanmadan, sabit cevaplar arasından rastgele seçim yapan basit bir akıllı asistan geliştirelim.
"""

import random

# Bu fonksiyon kullanıcıdan gelen mesaj ne olursa olsun, hazır cevaplar arasından rastgele bir tanesini döndürür

def fake_assistant(user_message:str) -> str:
    
    # Normal şartlar altında buraya ai gelecek.
    # ...
    
    responses = [
        "Merhaba, size nasıl yardımcı olabilirim?",
        "Tabii, bu konuda size destek olmaya çalışayım.",
        "Anladım, isterseniz bunu birlikte inceleyebiliriz.",
        "Elbette, size yardımcı olmak için buradayım."
    ]
    
    return random.choice(responses)

if __name__ == "__main__":
    user_text = input("Bir mesaj yazınız: ")
    answer = fake_assistant(user_text)
    print(f"Asistan Cevabı: {answer}")