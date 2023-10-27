Índice de Vegetação
==============================================

Os índices de vegetação, em sensoriamento remoto, são usados para avaliar
coberturas vegetais.
Podem ser obtidos através de cálculos com os dados da reflectância nas bandas do
infravermelho próximo (NIR) e do vermelho visível (RED).

*Normalized difference vegetation index (NDVI)*
-------------------------------------------------

Um dos índices de vegetação mais usados é o NDVI (Normalized Difference
Vegetation Index).
A fórmula do NDVI é dada por (NIR-RED)/(NIR+RED), conforme apresentado por 
[TUCKER1979]_.

Com respeito à diferença entre NIR e RED, quanto maior, mais forte está a
vegetação.
As áreas sem vegetação devem obter valores baixos de NDVI [LILLESAND2015]_

.. [TUCKER1979] TUCKER, C. J. *Red and photographic infrared linear combinations for monitoring vegetation*.
    Remote sensing of Environment, v. 8, n. 2, p. 127-150, 1979.

.. [LILLESAND2015] Thomas; KIEFER, Ralph W.; CHIPMAN, Jonathan. *Remote sensing and image interpretation*.
    John Wiley & Sons, 2015.
