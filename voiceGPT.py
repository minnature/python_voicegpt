from openai import OpenAI # ChatGPT
import speech_recognition as sr # Google speech-to-text
from gtts import gTTS # Google text-to-speach
import os
import pygame.mixer # Ootusmusiikin soittoa varten

client = OpenAI()
r = sr.Recognizer()

# Herätesanat/-lauseet:
wake_word = "tarvitsen apua"
exit_word = "voitte poistua"

# Muutetaan teksti puheeksi Googlen text-to-speach avulla:
def speak(text):
    tts = gTTS(text=text, lang='fi') 
    tts.save('response.mp3')
    os.system('mpg321 response.mp3')

# Lähetetään kysymys OpenAI:lle/ChatGPT:lle tekstinä ja palautetaan vastaus:
def ask_question(question):

    # Lisätään kysymyksen alkuun lyhyt ohjeistus ChatGPT:lle:
    start_question = "Vastaa lyhyesti ja hauskasti, max 3 lauseella, seuraavaan: "
    question = start_question + question

    # Odotusmusiikki päälle
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("waitmusic.mp3")
    pygame.mixer.music.play()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": question}] ,
        max_tokens=150
        )
    
    # Odotusmusiikki pois
    pygame.mixer.music.stop()
    pygame.quit()
    
    # ChatGPT:n vastausteksti puheeksi:
    print(completion.choices[0].message.content)
    speak(completion.choices[0].message.content)
    speak("Toivottavasti tämä auttoi. Jos tarvitset taas minua, hihkaise: TARVITSEN APUA.")


# Kuunnellaan kysymys ja muunnetaan tekstiksi:
def listen_command():
    speak("Mitä haluat tietää?")

    # Kuunnellaan mikrofonista audio
    with sr.Microphone(device_index=8) as source:
        audio = r.listen(source)

        # Toistetaan kysymys ja lähetetään se tekstinä ask_question-funktiolle
        try:
            # Odotusmusiikki päälle
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("waitmusic.mp3")
            pygame.mixer.music.play()

            text = r.recognize_google(audio, language="fi-FI")

            # Odotusmusiikki pois
            pygame.mixer.music.stop()
            pygame.quit()

            speak("Kysyit {}".format(text))
            ask_question(text)
        except Exception as e:
            print(f"Error: {e}")
            speak("Anteeksi - nyt kävi moka.")


# Odotetaan herätesanaa:
def listen_wakeword():
    speak("Olen valmis auttamaan. Jos haluat kysyä minulta jotain, hihkaise TARVITSEN APUA. Jos minulle ei ole juuri nyt käyttöä, sano VOITTE POISTUA.")
    while True:
        
        # Kuunnellaan mikrofonia:
        with sr.Microphone(device_index=8) as source:
            print("Listening for the wake up word...")
            audio = r.listen(source)

            try:
                # Audio tekstiksi:
                text = r.recognize_google(audio, language="fi-FI").lower()
        
                # Tarkastetaan, löytyykö heräte- tai poistumiskäskyä:
                if wake_word in text:
                    speak("Kutsuitte Valtias?")
                    listen_command() 
                elif exit_word in text:
                    speak("Nöyrä alamaisenne kiittää ja menee nyt lataamaan akkuja...")
                    break
            except sr.UnknownValueError:
                pass  # Ohitetaan, jos puhetta ei havaita
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

listen_wakeword()
