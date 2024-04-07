import cv2
import pickle # Biblioteca do python que permite salvar um objeto de dentro da programação em um ambiente externo. Então salvamos esse arquivo com algumas infos e dps podemos recuperar essa infos

img = cv2.imread('estacionamento.png') # Abre a img

vagas = []

for x in range(69): # 69 é o número de vagas do estacionamento do vídeo usado como base
    vaga = cv2.selectROI('vagas', img, False) # Nos permite selecionar um ROI(espaço da imagem) manualmente 
    cv2.destroyWindow('vagas')
    vagas.append((vaga))

    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)

# Depois de rodas pelas 69 vagas ele criará esse arquivo
with open('vagas.pkl', 'wb') as arquivo: # Estou criando o arquivo "vagas" e o "wb" indica que vou escrever um dado nele. "as arquivos" salva ele dentro da variável
    pickle.dump(vagas, arquivo) 