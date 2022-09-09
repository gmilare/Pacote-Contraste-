## Pacote Contraste

Este repositório contém o código fonte do Pacote - Contraste.

 Diego Marcochi de Melo, Gisele Milare e Marielcio Gonçalves Lacerda

## Contexto e Objetivos

O objetivo do trabalho consiste em disponibilizar um pacote que permite aplicar técnicas de contrastes em imagens Landsat 8 e também de forma otimizada e personalizada por classes de uso e cobertura do solo. 

O pacote fornece funções para aplicar cada um das seguintes técnincas de contrastes [1]: raiz quadrada, funcão quadrática, contraste linear; contraste de mínimo e máximo, contraste negativo e equalização de histograma.

O pacote também disponibiliza função de aplicação de técnica de contraste por classe de uso e cobertura da terra. O usuário pode realizar a escolha entre a aplicação de técnicas de contraste de forma otimizada, com aplicação de contraste conforme classes do Mapbiomas [2], ou de forma personalizada, onde o usuário seleciona a técnica de contraste desejada para cada classe constante na cena.

## Organização do Repositório

A organização usada para os códigos e dados disponibilizados neste trabalho é descrita a seguir:

Pacote-Contraste-/contraste/contraste - localização dos arquivos dos módulos do pacote contraste

Pacote-Contraste-/contraste/dist - localização do arquivo compactado para download do pacote

Pacote-Contraste-/contraste/examples - exemplo de utilização do pacote

Pacote-Contraste-/contraste/tests - arquivos de teste realizado para seleção de contraste por classe


## Referências
[1] MENESES, P. R.; ALMEIDA, T. de. Introdução ao processamento de imagens de sensoriamento remoto. Universidade de Brasília, Brasília, 2012.

[2] Projeto MapBiomas – Coleção 5 da Série Anual de Mapas de Cobertura e Uso de Solo do Brasil, acessado em 19 maio de 2021 através do link: https://mapbiomas.org/
