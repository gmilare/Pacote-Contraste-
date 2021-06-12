# Importação das bibliotecas
import math
import rasterio as rst
import matplotlib.pyplot as plt
import numpy as np
import os

#Definindo a variável CURR_DIR que receberá o path do diretório atual, com o objetivo de listar os arquivos .TIF no display
CURR_DIR = os.getcwd()

#################################################################################
#BLOCO DE CÓDIGO RESPONSÁVEL PELA APLICAÇÃO DAS FUNÇÕES DE CONTRASTE EM TODA A IMAGEM

# Definindo a função RaizQuadrada e RQ, sendo a função RQ a que implementa a matemática por trás da aplicação do contraste Raiz Quadrada
def RQ(DN):
    FatordeAjuste = 65535 / (math.sqrt(65535))
    y = (FatordeAjuste * math.sqrt(DN))
    return y
def RaizQuadrada():
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
    #printa a msg de executando, para o usuário entender que o programa está sendo executado
    print('EXECUTANDO...')
    #laço for que aplica a função de contraste percorrendo o array
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i][j] = RQ(red[i][j])
            nir[i][j] = RQ(nir[i][j])
            swir[i][j] = RQ(swir[i][j])
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    #Cria um array com valores zerados para receber os valores das bandas modificadas, com o intuito de plotar a composição colorida do contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste Raiz Quadrada')
    return plt.show()

# Definindo a função Quadrático e Qq, sendo a função Qq a que implementa a matemática por trás da aplicação do contraste Quadrático
def Qd(DN):
    FatordeAjuste = 1/65535
    y = (FatordeAjuste * math.pow(DN, 2))
    return y
def Quadratico():
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
    #printa a msg de executando, para o usuário entender que o programa está sendo executado
    print('EXECUTANDO...')
    #laço for que aplica a função de contraste percorrendo o array
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i][j] = Qd(red[i][j])
            nir[i][j] = Qd(nir[i][j])
            swir[i][j] = Qd(swir[i][j])
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    #Cria um array com valores zerados para receber os valores das bandas modificadas, com o intuito de plotar a composição colorida do contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste Quadrático')
    return plt.show()

# Definindo a função MinMax e mm, sendo a função mm a que implementa a matemática por trás da aplicação do contraste MinMax
def mm(DN, max, min):
    tan_ang_MinMax = (65535 / (max - min))
    y = tan_ang_MinMax * DN
    return y
def MinMax():
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
    #Armazena em variáveis os valores mínimos e máximos das bandas RED, NIR e SWIR
    min_red = red.min()
    max_red = red.max()
    min_nir = nir.min()
    max_nir = nir.max()
    min_swir = swir.min()
    max_swir = swir.max()
    #Armazena em variáveis o shape da dimensão 0 e 1 do array da imagem (essa informação será usada no laço que percorrerá a imagem, modificando os valores do pixel após aplicação do contraste)
    linhas = red.shape[0]
    colunas = red.shape[1]
    #printa a msg de executando, para o usuário entender que o programa está sendo executado
    print('EXECUTANDO...')
    #laço for que aplica a função de contraste percorrendo o array
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i][j] = mm(red[i][j],max_red, min_red)
            nir[i][j] = mm(nir[i][j], max_nir, min_nir)
            swir[i][j] = mm(swir[i][j], max_swir, min_swir)
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    #Cria um array com valores zerados para receber os valores das bandas modificadas, com o intuito de plotar a composição colorida do contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste MinMax')
    return plt.show()

# Definindo a função Linear e lin, sendo a função lin a que implementa a matemática por trás da aplicação do contraste Linear
def lin(DN, max, min):
    y = ((65535 / (max - min)) * (DN - min))
    return y

