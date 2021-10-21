# import speech_recognition as sr
# r = sr.Recognizer()
# source = "womanSound.mp3" 
# print("Speak Anything :")
# #audio = r.listen(source)
# text = r.recognize_google(source)
# print("You said : {}".format(text))

import requests
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
#from urllib.parse import urlencode
from os import path
def transkriptiranjeKlipa(klip):
    #print('klip: '+klip)
    audioFilename = klip
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audioFilename)
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        #print(type(audio))
    #recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        
        ## stari google API
        #textWithoutPunctuation = r.recognize_google(audio)
        
        #NOVI GOOGLE CLOUD API
        with open("[REDACTED]") as f:
            GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
        textWithoutPunctuation = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language="en-US", show_all = False)
        
##        data = {
##            'text': textWithoutPunctuation
##        }    
##        response = requests.post(url = "http://bark.phon.ioc.ee/punctuator", data = data)
##        textWithPunctuation = response.text
##        
        #crl = pycurl.Curl()
        #crl.setopt(crl.URL, 'http://bark.phon.ioc.ee/punctuator')
        
        #data="text="+textWithoutPunctuation.replace(' ','%20')
        
        #crl.setopt(crl.POSTFIELDS, data)
        #crl.setopt(crl.WRITEFUNCTION, textWithPunctuation.write)
        #crl.perform()
        #crl.close()
        #print("Original recognition: "+"\n"+textWithoutPunctuation)
        #print("\n"+"Punctuated recognition: "+"\n"+textWithPunctuation)
        print(textWithoutPunctuation)
        return textWithoutPunctuation
        
        #print(crl)
        
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    headers = {}
    #recognize speech using Sphinx
    # try:
    #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # except sr.UnknownValueError:
    #     print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #     print("Sphinx error; {0}".format(e))
#transkriptiranjeKlipa('material/leofavecolorglasniji/leofavecolorglasniji.wav')
