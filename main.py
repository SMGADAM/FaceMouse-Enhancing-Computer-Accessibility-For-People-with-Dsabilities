import eel
import movements
import time
import threading
import speechRec
import json

configfile = open('config.txt')
config = json.load(configfile)


eel.init('web')


@eel.expose 
def refreshKeyboard() :
    return (config['keyboard'])

@eel.expose 
def SetKeyboard(e) :
    config["keyboard"] = e
    with open("config.txt", 'w') as file:
        file.write(json.dumps(config))
    print(json.dumps(config))


@eel.expose
def getClick() :
    return config['aclick'];

@eel.expose
def getXsen() :
    return config['xSen'];


@eel.expose
def getYsen() :
    return config['ySen'];


@eel.expose
def getClickTime() :
    return config['clickAfter'];



@eel.expose
def setAclick() :
    if config["aclick"] == "0":
        config["aclick"] = "1"
    else:
        config["aclick"] = "0"

    with open("config.txt", 'w') as file:
        file.write(json.dumps(config))

    print(json.dumps(config))

@eel.expose
def setClickAfter(v) :
    config["clickAfter"] = int(v)
    with open("config.txt", 'w') as file:
        file.write(json.dumps(config))
    print(json.dumps(config))
@eel.expose
def setXsen(v) :
    config["xSen"] = int(v)
    with open("config.txt", 'w') as file:
        file.write(json.dumps(config))
    print(json.dumps(config))

@eel.expose
def setYsen(v) :
    config["ySen"] = int(v)
    with open("config.txt", 'w') as file:
        file.write(json.dumps(config))
    print(json.dumps(config))




@eel.expose
def track(x) :
    time.sleep(0.5)
    thread_a = threading.Thread(target=movements.startTracking)
    thread_b = threading.Thread(target=speechRec.Listen)
    thread_b.start()
    thread_a.start()

eel.start('main.html')

configfile.close()
