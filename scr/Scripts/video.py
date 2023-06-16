# De um pip install ultralytics NO TERMINAL MESMO  
from ultralytics import YOLO #Lib do yolo
import cv2 #Lib Do openCV


model = YOLO("./best.pt") #Salvando o modelo ja trienado em uma variavel


cap = cv2.VideoCapture('../../img/arsene.mp4') #Escolhendo a camera

# Loop principal
if cap.isOpened(): #Verificar se a camera esta conctada
    print("Camera está pronta")
    verificar, frame = cap.read()
    
    while True:
        
        verificar, frame = cap.read() #Parametros para a camera capturar os frames

        
        results = model(frame) # Comparando o modelo treiando com o frame

        annotated_frame = results[0].plot()# Anotando o frame com as detecções

        results = model.predict(frame, stream=True)

        # Criando a caixa
        for result in results:
            # Obtendo as coordenadas dos verificarângulos das caixas delimitadoras
            boxes = result.boxes.cpu().numpy()

            # Iterando sobre as caixas delimitadoras
            for box in boxes:
                r = box.xyxy[0].astype(int) # Obtendo as coordenadas do verificarângulo
                print(r)

                
                cv2.rectangle(
                    frame, r[:2], r[2:], (150, 55, 200), 2)#Desenhando o verificarângulo no frame

                # Definindo a fonte e escrevendo o nome do objeto detectado
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(
                    frame,
                    result.names[int(box.cls[0])],
                    (r[0] + 6, r[1] - 20),
                    font,
                    1.0,
                    (0, 0, 0),
                    1,
                )
        # Exibindo o frame com as detecções na janela "Webcam"
        cv2.imshow("Video", frame)
        cv2.imwrite('../img/img_teste_faces_video.png', frame)

        key = cv2.waitKey(1)
        # Verificando se a tecla 'q' foi pressionada para sair do loop
        if key == 27:
            print("Saindo")
            break

# Liberando a captura de vídeo e fechando as janelas
cap.release() #Desligando a camera
cv2.destroyAllWindows() #Fechando a janela
