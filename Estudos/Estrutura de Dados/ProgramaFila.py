#Para chamar uma fila para este progama é necessário usar o import, seguido pelo nome do arquivo onde se encontra a fila
#criamos uma variável para receber a Fila e manipula-lo, a variável é criado com o nome do arquivo + . + nome da classe
import criandofila
filaTeste = criandofila.Fila()

#Para printar uma fila temos que ir no arquivo dela e liberar essa possibilidade com a função getFIla
#em seguida podemos printa-la:
print (filaTeste.getFila())

#Para adicionar dados à fila temos que criar outra função mo arquivo da fila
#Usamos o comando de nome da variável da fila + . + nome da função de add dados ( o novo valor aqui dentro ):
#Só podemos add um dado por vez
filaTeste.novoDado(1)
filaTeste.novoDado(2)
filaTeste.novoDado(3)
filaTeste.novoDado(4)
filaTeste.novoDado(5)
print (f'Sitação do Fila: {filaTeste.getFila()}')

#Alem de add dados também podemos retirar dados, porém como a ordem da lista deve obrigatoriamente respeitado, só podemos
#retirar dados que estão na primeia posição ou tirar todos os dados que vem antes do dado que deseja retirar caso ele não
#seja o primeiro da fila.
#Também é necessário criar uma função no código de Criação de fila para podermos manipular isso aqui.
#Para remover a apenas o primeiro ítem usamos a função removerDado que foi criada
#A linha deve ser a variável + . + nome da função
filaTeste.removerDado()
print(f'Fila depois da remoção: {filaTeste.getFila()}')
#Agora precisamos criar uma nova função que removo o dado de qualquer posição na Fila
#Usamos a variavel + . + nome da função ( o dado que deseja remover ):
filaTeste.remover(3)
print(f'Linha depois da remoção do dado 3: {filaTeste.getFila()}')