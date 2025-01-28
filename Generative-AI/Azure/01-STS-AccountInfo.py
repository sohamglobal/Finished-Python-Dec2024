import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import pymysql


#speech_config.speech_synthesis_voice_name="en-US-AriaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-MiaNeural"
speech_config.speech_synthesis_voice_name="en-GB-RyanNeural"
#speech_config.speech_synthesis_voice_name="en-US-JennyNeural"
#speech_config.speech_synthesis_voice_name="en-US-GuyNeural"
#speech_config.speech_synthesis_voice_name="en-IN-NeerjaNeural"
#speech_config.speech_synthesis_voice_name="en-IN-PrabhatNeural"
#speech_config.speech_synthesis_voice_name="en-CA-ClaraNeural"
#speech_config.speech_synthesis_voice_name="en-CA-LiamNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
speech_config = speechsdk.SpeechConfig(subscription="25eb8d0ETHAN59a33b6e174dd44beb", region="eastus")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)


def from_mic():
    try:

        print("Speak account number : ")
        accno = speech_recognizer.recognize_once_async().get()
        print(accno.text)
        no=int(accno.text[:4])

        con=pymysql.connect(host='bixxegmwtl9a9xkbdrih-mysql.services.clever-cloud.com',user='uzyalmtlztnwutid',password='CDbYfQLWfmGBX1ZU3Uh2',database='bixxegmwtl9a9xkbdrih')
        curs=con.cursor()
        curs.execute("select accnm,balance from accounts where accno=%d" %no)
        rec=curs.fetchone()
        try:
            text='Account Name is '+rec[0]+' and balance is '+str(rec[1])
            print(text)
        except:
            text='account does not exist'

        con.close()

        result = speech_synthesizer.speak_text_async(text).get()

        
    except Exception as ex:
        print(ex)

from_mic()



