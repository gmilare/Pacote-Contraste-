#
# This file is part of Contraste.
# Copyright (C) 2021 INPE.
#
# Contraste is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

#Instalação dos pacotes necessários 
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import math

gdal.UseExceptions()

# Definições das Funções de Contraste


#Função Raiz Quadrada
def RaizQuadrada(DN):
    FatordeAjuste = 65535 / (math.sqrt(65535))
    y = (FatordeAjuste * math.sqrt(DN))
    return y

# Função Quadratica
def Quadratica(DN):
    FatordeAjuste = 1/65535
    y = (FatordeAjuste * math.pow(DN, 2))
    return y

# Função de contraste MinMax
def MinMax(DN, max, min):
    tan_ang_MinMax = (65535 / (max - min))
    y = tan_ang_MinMax * DN
    return y

# #Função de contraste Linear
def Linear(DN,min,max):
    y = (65535/(max-min))*(DN-min)
    return y

# #Função de contraste Negativo
def Negativo(DN,max,min):
    y = (-1*(65535/(min-max)))*(DN-min)
    return y

# #Função de equalização

def df(DN):  # histograma 
    values = [0]*65535
    for i in range(DN.shape[0]):
        for j in range(DN.shape[1]):
            values[DN[i,j]]+=1
    return values


def cdf(hist):  # distribuição de frequencia cumulativa
    cdf = [0] * len(hist)   
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i]= cdf[i-1]+hist[i]
    # normalização do histograma
    cdf = [ele*65535/cdf[-1] for ele in cdf]      
    return cdf

def equalize_image(image):
    my_cdf = cdf(df(image))
    image_equalized = np.interp(image, range(0,65535), my_cdf)
    return image_equalized

#abrindo a imagem classificada (MapBiomas) e a Landsat 8
dataset_mapbiomas = gdal.Open("rasterized2.tif", gdal.GA_ReadOnly)

dataset_L8 = gdal.Open("landsat2.tif", gdal.GA_ReadOnly)
dataset_L8.RasterCount

# obter os objetos com as informações do mapbiomas
mapbiomas_ = dataset_mapbiomas.GetRasterBand(1)
# obter os objetos com as informações das bandas do Landsat 8
banda_red = dataset_L8.GetRasterBand(1)
banda_nir = dataset_L8.GetRasterBand(2)
banda_swir = dataset_L8.GetRasterBand(3)

# obter as matrizes de pixels de cada banda
red = banda_red.ReadAsArray()
nir = banda_nir.ReadAsArray()
swir = banda_swir.ReadAsArray()
mapbiomas = mapbiomas_.ReadAsArray()

## obter os mínimos e os máximos de cada banda
min_red = red.min()
max_red = red.max()
min_nir = nir.min()
max_nir = nir.max()
min_swir = swir.min()
max_swir = swir.max()

##leitura de linhas e colunas - para matriz de visualização de falsa-cor
linhas = red.shape[0]
colunas = red.shape[1]

## array para visualização de falsa-cor sem contraste
sred = np.zeros((linhas,colunas))
snir = np.zeros((linhas,colunas))
sswir  = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      sred[i][j] = red[i][j]
      snir[i][j] = nir[i][j]
      sswir[i][j] = swir[i][j]


array_rgb = np.zeros((linhas, colunas, 3))
## valores entre 0-1
array_rgb[:, :, 0] = sswir/65535
array_rgb[:, :, 1] = snir/65535
array_rgb[:, :, 2] = sred/65535 

plt.figure(figsize=(20, 5))
plt.imshow(array_rgb)
plt.title('SEM contraste');

#Aplicando o contraste Raiz Quadrada
fraizred = np.zeros((linhas,colunas))
fraiznir = np.zeros((linhas,colunas))
fraizswir  = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      fraizred[i][j] = RaizQuadrada(red[i][j])
      fraiznir[i][j] = RaizQuadrada(nir[i][j])
      fraizswir[i][j] = RaizQuadrada(swir[i][j])
    else:
      fraizred[i][j] = fraizred[i][j]
      fraiznir[i][j] = fraiznir[i][j]
      fraizswir[i][j] = fraizswir[i][j]
      
      
    
fraiz_array_rgb = np.zeros((linhas, colunas, 3))

fraiz_array_rgb[:, :, 0] = fraizswir/65535
fraiz_array_rgb[:, :, 1] = fraiznir/65535
fraiz_array_rgb[:, :, 2] = fraizred/65535

plt.figure(figsize=(20, 5))
plt.imshow(fraiz_array_rgb)
plt.title('Contraste - Raiz Quadrada');