def Linear():
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
    #Armazena em variáveis os valores mínimos e máximos das bandas RED, NIR e SWIR
    min_red = red.min()
    max_red = red.max()
    min_nir = nir.min()
    max_nir = nir.max()
    min_swir = swir.min()
    max_swir = swir.max()
    #Armazena em variáveis o shape da dimensão 0 e 1 do array da imagem (essa informação será usada no laço que percorrerá a imagem, modificando os valores do pixel após aplicação do contraste)
    linhas = red.shape[0]
    colunas = red.shape[1]
    #printa a msg de executando, para o usuário entender que o programa está sendo executado
    print('EXECUTANDO...')
    #laço for que aplica a função de contraste percorrendo o array
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i][j] = lin(red[i][j],max_red, min_red)
            nir[i][j] = lin(nir[i][j], max_nir, min_nir)
            swir[i][j] = lin(swir[i][j], max_swir, min_swir)
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    #Cria um array com valores zerados para receber os valores das bandas modificadas, com o intuito de plotar a composição colorida do contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste Linear')
    return plt.show()

# Definindo a função Negativo e neg, sendo a função neg a que implementa a matemática por trás da aplicação do contraste Negativo
def neg(DN, max, min):
    y = ((-1 * (65535 / (max - min))) * (DN - max))
    return y

def Negativo():
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
    #Armazena em variáveis os valores mínimos e máximos das bandas RED, NIR e SWIR
    min_red = red.min()
    max_red = red.max()
    min_nir = nir.min()
    max_nir = nir.max()
    min_swir = swir.min()
    max_swir = swir.max()
    #Armazena em variáveis o shape da dimensão 0 e 1 do array da imagem (essa informação será usada no laço que percorrerá a imagem, modificando os valores do pixel após aplicação do contraste)
    linhas = red.shape[0]
    colunas = red.shape[1]
    #printa a msg de executando, para o usuário entender que o programa está sendo executado
    print('EXECUTANDO...')
    #laço for que aplica a função de contraste percorrendo o array
    for i in range(red.shape[0]):
        for j in range(red.shape[1]):
            red[i][j] = neg(red[i][j],max_red, min_red)
            nir[i][j] = neg(nir[i][j], max_nir, min_nir)
            swir[i][j] = neg(swir[i][j], max_swir, min_swir)
    #printa a msg de finalização da aplicação do contraste no array
    print('FINALIZADO!!!')
    #Cria um array com valores zerados para receber os valores das bandas modificadas, com o intuito de plotar a composição colorida do contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste Negativo')
    return plt.show()

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

def Equalizacao(): #função Equalizacao
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
    #Plota via matplotlib.pyplot o array contrastado e dá um título ao plot
    plt.imshow(array_rgb)
    plt.title('Contraste Equalização')
    return plt.show()

#################################################################################
#BLOCO DE CÓDIGO RESPONSÁVEL PELA APLICAÇÃO DAS FUNÇÕES DE CONTRASTE OTIMIZADO POR CLASSE E PERSONALIZADO POR CLASSE

