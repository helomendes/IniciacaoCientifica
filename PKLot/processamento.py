import LBP
import KNN
import argparse
import os
import time
import numpy as np

#recebe como argumento o diretorio das imagens a serem analisadas
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagens", required=True, help="caminho para as imagens segmentadas")
args = vars(ap.parse_args())

#cronômetro pra ter ideia de tempo do algoritmo
start_time = time.time()

#define os caminhos principais a serem usados pelo programa
dirImgs = args["imagens"]
dirAtual = os.getcwd()
os.chdir(dirImgs)
dirImgs = os.getcwd()

csv_train = os.path.join(dirAtual, "LBP_Histograms_Train.csv")
csv_test = os.path.join(dirAtual, "LBP_Histograms_Test.csv")

print("\n\tEtapa 1: Local Binary Patterns")
image_processing = LBP.LocalBinaryPattern(dirAtual, dirImgs)
image_processing.LBP(csv_train, csv_test)

print("\n\tEtapa 2: K-Nearst Neighbors\n")
archive_processing = KNN.KNearstNeighbors(3)
archive_processing.KNN(csv_train, csv_test)

#cálculo tempo
end_time = time.time()
elapsed_time = end_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"\n\nTempo: {int(hours)} horas {int(minutes)} minutos and {seconds:.2f} segundos")