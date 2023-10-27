Sentinel-2
==========

O texto a seguir refere-se à `coleção de imagens Sentinel-2`_ disponibilizada
pela agência espacial européia, conhecida pela sigla `ESA`.

.. _coleção de imagens Sentinel-2: https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2

Diferença entre `Level-1C` e `Level-2A`
---------------------------------------

Nessa coleção, o termo `Level-1C` determina o tipo do produto disponibilizado
pela fornecedora das imagens.
O produto `Level-1C` possui em seus pixels o valor reflectância no topo da
atmosfera - *Top Of Atmosphere (TOA)* - multiplicado por `10000` (dez mil).

De forma similar, é distribuído o produto `Level-2A`, que apresenta a
reflectância da superfície - `Bottom Of Atmosphere (BOA)` - multiplicada por
`10000` (dez mil).
O `Level-2A`` é obtido através da chamada correção atmosférica dos dados do
`Level-1C`.

Detalhes sobre o processamento dos dados do Sentinel-2 podem ser obtidos na
documentação oficial do produto `Level-2A`_. 

.. _Level-2A: https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook

Programa COPERNICUS
-------------------

O programa COPERNICUS é uma iniciativa da União Europeia em parceria com a
Agência Espacial Europeia (ESA) para monitoramento ambiental e segurança.

É através do COPERNICUS que a ESA disponibiliza os dados do Sentinel-2.
