Trabalhando com arquivos shapefile
================================================================================

A biblioteca ``geemap`` permite trabalhar com arquivos shapefile. Neste guia,
exploraremos como importar e exportar shapefiles usando o ``geemap``.

A principal referência para esses exemplos é o
`exemplo oficial <https://geemap.org/notebooks/10_shapefiles/?h=shapefile>`__
disponível no site do geemap.

Importando um shapefile
-----------------------

Primeiro, importamos a biblioteca e criamos um objeto mapa.

.. code-block:: python

    import geemap

    # Criação de um objeto Map
    Map = geemap.Map()
    Map

Em seguida, carregamos e adicionamos o shapefile de países ao mapa.

.. code-block:: python

    # Caminho para o shapefile de países
    countries_shp = '../data/countries.shp'
    
    # Conversão do shapefile para um objeto Earth Engine
    countries = geemap.shp_to_ee(countries_shp)
    
    # Adicionando o layer de países ao mapa
    Map.addLayer(countries, {}, 'Countries')

Agora, fazemos o mesmo para o shapefile dos estados dos EUA.

.. code-block:: python

    # Caminho para o shapefile dos estados dos EUA
    states_shp = '../data/us_states.shp'

    # Conversão e adição ao mapa
    states = geemap.shp_to_ee(states_shp)
    Map.addLayer(states, {}, 'US States')

Exportando um shapefile
-----------------------

Por fim, demonstramos como exportar um shapefile a partir de um objeto Earth Engine.

.. code-block:: python

    # Exportando o layer de estados dos EUA para um shapefile
    geemap.ee_to_shp(states, filename='../data/us_states_new.shp')
