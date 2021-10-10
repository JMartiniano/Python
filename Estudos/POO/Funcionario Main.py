from exerciciofuncionario import Funcionario

def main():
    #criando
    f = Funcionario('José', 'TI', 20000, '01/01/2019', 12334)
    #mostrando_
    print(f.get_salario())
    #setando
    f.set_salario(int(input('Novo Salário: ')))
    print (f'Salario atual: R$: {f.get_salario()}')
    print(f.get_salario())
    print(f'Ganho Anual com o salário R$: {f.get_salario()}:')
    print(f.get_GanhoAnual())
    f.set_aumento(int(input('Aumento de %: ')))
    print(f'Salário após aumento: {f.get_salario()}')
    print(f'Ganho Anual com o salário R$: {f.get_salario()}:')
    print(f.get_GanhoAnual())
    #Existe uma má prática para quebrar o encapsulamento das variáveis, não devemos usar mas devesmo saber:
    # --> f._Funcionario__salario = 0 (modelo: variável._Nome da classe__Nome da var = novo valor
    #isso é um acesso estatico
main()