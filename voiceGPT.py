from openai import OpenAI # ChatGPT
import speech_recognition as sr # Google speech-to-text
from gtts import gTTS # Google text-to-speach
import os
import pygame.mixer # For background music

# Initializing OpenAI client and speech recognizer:
client = OpenAI()
r = sr.Recognizer()

# Wake words/phrases:
wake_word = "tarvitsen apua"
exit_word = "voitte poistua"

# Convert text to speech using Google text-to-speech:
def speak(text):
    tts = gTTS(text=text, lang='fi') 
    tts.save('response.mp3')
    os.system('mpg321 response.mp3')

# Send question to OpenAI/ChatGPT as text and get response:
def ask_question(question):

    # Add a short instruction to ChatGPT before the question:
    start_question = "Vastaa lyhyesti ja hauskasti, max 3 lauseella, seuraavaan: "
    question = start_question + question

    # Play waiting music:
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("waitmusic.mp3")
    pygame.mixer.music.play()

    # Get completion from ChatGPT:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": question}] ,
        max_tokens=150
        )
    
    # Stop waiting music:
    pygame.mixer.music.stop()
    pygame.quit()
    
    # Convert ChatGPT's response to speech:
    print(completion.choices[0].message.content)
    speak(completion.choices[0].message.content)
    speak("Toivottavasti tämä auttoi. Jos tarvitset taas minua, hihkaise: TARVITSEN APUA.")


# Listen to command and convert it to text:
def listen_command():
    speak("Mitä haluat tietää?")

    # Listen for audio from microphone:
    with sr.Microphone(device_index=8) as source:
        audio = r.listen(source)

        try:
            # Play waiting music:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("waitmusic.mp3")
            pygame.mixer.music.play()

            # Convert audio to text:
            text = r.recognize_google(audio, language="fi-FI")

            # Stop waiting music:
            pygame.mixer.music.stop()
            pygame.quit()

            # Repeat the command and send it to ask_question function:
            speak("Kysyit {}".format(text))
            ask_question(text)
        except Exception as e:
            print(f"Error: {e}")
            speak("Anteeksi - nyt kävi moka.")


# Listen for wake word:
def listen_wakeword():
    speak("Olen valmis auttamaan. Jos haluat kysyä minulta jotain, hihkaise TARVITSEN APUA. Jos minulle ei ole juuri nyt käyttöä, sano VOITTE POISTUA.")
    while True:
        
        # Listen for microphone input:
        with sr.Microphone(device_index=8) as source:
            print("Listening for the wake up word...")
            audio = r.listen(source)

            try:
                # Convert audio to text:
                text = r.recognize_google(audio, language="fi-FI").lower()
        
                # Check for wake or exit command:
                if wake_word in text:
                    speak("Kutsuitte Valtias?")
                    listen_command() 
                elif exit_word in text:
                    speak("Nöyrä alamaisenne kiittää ja menee nyt lataamaan akkuja...")
                    break
            except sr.UnknownValueError:
                pass  # Ignore if no speech is detected
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Start listening for the wake word:
listen_wakeword()
