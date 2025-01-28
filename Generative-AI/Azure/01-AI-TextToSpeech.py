# pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

try:
    speech_config = SpeechConfig(subscription="25eb8d0ETHAN33b6e174dd44beb", region="eastus")
    #speech_config = SpeechConfig(subscription="010a95b0-90e2-4b29-b0c0-82569709bff4", region="eastus")

    #speech_config.speech_synthesis_voice_name="en-US-AriaNeural"
    #speech_config.speech_synthesis_voice_name="en-GB-MiaNeural"
    #speech_config.speech_synthesis_voice_name="en-AU-AnnetteNeural"
    #speech_config.speech_synthesis_voice_name="en-GB-SoniaNeural"
    #speech_config.speech_synthesis_voice_name="en-AU-FreyaNeural"
    #speech_config.speech_synthesis_voice_name="en-GB-RyanNeural"
    #speech_config.speech_synthesis_voice_name="en-US-JennyNeural"
    #speech_config.speech_synthesis_voice_name="en-US-GuyNeural"
    #speech_config.speech_synthesis_voice_name="en-IN-NeerjaNeural"
    #speech_config.speech_synthesis_voice_name="en-IN-PrabhatNeural"
    speech_config.speech_synthesis_voice_name="en-CA-ClaraNeural"
    #speech_config.speech_synthesis_voice_name="en-CA-LiamNeural"
    #speech_config.speech_synthesis_voice_name="en-US-NancyNeural"
    #speech_config.speech_synthesis_voice_name="en-US-SaraNeural"
    #speech_config.speech_synthesis_voice_name="en-GB-OliviaNeural"

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    #print("Type some text that you want to speak...")
    #text = input("Enter text : ")
    text="The Azure cloud platform is more than 200 products and cloud services designed to help you bring new solutions to life—to solve today’s challenges and create the future."
    #text="Hello everyone!!! Welcome to the school mates podcast series by sharayu and praful."
    #file=open("java.txt","r")
    #text=file.read()

    result = speech_synthesizer.speak_text_async(text).get()
except:
    print('error')


