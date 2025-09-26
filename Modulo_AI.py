from dotenv import load_dotenv
from elevenlabs.play import play
from elevenlabs.client import ElevenLabs
import speech_recognition as sr
import openai
import os
import playsound

class moduloIA():
    def __init__(self):
        load_dotenv()
    
        self.elevenlabs = ElevenLabs(
            api_key = os.getenv("ELEVENLABS_APIKEY")
        )
        openai.api_key = os.getenv("OPENAI_APIKEY")

    def escuchar(self):
        r = sr.Recognizer()

        with sr.Microphone() as fuente:
            r.adjust_for_ambient_noise(fuente)
            playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/TIMBRE.mp3")
            audio = r.listen(fuente)

        try:
            texto = r.recognize_google(audio,language="es-AR")
            return texto
        
        except sr.UnknownValueError:
            playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/hueso.mp3")
        except sr.RequestError:
            print("Error de Conexion")

    def prompt(self,texto):
        respuesta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"Sos Argentino"},
                {"role":"user","content":texto},        
            ],
            max_tokens=100
        )
        return respuesta

    respuesta = prompt()
    respuestaGPT = respuesta.choices[0].message.content

    def text_to_speech(self,respuestaGPT):
        audio = self.elevenlabs.text_to_speech.convert(
            text=respuestaGPT,
            voice_id="kq2txNbA7gDo4YxPud8y",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(audio)

moduloIA=moduloIA()
texto=moduloIA.escuchar()
respuesta=moduloIA.prompt(texto)
moduloIA.text_to_speech(respuesta)