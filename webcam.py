import numpy as np
import face_recognition as fr
import cv2
from engine import get_rostos

rosto_cadastrados, nome_dos_rosto = get_rostos()

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    localizacao_do_rosto = fr.face_locations(rgb_frame)
    rosto_desconhecido = fr.face_encodings(rgb_frame, localizacao_do_rosto)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_do_rosto, rosto_desconhecido):
        resultados = fr.compare_faces(rosto_cadastrados, rosto_desconhecido)
        print(resultados)

        face_distances = fr.face_distance(rosto_cadastrados, rosto_desconhecido)

        melhor_id = np.argmin(face_distances)
        if resultados[melhor_id]:
            nome = nome_dos_rosto[melhor_id]
        else:
            nome = "Desconhecido"

        # quadrado do rosto
        cv2.rectangle(frame,(left,top), (right, bottom), (0, 0, 255), 2)

        # identificao
        cv2.rectangle(frame,(left,bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #texto
        cv2.putText(frame, nome, (left + 6,bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Webcam_facerecognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
