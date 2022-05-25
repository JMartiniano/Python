'''
README

Este escript foi feito para corrigir um problema específico:

- Cenário:

Em uma máquina windows, existia um diretório repleto de arquivos de backup de clientes, existia um outro diretório repleto de diretórios que representavam os clintes e cada diretório de um cliente tem dentro dele diretórios que representam o ano, mês e dia do backup.

- O problema:

Era preciso mover os arquivos de backups de cada cliente para o diretório do cliente.

- A solução

O script aqui presente ao ser executado no diretório dos backups, irá:

[1] - Criar um array com todos os arquivos de backup
[2] - Criar um array com todos os clientes (no script chamados de empresa)
[3] - Um for passa por cada um dos arquivos
[4] - Enquanto o for passa pelo arquivo, ele verifica todos os clientes buscando se o nome do cliente está contido no nome do arquivo
[5] - Por segurança, se o nome do cliente for contido no nome do arquivo, ele faz um segundo teste antes de declarar que o arquivo pertence ao cliente
[6] - O segundo teste é basicamente gerar uma string de como seria o arquivo de backup do cliente atual (existe um padrão nos nomes dos arquivos) em caso verdadeiro o arquivo será movido.

'''


import os

lista_arq = os.listdir("./") # Pega todos os arquivos da pasta atual (a pasta atual deve ser a pasta que contém os backups)
lista_empresas = os.listdir('fileserve') # Pega o nome de todas as empresas (deve ser a pasta das empresas)

cont = 0 #contador começa em 0

for arquivo in lista_arq: # Pega um arquivo da lista de arquivos
        if ".txt" in arquivo: # Teste se o arquivo é do formato txt
            empresa = lista_empresas[cont] # Pega uma empresa da lista pelo índice
            if empresa in arquivo: # Teste se o nome da empresa está contido no nome do arquivo de backup
                teste = f"backup_{empresa}.txt"  # Monta uma variável de como seria o nome de backup da empresa atual
                if arquivo == teste: # Se o nome do backup atual realmente for igual ao teste, então temos uma segunda confirmação que o bakcup pertence à empresa
                    print(f"--> {empresa} copiada com sucesso!") # Essa linha não precisa
                    #print (f"FINALLLL\nArquivo: {arquivo}\nEmpresa: {empresa}\nTeste: {teste}")
                    #os.rename(f"./{arquivo}", f"{lista_empresas}/fev/{arquivo}")
        cont += 1
