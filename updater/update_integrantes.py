#encoding: iso-8859-1
#@note necessario para corrigir acentuacao

#@todo escrever diretamente no arquivo final em vez de um em branco
#@todo o que fazer com entries repetidas?


#IMPORTS
import pandas as pd    #pip install pandas
import os


#SETUP
path = os.getcwd()  #detecta endereco da pasta de trabalho do script
members_df = pd.read_csv(path + "/tabela.csv", sep=',', encoding='iso-8859-1')    #transforma o arquivo .csv gerado no Google Forms em um data frame
output_file = open(path + "/out.html", mode='w', encoding='iso-8859-1')    #abre o arquvio de saida
format_file = open(path + "/modelo.html", mode='r', encoding='iso-8859-1') #abre o arquivo para formatacao html
field = '#' #define caracter usado como indicador de campo


#PROCESSAMENTO DE DADOS
#conta o total de pessoas que preencheram o formulario
member_number = len(members_df.index)
print("Temos %d integrantes:\n" % member_number)    #@debug numero de integrantes

#conta o numero de caracteres no arquivo de formatacao modelo
format_file.seek(0, 2)  #coloca o cursor na posicao 0 relativo ao fim (parametro 2) do arquivo
format_end = format_file.tell() #guarda a posicao do cursor relativa ao inicio, ou seja, o numero de caracteres
#print("Caracteres no arquivo de formatacao:", format_end)  #@debug numero de caracteres no arquivo-modelo

#gera um trecho de codigo html para cada integrante do grupo, seguindo o modelo dado
for member in range(0, member_number):  #percorre cada linha da tabela
    print(members_df.iloc[member, 1] + "...")   #@debug preenchendo membros

    #copia o codigo do modelo para o arquivo de saida preenchendo os campos
    cursor = 0   #inicializa o cursor no inicio do arquivo
    while (cursor < format_end):
        format_file.seek(cursor, 0) #aponta a um endereco especifico
        ch = format_file.read(1)    #le somente um caracter por vez
        #se o caracter lido for o indicador
        if (ch == field):
            i = int(format_file.read(1))    #le o indice subsequente (qual a resposta desejada do formulario)
            cursor += 1    #pula esse indice
            output_file.write(str(members_df.iloc[member, i]))  #preenche o campo com a resposta adequada do integrante em questao
        else:
            #caso nao, continua copiando o codigo html de um arquivo ao outro
            output_file.write(ch)
        cursor += 1    #movimenta o cursor


#FINALIZACAO
output_file.close() #fecha os arquivos abertos
format_file.close()
print("\nArquivo html gerado!\n")   #@debug finalizacao
