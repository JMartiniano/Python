from universidade import Universidade
from curso import Curso
from disciplina import Disciplina
from professor import Professor
from coordenador import Coordenador
from inserir import InserirQuestao
from avaliar import Avaliar
import random

#   Setando disciplinas e temas de Redes de Computadores

dcp1 = Disciplina('Fundamentos De Redes', 'VLAN', 'IP')
dcp2 = Disciplina('Introdução à Programação', 'Estruturas de Repetição', 'Condição')
redes = Curso('Redes De Computadores', dcp1, dcp2)

#   Setando disciplinas e temas de Sistemas para Internet

dcp3 = Disciplina('Estrutura de Dados (ED)', 'Filas', 'Pilhas')
dcp4 = Disciplina('Orientação à Obejtos (OO)', 'Conceitos Iniciais', 'Herança')
sistemas = Curso('Sistemas Para Internet', dcp3, dcp4)

#   Setando os cursos na Alana University

universidade = Universidade('Alana University', redes, sistemas)

#   Cabeçalho

print('=' * 50)
print('~ BEM-VINDO AO PORTAL OFICIAL ALANA UNIVERSITY! ~')
print('      Você está no nosso banco de questões!')
print('=' * 50)

#   Abrindo listas que serão usadas

professoresNomesLista = []
questoesParaJulgar = []

#   Cadastro Inicial

print('Vamos aos primeiros passos!')
print('-' * 50)
print('~ Cadastrando um Coordenador ~')
nome = input('Nome: ')
senha = int(input('Crie uma senha numérica para acesso de coordenador: '))
coordenador = Coordenador(nome, universidade)
print('-' * 50)
print('Novo coordenador cadastrado com sucesso!')
print('Coordenador: ' + coordenador.nome)
print(coordenador.universidade)

print('-' * 50)

c = 1
while c == 1:
    print('~ Cadastrando Professor ~')
    nome = input('Nome do professor: ')
    print('-' * 50)
    print('Cadastrando o Curso:')
    print('Curso 1 - ' + str(universidade.curso1))
    print('Curso 2 - ' + str(universidade.curso2))
    curso = int(input('Escolha um curso:'))
    print('-' * 50)
    print('Cadastrando a Disciplina:')
    if curso == 1:
        print('1 - ' + dcp1.nome)
        print('2 - ' + dcp2.nome)
    elif curso == 2:
        print('1 - ' + dcp3.nome)
        print('2 - ' + dcp4.nome)
    dcp = int(input('Escolha uma disciplina:'))
    if curso == 1 and dcp == 1:
        professor = Professor(nome, redes, dcp1)
    elif curso == 1 and dcp == 2:
        professor = Professor(nome, redes, dcp2)
    elif curso == 2 and dcp == 1:
        professor = Professor(nome, sistemas, dcp1)
    elif curso == 2 and dcp == 2:
        professor = Professor(nome, sistemas, dcp2)
    print('-' * 50)
    print('Novo professor cadastrado!')
    print(professor)
    #prof2 = professor
    professoresNomesLista.append(professor.nome)
    print('-' * 50)
    esc = int(input(f'1 - Cadastrar outro professor\n2 - Continuar\n--> '))
    if esc == 1:
        c = 1
        #prof1 = professor
    else:
        c = 0
        print('Cadastros iniciais finalizados!\nVocê já pode navegar pelo nosso banco...')

#   Menu de cursos e disciplinas:

