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

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014702-2be0e028-42f7-4f88-9219-5455c44a65a7.png" width="600px" />
</div>

Para melhorar a vizualização foi aplicado limites nos plots:

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014705-d03cb915-8012-41af-a187-dae6b85d377a.png" width="600px" />
</div>

Recuperando o sinal:

Para recuperar o sinal, basta que o recepitor saiba qual é o chip daquele sinal, para isso são utilizadas tecnicas de correlação.

Uma vez que o recepitor conheça o chip, é só aplicar o mesmo processo para recuperar o sinal de entrada:

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014708-e5601f98-6f60-450f-809b-585182025c49.png" width="600px" />
</div>

Comparando os sinais:

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014705-d03cb915-8012-41af-a187-dae6b85d377a.png" width="600px" />
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014708-e5601f98-6f60-450f-809b-585182025c49.png" width="600px" />
</div>

Comprovando o método:

Para comprovar foi feito o espalhamento de maneira errada, ou seja, no chip foi colocado propositalmente um bit errado no transmissor.

Logo, no recepitor onde todos o bits do chip estarão corretos, quando o processo de recuperação rodar a saída será diferente da entrada.

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014709-62efd23b-58d2-4f8d-8ee1-339cb9a9b7ea.png" width="600px" />
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014710-b1933a66-2163-4c64-85f5-01254f4604f9.png" width="600px" />
</div>

Agora, para demonstrar como os códigos ortogonais são potentes, faremos o processo para dois usuarios.

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014711-8591437d-d514-4485-bebf-7ddba008dfe2.png" width="600px" />
</div>

Multiplicando cada entrada por um chip ortogonal e depois somando ambos os sinais.

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014713-cd751cdb-91b7-41b9-90d9-28774dc872e3.png" width="600px" />
</div> 

O vetor com a soma, quando for multiplicado pelo chip 1, deve retornar a entrada do primeiro usuário, pois a correlação entre o chip 1 e o chip 2 é zero.

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014714-a742c39f-0956-4a01-b37d-12ccc8b63737.png" width="600px" />
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/95134472/211014718-77bbc726-3705-4cd6-84be-fa48b52e4e7f.png" width="600px" />
</div>

Espero que tenha ficado claro com esse exemplo a tecnológia CDMA.

Obrigado pela atenção!!



