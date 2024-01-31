import speech_recognition as sr
import subprocess
import pyautogui


reco = sr.Recognizer()
proceso = None
anuncio = "Jesus que tal ,de sabatico que. el codigo esta esperado la api, aun hay problema en la bases de datos pero chill nada grave eso se le muestra al profe y listo " 

saludo = "Hola buenos dias aqui puedes anotar cualquier cosa" 

def ejecutar(comando):
    global proceso
    if("abrir bloc de notas" in comando):
        proceso = subprocess.Popen(["notepad.exe"])
    elif("mensaje" in comando):
        pyautogui.write(anuncio)
    elif("cerrar bloc de notas" in comando):
        proceso.teminate()
    elif("" in comando):
        pyautogui.write(saludo)

def escuchar():
    with sr.Microphone() as source:
        print("Hola buenas")
        reco.adjust_for_ambient_noise(source)
        audio = reco.listen(source)
    
    try:
        comando = reco.recognize_google(audio,language="es-ES")
        print(f"Comando reconocido: {comando}")
        ejecutar(comando)
    except sr.UnknownValueError:
        print("No pudo enteder el comando")
    except sr.RequestError as e :
        print(f"Error: {e}")

while True:
    escuchar()