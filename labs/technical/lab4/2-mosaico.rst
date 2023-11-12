Mosaicos de imagens
=======================

Pré-processamento de imagens são operações que objetivam corrigir imagens
degradadas ou distorcidas para criar uma representação mais fidedigna da cena
original e melhorar a utilidade da imagem para manipulação posterior.
Isso tipicamente envolve o processamento inicial de dados de imagens raw para
eliminar o ruído presente nos dados, calibrá-los radiometricamente, corrigir
distorções geométricas e expandir ou contrair a extensão de uma imagem através
da operação de mosaicking ou subsetting.

*Subsetting* (subdividir), *layer stacking* (empilhar imagens)
---------------------------------------------------------------------------------

Alguns passos do pré-processamento das imagens que serão utilizadas podem
envolver subdividir as imagens para reduzir o volume de dados - o chamado
subsetting - o layer stacking - que é utilizado para combinar múltiplas bandas
separadas ou layers em uma única imagem, e o mosaicking que é utilizado para
juntar diversas imagens que cobrem uma área mais ampla do que apenas uma
[LILLESAND2015]_ (cap 7).


No GEE, os termos composição e mosaico se referem a operações similares.
A ideia dessas operações é juntar imagens diferentes em uma só, seja através de
operações de agregação de pixels, através de operações matemáticas (composição
em imagens sobrepostas na mesma região) ou em imagens que não estão sobrepostas
ou que possuem descontinuidades dentro de suas áreas (mosaicos).

Mosaicos e composições
----------------------

No caso dos mosaicos, as descontinuidades das imagens são preenchidas na ordem
em que as imagens estão na coleção conforme pixels não "transparentes" são
encontrados na sequência.
É como se as imagens estivessem em uma pilha, sendo os
vazios da imagem do topo preenchidos pelas imagens abaixo, caso não se preencha
pela segunda imagem da pilha, a terceira é utilizada e assim sucessivamente até
o total preenchimento de todos os pixels possíveis (alguns podem não ter nenhuma
representação na coleção).
O termo composição, nesse contexto, não deve ser confundido com a composição
entre bandas para visualização no mapa, conforme visto nos laboratórios
anteriores.
