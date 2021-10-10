from universidade import Universidade
from curso import Curso
from disciplina import Disciplina
import random

#   Setando disciplinas e temas de Redes de Computadores

dcp1 = Disciplina('Fundamentos De Redes', 'VLAN', 'IP')
dcp2 = Disciplina('Introdução à Programação', 'Estruturas de Repetição', 'Condição')
redes = Curso('Redes De Computadores', dcp1, dcp2)

#   Setando disciplinas e temas de Sistemas para Internet

dcp3 = Disciplina('Estrutura de Dados (ED)', 'Filas', 'Pilhas')
dcp4 = Disciplina('Orientação à Obejtos (OO)', 'Conceitos Iniciais', 'Herança')
sistemas = Curso('Sistemas Para Internet', dcp3, dcp4)

#   falta ajeitar:

print(f'{"<>" * 25}\nFALTA AJEITAR:\nTROCAR NOME DO CURSO\nGERAR PROVA\nPROFESSOR\nINSERIR QUESTÕES\nGERAR MAIS DE UMA QUERSTÃO\nQUESTÕES ABERTAS E FECHADAS\n{"<>" * 25}')

#   Setando os cursos na Alana University

universidade = Universidade(redes, sistemas)

#   Cabeçalho

print('=' * 50)
print('~ BEM-VINDO AO PORTAL OFICIAL ALANA UNIVERSITY! ~')
print('      Você está no nosso banco de questões!')


#   Menu de cursos e disciplinas:

user = int(input(f'{"=" * 50}\nSelecionar usuário:\n1 - Professor\n2 - Coordenador\n--> '))
print('=' * 50)

