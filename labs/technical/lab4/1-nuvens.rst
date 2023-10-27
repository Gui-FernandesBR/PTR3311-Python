Remoção de nuvens em imagens
============================

A ideia da remoção de áreas cobertas por nuvens (e sombras) é tornar cada pixel
identificado como parte de uma nuvem - ou sombras de nuvens - transparente, para
o processamento, enquanto as outras áreas são mantidas na imagem.
Esse processo é feito através da Image Masking, onde é utilizada uma imagem
chamada de máscara.
Uma máscara (mask) é uma imagem binária com valores 0 e 1.
A máscara exclui da imagem onde ela é aplicada os pixels em que ela contém o
valor 0 (inválidos) e mantém o que contém o valor 1 (válidos).