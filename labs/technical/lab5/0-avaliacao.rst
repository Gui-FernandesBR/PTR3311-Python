Avaliação e seleção de modelo
=================================

Importância da avaliação do modelo
----------------------------------

Para avaliar a performance de um método de classificação, idealmente devem ser
utilizados conjuntos de dados separados do que foi utilizado para se treinar o
classificador.
Isso é importante para uma escolha apropriada do modelo e seus parâmetros, além
de se obter uma medida da qualidade do modelo escolhido.

Seleção do modelo 
------------------

A seleção de modelo tem o objetivo de verificar a performance de diferentes
modelos para escolher o melhor. Isso envolve comparar as características de cada
modelo, como a eficiência e a precisão na classificação.

Avaliação do modelo
--------------------

A avaliação de um modelo, por sua vez, é o processo de estimar o erro de
predição do modelo escolhido sobre novos dados [FRIEDMAN2001]_.
Essa etapa é crucial para garantir que o modelo selecionado seja eficaz em
cenários reais e com dados que não foram utilizados durante o treinamento.


Divisão da Amostra
------------------

Para executar adequadamente as tarefas de seleção e avaliação, uma prática comum é dividir a amostra apresentada em três partes:

#. Conjunto de Treinamento (*Training Dataset*): Geralmente compõe 70% da amostra e é usado para treinar o modelo.
#. Conjunto de Validação (*Validation Dataset*): Representa cerca de 15% da amostra e é utilizado para ajustar os parâmetros do modelo.
#. Conjunto de Teste (*Test Dataset*): Também compreendendo 15% da amostra, é usado para avaliar a performance do modelo final.

Essas proporções não são regras fixas, mas são comumente utilizadas na ciência de dados.

Seleção do melhor modelo
------------------------

Medida de Qualidade
~~~~~~~~~~~~~~~~~~~
Para escolher o melhor modelo, é necessário ter uma medida de qualidade para
cada um.
No contexto da classificação no Google Earth Engine (GEE), a acurácia associada
à matriz de confusão é frequentemente usada como essa medido.

Escolhendo o Modelo com Maior Acurácia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Em geral, o modelo que apresenta a maior acurácia é considerado o melhor.
Este critério leva em conta a capacidade do modelo de classificar corretamente
novos dados, o que é um indicador chave de seu desempenho.