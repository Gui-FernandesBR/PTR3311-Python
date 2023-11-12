Avaliação e seleção de modelo
=================================

Para avaliar a performance de um método de classificação, idealmente devem ser
utilizados conjuntos de dados separados do que foi utilizado para se treinar o
classificador.
Isso é importante para uma escolha apropriada do modelo e seus parâmetros, além
de se obter uma medida da qualidade do modelo escolhido.

A seleção de modelo tem por objetivo checar a performance de diferentes modelos
para se escolher o melhor.
Já a avaliação de um modelo é uma forma de, dado um modelo escolhido, estimar
seu erro de predição sobre novos dados [FRIEDMAN2019]_.

Para se executar as duas tarefas citadas, uma forma adequada é se definir a
amostra apresentada e dividi-la em três partes: uma parte para treinamento do
modelo (_training_ _dataset_), outra chamada de conjunto de validação
(_validation_ _dataset_) e finalmente uma que é conhecida por conjunto de teste
(_test_ _dataset_).
Normalmente, esses subconjuntos da amostra são separados na proporção de 70%
para o de treinamento, 15% para o de validação e 15% para o de teste.
Não há uma regra fixa para essas proporções, mas é uma prática comum no meio da
ciência de dados.
