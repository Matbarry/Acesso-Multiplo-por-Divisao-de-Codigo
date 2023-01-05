# Acesso-Multiplo-por-Divisao-de-Codigo
 CDMA- Tecnologia que utiliza portadoras ortogonais para esplhar um ou mais sinais, de forma que eles não interfiram destrutivamente com o outro.

 Essa técnica permite que varios sinais sejam enviados em um mesmo canal e para isso é necessário os codigos PN, que são basicamente chips que indentificam cada usuário. 
 
 Esses chips são encontrados através da matriz de Walsh, que pode ser observada logo em seguida:

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/210793466-a99855a8-9c97-40f4-83ae-733744a2d038.png" width="400px" />
</div>

 Nota-se que se aplicarmos a propriedade de ortogonalidade da geometria, os vetores de Walsh seram ortogonais entre si.
 
 Desta maneira, pela linearidade, garantimos que o resultado gerado ao multiplicar qualquer um desses vetores por outros vetores aleatórios(um sinal com vindo de uma fonte desconhecida) seja ortogonal aos demais. 
 
Ao rodar o código, dois vetores aleatórios são gerados, eles seram os nosso sinais.

Para que o processo seja entendido, o processo será feito primeiramente para um usuário.

Na imagem a seguir, vemos o sinal de entrada, o chip PN e o resultado do espalhamento (multiplicação entre a entrada e o chip):

FIGURE 1

Para melhorar a vizualização foi aplicado limites nos plots:

FIGURE 2

Recuperando o sinal:

Para recuperar o sinal, basta que o recepitor saiba qual é o chip daquele sinal, para isso são utilizadas tecnicas de correlação.

Uma vez que o recepitor conheça o chip, é só aplicar o mesmo processo para recuperar o sinal de entrada:

FIGURE 4

Comparando os sinais:

FIGURE 2 --- FIGURE 4

Comprovando o método:

Para comprovar foi feito o espalhamento de maneira errada, ou seja, no chip foi colocado propositalmente um bit errado no transmissor.

Logo, no recepitor onde todos o bits do chip estarão corretos, quando o processo de recuperação rodar a saída será diferente da entrada.





