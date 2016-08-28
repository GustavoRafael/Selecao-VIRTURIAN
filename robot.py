import csv
import matplotlib.pyplot as plt
import numpy as np
from functools import partial
import decimal


# entrada e separacao das classes
wave0 =  []
normal = []
colisao = []
obstrucao = []
fr_colisao = []
histog = []

count_normal = 0
count_colisao = 0
count_obstrucao = 0
count_fr_colisao = 0

times = 3

# entrada e tratamento dos dados



with open('novo_LP01.data', 'rb') as robot:
    reader = csv.reader(robot)
    for row in reader:
        classe = row

        if classe[0] == "normal" and classe[1] != '' :
            normal.append(classe[1:7])
            #print(normal)

        elif classe[0] == 'collision' and classe[1] != '':
            colisao.append(classe[1:7])

        elif classe[0] == 'obstruction' and classe[1] != '':
            obstrucao.append(classe[1:7])

        elif classe[0] == 'fr_collision' and classe[1] != '':
            fr_colisao.append(classe[1:7])

    # media dos valores das instancias para as tres ondas
    media_normal = []
    media_colisao = []
    media_obstrucao = []
    media_fr_colisao = []
    media_entradas_criticas = []

    # media normal
    for cw in range(6):
        med_norm = ([float(i[cw]) for i in normal])
        media_normal.append(np.average((med_norm)))
    print(media_normal)
    # media colisao
    for cw in range(6):
        med_colisao = ([float(i[cw]) for i in colisao])
        media_colisao.append(np.average((med_colisao)))
    print(media_colisao)
    # media Obstrucao
    for cw in range(6):
        med_obstrucao = ([float(i[cw]) for i in obstrucao])
        media_obstrucao.append(np.average((med_obstrucao)))
    print(media_obstrucao)
    # media fr_colisao
    for cw in range(6):
        med_fr_colisao = ([float(i[cw]) for i in fr_colisao])
        media_fr_colisao.append(np.average((med_fr_colisao)))
    print(media_fr_colisao)

    # media das entradas criticas
    entradas_criticas = [media_colisao,media_colisao, media_obstrucao, media_fr_colisao]
    for cw in range(6):
        med_entradas_criticas = ([float(i[cw]) for i in entradas_criticas])
        media_entradas_criticas.append(np.average((med_entradas_criticas)))
    print(media_entradas_criticas)


    # plot das medias

    plt.plot(media_normal, 'B', label='Normal')
    plt.plot(media_colisao, 'R', label='colisao')
    plt.plot(media_obstrucao, 'G', label='obstrucao')
    plt.plot(media_fr_colisao, 'k', label='fr_colisao')
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.ylabel(' $ Valor\ Medio\ por\ atributo $', fontsize=20)
    plt.xlabel(' $ Forca(1,2,3)\ e\ Torque(4,5,6) $', fontsize=20)
    plt.title('Forca e Torque Para um Robot em 4 situacoes')
    plt.grid(True)
    #plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()

    # plot das medias

    plt.plot(media_normal, 'B', label='Normal')
    plt.plot(media_entradas_criticas, 'R', label='entradas_criticas')
    #plt.plot(media_obstrucao, 'G', label='obstrucao')
    #plt.plot(media_fr_colisao, 'k', label='fr_colisao')
    legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.ylabel(' $ Valor\ Medio\ por\ atributo $', fontsize=20)
    plt.xlabel(' $ Forca(1,2,3)\ e\ Torque(4,5,6) $', fontsize=20)
    plt.title('Comparacao entre o valor normal e a media das entradas criticas')
    plt.grid(True)
    # plt.savefig("test.png")
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()