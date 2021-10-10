#   Importações necessárias

from universidade import Universidade
from curso import Curso
from disciplina import Disciplina
from professor import Professor
from coordenador import Coordenador
from inserir import InserirQuestao
from avaliar import Avaliar
import random
import os
import shutil

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
        professor = Professor(nome, sistemas, dcp3)
    elif curso == 2 and dcp == 2:
        professor = Professor(nome, sistemas, dcp4)
    print('-' * 50)
    print('Novo professor cadastrado!')
    print(professor)
    professoresNomesLista.append(professor.nome)
    print('-' * 50)
    esc = int(input(f'1 - Cadastrar outro professor\n2 - Continuar\n--> '))
    if esc == 1:
        c = 1
    else:
        c = 0
        print('Cadastros iniciais finalizados!\nVocê já pode navegar pelo nosso banco...')

#   Menu de cursos e disciplinas:

user = int(input(f'{"=" * 50}\nMas antes faça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))
while user != 00:
    while user == 2:
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
                            shutil.copy(questaoNova, 'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Arquivos de questao')
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

                    '''
                    Oi prof. (O mesmo vale para a parte de gerar prova com user de professor)
                    Nessa parte eu usei a lógica de chamar aleatoriamente as questões pelo número delas,
                    porém como eu não sei o número exato de questões (já que o usuário vai add mais) eu precisaria conta-las,
                    para isso eu teria que salva-las em uma pasta à parte, listar essa pasta com a biblioteca OS e fazer a contagem. 
                    O porblema está na parte de salvar o mesmo arquivo em uma pasta distinta da pasta raiz do programa. Não fui capaz
                    de desenvolver esse processo.
                    Então isso ficou como uma dívida técnica, já que eu só percebi essa falha hoje (dia da entrega final). Como medida
                    imediata eu tornei o processo redondo, ou seja, quando a questão chamada não existir, ele informa esse acontecimento
                    e continua rodando sem travar.
                    Vou add um comentário "#ERROR" na linha que acontece isso. (Vale para todos os IFs e ELIFs dessa parte).
                    '''

                    for x in range(uni):
                        if cursos == 1 and d == 1 and tema == 1 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2) #ERROR
                            num = str(num)
                            busca = ('1.1.1.' + num + '.a.txt')
                            if busca not in todos:
                                print ('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.1.1.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 1 and tema == 1 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 10)
                            num = str(num)
                            busca = ('1.1.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.1.2.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 1 and tema == 2 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('1.1.1.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.1.1.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 1 and tema == 2 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 10)
                            num = str(num)
                            busca = ('1.1.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.1.2.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 2 and tema == 1 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 10)
                            num = str(num)
                            busca = ('1.2.1.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.2.1.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 2 and tema == 1 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('1.2.1.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.2.1.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 2 and tema == 2 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 10)
                            num = str(num)
                            busca = ('1.2.2.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.2.2.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 1 and d == 2 and tema == 2 and natureza == 2:
                            for _, _, arquivo in os.walk(
                                    'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('1.2.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('1.2.2.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 1 and tema == 1 and natureza == 1:
                            for _, _, arquivo in os.walk(
                                    'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 9)
                            num = str(num)
                            busca = ('2.1.1.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.1.1.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 1 and tema == 1 and natureza == 2:
                            for _, _, arquivo in os.walk(
                                    'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('2.1.1.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.1.1.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 1 and tema == 2 and natureza == 1:
                            for _, _, arquivo in os.walk(
                                    'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 8)
                            num = str(num)
                            busca = ('2.1.2.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.1.2.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 1 and tema == 2 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('2.1.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.1.2.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 2 and tema == 1 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 3)
                            num = str(num)
                            busca = ('2.2.1.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.2.1.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 2 and tema == 2 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('2.2.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.2.2.' + num + '.f.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 2 and tema == 2 and natureza == 1:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 4)
                            num = str(num)
                            busca = ('2.2.2.' + num + '.a.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.2.2.' + num + '.a.txt', 'r')
                                arquivo = arq.read()
                                print(f'Questão {x + 1}: \n{arquivo}')
                        elif cursos == 2 and d == 2 and tema == 2 and natureza == 2:
                            for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                                todos = arquivo
                            num = random.randint(1, 2)
                            num = str(num)
                            busca = ('2.2.2.' + num + '.f.txt')
                            if busca not in todos:
                                print('Não exite questões no banco para essa solicitação!')
                                pass
                            else:
                                arq = open('2.2.2.' + num + '.f.txt', 'r')
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
                    for _, _, arquivo in os.walk(
                            'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                        for x in range(len(arquivo)):
                            if arquivo[x] == 'universidade.cpython-38.pyc' \
                                    or arquivo[x] == 'professor.cpython-38.pyc' \
                                    or arquivo[x] == 'inserir.cpython-38.pyc' \
                                    or arquivo[x] == 'disciplina.cpython-38.pyc' \
                                    or arquivo[x] == 'curso.cpython-38.pyc' \
                                    or arquivo[x] == 'coordenador.cpython-38.pyc' \
                                    or arquivo[x] == 'avaliar.cpython-38.pyc' \
                                    or arquivo[x] == 'universidade.py' \
                                    or arquivo[x] == 'teste.py' \
                                    or arquivo[x] == 'professor.py' \
                                    or arquivo[x] == 'mostrando tudo de uma pasta.py' \
                                    or arquivo[x] == 'mostrando tudo de uma pasta.py' \
                                    or arquivo[x] == 'inserir.py' or arquivo[x] == 'disciplina.py' \
                                    or arquivo[x] == 'curso.py' or arquivo[x] == 'CORRIGIR.TXT' \
                                    or arquivo[x] == 'coordenador.py' \
                                    or arquivo[x] == 'avaliar.py':
                                pass
                            else:
                                print(arquivo[x])
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
                            v1 = int(input(f'Voto do {prof1}: '))
                            v2 = int(input(f'Voto do {prof2}: '))
                            avaliar = Avaliar(questoesParaJulgar[questao-1], v1, v2 )
                            if v1 == 3 and v2 == 3:
                                print('Questão Aprovada!')
                                addquestao = arq.write(str(questoesParaJulgar[questao-1]))
                                addquestaolistando = arq.write('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Arquivos de questao',)
                            else:
                                print('Questão Reprovada !')
                    menu1 = int(input('~ Home ~ \n1 - Cursos\n2 - Disciplinas\n3 - Inserir Questões\n4 - Gerar Prova\n5 - Cadastrar Professor\n6 - Todas as questões\n0 - Sair\n--> '))
            else:
                print('Saiu')
                print('Trocando de usuário')
                user = int(input(f'{"=" * 50}\nFaça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))
        else:
            print('Senha incorreta!\nSISTEMA ENCERRADO POR SEGURANÇA!')
    while user == 1:
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
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
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
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
            while menu1 == 3:
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
                        for _, _, arquivo in os.walk(
                                'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)  # ERROR
                        num = str(num)
                        busca = ('1.1.1.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.1.1.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 1 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 10)
                        num = str(num)
                        busca = ('1.1.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.1.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 2 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('1.1.1.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.1.1.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 1 and tema == 2 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 10)
                        num = str(num)
                        busca = ('1.1.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.1.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 1 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 10)
                        num = str(num)
                        busca = ('1.2.1.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.2.1.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 1 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('1.2.1.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.2.1.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 2 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 10)
                        num = str(num)
                        busca = ('1.2.2.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.2.2.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 1 and d == 2 and tema == 2 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('1.2.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('1.2.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 1 and tema == 1 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 9)
                        num = str(num)
                        busca = ('2.1.1.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.1.1.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 1 and tema == 1 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('2.1.1.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.1.1.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 1 and tema == 2 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 8)
                        num = str(num)
                        busca = ('2.1.2.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.1.2.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 1 and tema == 2 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('2.1.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.1.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 2 and tema == 1 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 3)
                        num = str(num)
                        busca = ('2.2.1.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.2.1.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 2 and tema == 2 and natureza == 2:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('2.2.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.2.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 2 and tema == 2 and natureza == 1:
                        for _, _, arquivo in os.walk('G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 4)
                        num = str(num)
                        busca = ('2.2.2.' + num + '.a.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.2.2.' + num + '.a.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                    elif cursos == 2 and d == 2 and tema == 2 and natureza == 2:
                        for _, _, arquivo in os.walk(
                                'G:\Documentos\Estudos\Programas Python\Resolvendo listas da faculdade\Projeto OO\Versao 1.2'):
                            todos = arquivo
                        num = random.randint(1, 2)
                        num = str(num)
                        busca = ('2.2.2.' + num + '.f.txt')
                        if busca not in todos:
                            print('Não exite questões no banco para essa solicitação!')
                            pass
                        else:
                            arq = open('2.2.2.' + num + '.f.txt', 'r')
                            arquivo = arq.read()
                            print(f'Questão {x + 1}: \n{arquivo}')
                print('Fim da prova!')
                print('=' * 50)
                menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
            cont = 0
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
                julgar = int(input('Sua questão foi enviada para julgamento.\nPrecione:\n1 - Solicitar julgamento do Coordenador\n2 - Continuar navegando como Professor'))
                if julgar == 1:
                    print('O coordenador deve fazer login para abrir o julgamento desta questão!')
                    menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
                elif julgar == 2:
                    menu1 = int(input('1 - Cursos\n2 - Disciplinas\n3 - Gerar Prova\n4 - Inserir Questão\n0 - Sair\n--> '))
        else:
            print('Trocando de usuário')
            user = int(input(f'{"=" * 50}\nFaça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))
    while user == 00:
        print('Trocando de usuário')
        user = int(input(f'{"=" * 50}\nFaça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))
    if user != 1 and user != 2 and user != 3:
        print('Opção Inválida!')
        pass
        user = int(input(f'{"=" * 50}\nFaça o seu login de usuário:\n1 - Professor\n2 - Coordenador\n{"=" * 50}\n--> '))
else:
    print('Sistema Encerrado!')