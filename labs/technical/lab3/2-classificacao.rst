Classificação de imagens
========================

O objetivo de uma classificação de imagens é separar os pixels dentro de uma
imagem em classes [LILLESAND2015]_, ou seja, agrupá-los de acordo com algum
critério.
No caso de imagens de satélite, procura-se padrões espectrais semelhantes de
acordo com a reflectância em cada pixel da imagem [LILLESAND2015]_. 

A classificação pode ser feita pixel a pixel individualmente, por regiões ou por
objetos [LILLESAND2015]_.
Para este laboratório trabalharemos com um método pixel a pixel.

Classificação não-supervisionada
--------------------------------

A classificação não-supervisionada, não utiliza nenhum tipo de conhecimento
prévio como base para classificação, não tendo assim o processo chamado de
treinamento [LILLESAND2015]_.
Estes tipos de algoritmos checam os pixels e os combinam em grupos baseados em
alguma forma na qual eles possam ser comparados.
A questão que fica, nesse caso, é que as classes não possuem uma identidade,
apenas suas divisões. Especificamente no caso de imagens de satélite, pode-se
pensar em termos de classes espectrais, onde não se sabe o que cada uma
representa na superfície e esta associação é feita a posteriori pelo analista.
