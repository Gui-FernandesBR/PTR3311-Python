Índices de Vegetação
==============================================

Os índices de vegetação são ferramentas cruciais no sensoriamento remoto,
desempenhando um papel vital na avaliação e monitoramento de coberturas vegetais
na Terra.

Estes índices são calculados utilizando-se os dados de reflectância obtidos em
diferentes bandas espectrais, principalmente no infravermelho próximo (NIR) e no
vermelho (RED).

NDVI
-------------------------------------------------

O Normalized difference vegetation index (NDVI), ou Índice de Vegetação por
diferença normalizada, é um dos mais
populares e amplamente utilizados índices de vegetação.

Fórmula
~~~~~~~~~~~~~~

A fórmula do NDVI é expressa por:

.. math::

    NDVI = \frac{(NIR - RED)}{(NIR + RED)}

onde ``NIR`` representa a reflectância no infravermelho próximo e ``RED``
representa a reflectância na banda do vermelho visível.

Esta fórmula foi originalmente proposta por [TUCKER1979]_.

Exemplo de uso
~~~~~~~~~~~~~~

Abaixo exemplificamos como calcular o NDVI com as imagens do Landsat 9. Vamos
utilizar linguagem ``python``:

.. code:: python

    # Selecionar as bandas necessárias (valores relativos à imagem Landsat 9)
    # Atenção: alterar as bandas de acordo com a imagem utilizada
    nir = landsatImage.select('B5') # NIR
    red = landsatImage.select('B4') # Vermelho

    # Calcular a banda NDVI
    ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')

    # Adicionar a banda NDVI à imagem do Landsat 9
    landsatWithNDVI = landsatImage.addBands(ndvi)

    # Exibir a banda NDVI no mapa (Map deve ser um objeto geemap)
    Map.addLayer(landsatWithNDVI.select('NDVI'), {'min': -1, 'max': 1}, 'NDVI')

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

NDBI
-------------------------------------------------

O *Normalized Difference Built-Up Index* (NDBI) é usado para identificar áreas
urbanizadas construídas, contrastando as
bandas espectrais que são mais refletivas em superfícies artificiais do que em
vegetação ou solo.

Fórmula
~~~~~~~~~~~~~~

A fórmula do NDBI é expressa por:

.. math::

    NDBI = \frac{(SWIR - NIR)}{(SWIR + NIR)}

onde ``SWIR`` representa a reflectância no infravermelho de onda curta e ``NIR``
representa a reflectância no infravermelho próximo.

Interpretação
~~~~~~~~~~~~~~~~~~

O valor do NDBI varia de -1 a 1, onde valores mais altos indicam maior
probabilidade de áreas urbanizadas construídas.

Exemplo de uso
~~~~~~~~~~~~~~

Abaixo exemplificamos como calcular o NDBI com as imagens do Landsat 9. Vamos
utilizar linguagem ``python``:

.. code:: python

    # Selecionar as bandas necessárias (valores relativos à imagem Landsat 9)
    # Atenção: alterar as bandas de acordo com a imagem utilizada
    swir = landsatImage.select('B6') # SWIR
    nir = landsatImage.select('B5') # NIR

    # Calcular a banda NDBI
    ndbi = swir.subtract(nir).divide(swir.add(nir)).rename('NDBI')

    # Adicionar a banda NDBI à imagem do Landsat 9
    landsatWithNDBI = landsatImage.addBands(ndbi)

    # Exibir a banda NDBI no mapa (Map deve ser um objeto geemap)
    Map.addLayer(landsatWithNDBI.select('NDBI'), {'min': -1, 'max': 1}, 'NDBI')

EVI
---------------------------------------

O *Enhanced Vegetation Index* (EVI) é uma alternativa ao NDVI, otimizado para separar melhor a sinalização da
vegetação em áreas de alta densidade foliar, onde o NDVI pode tornar-se saturado.
O EVI também corrige algumas distorções atmosféricas e de fundo, proporcionando
uma medição mais precisa em áreas com grande quantidade de vegetação [GINCIENE2011]_.

Ambos os índices, NDBI e EVI, são complementares ao NDVI e oferecem uma
perspectiva mais ampla para os estudos ambientais e de planejamento urbano.

Fórmula
~~~~~~~~~~~~~~

A fórmula do EVI é expressa por:

.. math::

    EVI = 2.5 * \frac{(NIR - RED)}{(NIR + 6 * RED - 7.5 * BLUE + 1)}

onde ``NIR`` representa a reflectância no infravermelho próximo, ``RED``
representa a reflectância na banda do vermelho visível e ``BLUE`` representa a
reflectância na banda do azul visível.

Fontes:
- `USGS Landsat Enhanced Vegetation Index <https://www.usgs.gov/landsat-missions/landsat-enhanced-vegetation-index>`_
- `Enhanced Vegetation Index on Wikipedia <https://en.wikipedia.org/wiki/Enhanced_vegetation_index>`_


Interpretação
~~~~~~~~~~~~~~~~~~

O EVI varia de -1 a 1, onde valores mais altos indicam maior densidade da
vegetação.

Exemplo de uso
~~~~~~~~~~~~~~

Abaixo exemplificamos como calcular o EVI com as imagens do Landsat 9. Vamos
ver primeiro um exemplo de como fazer isso utilizando ``javascript``:

.. code:: javascript

    // Coeficientes para o cálculo do EVI
    var gainFactor = 2.5;
    var coefficient1 = 6.0;
    var coefficient2 = 7.5;
    var L = 1.0;

    // Selecionar as bandas necessárias (valores relativos à imagem Landsat 9)
    // Atenção: alterar as bandas de acordo com a imagem utilizada
    var nir = landsatImage.select('B5'); // NIR
    var red = landsatImage.select('B4'); // Vermelho
    var blue = landsatImage.select('B2'); // Azul

    // Calcular a banda EVI
    var evi = nir.subtract(red).multiply(gainFactor)
                .divide(nir.add(red.multiply(coefficient1)).subtract(blue.multiply(coefficient2)).add(L))
                .rename('EVI');

    // Adicionar a banda EVI à imagem do Landsat 9
    var landsatWithEVI = landsatImage.addBands(evi);

    // Exibir a banda EVI no mapa
    Map.addLayer(landsatWithEVI.select('EVI'), {min: -1, max: 1}, 'EVI');


A sintaxe em ``python`` é muito semelhante:

.. code:: python

    # Coeficientes para o cálculo do EVI
    gainFactor = 2.5
    coefficient1 = 6.0
    coefficient2 = 7.5
    L = 1.0

    # Selecionar as bandas necessárias (valores relativos à imagem Landsat 9)
    # Atenção: alterar as bandas de acordo com a imagem utilizada
    nir = landsatImage.select('B5') # NIR
    red = landsatImage.select('B4') # Vermelho
    blue = landsatImage.select('B2') # Azul

    # Calcular a banda EVI
    evi = nir.subtract(red).multiply(gainFactor) \
                .divide(nir.add(red.multiply(coefficient1)).subtract(blue.multiply(coefficient2)).add(L)) \
                .rename('EVI')

    # Adicionar a banda EVI à imagem do Landsat 9
    landsatWithEVI = landsatImage.addBands(evi)

    # Exibir a banda EVI no mapa (Map deve ser um objeto geemap)
    Map.addLayer(landsatWithEVI.select('EVI'), {'min': -1, 'max': 1}, 'EVI')