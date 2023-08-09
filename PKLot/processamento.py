import LBP
import KNN
import argparse
import os
import time
import numpy as np
import csv
import matplotlib.pyplot as plt

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

print("\nEtapa 1: Local Binary Patterns")
image_processing = LBP.LocalBinaryPattern(dirAtual, dirImgs)
for estacionamento in os.listdir(dirImgs):
    print("\n\tEstacionamento: ", estacionamento)
    csv_train = os.path.join(dirAtual, f"LBP_Histograms_Train_{estacionamento}.csv")
    csv_test = os.path.join(dirAtual, f"LBP_Histograms_Test_{estacionamento}.csv")
    image_processing.PKLotLBP(csv_train, csv_test, estacionamento)

lbp_time = time.time()
elapsed_time = lbp_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"\n\nTempo LBP: {int(hours)} horas {int(minutes)} minutos e {seconds:.2f} segundos")
print("\n\nEtapa 2: K-Nearst Neighbors\n")

for k in (3, 7, 11):
    archive_processing = KNN.KNearstNeighbors(k)
    print(f"\nK = {k}  Single parking lot training and testing:\n")
    print("\n\tPUC\n")
    archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_PUC.csv", f"{dirAtual}/LBP_Histograms_Test_PUC.csv")
    print("\n\tUFPR04\n")
    archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR04.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR04.csv")
    print("\n\tUFPR05\n")
    archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR05.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR05.csv")

    matrix = []
    print(f"\n\tSingle parking lot training and multiple parking lot testing:\n")
    print("\n\tUFPR04 x PUC\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR04.csv", f"{dirAtual}/LBP_Histograms_Test_PUC.csv")
    matrix.append([ac, f1, "UFPR04 x PUC"])
    print("\n\tUFPR04 x UFPR05\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR04.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR05.csv")
    matrix.append([ac, f1, "UFPR04 x UFPR05"])
    
    print("\n\tUFPR05 x UFPR04\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR05.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR04.csv")
    matrix.append([ac, f1, "UFPR05 x UFPR04"])
    print("\n\tUFPR05 x PUC\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_UFPR05.csv", f"{dirAtual}/LBP_Histograms_Test_PUC.csv")
    matrix.append([ac, f1, "UFPR05 x PUC"])
    
    print("\n\tPUC x UFPR04\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_PUC.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR04.csv")
    matrix.append([ac, f1, "PUC x UFPR04"])
    print("\n\tPUC x UFPR05\n")
    ac, f1 = archive_processing.KNN(f"{dirAtual}/LBP_Histograms_Train_PUC.csv", f"{dirAtual}/LBP_Histograms_Test_UFPR05.csv")
    matrix.append([ac, f1, "PUC x UFPR05"])

    ac = [linha[0] for linha in matrix]
    f1 = [linha[1] for linha in matrix]
    nomes = [linha[2] for linha in matrix]

    plt.figure(figsize=(8,6))
    plt.scatter(ac, f1, color='blue', label='Pontos')

    for i, txt, in enumerate(matrix):
        plt.text(ac[i], f1[i], nomes[i], fontsize=9, ha='center', va='bottom')

    plt.xlabel('Acurácia')
    plt.ylabel('F1-Score')
    plt.title('Relação entre Acurácia e F1-Score')
    plt.grid(True)

    plt.savefig(f"{dirAtual}/Grafico_Dispersao_{k}.png")

#cálculo tempo
end_time = time.time()
elapsed_time_knn = end_time - lbp_time
hours, remainder = divmod(elapsed_time_knn, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"\n\nTempo KNN: {int(hours)} horas {int(minutes)} minutos e {seconds:.2f} segundos")

end_time = time.time()
elapsed_time += elapsed_time_knn
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"\n\nTempo: {int(hours)} horas {int(minutes)} minutos e {seconds:.2f} segundos")