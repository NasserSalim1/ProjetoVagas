# Detecção de Vagas de Estacionamento em Tempo Real

Este projeto utiliza a biblioteca OpenCV para detectar vagas de estacionamento em uma imagem estática e em um vídeo em tempo real.

![image](https://github.com/NasserSalim1/ProjetoVagas/assets/87777276/39fd5b2e-5674-4dee-a180-4cd44208d334)


## Visão Geral

O objetivo deste projeto é fornecer uma solução para identificar vagas de estacionamento disponíveis em um estacionamento através do processamento de imagens estáticas e vídeos em tempo real. O processo é dividido em duas etapas principais:

1. **Seleção de Vagas de Estacionamento**: O script `detectar_vagas.py` permite ao usuário selecionar manualmente as regiões de interesse (ROIs) que representam as vagas de estacionamento em uma imagem do estacionamento. Essas informações são então salvas em um arquivo `vagas.pkl`.

2. **Detecção em Tempo Real**: O script `detecao_em_tempo_real.py` utiliza as informações das vagas salvas no arquivo `vagas.pkl` para analisar um vídeo em tempo real do estacionamento. Ele identifica vagas abertas e ocupadas e exibe uma contagem atualizada de vagas livres no vídeo.

## Como Usar

1. **Instalação de Dependências**: Certifique-se de ter Python instalado, juntamente com as seguintes bibliotecas:
   - OpenCV
   - pickle
   - numpy

2. **Execução dos Scripts**:
   - Execute o script `detectar_vagas.py` para selecionar manualmente as vagas de estacionamento na imagem do estacionamento e criar o arquivo `vagas.pkl`.
   - Com o arquivo `vagas.pkl` criado, execute o script `detecao_em_tempo_real.py` para iniciar a detecção em tempo real das vagas de estacionamento no vídeo fornecido.

## Implementação

### Seleção de Vagas de Estacionamento (`detectar_vagas.py`)

- O script carrega uma imagem do estacionamento usando a função `cv2.imread()`.
- Em seguida, utiliza a função `cv2.selectROI()` para permitir ao usuário selecionar manualmente as regiões de interesse (vagas de estacionamento) na imagem.
- As coordenadas das vagas selecionadas são armazenadas em uma lista e, em seguida, salvas em um arquivo `vagas.pkl` usando a biblioteca `pickle`.

### Detecção em Tempo Real (`detecao_em_tempo_real.py`)

- O script carrega as informações das vagas previamente selecionadas do arquivo `vagas.pkl` usando a biblioteca `pickle`.
- Ele inicializa um objeto `cv2.VideoCapture()` para capturar o vídeo do estacionamento em tempo real.
- A cada quadro do vídeo, a imagem é processada para identificar vagas abertas e ocupadas. Isso é feito através de:
  - Conversão da imagem para escala de cinza (`cv2.cvtColor()`).
  - Aplicação de um limiar adaptativo para destacar as áreas de interesse (`cv2.adaptiveThreshold()`).
  - Suavização da imagem com um filtro de mediana para reduzir o ruído (`cv2.medianBlur()`).
  - Dilatação da imagem para conectar componentes menores e preencher pequenos buracos (`cv2.dilate()`).
- As vagas são verificadas em relação ao número de pixels brancos para determinar se estão ocupadas ou livres.
- O número de vagas livres é contado e exibido no vídeo.

## Arquivos no Repositório

- `detectar_vagas.py`: Script para seleção manual de vagas de estacionamento e criação do arquivo `vagas.pkl`.
- `detecao_em_tempo_real.py`: Script para detecção em tempo real das vagas de estacionamento em um vídeo.
- `estacionamento.png`: Imagem do estacionamento para processamento.
- `Video.mp4`: Vídeo do estacionamento para análise em tempo real.
- `vagas.pkl`: Arquivo que armazena as coordenadas das vagas de estacionamento selecionadas.
