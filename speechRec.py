from numpy import tri
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyautogui
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
configfile = open('config.txt')
config = json.load(configfile)
commands = json.loads(config["keyboard"])
configfile.close()

def Listen ():
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
        
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            text = result_json['text']
            print(f"Recognized: {text}")

            # pyautogui.press('esc')




            
            flag = False
            for e in commands:
                if text == e["word"]:
                    if len(e["key"].split(",")) != 1 :
                        pyautogui.hotkey(*(e["key"].split(",")))
                    else:
                        pyautogui.press(e["key"])
                    
                    flag = True

            if not flag :
                pyautogui.typewrite(text)
    

            # if text == 'start' or text == 'a start' or text == 'the start' or text == 'star':
            #     pyautogui.press('win')
            # elif text == 'click' :
            #     pyautogui.click()
            # elif text == 'close' :
            #     pyautogui.hotkey('alt', 'f4')
            # elif text == 'minimize' :
            #     pyautogui.hotkey('win', 'd')
            # elif text == 'right click' :
            #     pyautogui.rightClick()
            # elif text == 'enter' :
            #     pyautogui.press('enter')
            # else :
            #     pyautogui.typewrite(text)

    