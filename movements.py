import cv2
import time
import json

from pynput.mouse import Button, Controller
mouse = Controller()

# تحريك الماوس إلى موقع معين
import mediapipe as mp

# تحميل Face Mesh من MediaPipe
mp_face_mesh = mp.solutions.face_mesh

# إعداد MediaPipe Face Mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX


vid = cv2.VideoCapture(0)

def startTracking():
    #load config 
    configfile = open('config.txt')
    config = json.load(configfile)
    configfile.close()

    Xsen = 450 - int(config["xSen"]) 
    Ysen = 220 - int(config["ySen"]) 
    clickTime = int(config["clickAfter"]) 


    detectedTime = 0; 
    fpsDetectedTime = 0
    LastPoint = [0,0]
    FirstPoint = [0,0]
    checked = False
    tmp_fps = 0
    fps = 0

    while(True):       
        
        ret , image  = vid.read() 
         
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

      

        rgb_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # كشف معالم الوجه
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                ih, iw, _ = image.shape
                # نقاط الأنف من معالم الوجه
                nose_landmark = face_landmarks.landmark[1]  # رقم 1 في MediaPipe هو طرف الأنف

                # تحويل إحداثيات النقطة إلى بكسل
                x = int(nose_landmark.x * iw)
                y = int(nose_landmark.y * ih)


                if not checked:
                    checked = True;
                    FirstPoint = [x,y]
                    print(x - FirstPoint[0] ,y - FirstPoint[1])
                    print(x , y)
                # else:
                #     cv2.rectangle(image, (x, y), (x + w, y + h), (30,255,50), 2)

                
                #print(x , w)
                mouseX =  (( -(x - FirstPoint[0])  + Xsen/2) / Xsen) * 1920
                mouseY = (( (y - FirstPoint[1] - 10)  + Ysen/2 ) / Ysen) * 1080


                
                if abs(LastPoint[0] - x) < 4 and abs(LastPoint[1] - y) < 3 and config["aclick"] == "1" :
                    if detectedTime != 0 :
                        # print(time.time() - detectedTime)
                        if(time.time() - detectedTime > clickTime):
                            detectedTime = 0  
                            mouse.click(Button.left, 1)

                    else:
                        detectedTime = time.time()
                else :
                    detectedTime = 0 
                    print(x - FirstPoint[0] ,y - FirstPoint[1])
                mouse.position = (mouseX, mouseY)




                LastPoint = [x,y] 
                
                if(time.time() - fpsDetectedTime < 1):
                    tmp_fps += 1
                else :
                    fps = tmp_fps 
                    tmp_fps = 0
                    fpsDetectedTime = time.time()
                

                cv2.putText(image,('Movements Per Second : ' + str(fps)) ,(50,50),font, 1,(30, 30, 180),2,cv2.LINE_4) 
                    # رسم مربع حول الأنف
                size = 20  # حجم المربع
                cv2.rectangle(image, (x - size, y - size), (x + size, y + size), (0, 255, 0), 2)

                if checked :
                    cv2.rectangle(image, (int(FirstPoint[0]), int(FirstPoint[1])), (int(FirstPoint[0]) + 20, int(FirstPoint[1]) + 20), (200,100,100), 2)

        cv2.imshow('Mouse Movements', image)
       


    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows()



