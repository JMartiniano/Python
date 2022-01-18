from criandoconta import Conta
from cliente import Cliente

cliente = Cliente("José", 70588220442, '26/04/2001', "Estados")
conta = Conta(cliente, 123, 456, 100)
conta.depositar(2000)
print(f'Saldo: R$:{conta.get_saldoBanco()}')
print(f'Saldo Real: R$:{conta._Conta__get_saldoReal()}')
print(f'Titular: {conta.titular}')
