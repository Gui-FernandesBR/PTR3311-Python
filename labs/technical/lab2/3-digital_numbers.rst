*Digital Numbers (DN)* e Reflectância
=======================================

Os valores fornecidos nos produtos do ``Sentinel-2`` são baseados na reflectância.

Já para as coleções derivadas do ``Landsat``, estão disponíveis nas chamadas *Raw*,
os valores *Digital Number (DN)*, que são os valores das intensidades, ou nível de
cinza, dos pixels das imagens digitais geradas pelo satélite, a partir de onde
são calculadas a radiância e as reflectâncias no topo da atmosfera e da
superfície.

Intervalo de valores
--------------------

O intervalo dos valores dos DN's é derivado da quantidade de *bits* utilizada
para armazenar um pixel, no caso de uma imagem onde o DN está armazenado em 8
*bits*, os níveis de cinza de uma banda ficam entre 0 e 255 (2^8 - 1).

Essas informações podem impactar no modo como se trabalha com os parâmetros do
histograma gerado neste laboratório.

Imagens super saturadas
-----------------------

Cabe aqui uma observação a respeito de um passo do pré-processamento, que deve
ser levado em consideração.
Caso verifique mais apropriadamente os valores dos pixels, após a reescala,
provavelmente encontrará valores fora do intervalo entre 0 e 1.
O ideal é se fazer o tratamento desses valores durante o pré-processamento dos
dados.

Mascarar pixels super saturados
--------------------------------

Uma das maneiras seria simplesmente mascarar os pixels (sendo esses pixels
anulados e não utilizados nos cálculos).
Para fazer isso, utiliza-se as informações da banda ``radsat_qa``, que apresenta,
em uma sequência codificada de bits, quais bandas estavam muito saturadas
(fenômeno chamado de *oversaturation*) no pixel relativo durante aquela coleta
dos dados.
