import os
import csv
import cv2
import numpy as np
from imutils import paths

class LocalBinaryPattern:
    def __init__(self, dirSalvar, dirImagens):
        self.Salvar = dirSalvar
        self.Imagens = dirImagens
   
    #define se o valor do pixel vizinho deve ser 0 ou 1
    def getValor(self, img, center, x, y):
        new_value = 0
        try:
            if img[x][y] >= center:
                    new_value = 1
        except:
            pass
        return new_value

    #obtem os valores dos pixels vizinhos e calcula o valor do pixel central para a imagem LBP
    #usa a função getValor para cada um dos 8 pixels vizinhos de forma uniforme, começando pelo canto superior esquerdo
    #transforma o binário obtido para base decimal e retorna o decimal
    def calculoLBP(self, img, x, y):
        center = img[x][y]
        val_ar = []
        val_ar.append(self.getValor(img, center, x-1, y+1))
        val_ar.append(self.getValor(img, center, x, y+1))
        val_ar.append(self.getValor(img, center, x+1, y+1))
        val_ar.append(self.getValor(img, center, x+1, y))
        val_ar.append(self.getValor(img, center, x+1, y-1))
        val_ar.append(self.getValor(img, center, x, y-1))
        val_ar.append(self.getValor(img, center, x-1, y-1))
        val_ar.append(self.getValor(img, center, x-1, y))
        val_exp = [1, 2, 4, 8, 16, 32, 64, 128]
        val = 0
        for i in range(len(val_ar)):
            val += val_ar[i] * val_exp[i]
        return val

    def LBP(self, diretorio, val_class):
        histograms = []
        for imagem in paths.list_images(diretorio):
            img = cv2.imread(imagem)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            height, width = gray_img.shape
            #gera uma imagem de mesma proporção com 0 em todos os pixels (imagem preta)
            lbp_img = np.zeros((height, width), np.uint8)
            #preenche a imagem com os mumeros gerados pelo calculo lbp
            for i in range (height):
                for j in range (width):
                    lbp_img[i, j] = self.calculoLBP(gray_img, i, j)
            #calculo do histograma
            hist = cv2.calcHist([lbp_img], [0], None, [256], [0, 256])
            histograms.append([val_class] + np.ravel(hist).tolist())
        return histograms
    
    def PKLotLBP(self, csv_treino, csv_teste, diretorio):
        header = []
        header.append("Classe")
        for i in range (256):
            header.append(i)

        file_treino = open(csv_treino, 'w')
        treino = csv.writer(file_treino)
        treino.writerow(header)
        file_teste = open(csv_teste, 'w')
        teste = csv.writer(file_teste)
        teste.writerow(header)

        hist1 = []
        hist2 = []
        contador = 0
        for dia in os.listdir(diretorio):
            diretorioDia = os.path.join(diretorio, dia)    
            for classe in os.listdir(diretorioDia):
                diretorioClasse = os.path.join(diretorioDia, classe)
                if (classe.lower() == "empty"):
                    val_class = 0
                elif (classe.lower() == "occupied"):
                    val_class = 1
                if (contador % 2 == 0):
                    hist1 += self.LBP(diretorioClasse, val_class)
                else:
                    hist2 += self.LBP(diretorioClasse, val_class)
            contador += 1

        for hists1 in hist1:
            treino.writerow(hists1)
        for hists2 in hist2:
            teste.writerow(hists2)
        
        file_treino.close()
        file_teste.close()
        
        file_treino = open(csv_treino, 'r')
        linhas = file_treino.readlines()
        print("\n\ttreino: ", len(linhas)-1)
        file_treino.close()
        
        file_teste = open(csv_teste, 'r')
        linhas = file_teste.readlines()
        print("\tteste: ", len(linhas)-1)
        file_teste.close()
        