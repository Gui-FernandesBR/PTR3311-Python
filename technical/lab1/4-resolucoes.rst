Resoluções de imagens de satélite
=================================

As imagens de satélite podem apresentar diferentes características que impactam na qualidade da informação. 
stas características incluem:

Resolução espacial
------------------

A resolução espacial das imagens de satélite é a precisão na captura de detalhes geográficos.
Você pode encontrar essa informação na aba "BANDS" das informações de coleções do Google Earth Engine.
Em alguns casos, a resolução é listada como "Resolution" para cada banda na tabela.
Em outros casos, a resolução é a mesma para todas as bandas, e essa informação fica na parte superior da aba "BANDS".

Figura  - Aba com as propriedades das bandas

Resolução espectral
-------------------------

A resolução espectral das imagens é definida pelas faixas de comprimento de onda das bandas e pelo número de bandas na coleção.
Você pode verificar isso na coluna "Wavelength" da tabela na aba "BANDS".
Note que algumas bandas podem conter informações adicionais além das espectrais.


Resolução temporal 
----------------------------

A resolução temporal, que depende do tempo de revisita do satélite, está disponível nas especificações técnicas do satélite, geralmente encontradas em seus manuais.
Outra maneira de obter informações sobre a resolução temporal é verificar as datas de coleta das imagens, como será explicado mais adiante neste laboratório.


Resolução radiométrica
----------------------------

A resolução radiométrica, que diz respeito à precisão das medições de intensidade de radiação, está documentada nos dados originais do satélite que coletou a coleção.
É importante notar que cada coleção pode conter imagens derivadas dos dados originais e, portanto, os valores numéricos podem estar em uma faixa diferente dos valores das imagens originais (raw data).
Para verificar a resolução radiométrica, é possível examinar o tipo de dado numérico dos pixels das bandas de uma imagem da coleção, conforme será explicado posteriormente.




