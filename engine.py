import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rosto = fr.face_encodings(foto)
    if(len(rosto) > 0):
        return True, rosto
    
    return False, []

def get_rostos():
    rostos_cadastrados = []
    nomes_dos_rostos = []

    gabriel1 = reconhece_face("./img/gabriel1.jpeg")
    if(gabriel1[0]):
        rostos_cadastrados.append(gabriel1[1][0])
        nomes_dos_rostos.append("Gabriel")

    renan1 = reconhece_face("./img/renan1.jpeg")
    if(renan1[0]):
        rostos_cadastrados.append(renan1[1][0])
        nomes_dos_rostos.append("Renan")

    return rostos_cadastrados, nomes_dos_rostos