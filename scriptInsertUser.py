# Importando bibliotecas necessárias
import os

# Abrindo/criando arquivos necessários
arqids = open('/home/martiniano/Documentos/CadastroEscolas/soIds.txt')
arqScriptPronto = open('/home/martiniano/Documentos/CadastroEscolas/scriptPronto.txt', 'a')

# Lendo linha por linha do arquivo de IDs
ids = arqids.readlines()

# For que percorre o arquivo de IDs, formata cada linha e escreve a formatação nova no arquivo novo
for id in ids:
    id = id.rstrip('\n') # Remove qualquer quebra de linhas que exista
    arqScriptPronto.write(f"insert into glpi_users (name, password, authtype) values ('{id}'\n") # Escrevendo formatação nova no arquivo novo

# Abrindo/criando arquivos necessários
arqScriptPronto = open('/home/martiniano/Documentos/CadastroEscolas/scriptPronto.txt')
arqsenhas = open('/home/martiniano/Documentos/CadastroEscolas/senhasCriptografadas.txt')
arqScriptFinal = open('/home/martiniano/Documentos/CadastroEscolas/scriptFinalUsers2.txt', 'a')

# Lendo linha por linha do arquivo de senhas e o arquivo parcial
senhas = arqsenhas.readlines()
linhas = arqScriptPronto.readlines()

# Criando e alimenando um array com as senhas que estão no arquivo de senha
senhasArray = []
for senha in senhas:
    senhasArray.append(senha)

# Criando e alimenando um array com as linhas que estão no arquivo parcial
linhasArray = []
for linha in linhas:
    linhasArray.append(linha)

# Iniciando contador em 0
cont = 0

# For que percorre o arquivo parcial, formata as linhas e adiciona o complemento, no final escreve no arquivo novo a linha formatada 
for linha in linhas:
    while cont < len(senhasArray): # While que limita o fim do for ao fim do arquivo parcial
        a = str(linhasArray[cont]) # Variável com o valor da linha do arquivo parcial e já garante o tipo string
        a = a.rstrip('\n') # Remove qualquer quebra de linha que exista
        b = str(senhasArray[cont]) # Variável com o valor da linha do arquivo de senhas e já garante o tipo string
        b = b.rstrip('\n') # Remove qualquer quebra de linha que exista
        cont+=1 # Acrescenta um ao contador para pular para a próxima linha e senha
        arqScriptFinal.write(f"{a}, '{b}', 1);\n") # Junta a linha parcial com o complemento já gravando no arquivo novo

os.remove('/home/martiniano/Documentos/CadastroEscolas/scriptPronto.txt') # Remove o arquivo parcial