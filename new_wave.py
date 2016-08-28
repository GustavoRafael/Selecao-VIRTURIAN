import csv
import matplotlib.pyplot as plt
import numpy as np
from functools import partial
import decimal


# entrada e separacao das classes
wave0 =  []
wave_1 = []
wave_2 = []
wave_3 = []
histog = []
with open('waveform.data', 'rb') as wave:
    reader = csv.reader(wave)
    for row in reader:
        classe = row
        histog.append(int(classe[21]))
        if classe[21] == "0":
            wave_1.append(classe[0:21])
            #wave_1 = np.asarray(wave0)
        elif classe[21] == "1":
            wave_2.append(classe[0:21])
        else: #classe[21] == "2"
            wave_3.append(classe[0:21])

    # media dos valores das instancias para as tres ondas
    media_w1 = []
    media_w2 = []
    media_w3 = []
    # medias wave_01
    for cw in range(21):
        npwave_1 = ([float(i[cw]) for i in wave_1])
        media_w1.append(np.average((npwave_1)))

    #medias wave_02
    for cw in range(21):
        npwave_2 = ([float(i[cw]) for i in wave_2])
        media_w2.append(np.average((npwave_2)))

    # medias wave_03
    for cw in range(21):
        npwave_3 = ([float(i[cw]) for i in wave_3])
        media_w3.append(np.average((npwave_3)))

    # plot das medias

    plt.plot(media_w1, 'B', label='wave_01')
    plt.plot(media_w2, 'R', label='wave_02')
    plt.plot(media_w3, 'G', label='wave_03')
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.ylabel(' $ Media\ por\ atributo $', fontsize=20)
    plt.xlabel(' $ Numero\ do\ atributo $', fontsize=20)
    plt.title('Medias dos atributo das ondas.')
    plt.grid(True)
    #plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()

    # Desvio padrao
    # Desvio dos valores das instancias para as tres ondas
    desv_w1 = []
    desv_w2 = []
    desv_w3 = []
    # medias wave_01
    for cw in range(21):
        npwave_1 = ([float(i[cw]) for i in wave_1])
        desv_w1.append(np.std((npwave_1)))
    #print(desv_w1)
    # medias wave_02
    for cw in range(21):
        npwave_2 = ([float(i[cw]) for i in wave_2])
        desv_w2.append(np.std((npwave_2)))
    #print(desv_w2)
    # medias wave_03
    for cw in range(21):
        npwave_3 = ([float(i[cw]) for i in wave_3])
        desv_w3.append(np.std((npwave_3)))
    #print(desv_w3)

    # plot dos devios padrao

    plt.plot(desv_w1, 'B', label='desv_01')
    plt.plot(desv_w2, 'R', label='desv_02')
    plt.plot(desv_w3, 'G', label='desv_03')
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.ylabel(' $ Desvio Padrao\ por\ atributo $', fontsize=20)
    plt.xlabel(' $ Numero\ do\ atributo $', fontsize=20)
    plt.title('Desvio Padrao dos atributo das ondas.')
    plt.grid(True)
    # plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()

    #Plot onda 1: media - desvio padrao
    # plot dos devios padrao

    plt.plot(media_w1, 'B', label='media_01')
    plt.plot(desv_w1, 'R', label='desv_01')
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.ylabel(' $ Media e Desvio Padrao\ por\ atributo $', fontsize=20)
    plt.xlabel(' $ Numero\ do\ atributo $', fontsize=20)
    plt.title('Media e Desvio Padrao dos atributo da Onda 1.')
    plt.grid(True)
    # plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()
    # npwave_1 = np.concatenate(wave_1[,0])

    #Distribuicao das classes de ondas nos dados

    plt.hist(histog, bins='auto')  # plt.hist passes it's arguments to np.histogram
    plt.title("Distriuicao das classes nos dados")
    plt.ylabel(' $ Quantidade $', fontsize=20)
    plt.xlabel(' $ Onda $', fontsize=20)
    plt.grid(True)
    # plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()
    print(histog)

    size_w1 = len(wave_1)
    size_w2 = len(wave_2)
    size_w3 = len(wave_3)
    print(size_w1)
    print(size_w2)
    print(size_w3)
