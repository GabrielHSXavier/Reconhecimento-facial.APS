import face_recognition as fr
from engine import reconhece_face, get_rostos

desconhecido = reconhece_face("./img/desconhecido.png")
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rosto_cadastrados, nome_dos_rosto = get_rostos()
    resultados = fr.compare_faces(rosto_cadastrados, rosto_desconhecido)
    print(resultado)

    for i in range(len(rosto_cadastrados)):
        resultado = resultados[i]
        if(resultado):
            print("Rosto do", nome_dos_rosto[i], "foi reconhecido") 

else:
    print ("Não foi enconytrado nenhum rosto cadastrado")