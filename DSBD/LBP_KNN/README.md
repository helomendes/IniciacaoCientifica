Esse projeto foi baseado epecíficamente na estrutura do [Parking Lot Database](https://web.inf.ufpr.br/vri/databases/parking-lot-database)

O programa a ser executado é o processamento.py, ele apenas fará uso das bibliotecas LBP.py e KNN.py, além de cronometrar o tempo de execução.

É passado como argumento na linha de comando o diretório pai de onde estão armazenadas as imagens a serem processadas, neste caso, o programa é específico para receber como argumento a pasta /PKLot/PKLotSegmented do dataset citado.
Mas pode ser facilmente ajustada alterando alguns loops de varredura de pastas da biblioteca LBP.py.

Local Binary Patterns
A primeira etapa do programa trata do modelo descritor de textura Local Binary Patterns (LBP).
A biblioteca LBP.py é usada unicamente para o desenvolvimento deste modelo.
Foram utilizadas as bibliotecas os, csv, cv2, numpy e imutils.paths.
Nela é descrita a classe LocalBinaryPattern, constituida pelos metodos getValor(), calculoLBP() e LBP(), sendo o último deles o principal.
No metodo LBP(), são passados como parâmetros o nome desajado para os arquivos csv gerados ao fim do programa, um para o conjunto de treino e outro para o de teste.


assim, cada imagem segmentada do dataset é:
  carregada
  transformada para escala cinza
  usada como base para gerar uma imagem LBP

K-Nearst Neighbors