#Aplicando o contraste Quadrático
fqred = np.zeros((linhas,colunas))
fqnir = np.zeros((linhas,colunas))
fqswir = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
          fqred[i][j] = Quadratica(red[i][j])
          fqnir[i][j] = Quadratica(nir[i][j])
          fqswir[i][j] = Quadratica(swir[i][j])

fq_array_rgb = np.zeros((linhas, colunas, 3))


fq_array_rgb[:, :, 0] = fqswir /65535
fq_array_rgb[:, :, 1] = fqnir /65535
fq_array_rgb[:, :, 2] = fqred /65535

plt.figure(figsize=(20, 5))
plt.imshow(fq_array_rgb)
plt.title('Contraste - Quadrática');

#Aplicando o contraste MinMax
fmmred = np.zeros((linhas,colunas))
fmmnir = np.zeros((linhas,colunas))
fmmswir = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      fmmred[i][j] = MinMax(red[i][j],max_red, min_red)
      fmmnir[i][j] = MinMax(nir[i][j],max_nir, min_nir)
      fmmswir[i][j] = MinMax(swir[i][j],max_swir, min_swir)

fmm_array_rgb = np.zeros((linhas, colunas, 3))


fmm_array_rgb[:, :, 0] = fmmswir /65535
fmm_array_rgb[:, :, 1] = fmmnir /65535
fmm_array_rgb[:, :, 2] = fmmred /65535

plt.figure(figsize=(20, 5))
plt.imshow(fmm_array_rgb)
plt.title('Contraste - MinMax');

#Aplicando o contraste Linear
flred = np.zeros((linhas,colunas))
flnir = np.zeros((linhas,colunas))
flswir = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      flred[i][j] = Linear(red[i][j],min_red, max_red)
      flnir[i][j] = Linear(nir[i][j],min_nir, max_nir)
      flswir[i][j] = Linear(swir[i][j],min_swir, max_swir)

fl_array_rgb = np.zeros((linhas, colunas, 3))


fl_array_rgb[:, :, 0] = flswir/65535
fl_array_rgb[:, :, 1] = flnir/65535
fl_array_rgb[:, :, 2] = flred/65535

plt.figure(figsize=(20, 5))
plt.imshow(fl_array_rgb)
plt.title('Contraste - Linear');

#Aplicando o contraste Negativo
fnred = np.zeros((linhas,colunas))
fnnir = np.zeros((linhas,colunas))
fnswir = np.zeros((linhas,colunas))
for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      fnred[i][j] = Negativo(red[i][j],max_red, min_red)
      fnnir[i][j] = Negativo(nir[i][j],max_nir, min_nir)
      fnswir[i][j] = Negativo(swir[i][j],max_swir, min_swir)

fn_array_rgb = np.zeros((linhas, colunas, 3))


fn_array_rgb[:, :, 0] = abs(fnswir/65535)
fn_array_rgb[:, :, 1] = abs(fnnir/65535)
fn_array_rgb[:, :, 2] = abs(fnred/65535)

plt.figure(figsize=(20, 5))
plt.imshow(fn_array_rgb)
plt.title('Contraste - Negativo');

#Aplicando o contraste Equalização
feqred = np.zeros((linhas,colunas))
feqnir = np.zeros((linhas,colunas))
feqswir = np.zeros((linhas,colunas))
fered = equalize_image(red)
fenir = equalize_image(nir)
feswir = equalize_image(swir)

for i in range(0,mapbiomas.shape[0]):
  for j in range(0,mapbiomas.shape[1]):
    if mapbiomas[i][j] == 24:
      feqred[i][j] = fered[i][j]
      feqnir[i][j] = fenir[i][j]
      feqswir[i][j] = feswir[i][j]


fe_array_rgb = np.zeros((linhas, colunas, 3))

fe_array_rgb[:, :, 0] = feqswir/65535
fe_array_rgb[:, :, 1] = feqnir /65535
fe_array_rgb[:, :, 2] = feqred /65535

plt.figure(figsize=(20, 5))
plt.imshow(fe_array_rgb)
plt.title('Contraste por Equalização');

#Comparando os contrastes por classe -- imagem sem demais classes
plt.figure(figsize=(20, 10))
plt.subplot(241)
plt.imshow(array_rgb)
plt.title('Classe: Área não Vegetada \n SEM contraste')

plt.subplot(242)
plt.imshow(fraiz_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste - Raiz Quadrada')

plt.subplot(243)
plt.imshow(fq_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste - Quadrática')

plt.subplot(244)
plt.imshow(fmm_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste - MinMax')

plt.subplot(245)
plt.imshow(fl_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste - Linear')

plt.subplot(246)
plt.imshow(fn_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste - Negativo')

plt.subplot(247)
plt.imshow(fe_array_rgb)
plt.title('Classe: Área não Vegetada \n Contraste por Equalização')
plt.show()