# Definindo a função PorClasse
def PorClasse():
    #################################################################################
    # Definições o conjunto das Funções de Contraste que serão utilizadas nos contrastes otimizado e personalizado
    # Função Raiz Quadrada
    def RaizQuadrada(DN):
        FatordeAjuste = 65535 / (math.sqrt(65535))
        y = (FatordeAjuste * math.sqrt(DN))
        return y

    # Função Quadrático
    def Quadratico(DN):
        FatordeAjuste = 1 / 65535
        y = (FatordeAjuste * math.pow(DN, 2))
        return y

    # Função de contraste MinMax
    def MinMax(DN, max, min):
        tan_ang_MinMax = (65535 / (max - min))
        y = tan_ang_MinMax * DN
        return y

    # Função de contraste Linear
    def Linear(DN, min, max):
        y = (65535 / (max - min)) * (DN - min)
        return y

    # Função de contraste Negativo
    def Negativo(DN, min, max):
        y = ((-1 * (65535 / (max - min))) * (DN - max))
        return y

    # Função de equalização
    def df(DN): # histograma
        values = [0] * 65535
        for i in range(DN.shape[0]):
            for j in range(DN.shape[1]):
                values[DN[i, j]] += 1
        return values

    def cdf(hist): # distribuição de frequencia cumulativa
        cdf = [0] * len(hist)
        cdf[0] = hist[0]
        for i in range(1, len(hist)):
            cdf[i] = cdf[i - 1] + hist[i]
        # normalização do histograma
        cdf = [ele * 65535 / cdf[-1] for ele in cdf]
        return cdf

    def equalize_image(image):
        my_cdf = cdf(df(image))
        image_equalized = np.interp(image, range(0, 65535), my_cdf)
        return image_equalized
    #################################################################################
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
    classe_pos = input('Entre com o número associado à imagem classificada - Mapbiomas, de acordo com a lista acima: ') #input para o usuário escolher através do número sequencial qual arquivo ele deseja para entrada da imagem do Mapbiomas
    while classe_pos not in lista_pos_arquivos: #laço criado para valores numéricos diferentes do armazenado na lista de posições
        classe_pos = input('Valor não encontrado. Entre com o número associado à imagem classificada - Mapbiomas: ') #msg para nova entrada de valores
    for pos, arq in zip(range(1, tam + 1), arquivos_tif): #novo laço for que armazena na variável image o nome do arquivo de imagem associada a posição na lista de arquivos
        if classe_pos == str(pos):
            classe = arq
    #Abertura das imagens L8 e Mapbiomas e posterior leitura de cada uma das bandas através da biblioteca rasterio
    mapbiomas = rst.open(classe) #abertura da imagem Mapbiomas
    L8 = rst.open(image) #abertura da imagem L8
    banda_classificada_array = mapbiomas.read(1) #leitura da banda da imagem Mapbiomas
    # leitura das bandas da imagem L8
    red = L8.read(1)
    nir = L8.read(2)
    swir = L8.read(3)
    ## obter os mínimos e os máximos de cada banda do L8
    min_red = red.min()
    max_red = red.max()
    min_nir = nir.min()
    max_nir = nir.max()
    min_swir = swir.min()
    max_swir = swir.max()
    #Armazena em variáveis o shape da dimensão 0 e 1 do array da imagem (essa informação será usada no laço que percorrerá a imagem, modificando os valores do pixel após aplicação do contraste)
    linhas = red.shape[0]
    colunas = red.shape[1]
    ## array para visualização de falsa-cor sem contraste
    array_rgb = np.zeros((linhas, colunas, 3))
    ## valores entre 0-1
    array_rgb[:, :, 0] = swir / 65535
    array_rgb[:, :, 1] = nir / 65535
    array_rgb[:, :, 2] = red / 65535
    # criando variáveis para aplicação do contraste de Equalização
    fered = equalize_image(red)
    fenir = equalize_image(nir)
    feswir = equalize_image(swir)
    # Entrada de teclado do usuário para escolher entre o contraste otimizado ou personalizado
    escolha = input('Você deseja aplicar um contraste otimizado por classe ou personalizado? Digite 1 para otimizado e 2 para personalizado: ')
    while escolha != '1' and escolha != '2': #laço criado para valores numéricos diferentes do armazenado entrada de teclado da escolha do contraste
        escolha = input('Valor incorreto. Entre com 1 para otimizado e 2 para personalizado: ')

    ###########################################################################################
    # BLOCO DE CÓDIGO DA APLICAÇÃO DO CONTRASTE OTIMIZADO
    if escolha == '1':
        # printa a msg de executando, para o usuário entender que o programa está sendo executado
        print('EXECUTANDO...')
        # laço for que aplica a função de contraste otimizado para todas as classes percorrendo o array
        for i in range(banda_classificada_array.shape[0]):
            for j in range(banda_classificada_array.shape[1]):
                if banda_classificada_array[i][j] == 3:
                    # aplica o contraste Quadrático para a classe 3 (Formação Florestal)
                    red[i][j] = Linear(red[i][j],min_red,max_red)
                    nir[i][j] = Linear(nir[i][j],min_nir,max_nir)
                    swir[i][j] = Linear(swir[i][j],min_swir,max_swir)
                elif banda_classificada_array[i][j] == 15:
                    # aplica o contraste MinMax para a classe 15 (Agropecuária)
                    red[i][j] = MinMax(red[i][j], max_red, min_red)
                    nir[i][j] = MinMax(nir[i][j], max_nir, min_nir)
                    swir[i][j] = MinMax(swir[i][j], max_swir, min_swir)
                elif banda_classificada_array[i][j] == 12 or 33:
                    # aplica o contraste equalização para as classes 12 ou 33 (classe 15: Formação Natural não Florestal; classe 33: Corpos dágua)
                    red[i][j] = fered[i][j]
                    nir[i][j] = fenir[i][j]
                    swir[i][j] = feswir[i][j]
                elif banda_classificada_array[i][j] == 25:
                    # aplica o contraste MinMax para a classe 25 (Área não Vegetada)
                    red[i][j] = MinMax(red[i][j], max_red, min_red)
                    nir[i][j] = MinMax(nir[i][j], max_nir, min_nir)
                    swir[i][j] = MinMax(swir[i][j], max_swir, min_swir)
        # printa a msg de finalização da aplicação do contraste no array
        print('FINALIZADO!!!')
        # Usa a matplotlib para plotar as duas imagens (a sem contraste e a com contraste otimizado)
        # montando a composição colorida falsa-cor 543
        #Plota nesta primeira figura a imagem original, sem contraste
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.imshow(array_rgb)
        plt.title('Imagem SEM Contraste')
        # array para visualização de falsa-cor com contraste
        array_rgb_contraste = np.zeros((linhas, colunas, 3))
        array_rgb_contraste[:, :, 0] = swir / 65535
        array_rgb_contraste[:, :, 1] = nir / 65535
        array_rgb_contraste[:, :, 2] = red / 65535
        #Plota nesta segunda figura a imagem com contraste otimizado
        plt.subplot(122)
        plt.imshow(array_rgb_contraste)
        plt.title('Imagem COM Contraste Otimizado')
        plt.show()

    ###########################################################################################
    ###########################################################################################
    # BLOCO DE CÓDIGO DA APLICAÇÃO DO CONTRASTE PERSONALIZADO
    elif escolha == '2':
        # Lista os valores únicos do array da imagem classificada (Mapbiomas) e transforma esses valores em uma nova lista
        lista_unicos_classes = np.unique(banda_classificada_array).tolist()
        # Através de um list comprehension, transforma cada um dos valores da lista de valores únicos em uma string
        lista_unicos_classes = [str(val) for val in lista_unicos_classes]
        #Cria um dicionário com o valor numérico da classe de acordo com o MapBiomas e o respectivo nome da classe
        dict_classes = {
            '1': 'Formação Florestal',
            '2': 'Formação Florestal',
            '3': 'Formação Florestal',
            '4': 'Formação Florestal',
            '5': 'Formação Florestal',
            '9': 'Formação Florestal',
            '10': 'Formação Natural não Florestal',
            '11': 'Formação Natural não Florestal',
            '12': 'Formação Natural não Florestal',
            '32': 'Formação Natural não Florestal',
            '29': 'Formação Natural não Florestal',
            '13': 'Formação Natural não Florestal',
            '14': 'Agropecuária',
            '15': 'Agropecuária',
            '18': 'Agropecuária',
            '19': 'Agropecuária',
            '39': 'Agropecuária',
            '20': 'Agropecuária',
            '41': 'Agropecuária',
            '36': 'Agropecuária',
            '21': 'Agropecuária',
            '22': 'Área não Vegetada',
            '23': 'Área não Vegetada',
            '24': 'Área não Vegetada',
            '30': 'Área não Vegetada',
            '25': 'Área não Vegetada',
            '26': 'Corpos dágua',
            '33': 'Corpos dágua',
            '31': 'Corpos dágua',
            '27': 'Não Observado'
        }
        #Cria um dicionário com um valor numérico e o nome das funções existentes para posterior escolha do usuário
        dict_cont = {
            '1': 'Raiz Quadrada',
            '2': 'Quadrático',
            '3': 'MinMax',
            '4': 'Linear',
            '5': 'Negativo',
            '6': 'Equalização'
        }
        # Cria uma string numa lista. Está frase será utilizada para compor o título da imagem no plot final
        lista_resumo_Cont = ['Resumo dos contrastes aplicados:\n']
        # dois laços for que percorrem para cada valor da lista de valores únicos o dicionário de classes
        # o funcionamento deste laço é: para cada valor da lista, ele compara esse valor com a key do dicionário
        # sendo verdadeira essa comparação, ele pergunta se o usuário deseja aplicar o contraste para àquela classe
        # Nesta condicional também é testado se usuário entrou com um valor diferente de 1 (sim) e 2 (não), permitindo nova entrada
        for y in lista_unicos_classes:
            for key, value in dict_classes.items():
                if y == key:
                    escolha_ContClasse = input(
                        f'Deseja aplicar o contraste personalizado para a classe {value}? (Digite 1 para sim e 2 para não): ')
                    while escolha_ContClasse != '1' and escolha_ContClasse != '2':
                        escolha_ContClasse = input(
                            f'VALOR INCORRETO! Digite 1 para sim e 2 para não para aplicar o contraste personalizado para a classe {value}: ')
                    # Se o usuário deseja aplicar o contraste para a classe escolhida, uma nova entrada permitirá o usuário
                    # escolher qual o tipo de contraste desejado para a banda RED
                    if escolha_ContClasse == '1':
                        escolha_ContTipo_RED = input(
                            'Qual contraste personalizado deseja aplicar para a banda RED? \n(Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICO, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO): ')
                        while escolha_ContTipo_RED != '1' and escolha_ContTipo_RED != '2' and escolha_ContTipo_RED != '3' and escolha_ContTipo_RED != '4' and escolha_ContTipo_RED != '5' and escolha_ContTipo_RED != '6':
                            escolha_ContTipo_RED = input(
                                'VALOR INCORRETO! Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICO, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO: ')
                        # Adiciona através de uma string formatada a classe escolhida e o tipo de contraste escolhido
                        # realizando a leitura do valor pelo dicionário de contrastes
                        lista_resumo_Cont.append(f'Banda RED: Classe {value}: {dict_cont[escolha_ContTipo_RED]}\n')
                        # Caso o contraste escolhida seja do tipo Linear ou Negativo, o código permite o usuário entrar
                        # com os valores de limite mínimo e máximo
                        # A condicional if abaixo permite o usuário entrar com esses valores mínimo e máximo, armazenando-os
                        # em variáveis que serão utilizadas na aplicação da função Linear ou Negativo
                        if escolha_ContTipo_RED == '4' or escolha_ContTipo_RED == '5':
                            escolha_ContParametros_A = float(input(
                                f'Entre com o valor do Número Digital MÍNIMO (O valor deve ser maior ou igual a {red.min()}): '))
                            while escolha_ContParametros_A < red.min():
                                escolha_ContParametros_A = float(
                                    input(f'VALOR INCORRETO! O valor MÍNIMO deve ser maior ou igual a {red.min()}: '))
                            escolha_ContParametros_B = float(input(
                                f'Entre com o valor do Número Digital MÁXIMO (O valor deve ser menor ou igual a {red.max()}): '))
                            while escolha_ContParametros_B > red.max():
                                escolha_ContParametros_B = float(
                                    input(f'VALOR INCORRETO! O valor MÁXIMO deve ser menor ou igual a {red.max()}: '))
                        # printa a msg de executando, para o usuário entender que o programa está sendo executado
                        print('EXECUTANDO...')
                        # laço for que aplica a função de contraste personalizado para todas as classes escolhidas percorrendo o array
                        for i in range(banda_classificada_array.shape[0]):
                            for j in range(banda_classificada_array.shape[1]):
                                if banda_classificada_array[i][j] == int(key):
                                    if escolha_ContTipo_RED == '1':
                                        # aplica o contraste Raiz Quadrada
                                        red[i][j] = RaizQuadrada(red[i][j])
                                    elif escolha_ContTipo_RED == '2':
                                        # aplica o contraste Quadrático
                                        red[i][j] = Quadratico(red[i][j])
                                    elif escolha_ContTipo_RED == '3':
                                        # aplica o contraste MinMax
                                        red[i][j] = MinMax(red[i][j], max_red, min_red)
                                    elif escolha_ContTipo_RED == '4':
                                        # aplica o contraste Linear
                                        red[i][j] = Linear(red[i][j], escolha_ContParametros_A,
                                                           escolha_ContParametros_B)
                                    elif escolha_ContTipo_RED == '5':
                                        # aplica o contraste Negativo
                                        red[i][j] = Negativo(red[i][j], escolha_ContParametros_A,
                                                             escolha_ContParametros_B)
                                    elif escolha_ContTipo_RED == '6':
                                        # aplica o contraste Equalização
                                        red[i][j] = fered[i][j]
                        # escolher qual o tipo de contraste desejado para a banda NIR
                        escolha_ContTipo_NIR = input('Qual contraste personalizado deseja aplicar para a Banda NIR? \n(Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICA, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO): ')
                        while escolha_ContTipo_NIR != '1' and escolha_ContTipo_NIR != '2' and escolha_ContTipo_NIR != '3' and escolha_ContTipo_NIR != '4' and escolha_ContTipo_NIR != '5' and escolha_ContTipo_NIR != '6':
                            escolha_ContTipo_NIR = input('VALOR INCORRETO! Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICA, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO: ')
                        # Adiciona através de uma string formatada a classe escolhida e o tipo de contraste escolhido
                        # realizando a leitura do valor pelo dicionário de contrastes
                        lista_resumo_Cont.append(f'Banda NIR: Classe {value}: {dict_cont[escolha_ContTipo_NIR]}\n')
                        # Caso o contraste escolhida seja do tipo Linear ou Negativo, o código permite o usuário entrar
                        # com os valores de limite mínimo e máximo
                        # A condicional if abaixo permite o usuário entrar com esses valores mínimo e máximo, armazenando-os
                        # em variáveis que serão utilizadas na aplicação da função Linear ou Negativo
                        if escolha_ContTipo_NIR == '4' or escolha_ContTipo_NIR == '5':
                            escolha_ContParametros_A = float(input(f'Entre com o valor do Número Digital MÍNIMO (O valor deve ser maior ou igual a {nir.min()}): '))
                            while escolha_ContParametros_A < nir.min():
                                escolha_ContParametros_A = float(
                                    input(f'VALOR INCORRETO! O valor MÍNIMO deve ser maior ou igual a {nir.min()}: '))
                            escolha_ContParametros_B = float(input(
                                f'Entre com o valor do Número Digital MÁXIMO (O valor deve ser menor ou igual a {nir.max()}): '))
                            while escolha_ContParametros_B > nir.max():
                                escolha_ContParametros_B = float(
                                    input(f'VALOR INCORRETO! O valor MÁXIMO deve ser menor ou igual a {nir.max()}: '))
                        # printa a msg de executando, para o usuário entender que o programa está sendo executado
                        print('EXECUTANDO...')
                        # laço for que aplica a função de contraste personalizado para todas as classes escolhidas percorrendo o array
                        for i in range(banda_classificada_array.shape[0]):
                            for j in range(banda_classificada_array.shape[1]):
                                if banda_classificada_array[i][j] == int(key):
                                    if escolha_ContTipo_NIR == '1':
                                        # aplica o contraste Raiz Quadrada
                                        nir[i][j] = RaizQuadrada(nir[i][j])
                                    elif escolha_ContTipo_NIR == '2':
                                        # aplica o contraste Quadrático
                                        nir[i][j] = Quadratico(nir[i][j])
                                    elif escolha_ContTipo_NIR == '3':
                                        # aplica o contraste MinMax
                                        nir[i][j] = MinMax(nir[i][j], max_nir, min_nir)
                                    elif escolha_ContTipo_NIR == '4':
                                        # aplica o contraste Linear
                                        nir[i][j] = Linear(nir[i][j], escolha_ContParametros_A,
                                                           escolha_ContParametros_B)
                                    elif escolha_ContTipo_NIR == '5':
                                        # aplica o contraste Negativo
                                        nir[i][j] = Negativo(nir[i][j], escolha_ContParametros_A,
                                                             escolha_ContParametros_B)
                                    elif escolha_ContTipo_NIR == '6':
                                        # aplica o contraste Equalização
                                        nir[i][j] = fenir[i][j]
                        # escolher qual o tipo de contraste desejado para a banda SWIR
                        escolha_ContTipo_SWIR = input(
                            'Qual contraste personalizado deseja aplicar para a Banda SWIR? \n(Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICA, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO): ')
                        while escolha_ContTipo_SWIR != '1' and escolha_ContTipo_SWIR != '2' and escolha_ContTipo_SWIR != '3' and escolha_ContTipo_SWIR != '4' and escolha_ContTipo_SWIR != '5' and escolha_ContTipo_SWIR != '6':
                            escolha_ContTipo_SWIR = input(
                                'VALOR INCORRETO! Digite 1 para RAIZ QUADRADA, 2 para QUADRÁTICA, 3 para MINMAX, 4 para LINEAR, 5 para NEGATIVO e 6 para EQUALIZAÇÃO: ')
                        # Adiciona através de uma string formatada a classe escolhida e o tipo de contraste escolhido
                        # realizando a leitura do valor pelo dicionário de contrastes
                        lista_resumo_Cont.append(f'Banda SWIR: Classe {value}: {dict_cont[escolha_ContTipo_SWIR]}\n')
                        # Caso o contraste escolhida seja do tipo Linear ou Negativo, o código permite o usuário entrar
                        # com os valores de limite mínimo e máximo
                        # A condicional if abaixo permite o usuário entrar com esses valores mínimo e máximo, armazenando-os
                        # em variáveis que serão utilizadas na aplicação da função Linear ou Negativo
                        if escolha_ContTipo_SWIR == '4' or escolha_ContTipo_SWIR == '5':
                            escolha_ContParametros_A = float(input(
                                f'Entre com o valor do Número Digital MÍNIMO (O valor deve ser maior ou igual a {swir.min()}): '))
                            while escolha_ContParametros_A < swir.min():
                                escolha_ContParametros_A = float(
                                    input(f'VALOR INCORRETO! O valor MÍNIMO deve ser maior ou igual a {swir.min()}: '))
                            escolha_ContParametros_B = float(input(
                                f'Entre com o valor do Número Digital MÁXIMO (O valor deve ser menor ou igual a {swir.max()}): '))
                            while escolha_ContParametros_B > swir.max():
                                escolha_ContParametros_B = float(
                                    input(f'VALOR INCORRETO! O valor MÁXIMO deve ser menor ou igual a {swir.max()}: '))
                        # printa a msg de executando, para o usuário entender que o programa está sendo executado
                        print('EXECUTANDO...')
                        # laço for que aplica a função de contraste personalizado para todas as classes escolhidas percorrendo o array
                        for i in range(banda_classificada_array.shape[0]):
                            for j in range(banda_classificada_array.shape[1]):
                                if banda_classificada_array[i][j] == int(key):
                                    if escolha_ContTipo_SWIR == '1':
                                        # aplica o contraste Raiz Quadrada
                                        swir[i][j] = RaizQuadrada(swir[i][j])
                                    elif escolha_ContTipo_SWIR == '2':
                                        # aplica o contraste Quadrático
                                        swir[i][j] = Quadratico(swir[i][j])
                                    elif escolha_ContTipo_SWIR == '3':
                                        # aplica o contraste MinMax
                                        swir[i][j] = MinMax(swir[i][j], max_swir, min_swir)
                                    elif escolha_ContTipo_SWIR == '4':
                                        # aplica o contraste Linear
                                        swir[i][j] = Linear(swir[i][j], escolha_ContParametros_A,
                                                            escolha_ContParametros_B)
                                    elif escolha_ContTipo_SWIR == '5':
                                        # aplica o contraste Negativo
                                        swir[i][j] = Negativo(swir[i][j], escolha_ContParametros_A,
                                                              escolha_ContParametros_B)
                                    elif escolha_ContTipo_SWIR == '6':
                                        # aplica o contraste Equalização
                                        swir[i][j] = feswir[i][j]
        # Transforma as strings armazenadas na lista_resumo_Cont em uma string através do método join
        # essa variável string será utilizada no título da figura 2 do plot
        string_titulo_plot = " ".join(lista_resumo_Cont)
        # printa a msg de finalização da aplicação do contraste no array
        print('FINALIZADO!!!')
        # Usa a matplotlib para plotar as duas imagens (a sem contraste e a com contraste otimizado)
        # montando a composição colorida falsa-cor 543
        # Plota nesta primeira figura a imagem original, sem contraste
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.imshow(array_rgb)
        plt.title('Imagem SEM contraste')
        # array para visualização de falsa-cor com contraste
        array_rgb_contraste = np.zeros((linhas, colunas, 3))
        array_rgb_contraste[:, :, 0] = swir / 65535
        array_rgb_contraste[:, :, 1] = nir / 65535
        array_rgb_contraste[:, :, 2] = red / 65535
        #Plota nesta segunda figura a imagem com contraste otimizado
        plt.subplot(122)
        plt.imshow(array_rgb_contraste)
        plt.title(string_titulo_plot)
        plt.show()

    ###########################################################################################