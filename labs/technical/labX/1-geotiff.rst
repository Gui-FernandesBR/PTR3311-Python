Exportando imagens GeoTIFF
==========================

O Google Earth Engine oferece a capacidade de exportar imagens georreferenciadas
diretamente para o Google Drive.
O formato comum para essas exportações é o GeoTIFF, que é amplamente utilizado
para armazenar imagens georreferenciadas.

A seguir, apresentamos os procedimentos para realizar essa operação tanto em
JavaScript quanto em Python.


.. code-block:: python

    import ee

    # Autenticação e inicialização do Earth Engine
    ee.Authenticate()
    ee.Initialize()

    # Exporta uma imagem GeoTIFF para o Google Drive
    # Substitua 'imagemClassificada' pela imagem desejada
    # Substitua 'retanguloSelecao' pelo polígono que define a região da imagem
    # Ajuste 'escala' conforme necessário, considerando o tamanho do pixel
    # Uma tarefa será iniciada. Acompanhe-a na aba "Tasks".
    task = ee.batch.Export.image.toDrive(
        image=imagemClassificada,
        description='classificacao',
        scale=escala,
        region=retanguloSelecao,
        fileFormat='GeoTIFF',
        formatOptions={
            'cloudOptimized': True
        }
    )
    task.start()
