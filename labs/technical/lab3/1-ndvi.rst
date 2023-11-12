Índice de Vegetação
==============================================

Os índices de vegetação são ferramentas cruciais no sensoriamento remoto,
desempenhando um papel vital na avaliação e monitoramento de coberturas vegetais
na Terra.

Estes índices são calculados utilizando-se os dados de reflectância obtidos em
diferentes bandas espectrais, principalmente no infravermelho próximo (NIR) e no
vermelho (RED).

*Normalized difference vegetation index (NDVI)*
-------------------------------------------------

O NDVI, ou Índice de Vegetação por Diferença Normalizada, é um dos mais
populares e amplamente utilizados índices de vegetação.

Fórmula
~~~~~~~~~~~~~~

A fórmula do NDVI é expressa por (NIR - RED) / (NIR + RED), onde NIR representa
a reflectância no infravermelho próximo e RED representa a reflectância na banda
do vermelho visível.

Esta fórmula foi originalmente proposta por [TUCKER1979]_.

Interpretação
~~~~~~~~~~~~~~~~~~

O NDVI aproveita o contraste entre as propriedades espectrais da vegetação viva
— que normalmente absorve a maior parte da luz visível e reflete grandes
quantidades de infravermelho próximo — em comparação com outras superfícies como
solo ou construções.

Valores de NDVI mais altos indicam maior densidade da vegetação, enquanto
valores mais baixos correspondem a superfícies desprovidas de vegetação
saudável, como áreas urbanizadas ou solos expostos [LILLESAND2015]_.

Além do NDVI, outros índices também são importantes para análises mais
específicas:

*Normalized Difference Built-Up Index (NDBI)*
-------------------------------------------------

O NDBI é usado para identificar áreas urbanizadas construídas, contrastando as
bandas espectrais que são mais refletivas em superfícies artificiais do que em
vegetação ou solo.

Fórmula
~~~~~~~~~~~~~~

A fórmula do NDBI é expressa por (SWIR - NIR) / (SWIR + NIR), onde SWIR
representa a reflectância na banda do infravermelho de onda curta.

Interpretação
~~~~~~~~~~~~~~~~~~

O valor do NDBI varia de -1 a 1, onde valores mais altos indicam maior
probabilidade de áreas urbanizadas construídas.

*Enhanced Vegetation Index (EVI)*
---------------------------------------

O EVI é uma alternativa ao NDVI, otimizado para separar melhor a sinalização da
vegetação em áreas de alta densidade foliar, onde o NDVI pode tornar-se saturado.
O EVI também corrige algumas distorções atmosféricas e de fundo, proporcionando
uma medição mais precisa em áreas com grande quantidade de vegetação
[GINCIENE; BITENCOURT, 2011].

Ambos os índices, NDBI e EVI, são complementares ao NDVI e oferecem uma
perspectiva mais ampla para os estudos ambientais e de planejamento urbano.

Fórmula
~~~~~~~~~~~~~~

A fórmula do EVI é expressa por 2.5 * (NIR - RED) / ((NIR + 6 * RED - 7.5 * BLUE
+ 1)), onde NIR representa a reflectância no infravermelho próximo, RED
representa a reflectância na banda do vermelho visível e BLUE representa a
reflectância na banda do azul visível.

.. Source: https://www.usgs.gov/landsat-missions/landsat-enhanced-vegetation-index#:~:text=These%20enhancements%20allow%20for%20index,and%20saturation%20in%20most%20cases.&text=In%20Landsat%204%2D7%2C%20EVI,*%20Band%201%20%2B%201)).

Interpretação
~~~~~~~~~~~~~~~~~~

O EVI varia de -1 a 1, onde valores mais altos indicam maior densidade da
vegetação.