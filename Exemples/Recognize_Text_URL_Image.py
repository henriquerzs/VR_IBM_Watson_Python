__author__ = 'henrique.zinidasilva@student.hamk.fi'

import json
from watson_developer_cloud import VisualRecognitionV3

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key = 'YOUR_API_KEY' )

#URL da imagem a ser classificada
url_image='http://i.imgur.com/BTT8zsO.jpg'


# Detectar Faces de uma imagem por URL
Resultados = VR.recognize_text(images_url=url_image)

#Mostra o resultado no formato json
print(json.dumps(Resultados))
