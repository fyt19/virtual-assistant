import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
# Konuşmayı anlama kısmı
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Size nasıl yardımcı olabilirim?")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='tr-TR', show_all=False)
        print(f"Söylediniz: {text}")
        return text
    except sr.UnknownValueError:
        print("Üzgünüm, ne dediğinizi anlayamadım.")
        return ""
    except sr.RequestError:
        print("Bağlantı hatası, lütfen internet bağlantınızı kontrol edin.")
        return ""
# Yazıyı konuşmaya dönüştürme kısmı
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', 'turkish')  # Ses ayarını Türkçe yaptığımız kısım
    engine.say(text)
    engine.runAndWait()
# Komutları işleme kısmı
def process_command(command):
    if "nasılsın" in command:
        speak("Ben iyiyim, teşekkür ederim. Sen nasılsınız?")
    elif "saat kaç" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Şu anda saat {current_time}.")
    elif "arama yap" in command:
        speak("Ne aramamı istersiniz?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "wikipedia'da ara" in command:
        speak("Ne aramamı istersiniz?")
        search_query = listen()
        if search_query:
            try:
                result = wikipedia.summary(search_query, sentences=2)
                speak(result)
            except wikipedia.exceptions.PageError:
                speak("Üzgünüm, aradığınız konuyu bulamadım.")
    elif "hesap makinesi" in command:
        speak("İlk sayıyı söyleyin:")
        num1 = int(listen())
        speak("İkinci sayıyı söyleyin:")
        num2 = int(listen())
        result = num1 + num2
        speak(f"Sonuç: {result}")
    elif "müzik çal" in command:
        music_folder = "müzik_klasörü_yolu"
        music_files = os.listdir(music_folder)
        if music_files:
            os.startfile(os.path.join(music_folder, music_files[0]))
        else:
            speak("Müzik bulunamadı.")
    elif "kapat" in command:
        speak("Görüşürüz!")
        exit()
    else:
        speak("Üzgünüm, anlamadım.")
# Sanal asistanı çalıştırma kısmı
def run_assistant():
    speak("Merhaba! Sana nasıl yardımcı olabilirim?")
    while True:
        command = listen().lower()
        process_command(command)
run_assistant()