if user == 2:
    senha = int(input('Digite a senha do coordenador: '))
    if senha == 123:
        print('Bem-vindo, Coordenador!')
        print('=' * 50)
        menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
        while menu1 != 0 and menu1 != 5:
            while menu1 == 1:
                print('=' * 50)
                print('~ Cursos ~')
                print('I - ' + str(universidade.curso1))
                print('II - ' + str(universidade.curso2))
                print('-' * 50)
                entrar = int(input('1 - Configurações do Curso 1\n2 - Configurações do Curso 2\n3 - Home\n--> '))
                if entrar == 1:
                    cursos = 1
                    print(' ~ Configurações de Redes de Computadores ~ ')
                    menu2 = int(input("1 - Mudar nome do Curso\n2 - Sair\n--> "))
                    if menu2 == 1:
                        (input('Novo nome: '))
                    elif menu2 == 2:
                        pass
                elif entrar == 2:
                    cursos = 2
                    print(' ~ Configurações de Sistemas para Internet ~ ')
                    menu2 = int(input("1 - Mudar nome do Curso\n2 - Sair\n--> "))
                    if menu2 == 1:
                        redes.set_nome(input('Novo nome: '))
                    elif menu2 == 2:
                        pass
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
            while menu1 == 2:
                print('=' * 50)
                print(' ~ Disciplinas ~ ')
                cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
                print('=' * 50)
                if cursos == 1:
                    print(' ~ Disciplinas de Redes de Computadores ~ ')
                    print('I - ' + dcp1.nome)
                    print('II - ' + dcp2.nome)
                elif cursos == 2:
                    print(' ~ Disciplinas de Sistemas para Internet ~ ')
                    print('I - ' + dcp3.nome)
                    print('II - ' + dcp4.nome)
                print('-' * 50)
                verTema = int(input('1 - Ver temas\n2 - Voltar para Home\n-->'))
                if verTema == 1 and cursos == 1:
                    print('=' * 50)
                    print('Temas de ' + dcp1.nome)
                    print()
                    print('I - ' + dcp1.tema1)
                    print('II - ' + dcp1.tema2)
                    print()
                    print('Temas de '+ dcp2.nome)
                    print()
                    print('I - ' + dcp2.tema1)
                    print('II - ' + dcp2.tema2)
                elif verTema == 2 and cursos == 2:
                    print('=' * 50)
                    print('Temas de ' + dcp3.nome)
                    print()
                    print('I - ' + dcp3.tema1)
                    print('II - ' + dcp3.tema2)
                    print()
                    print('Temas de ' + dcp4.nome)
                    print()
                    print('I - ' + dcp4.tema1)
                    print('II - ' + dcp4.tema2)
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
            while menu1 == 3:
                print('=' * 50)
                print('Opção 3:')
                print('Estamos em obra, volte mais tarde!')
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
            while menu1 == 4:
                print('=' * 50)
                cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
                print('=' * 50)
                if cursos == 1:
                    print(' ~ Disciplinas de Redes de Computadores ~ ')
                    print('1 - ' + dcp1.nome)
                    print('2 - ' + dcp2.nome)
                elif cursos == 2:
                    print(' ~ Disciplinas de Sistemas para Internet ~ ')
                    print('1 - ' + dcp3.nome)
                    print('2 - ' + dcp4.nome)
                d = int(input(f'Escolha a disciplina:\n--> '))
                print('-' * 50)
                if cursos == 1 and d == 1:
                    print('1 - ' + dcp1.tema1)
                    print('2 - ' + dcp1.tema2)
                    tema = int(input('Escolha o tema:\n--> '))
                    if tema == 1:
                        num = random.randint(1,2)
                        num = str(num)
                        arq = open('1.1.1.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão: \n{arquivo}') #IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                    elif tema == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.1.2.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão: \n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif cursos == 1 and d == 2:
                    print('1 - ' + dcp2.tema1)
                    print('2 - ' + dcp2.tema2)
                    tema = int(input('Escolha o tema:\n--> '))
                    if tema == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.1.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}') # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                    elif tema == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.2.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif cursos == 2 and d == 1:
                    print('1 - ' + dcp3.tema1)
                    print('2 - ' + dcp3.tema2)
                    tema = int(input('Escolha o tema:\n--> '))
                    if tema == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('2.1.1.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                    elif tema == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('2.1.2.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif cursos == 2 and d == 2:
                    tema = int(input('Escolha o tema:\n--> '))
                    print('1 - ' + dcp4.tema1)
                    print('2 - ' + dcp4.tema2)
                    if tema == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('2.2.1.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                    elif tema == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('2.2.2.' + num + '.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                print('Fim da Questão!')
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
        else:
            print('Saiu')
    else:
        print('Senha incorreta!\nSISTEMA ENCERRADO POR SEGURANÇA!')
if user == 1:
    print('Bem-vindo, Professor!')
    print('=' * 50)
    menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
    while menu1 != 0 and menu1 != 4:
        while menu1 == 1:
            print('=' * 50)
            print('~ Cursos ~')
            print('I - ' + str(universidade.curso1))
            print('II - ' + str(universidade.curso2))
            print('=' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
        while menu1 == 2:
            print('=' * 50)
            print(' ~ Disciplinas ~ ')
            cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
            print('=' * 50)
            if cursos == 1:
                print(' ~ Disciplinas de Redes de Computadores ~ ')
                print('I - ' + dcp1.nome)
                print('II - ' + dcp2.nome)
            elif cursos == 2:
                print(' ~ Disciplinas de Sistemas para Internet ~ ')
                print('I - ' + dcp3.nome)
                print('II - ' + dcp4.nome)
            print('-' * 50)
            verTema = int(input('1 - Ver temas\n2 - Voltar para Home\n-->'))
            if verTema == 1 and cursos == 1:
                print('=' * 50)
                print('Temas de ' + dcp1.nome)
                print()
                print('I - ' + dcp1.tema1)
                print('II - ' + dcp1.tema2)
                print()
                print('Temas de ' + dcp2.nome)
                print()
                print('I - ' + dcp2.tema1)
                print('II - ' + dcp2.tema2)
                print('=' * 50)
            elif verTema == 2 and cursos == 2:
                print('=' * 50)
                print()
                print('Temas de ' + dcp3.nome)
                print()
                print('I - ' + dcp3.tema1)
                print('II - ' + dcp3.tema2)
                print()
                print('Temas de ' + dcp4.nome)
                print()
                print('I - ' + dcp4.tema1)
                print('II - ' + dcp4.tema2)
                print('=' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
        while menu1 == 3:
            print('=' * 50)
            cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
            print('=' * 50)
            if cursos == 1:
                print(' ~ Disciplinas de Redes de Computadores ~ ')
                print('1 - ' + dcp1.nome)
                print('2 - ' + dcp2.nome)
            elif cursos == 2:
                print(' ~ Disciplinas de Sistemas para Internet ~ ')
                print('1 - ' + dcp3.nome)
                print('2 - ' + dcp4.nome)
            d = int(input(f'Escolha a disciplina:\n--> '))
            print('-' * 50)
            if cursos == 1 and d == 1:
                print('1 - ' + dcp1.tema1)
                print('2 - ' + dcp1.tema2)
                tema = int(input('Escolha o tema:\n--> '))
                if tema == 1:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('1.1.1.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão: \n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif tema == 2:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('1.1.2.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão: \n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
            elif cursos == 1 and d == 2:
                print('1 - ' + dcp2.tema1)
                print('2 - ' + dcp2.tema2)
                tema = int(input('Escolha o tema:\n--> '))
                if tema == 1:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('1.2.1.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif tema == 2:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('1.2.2.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
            elif cursos == 2 and d == 1:
                print('1 - ' + dcp3.tema1)
                print('2 - ' + dcp3.tema2)
                tema = int(input('Escolha o tema:\n--> '))
                if tema == 1:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('2.1.1.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif tema == 2:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('2.1.2.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
            elif cursos == 2 and d == 2:
                tema = int(input('Escolha o tema:\n--> '))
                print('1 - ' + dcp4.tema1)
                print('2 - ' + dcp4.tema2)
                if tema == 1:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('2.2.1.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
                elif tema == 2:
                    num = random.randint(1, 2)
                    num = str(num)
                    arq = open('2.2.2.' + num + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão:\n{arquivo}')  # IMPLEMENTAR UM FOR PARA VÁRIAS QUESTÕES
            print('Fim da Questão!')
            print('=' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
    else:
        user = 3
if user != 1 and user != 2 and user != 3:
    print('Opção Inválida!')
if user == 3:
    print('Saiu')
#curso1.set_curso1DCP1('Roteamento')