user = int(input(f'{"=" * 50}\nMas antes faça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))

if user == 2:
    login = int(input('Digite a senha do coordenador: '))
    if login == senha:
        print('Bem-vindo, Coordenador!')
        print('=' * 50)
        menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n7 - Avaliar questões\n0 - Sair\n--> '))
        while menu1 != 0 and menu1 != 0:
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
                        redes.nome  = input('Novo nome: ')
                        print(f'Novo nome cadastrado: {redes.nome}')
                    elif menu2 == 2:
                        pass
                elif entrar == 2:
                    cursos = 2
                    print(' ~ Configurações de Sistemas para Internet ~ ')
                    menu2 = int(input("1 - Mudar nome do Curso\n2 - Sair\n--> "))
                    if menu2 == 1:
                        sistemas.nome = input('Novo nome: ')
                        print(f'Novo nome cadastrado: {sistemas.nome}')
                    elif menu2 == 2:
                        pass
                print('=' * 50)
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
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
                    print('Abrir um sub menu para cadastrar novas disciplinas')
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
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
            cont = 0
            while menu1 == 3:
                print('=' * 50)
                print('Inserindo uma nova questão ao banco de dados!')
                print('Selecione o curso:')
                print('1 - ' + str(universidade.curso1))
                print('2 - ' + str(universidade.curso2))
                curso = int(input('--> '))
                print('-' * 50)
                if curso == 1:
                    print('Selecione a disciplina:')
                    print('1 - ' + dcp1.nome)
                    print('2 - ' + dcp2.nome)
                    dcp = int(input('--> '))
                elif curso == 2:
                    print('Selecione a disciplina:')
                    print('1 - ' + dcp3.nome)
                    print('2 - ' + dcp4.nome)
                    dcp = int(input('--> '))
                print('-' * 50)
                print('Selecione o tema: ')
                if dcp == 1 and curso == 1:
                    print('1 - ' + dcp1.tema1)
                    print('2 - ' + dcp1.tema2)
                elif dcp == 2 and curso == 1:
                    print('1 - ' + dcp2.tema1)
                    print('2 - ' + dcp2.tema2)
                elif dcp == 1 and curso == 2:
                    print('1 - ' + dcp3.tema1)
                    print('2 - ' + dcp3.tema2)
                elif dcp == 2 and curso == 2:
                    print('1 - ' + dcp4.tema1)
                    print('2 - ' + dcp4.tema2)
                else:
                    menu1 = 3
                tema = int(input('-->'))
                print('-' * 50)
                if curso == 1 and dcp == 1 and tema == 1:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('1.1.1.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('1.1.1.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 1 and dcp == 1 and tema == 2:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('1.1.2.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('1.1.2.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 1 and dcp == 2 and tema == 1:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('1.2.1.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('1.2.1.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 1 and dcp == 2 and tema == 2:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('1.2.2.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('1.2.2.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 2 and dcp == 1 and tema == 1:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('2.1.1.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('2.1.1.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 2 and dcp == 1 and tema == 2:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('2.1.2.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('2.1.2.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 2 and dcp == 2 and tema == 1:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('2.2.1.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('2.2.1.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                elif curso == 2 and dcp == 2 and tema == 2:
                    af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                    if af == 'A' or af == 'a':
                        cont += 1
                        arq = open('2.2.2.' + str(cont) + '.a.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                    elif af == "f" or af == "F":
                        cont += 1
                        arq = open('2.2.2.' + str(cont) + '.f.txt', 'w')
                        questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                        inserindo = InserirQuestao(questaoNova)
                        questoesParaJulgar.append(questaoNova)
                else:
                    menu1 = 3
                print('=' * 50)
                print('Sua questão foi enviada para julgamento!\nVocê está logado como coordenador, entre na sessão de Avaliar questões no menu home para julgar a questão.')
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as Questões\n7 - Avaliar Questões\n0 - Sair\n--> '))
            while menu1 == 4:
                print('=' * 50)
                uni = int(input('Quantidade de questões\n--> '))
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
                elif cursos == 1 and d == 2:
                    print('1 - ' + dcp2.tema1)
                    print('2 - ' + dcp2.tema2)
                    tema = int(input('Escolha o tema:\n--> '))
                elif cursos == 2 and d == 1:
                    print('1 - ' + dcp3.tema1)
                    print('2 - ' + dcp3.tema2)
                    tema = int(input('Escolha o tema:\n--> '))
                elif cursos == 2 and d == 2:
                    tema = int(input('Escolha o tema:\n--> '))
                    print('1 - ' + dcp4.tema1)
                    print('2 - ' + dcp4.tema2)
                else:
                    pass
                natureza = int(input('1 - Questãos abertas\n2 - Questões fechadas'))
                for x in range(uni):
                    if cursos == 1 and d == 1 and tema == 1 and natureza == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.1.1.' + num + '.a.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 1 and natureza == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.1.2.' + num + '.f.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 2 and natureza == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.1.1.' + num + '.a.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 2 and natureza == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.1.2.' + num + '.f.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 1 and natureza == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.1.' + num + '.a.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 1 and natureza == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.1.' + num + '.f.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 2 and natureza == 1:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.2.' + num + '.a.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 2 and natureza == 2:
                        num = random.randint(1, 2)
                        num = str(num)
                        arq = open('1.2.2.' + num + '.f.txt', 'r')
                        arquivo = arq.read()
                        print(f'Questão {x + 1}: \n{arquivo}')

                print('Fim da prova!')
                print('=' * 50)
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
            while menu1 == 5:
                print('=' * 50)
                print('Cadastrando professor')
                nome = input('Nome do professor: ')
                print('-' * 50)
                print('Cadastrando o Curso:')
                print('Curso 1 - ' + str(universidade.curso1))
                print('Curso 2 - ' + str(universidade.curso2))
                curso = int(input('Escolha um curso:' ))
                print('-' * 50)
                print('Cadastrando a Disciplina:')
                if curso == 1:
                    print('1 - ' + dcp1.nome)
                    print('2 - ' + dcp2.nome)
                elif curso == 2:
                    print('1 - ' + dcp3.nome)
                    print('2 - ' + dcp4.nome)
                dcp = int(input('Escolha uma disciplina:'))
                if curso == 1 and dcp == 1:
                    professor = Professor(nome, redes, dcp1)
                elif curso == 1 and dcp == 2:
                    professor = Professor(nome, redes, dcp2)
                elif curso == 2 and dcp == 1:
                    professor = Professor(nome, sistemas, dcp1)
                elif curso == 2 and dcp == 2:
                    professor = Professor(nome, sistemas, dcp2)
                print('-' * 50)
                print('Novo professor cadastrado!')
                print(professor)
                professoresNomesLista.append(professor.nome)
                print('=' * 50)
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
            while menu1 == 6:
                print('=' * 50)
                print('~ Mostrando todas as Questões do nosso banco ~')

                # Mostrando as questões do curso 1, dcp 1, tema 1:
                cont = 0
                while cont < 2:
                    cont += 1
                    x = str(cont)
                    arq = open('1.1.1.' + x + '.txt', 'r')
                    arquivo = arq.read()
                    print(f'Questão {x}:\n{arquivo}')
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
            while menu1 == 7:
                print('=' * 50)
                print('Escolha questão para votar:')
                if len(questoesParaJulgar) == 0:
                    print('Nenhuma questão para ser avaliada.')
                else:
                    for k in range(len(questoesParaJulgar)):
                        print(f'{k + 1} - {questoesParaJulgar[k]}')
                        questao = int(input('--> '))
                        print(questoesParaJulgar[questao-1])
                        for k in range(len(professoresNomesLista)):
                            print(f'{k +1} - {professoresNomesLista[k]}')
                        prof1 = int(input('Professor Avaliador 1: '))
                        prof1 = professoresNomesLista[prof1-1]
                        prof2 = int(input('Professor Avaliador 2: '))
                        prof2 = professoresNomesLista[prof2-1]
                        avaliar = Avaliar(questoesParaJulgar[questao-1], int(input(f'Voto de {prof1}: ')), int(input(f'Voto de {prof2}: ')))
                menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
        else:
            print('Saiu')
    else:
        print('Senha incorreta!\nSISTEMA ENCERRADO POR SEGURANÇA!')
if user == 1:
    print('Bem-vindo, Professor!')
    print('=' * 50)
    menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
    while menu1 != 0 and menu1 != 0:
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
        while menu1 == 4:
            print('=' * 50)
            print('Inserindo uma nova questão ao banco de dados!')
            print('Selecione o curso:')
            print('1 - ' + str(universidade.curso1))
            print('2 - ' + str(universidade.curso2))
            curso = int(input('--> '))
            print('-' * 50)
            if curso == 1:
                print('Selecione a disciplina:')
                print('1 - ' + dcp1.nome)
                print('2 - ' + dcp2.nome)
                dcp = int(input('--> '))
            elif curso == 2:
                print('Selecione a disciplina:')
                print('1 - ' + dcp3.nome)
                print('2 - ' + dcp4.nome)
                dcp = int(input('--> '))
            print('-' * 50)
            print('Selecione o tema: ')
            if dcp == 1 and curso == 1:
                print('1 - ' + dcp1.tema1)
                print('2 - ' + dcp1.tema2)
            elif dcp == 2 and curso == 1:
                print('1 - ' + dcp2.tema1)
                print('2 - ' + dcp2.tema2)
            elif dcp == 1 and curso == 2:
                print('1 - ' + dcp3.tema1)
                print('2 - ' + dcp3.tema2)
            elif dcp == 2 and curso == 2:
                print('1 - ' + dcp4.tema1)
                print('2 - ' + dcp4.tema2)
            else:
                menu1 = 3
            tema = int(input('-->'))
            print('-' * 50)
            if curso == 1 and dcp == 1 and tema == 1:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('1.1.1.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('1.1.1.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 1 and dcp == 1 and tema == 2:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('1.1.2.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('1.1.2.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 1 and dcp == 2 and tema == 1:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('1.2.1.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('1.2.1.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 1 and dcp == 2 and tema == 2:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('1.2.2.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('1.2.2.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 2 and dcp == 1 and tema == 1:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('2.1.1.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('2.1.1.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 2 and dcp == 1 and tema == 2:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('2.1.2.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('2.1.2.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 2 and dcp == 2 and tema == 1:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('2.2.1.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('2.2.1.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            elif curso == 2 and dcp == 2 and tema == 1:
                af = input('Digite A para questão aberta\nDigite F para questão fechada\n-->')
                if af == 'A' or af == 'a':
                    cont += 1
                    arq = open('2.2.2.' + str(cont) + '.a.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
                elif af == "f" or af == "F":
                    cont += 1
                    arq = open('2.2.2.' + str(cont) + '.f.txt', 'w')
                    questaoNova = input('Insira a nova questão (Evite usar acentos):\n ')
                    inserindo = InserirQuestao(questaoNova)
                    questoesParaJulgar.append(questaoNova)
            else:
                menu1 = 4
            print('=' * 50)
            julgar = int(input('Sua questão foi enviada para julgamento.\nPrecione:\n1 - Para solicitar julgamento do Coordenador\n2 - Para continuar navegando como Professor'))
            if julgar == 1:
                print('O coordenador deve fazer login para abrir o julgamento desta questão!')
                user = 2
            elif julgar == 2:
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
    else:
        user = 3
if user != 1 and user != 2 and user != 3:
    print('Opção Inválida!')
if user == 3:
    print('Saiu')