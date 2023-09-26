Tipos de dados do GEE
=========================

1. Images: Dados do tipo raster que armazenam informações numéricas em forma de matriz, como imagens de satélite.
2. Image Collections: Coleções de objetos do tipo image.
3. Feature: Dados vetoriais que contêm geometrias e atributos.
4. Feature Collection: Um grupo de features.

Dados do tipo Raster
--------------------

Dados raster são representados como uma matriz de células, cada uma armazenando valores (atributos) e representando pixels.
Um arquivo raster pode ter mais de um atributo em cada célula, conhecidos como bandas.
Sensores de satélite normalmente produzem dados raster com múltiplas bandas, cada uma representando um comprimento de onda do espectro eletromagnético.

Metadados:
----------

Metadados são informações sobre o conteúdo de um arquivo raster e são essenciais para sua manipulação.
Os metadados incluem detalhes como a inclinação do sol, que pode ser usada para correção radiométrica.
Eles também ajudam na busca de dados com características específicas e podem ser encontrados em manuais ou na internet.