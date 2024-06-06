import cv2
import pyautogui
import time
pyautogui.FAILSAFE = False


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX


vid = cv2.VideoCapture(0)

def startTracking():
    detectedTime = 0; 
    fpsDetectedTime = 0
    LastPoint = [0,0]
    FirstPoint = [0,0]
    checked = False
    tmp_fps = 0
    fps = 0

    while(True):       
        
        ret , image = vid.read() 
         
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        

        width = vid.get(3) 
        height = vid.get(4) 

        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10, minSize=(150, 150))

        
        for (x, y, w, h) in faces:
            
            if w < 150 :
                continue
            
            #cv2.rectangle(image, (x, y), (x + w, y + h), (30,255,50), 2)
            
            if checked :
                cv2.rectangle(image, (int(FirstPoint[0]), int(FirstPoint[1])), (int(FirstPoint[0]) + 20, int(FirstPoint[1]) + 20), (200,100,100), 2)





            x = x + (0.5 * w)
            y = y + (0.5 * h)
            cv2.rectangle(image, (int(x-20), int(y-40)), (int(x) + 40, int(y) + 40), (50,200,50), 2)
            cv2.line(image, (int(FirstPoint[0])+10,int(FirstPoint[1])+10), (int(x),int(y)), (0, 255, 0), thickness=2, lineType=8)


            if not checked:
                checked = True;
                FirstPoint = [x,y]
                print(x - FirstPoint[0] ,y - FirstPoint[1])
                print(x , y)
            # else:
            #     cv2.rectangle(image, (x, y), (x + w, y + h), (30,255,50), 2)

            
            #print(x , w)
            mouseX =  (( -(x - FirstPoint[0])  + 120) / 240) * 1366
            mouseY = (( (y - FirstPoint[1] - 10)  + 30 ) / 60) * 768



            if abs(LastPoint[0] - x) < 4 and abs(LastPoint[1] - y) < 3 :
                if detectedTime != 0 :
                    # print(time.time() - detectedTime)
                    if(time.time() - detectedTime > 1):
                        detectedTime = 0  
                        pyautogui.leftClick(mouseX , mouseY)
                        
                else:
                   detectedTime = time.time()
            else :
                detectedTime = 0 
                print(x - FirstPoint[0] ,y - FirstPoint[1])
            pyautogui.moveTo(mouseX,mouseY)



            LastPoint = [x,y] 
            
            if(time.time() - fpsDetectedTime < 1):
                tmp_fps += 1
            else :
                fps = tmp_fps 
                tmp_fps = 0
                fpsDetectedTime = time.time()
            

            cv2.putText(image,('Movements Per Second : ' + str(fps)) ,(50,50),font, 1,(30, 30, 180),2,cv2.LINE_4) 
        cv2.imshow('Mouse Movements', image)
       


    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows()



