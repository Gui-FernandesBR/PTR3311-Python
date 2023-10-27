O GEE, arquitetura Big Data e padrões de computação paralela
================================================================

O Google Earth Engine (GEE) é uma plataforma que lida com grandes volumes de dados de satélites usando arquitetura baseada em Cloud Computing, apropriada para o processamento de Big Data.
Big Data refere-se a conjuntos de dados volumosos, variados e de alta velocidade (3xV).
Para otimizar o processamento, o GEE utiliza computação paralela, com destaque para os padrões "Map" e "Reduce", que executam operações em paralelo em dados independentes.


Figura 1 - Diagrama do padrão Map
FONTE: adaptado de GRIEBLER (2011, p. 31)


O padrão Reduction - também referido como Reduce - é um procedimento que executa operações de sumarização de dados, gerando uma saída única.
Conceituando de forma direta, ele reduz o conjunto de dados a um único elemento com valor derivado dos dados de entrada - Figura 2.


Figura 2 - Diagrama do padrão Reduce
FONTE: adaptado de GRIEBLER (2011, p. 32)

Finalmente, o modelo MapReduce é uma combinação apropriada dos dois padrões discutidos acima, com o resultado de uma operação em Map sendo a entrada para uma em Reduce.
