from exercicioAluno import Aluno

def main():

    a = Aluno('José Martiniano', '20191380006', 'Rua Lionildo Francisco de Oliveira, 409 Bairro dos Estados - JPA, PB', '70588330442')
    print ('~' * 50)
    print('DADOS DO ALUNO:')
    print(f'Nome: {a.get_nome()}')
    print(f'Maticula: {a.get_matricula()}')
    print(f'Enderaço: {a.get_endereco()}')
    print(f'CPF: {a.get_cpf()}')
    print('~' * 50)

main()