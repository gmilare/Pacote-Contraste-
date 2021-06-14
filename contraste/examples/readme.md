Para execução do código de exemplo, copie os arquivos landsat8.tif, mapbiomas.tif e example.py para um mesmo diretório. Baixe o pacote em: https://github.com/gmilare/ser-347/tree/main/contraste/dist e realize a instalação.

Para utilização do pacote contraste é necessária a instalação do pacote gdal, versão igual ou superior a 3.3.0 (https://gdal.org/).

A instalação de pacote via pip, instala o pacote na pasta site-package. Para instalação no mesmo diretório, cooloque o arquivo contraste-1.0.tar.gz e execute o pip install contraste-1.0.tar.gz com o python setado neste diretório.

Depois de instalado, entre no Terminal python e importe o módulo de intersse (ou use o * para importar todos), atraves destes comandos:

    from contraste.RaizQuadrada import RAIZQUADRADA

    from contraste.Equalizacao import EQUALIZACAO

    from contraste.Linear import LINEAR

    from contraste.Negativo import NEGATIVO

    from contraste.Quadratico import QUADRATICO

    from contraste.PorClasse import PORCLASSE

    from contraste.MinMax import MINMAX

    from contraste import *

Para execução das funções dos módulos, use os comandos:

    RAIZQUADRADA()
  
    EQUALIZACAO()
  
    LINEAR()
  
    NEGATIVO()
  
    QUADRATICO()
  
    PORCLASSE()
  
    MINMAX()
  

O arquivo Landsat8.tif é uma imagem recortada da cena 225/065 do Landast8 das bandas 4, 5 e 6, com data de passagem em 23/07/2018. O arquivo mapbiomas.tif é o recorte da mesma área dos dados disponibilizados da Coleção 5 do Projeto Mapbiomas, disponível em https://mapbiomas.org/.
