Processo de avaliação e seleção do modelo
==================================================

Na Figura 1, é apresentado um fluxograma detalhando os passos para a escolha de
um modelo para um dado conjunto de dados.

Primeiramente os modelos são inicializados com os parâmetros desejados.
Em seguida, cada um dos modelos é treinado com o conjunto de treinamentos.
Na fase seguinte, aplica-se o modelo treinado no conjunto de validação e a
partir do resultado deste passo é obtida uma medida de performance.
O melhor modelo é então escolhido e aplicado ao conjunto de testes para se obter
a real performance do modelo em um conjunto independente.

Como dito anteriormente, na fase da avaliação no conjunto de validação, caso o
modelo tenha respondido exageradamente bem no conjunto treinamento e mal na
avaliação sobre o conjunto de validação, pode ter ocorrido o chamado *overfitting*
(sobreajuste).
Nesse caso, pode se voltar à inicialização para reparametrizar o modelo.
Também pode ocorrer do modelo já responder mal na avaliação no próprio conjunto
de treinamento, o chamado *underfitting* (sub-ajuste), significando que algo não
foi bem parametrizado no treinamento, o que as amostras são insuficientes ou
desbalanceadas.

Outra opção que pode ser imaginada a partir do fluxograma é a de que cada modelo
inicializado (no exemplo: A, B e C) pode ser um mesmo algoritmo, mas com
diferentes configurações de seus parâmetros.
Também cabe ressaltar que o que é apresentado na Figura 1 a seguir pode ser
generalizado para n modelos e parametrizações.


.. # TODO: insert figure HERE