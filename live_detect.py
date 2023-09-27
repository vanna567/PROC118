# Importa la biblioteca opencv
import cv2

# Define un objeto video capture
vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
             

while(True):
   
    # Captura el video cuadro por cuadro
    ret, frame = vid.read()
    #escala de grises
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detecta rostros y rasgos
    faces = face_cascade.detectMultiScale(gray, 1.1,5)
    #crea el cuadro alrededor de las caras
    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       #roi_color = img[y:y + h, x:x + w]
       #cv2.imwrite("caras.jpg", roi_color)

    # Muestra el cuadro de resultado
    cv2.imshow("Web cam", frame)
      
    # Cierra la ventana con la tecla espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, libera el objeto capturado
vid.release()

# Cierra todas las ventanas
cv2.destroyAllWindows()