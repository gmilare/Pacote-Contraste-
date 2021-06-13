# Importação das bibliotecas
import math
import rasterio as rst
import matplotlib.pyplot as plt
import numpy as np
import os

#Definindo a variável CURR_DIR que receberá o path do diretório atual, com o objetivo de listar os arquivos .TIF no display
CURR_DIR = os.getcwd()

#################################################################################

# Definindo a função Equalizacao e df, cdf e equalize_image
def df(DN):  # histograma
    values = [0]*65535
    for i in range(DN.shape[0]):
        for j in range(DN.shape[1]):
            values[DN[i,j]]+=1
    return values

def cdf(hist): # distribuição de frequencia cumulativa
    cdf = [0] * len(hist)
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i]= cdf[i-1]+hist[i]
    # normalização do histograma
    cdf = [ele*65535/cdf[-1] for ele in cdf]
    return cdf

def equalize_image(img): #aplicação da equalização
    my_cdf = cdf(df(img))
    image_equalized = np.interp(img, range(0,65535), my_cdf)
    return image_equalized

def EQUALIZACAO(): #função Equalizacao
    ### Bloco de código responsável por listar os arquivos .TIF (imagens) do diretório atual e exibi-los para o usuário escolher qual
    ### imagem ele deseja aplicar o contraste
    lista_arqs = [arq for arq in os.listdir(CURR_DIR)] # armazena em variável os arquivos presentes no diretório atual
    arquivos_tif = [a for a in lista_arqs if a[-4:] == '.tif'] # armazena em variável os arquivos .TIF do diretório atual
    tam = len(arquivos_tif) #Obtem o tamanho da lista de arquivos .TIF
    lista_pos_arquivos = [] #cria uma lista em branco para receber posteriormente a posição do arquivo na lista
    print('Arquivos .TIF listados no diretório raiz:') #printa para o usuário o cabeçalho da mensagem de arquivos .TIF
    for pos, arq in zip(range(1, tam + 1), arquivos_tif): #laço for que adiciona na lista criada acima a posição a partir de 1 do arquivo .TIF a lista
        lista_pos_arquivos.append(str(pos))
        print(pos, '-', arq) #printa na tela após a msg de cabeçalho os arquivos .TIF com um valor numérico sequencial
    image_pos = input('Entre com o número associado à imagem de satélite, de acordo com a lista acima: ') #input para o usuário escolher através do número sequencial qual arquivo ele deseja para entrada da imagem de satélite
    while image_pos not in lista_pos_arquivos: #laço criado para valores numéricos diferentes do armazenado na lista de posições
        image_pos = input('Valor não encontrado. Entre com o número associado à imagem de satélite: ') #msg para nova entrada de valores
    for pos, arq in zip(range(1, tam + 1), arquivos_tif): #novo laço for que armazena na variável image o nome do arquivo de imagem associada a posição na lista de arquivos
        if image_pos == str(pos):
            image = arq
    #Abertura da imagem e posterior leitura de cada uma das bandas através da biblioteca rasterio
    L8 = rst.open(image)
    red = L8.read(1)
    nir = L8.read(2)
    swir = L8.read(3)
    #Armazena em variáveis o shape da dimensão 0 e 1 do array da imagem (essa informação será usada no laço que percorrerá a imagem, modificando os valores do pixel após aplicação do contraste)
    linhas = red.shape[0]
    colunas = red.shape[1]
    print('EXECUTANDO...')
    #Aplica a função de Equalização
    fered = equalize_image(red)
    fenir = equalize_image(nir)
    feswir = equalize_image(swir)
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = feswir / 65535
    array_rgb[:, :, 1] = fenir / 65535
    array_rgb[:, :, 2] = fered / 65535

    # array para visualização de falsa-cor sem contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535

    # array para visualização de falsa-cor com contraste
    array_rgb_contraste = np.zeros((linhas, colunas, 3))
    array_rgb_contraste[:, :, 0] = feswir / 65535
    array_rgb_contraste[:, :, 1] = fenir / 65535
    array_rgb_contraste[:, :, 2] = fered / 65535

    # Computa os histogramas para as 3 bandas original e com contraste
    red_ori, x = np.histogram(red, bins=np.arange(65535))
    nir_ori, x = np.histogram(nir, bins=np.arange(65535))
    swir_ori, x = np.histogram(swir, bins=np.arange(65535))
    red_cont, x = np.histogram(fered, bins=np.arange(65535))
    nir_cont, x = np.histogram(fenir, bins=np.arange(65535))
    swir_cont, x = np.histogram(feswir, bins=np.arange(65535))

    # Plota as imagens e histogramas com e sem contraste
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(array_rgb)
    ax1.set_title('Imagem SEM contraste')

    ax2.imshow(array_rgb_contraste)
    ax2.set_title('Contraste Equalização')

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x[:-1], red_ori, 'r-', label='banda RED')
    ax1.plot(x[:-1], nir_ori, 'c-', label='banda NIR')
    ax1.plot(x[:-1], swir_ori, 'g-', label='banda SWIR')
    ax1.set_title('Histograma imagem original')
    ax1.set_xlim(0, 65535)
    ax1.set_ylim(0, 30000)
    ax1.set_xlabel('DN')
    ax1.set_ylabel('Frequência')
    ax1.grid(True)
    fig.legend(loc='center right')

    ax2.plot(x[:-1], red_cont, 'r-')
    ax2.plot(x[:-1], nir_cont, 'c-')
    ax2.plot(x[:-1], swir_cont, 'g-')
    ax2.set_title('Histograma imagem com contraste')
    ax2.set_xlim(0, 65535)
    ax2.set_ylim(0, 30000)
    ax2.set_xlabel('DN')
    ax2.set_ylabel('Frequência')
    ax2.grid(True)

    plt.show()