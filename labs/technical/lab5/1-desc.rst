Descrição dos conjuntos
================================================================================

Abaixo é fornecidas uma descrição dos conjuntos de dados utilizados no processo
de aprendizado supervisionado.

Conjunto de Treinamento
-----------------------

O conjunto de treinamento é usado para ajustar o modelo (*fit*) a partir de suas
características - os pixels com os valores nas bandas e as respectivas classes
atribuídas a eles.
De forma resumida, pode ser dito que o modelo aprende a partir deste conjunto.

Conjunto de Validação
---------------------

O conjunto de validação é uma parte da amostra que é utilizada para fornecer uma
avaliação sem viés da forma em que um modelo foi ajustado com os dados do
conjunto de treinamento e também pode ser utilizado para aprimorar os
hiperparâmetros do modelo treinado.

Avaliação e ajuste com o Conjunto de Validação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O conjunto de validação é usado para avaliar um determinado modelo específico.

O modelo validado, embora use esses dados, não aprende com eles.
A ideia é usar os resultados obtidos com o conjunto de validação para se voltar
e ajustar os hiperparâmetros do modelo, fazendo com que ele eventualmente
incorpore indiretamente características do conjunto de validação.

Seleção de Modelo
~~~~~~~~~~~~~~~~~

Outra função do conjunto de validação, que será vista mais adiante, é apresentar
uma forma de se selecionar qual o melhor dentre um grupo de modelos aplicados em
um mesmo conjunto de treinamento.

Conjunto de Teste
-----------------

O conjunto de teste é usado para fornecer uma avaliação não enviesada do modelo
final e seus parâmetros escolhidos a partir dos procedimentos feitos com o
conjunto de validação.
Este conjunto é utilizado apenas uma vez no fim do processo, quando o modelo foi
treinado com o conjunto de treinamento e validado com o de validação.
