# voiceGPT

## Summary

> Programming with Python for Raspberry Pi, utilizing a speaker and microphone to convert speech into text. The program utilizes an API interface to connect text with OpenAI's ChatGPT and ultimately converts the response back into speech.

![Kuva1][Kuva1]

[Kuva1]: voiceGPT.png


## Tools and Specifications
- Raspberry Pi 4 Model B
- Bluetooth speaker
- USB Headset microphone

## Specifications
- Creation of accounts and acquisition of API key for OpenAI:
	+ [Done according to the website's instructions](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key?context=python)
	+ OpenAI charges based on API usage (see detailed pricing [on their website](https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free)
- Google services used for speech-to-text and text-to-speech functionalities:
	+ Speech to text: [Google's Speech-To-Text](https://pypi.org/project/SpeechRecognition/)
	+ Text to speech: [Google's Text-To-Speech](https://pypi.org/project/gTTS/)
- Full list of used Python libraries:
	+ openai (OpenAI)
	+ speech_recognition (Google's Speech-To-Text)
	+ gtts (Google's Text-To-Speech)
	+ pygame.mixer (for background music)
- MP3 audio file for playing background music, download one e.g., from [here.](https://pixabay.com/music/)


## Personal Reflections on the Project
- The Finnish speech recognition service may be slightly inaccurate, but it works well for hobby projects. English language support would likely significantly improve accuracy.
- I added background music to the program during waiting periods. This, in my opinion, enhanced the user experience, as there was no need to endure silence while waiting for responses from services like ChatGPT.
- ChatGPT's responses were sometimes too long, so I added instructions to the prompt that responses should be short and entertaining.
- Overall, the implementation of the project was rewarding and interesting. There was plenty of information available online regarding different stages, and I found inspiration and references from sources such as:
	+ [VoiceGPT](https://www.hackster.io/nickbild/voicegpt-f88f8f)
	+ [ChatGPT + Raspberry Pi - A ChatGPT powered Raspberry Pi chatbot](https://youtu.be/lHxFFn04L10?si=tTpYD0P3A3huxNap)


## Ideas for Further Development of the Program
- Timeouts could be added to the code if it takes longer than x-time to receive a response from ChatGPT.
- The program could incorporate almost limitless additional voice commands, including those not requiring ChatGPT (e.g., current date or time of the system).


------------------------------


## Tiivistelmä
> Ohjelmointi Pythonilla Raspberry Pi -tietokoneelle, joka käyttää kaiutinta ja mikrofonia puheen muuttamiseksi tekstiksi. Ohjelma hyödyntää API-rajapintaa, joka yhdistää tekstin OpenAI:n ChatGPT:llä ja muuntaa lopuksi vastauksen takaisin puheeksi.

![Kuva1][Kuva1]

[Kuva1]: voiceGPT.png


## Välineet ja speksit
- Raspberry Pi 4 Model B
- Bluetooth kaiutin
- USB Headset mikrofoni


## Speksit
- OpenAI:ta varten luotava tunnukset ja hankittava projektilla API-avain:
	+ [Tehty sivuston ohjeiden mukaisesti](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key?context=python)
	+ OpenAI laskuttaa API:sta käytön mukaan (kts. tarkempi hinnasto [sivustolta.)](https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free)
- Puhe-tekstiksi ja teksti-puheeksi toiminnoissa taustalla käytin Googlen palveluja:
	+ Puhe tekstiksi: [Googlen Speech-To-Text](https://pypi.org/project/SpeechRecognition/)
	+ Teksti puheeksi: [Googlen Text-To-Speach](https://pypi.org/project/gTTS/)
- Python kirjastot:
	+ openai (OpenAI)
	+ speech_recognition (=Googlen Speech-To-Text)
	+ gtts (=Googlen Text-To-Speach)
	+ pygame.mixer (=odotusmusiikkia varten)
- mp3 äänitiedosto taustamusiikin soittoon, esim. [täältä.](https://pixabay.com/music/)


## Omia huomioita projektista
- Suomenkielinen puheentunnistus palvelu saattaa olla hieman epätarkka, mutta se toimii hyvin harrasteprojekteissa. Englanninkielinen tuki parantaisi todennäköisesti tarkkuutta merkittävästi.
- Lisäsin ohjelmaan taustamusiikkia odotusvaiheisiin. Tämä paransi mielestäni käyttäjäkokemusta, sillä esim. ChatGPT:n vastausta odottaessa ei tarvinnut kuunnella hiljaisuutta.
- ChatGPT:n vastaukset olivat joskus liian pitkiä, joten lisäsin promptiin ohjeen, että vastauksen tulisi olla lyhyt ja viihdyttävä.
- Yleisesti ottaen projektin toteuttaminen oli palkitsevaa ja mielenkiintoista. Internetistä löytyi paljon tietoa eri vaiheista, ja sain inspiraatiota ja lähteitä esimerkiksi:
	+ [VoiceGPT](https://www.hackster.io/nickbild/voicegpt-f88f8f)
	+ [ChatGPT + Raspberry Pi - A ChatGPT powered Raspberry Pi chatbot](https://youtu.be/lHxFFn04L10?si=tTpYD0P3A3huxNap)


## Ideoita ohjelman jatkokehitykseen
- Koodiin voisi lisätä aikakatkaisun, jos vastauksen saamisessa ChatGPT:ltä kuluu pidempään kuin x-aika.
- Ohjelmaan voisi lisätä lähes rajattomasti muitakin puhekäskyjä, myös sellaisia joihin ei tarvitse ChatGPT:tä (esim. systeemin sen hetkinen päivä tai aika).


