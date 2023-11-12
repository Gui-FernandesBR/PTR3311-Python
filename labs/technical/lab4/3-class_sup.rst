Classificação supervisionada
==================================

Ajustar um modelo de classificação supervisionada pode ser entendido como
encontrar um modelo ajustado que relaciona uma resposta às entradas, tentando
fazer a predição da resposta de forma mais acurada possível para futuros dados
de entrada.

Classificação de imagens de satélite
------------------------------------

No caso da classificação supervisionada de imagens de satélite, aqui
apresentada, a ideia é associar classes do mundo real aos pixels e
posteriormente, dado um pixel sem a associação, encontrar a classe à qual ele
pertence.

Random Forest
----------------------

Árvores de decisão
~~~~~~~~~~~~~~~~~~

Árvores de decisão são modelos utilizados quando as variáveis de entrada podem
ser tratadas na forma de estruturas de seleção, as chamadas condicionais
(se-então), até se chegar no resultado da predição.
Essas estruturas de seleção são as regras que são utilizadas para se classificar
um objeto.

O que é Random Forest?
~~~~~~~~~~~~~~~~~~~~~~~

O Random Forest nada mais é do que uma forma mais sofisticada derivada das
árvores de decisão.

Métodos Preditivos e Bootstrap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No Random Forest diversas árvores são utilizadas para se construir um modelo
preditivo mais robusto.
Para isso é utilizada a técnica de bootstrap, que é uma ferramenta usada para
quantificar a incerteza associada com um determinado método de aprendizagem de
máquina (modelo).
Ele pode ser usado em situações onde é complicado se calcular o desvio padrão
de um conjunto de interesse.

Variação e Consistência com Árvores de Decisão
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uma árvore de decisão pode ter alta variância, o que significa que se o conjunto
de treinamento for dividido, consequentemente, cada modelo treinado com uma
dessas divisões levará a resultados bem diversos.
É neste ponto que o bootstrap entra em cena, para se reduzir a variância de um
método de aprendizado de máquina (procedimento chamado de bagging).

Construção e Resultados do Random Forest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para se obter o resultado desejado, um grupo de árvores é construído usando
conjuntos de treinamento a partir da amostragem por bootstrap.
Além disso, o Random Forest é capaz de descorrelacionar as árvores geradas.
Mais detalhes dessas implementações podem ser encontradas em [FRIEDMAN2001]_