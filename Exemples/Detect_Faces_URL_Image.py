__author__ = 'henrique.zinidasilva@student.hamk.fi'

import json
from watson_developer_cloud import VisualRecognitionV3

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key = '9b367cc730c4e57599441b0b9b01bb612eb25a1a' )

#URL da imagem a ser classificada
url_image='http://www.americareadsspanish.org/images/stories/amigos_espanol/angelina-jolie-2.jpg'


# Detectar Faces de uma imagem por URL
Resultados = VR.detect_faces(images_url=url_image)

#Mostra o resultado no formato json
print(json.dumps(Resultados))
