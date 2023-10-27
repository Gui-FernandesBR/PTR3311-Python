K-means
=======

Neste laboratório é utilizado um método de agrupamento conhecido como `k-means`.
O k-means trabalha com base em medidas de similaridade entre os objetos
(pixels no caso de uma imagem) a fim de agrupá-los quando são similares, ou
próximos entre si.
Também existem outros métodos que consideram as medidas de dissimilaridade que
ao invés da proximidade, trabalha com a distância (diferença) entre os objetos.

Como os atributos (bandas) possuem valores numéricos e contínuos se utiliza uma
métrica, ou medida, de distância. No caso, o usual, para o k-means com dados
numéricos reais é o uso da distância euclidiana no espaço.
O princípio do k-means é buscar uma similaridade alta dentro dos grupos
(clusters) e uma similaridade baixa entre os objetos de clusters distintos
(BOEHMKE; GREENWELL, 2019).

De forma resumida, o k-means segue os seguintes passos:

#. Recebe um valor de entrada k <= n (onde n é o número de objetos do conjunto de dados), que é o número de grupos a ser formado e os dados que serão tratados;

#. Seleciona de forma aleatória - ou direcionada e otimizada, como no caso do k-means++ descrito em ARTHUR e VASSILVITSKII (2006) - k objetos que serão as centróides iniciais;

#. Calcula a distância dos objetos para as centróides;

#. Cada objeto é associado com a centróide da qual ele tem a menor distância, fazendo assim parte desse grupo;

#. Recalcula as centróides de cada grupo;

#. Verifica se o centróide se deslocou consideravelmente:

#. se não, termina o algoritmo,

#. se sim volta para o passo 3.

#. Um critério de máximo de interações pode ser utilizado para a parada do algoritmo após um certo número de execuções.


WEKA - K-means (GEE)
~~~~~~~~~~~~~~~~~~~~~

Esta alternativa oferecida pelo GEE está na classe `ee.Clusterer`.
Neste caso, há uma estratégia para a execução da classificação, que diverge do k-means básico.


Seleção de número de clusters ótimo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ao fim desta seção é apresentado um código, nele pode ser observado um procedimento onde se tenta obter um número ótimo de clusters automaticamente.
Para isso, o k-means é processado diversas vezes, para diversos números de clusters a partir de dois e incrementando um a um, para a mesma imagem.
Para cada uma das segmentações geradas, é calculada a soma da distância quadrática entre cada pixel e a centróide de seu respectivo cluster.
Esse procedimento é feito para todos os clusters gerados por uma clusterização e a soma de todos os valores resultantes de cada cluster é feita.
Essa é chamada Soma das Distâncias intra-cluster ou Within Cluster Sum of Squares, conhecido pela sigla WCSS (BOEHMKE ; GREENWELL, 2019).
Faz-se isso para as clusterizações criadas de forma iterativa, e depois plota-se um gráfico em que no eixo x estão o número de clusters parametrizados para o k-means e no eixo y o WCSS - Figura 11.
Visualmente, o que o gráfico apresenta, é uma distribuição cuja curva indica a partir de quando o esforço computacional deixa de fazer sentido dado o pouco ganho na diminuição da variação dos dados intra-cluster.
Esse gráfico pode ser comparado com um outro gráfico onde o que se calcula é a variação entre clusters distintos, em que o objetivo é maximizar as distâncias.
Ele também serve de base para o chamado elbow method, ou método do cotovelo (BOEHMKE ; GREENWELL, 2019). 