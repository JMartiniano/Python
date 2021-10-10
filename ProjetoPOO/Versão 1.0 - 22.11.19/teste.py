from universidade import Universidade
import random

curso1 = Universidade()

#Cabeçalho

print('=' * 50)
print('~ BEM-VINDO AO PORTAL OFICIAL ALANA UNIVERSITY! ~')
print('      Você está no nosso banco de questões!')
#menu de cursos e disciplinas:
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
                print('Cursos:')
                print(curso1.get_nomeCurso1())
                print(curso1.get_nomeCurso2())
                print('-' * 50)
                entrar = int(input('1 - Configurações do Curso 1\n2 - Configurações do Curso 2\n3 - Home\n--> '))
                if entrar == 1:
                    cursos = 1
                    print('Configurações de Redes de Computadores')
                    menu2 = int(input("1 - Mudar nome do Curso\n2 - Sair\n--> "))
                    if menu2 == 1:
                        curso1.set_nomeCurso1(input('Novo nome: '))
                    elif menu2 == 2:
                        pass
                elif entrar == 2:
                    cursos = 2
                    print('Configurações de Sistemas para Internet')
                    menu2 = int(input("1 - Mudar nome do Curso\n2 - Sair\n--> "))
                    if menu2 == 1:
                        curso1.set_nomeCurso1(input('Novo nome: '))
                    elif menu2 == 2:
                        pass
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Sair\n--> '))
            while menu1 == 2:
                print('=' * 50)
                print('Disciplinas ')
                cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
                print('=' * 50)
                if cursos == 1:
                    print('Disciplinas de Redes de Computadores: ')
                    print('1- ' + curso1.get_curso1DCP1())
                    print('2- ' + curso1.get_curso1DCP2())
                elif cursos == 2:
                    print('Disciplinas de Sistemas para Internet: ')
                    print('1- ' + curso1.get_curso2DCP1())
                    print('2- ' + curso1.get_curso2DCP2())
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
                    print('Disciplinas de Redes de Computadores: ')
                    print('1- ' + curso1.get_curso1DCP1())
                    print('2- ' + curso1.get_curso1DCP2())
                elif cursos == 2:
                    print('Disciplinas de Sistemas para Internet: ')
                    print('1- ' + curso1.get_curso2DCP1())
                    print('2- ' + curso1.get_curso2DCP2())
                d = int(input(f'Escolha a disciplina:\n--> '))
                if cursos == 1 and d == 1:
                    print('Escolha o tema:')
                    print(f'1 - {curso1.get_curso1DCP1T1()}\n2 - {curso1.get_curso1DCP1T2()}')
                    tema = int(input('--> '))
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
                    print('Escolha o tema: ')
                    print(f'1 - {curso1.get_curso2DCP2T1()}\n2 - {curso1.get_curso2DCP2T2()}')
                    tema = int(input('--> '))
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
                    print('Escolha o tema: ')
                    print(f'1 - {curso1.get_curso2DCP2T1()}\n2 - {curso1.get_curso2DCP2T2()}')
                    tema = int(input('--> '))
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
                    print('Escolha o tema: ')
                    print(f'1 - {curso1.get_curso2DCP2T1()}\n2 - {curso1.get_curso2DCP2T2()}')
                    tema = int(input('--> '))
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
            print('Cursos:')
            print(curso1.get_nomeCurso1())
            print(curso1.get_nomeCurso2())
            print('-' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
        while menu1 == 2:
            print('=' * 50)
            print('Disciplinas ')
            cursos = int(input('Escolha um curso:\n1 - Redes de Computadores\n2 - Sistemas para Internet\n--> '))
            print('=' * 50)
            if cursos == 1:
                print('Disciplinas de Redes de Computadores: ')
                print('1- ' + curso1.get_curso1DCP1())
                print('2- ' + curso1.get_curso1DCP2())
            elif cursos == 2:
                print('Disciplinas de Sistemas para Internet: ')
                print('1- ' + curso1.get_curso2DCP1())
                print('2- ' + curso1.get_curso2DCP2())
            print('=' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
        while menu1 == 3:
            print('=' * 50)
            print('Opção 3:')
            print('Estamos em obra, volte mais tarde!')
            print('=' * 50)
            menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Sair\n--> '))
    else:
        user = 3
if user != 1 and user != 2 and user != 3:
    print('Opção Inválida!')
if user == 3:
    print('Saiu')
#curso1.set_curso1DCP1('Roteamento')
