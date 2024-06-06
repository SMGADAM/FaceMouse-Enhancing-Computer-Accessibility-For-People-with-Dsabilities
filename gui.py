# hello.py
import eel
import movements
import time
import threading
import speechRec




eel.init('web')

@eel.expose
def track(x) :
    time.sleep(0.5)
    thread_a = threading.Thread(target=movements.startTracking)
    thread_b = threading.Thread(target=speechRec.Listen)
    thread_b.start()
    thread_a.start()

eel.start('main.html')
