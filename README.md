# SER-347 - Projeto Final

Este repositório contém o código fonte do trabalho
final da disciplina SER-347: Projeto 8 - Contraste de imagens.

## Contexto e Objetivos

O objetivo do trabalho consiste em disponibilizar um pacote que permite aplicar técnicas de contrastes em imagens Landsat 8 e também de forma otimizada e personalizada por classes de uso e cobertura do solo. 

O pacote fornece funções para aplicar cada um das seguintes técnincas de contrastes: raiz quadrada, funcão quadrática, contraste linear; contraste de mínimo e máximo, contraste negativo e equalização de histograma.

Na forma otimizada, o pacote disponibiliza a escolha para aplicação de técnicas de contraste previamente selecionadas por classes registradas no Mapbiomas [1].

Na parte personalizada, o pacote permite o usuário aplicar os contrastes desejados para cada classe constante na cena.

## Organização do Repositório

Nesta seção explicamos a organização usada para os códigos e dados disponibilizados neste trabalho.


ser-347/contraste/contraste/contraste.py - código principal do pacote contraste

ser-347/contraste/dist - localização do arquivo compactado para download do pacote

ser-347/contraste/examples - exemplos de utilização do pacote

ser-347/contraste/tests - testes realizados para implementação do pacote


## Referências

[1] Projeto MapBiomas – Coleção 5 da Série Anual de Mapas de Cobertura e Uso de Solo do Brasil, acessado em 19 maio de 2021 através do link: https://mapbiomas.org/
