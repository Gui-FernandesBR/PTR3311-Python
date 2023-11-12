============
Sobre Python
============

Python é uma linguagem de programação de alto nível e interpretada, isso
significa que não é necessário compilar o código para executá-lo, o
interpretador faz isso para você.
É uma linguagem de propósito geral, ou seja, pode ser usada para
desenvolver qualquer tipo de aplicação, desde um simples *script* até um
sistema complexo.
Essas características fazem com que Python seja uma linguagem bastante
acessível para iniciantes, mas também bastante útil para profissionais
experientes.

Os laboratórios deste curso foram escritos para ``Python 3.8`` ou superior.
É recomendável revisar alguns conceitos básicos de programação antes de iniciar.
Se você já tem experiência com Python ou outra linguagem de programação,
sinta-se à vontade para pular esta parte.

Estrutura de dados
------------------

- Variáveis:
    - Espaços de memória para armazenar dados que podem ser alterados durante a execução do programa.
    - Em Python, não é necessário declarar o tipo de uma variável antes de utilizá-la.
    - O tipo de uma variável é definido no momento em que um valor é atribuído a ela.
    - Isso aqui é uma variável em Python: ``variavel = 1``.
    - Isso aqui é uma variável em Python: ``variavel = "eu sou uma string"``.
- Números:
    - Incluem inteiros (``int``), números de ponto flutuante (``float``) e números complexos (``complex``).
    - Em Python, são permitidas operações aritméticas entre diferentes tipos de números. Isso é uma flexibilidade que não necessariamente está presente em outras linguagens de programação.
    - Isso aqui é um número inteiro em Python: ``numero = 1``.
- Strings:
    - Sequências de caracteres delimitadas por aspas simples ou duplas.
    - Em Python, strings são imutáveis, ou seja, não podem ser alteradas após a sua criação.
    - Podem ser concatenadas utilizando o operador ``+``.
    - Podem ser acessadas utilizando índices ou fatiamento.
    - Isso aqui é uma string em Python: ``string = "eu sou uma string"``.
- Listas:
    - Coleções ordenadas e mutáveis que podem conter itens de diferentes tipos.
    - Em Python, são identificadas por colchetes ``[]``.
    - Isso aqui é uma lista em Python: ``lista = [1, 2, 3, 4, 5]``.
- Tuplas:
    - Coleções ordenadas e imutáveis, utilizadas para agrupar dados relacionados.
    - Em Python, são identificadas por parênteses ``()``.
    - Isso aqui é uma tupla em Python: ``tupla = (1, 2, 3, 4, 5)``.
- Dicionários:
    - Estruturas de dados que armazenam pares chave-valor, permitindo a rápida recuperação de dados.
    - Em Python, são identificados por chaves ``{}``.
    - Isso aqui é um dicionário em Python: ``dicionario = {"chave1": "valor1", "chave2": "valor2", ...}``.
- Funções:
    - Blocos de código que executam uma tarefa específica.
    - Em Python, são definidas utilizando a palavra-chave ``def``.
    - Isso aqui é uma função em Python: ``def funcao():``.

Orientação a objetos
--------------------

Orientação a objetos é um paradigma de programação que utiliza ``objetos`` para
representar dados e métodos para interagir com esses dados.

- Classes:
    - Estruturas que definem o comportamento e as características dos objetos.
    - Em Python, são definidas utilizando a palavra-chave ``class``.
    - Isso aqui é uma classe em Python: ``class NomeDaClasse``.
    - No nosso curso, dificilmente vamos criar classes, mas é importante entender o conceito.
- Objetos:
    - Instâncias de classes que encapsulam dados e comportamentos.
    - Em Python, são criados utilizando a função ``__init__``.
    - Isso aqui é um objeto em Python: ``objeto = NomeDaClasse()``.
- Métodos:
    - Funções definidas dentro de uma classe que descrevem as ações dos objetos.
    - Em Python, são definidos utilizando a palavra-chave ``def``.
    - Um método é uma função, mas nem toda função é um método.

Controle de fluxo
-----------------

- Condicionais:
    - Estruturas que permitem a execução de um bloco de código caso uma condição seja verdadeira.
    - Em Python, são definidas utilizando as palavras-chave ``if``, ``elif`` e ``else``.
    - Isso aqui é um condicional em Python: ``if condicao:``.
- Loops:
    - Estruturas que permitem a repetição de um bloco de código.
    - Em Python, são definidos utilizando as palavras-chave ``for`` e ``while``.
    - Isso aqui é um loop em Python: ``for item in lista:``.
    - A estrutura ``for`` é geralmente mais utilizada e permite iterar sobre uma sequência de itens, como visto no exemplo acima.  
- Funções e métodos nativos:
    - Funções e métodos que já vêm instalados com o Python e permitem a execução de tarefas específicas.
    - Em geral, são mais eficientes do que escrever o código do zero.
    - São exemplos de funções e métodos nativos: ``sum()``, ``map()``, ``reduce()``, entre outros 

Bibliotecas
-----------

Bibliotecas são conjuntos de códigos que podem ser reutilizados em diferentes
programas, simplificando o desenvolvimento ao fornecer funcionalidades
pré-definidas.

Além das bibliotecas nativas do Python, existem bibliotecas de terceiros.
No nosso curso, utilizaremos algumas como o ``geemap``, ``geopandas``, ``matplotlib``,
que são importantes para trabalhar com geoprocessamento e visualização de dados.

Jupyter Notebook
----------------

Jupyter Notebook é uma ferramenta interativa que permite a escrita de código,
visualização de resultados e documentação em um único lugar.
É amplamente utilizado para análise de dados, aprendizado de máquina e
visualização.

Onde pedir ajuda?
-----------------

Utilize o comando ``help()`` do Python para obter informações sobre o uso de funções e módulos.
Abaixo damos um exemplo de como utilizar o comando ``help()`` para obter informações sobre a função ``print()``.

.. code-block:: python

    help(print)

Participe do fórum de discussão do curso para colaborar e aprender com outros
alunos.
Em geral, você encontrará respostas para dúvidas frequentes e poderá
compartilhar suas experiências com outros alunos.
Acesse aqui: https://github.com/Gui-FernandesBR/PTR3311-Python/discussions

O Stack Overflow é um recurso valioso para solucionar dúvidas específicas de
programação e encontrar soluções para problemas comuns.


