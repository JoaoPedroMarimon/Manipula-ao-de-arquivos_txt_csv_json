#Importar o módulo csv
import csv


# Criar um arquivo csv com as funções writer e writerow

with open('Arquivos/nomes.csv','w+', newline="",encoding='utf-8') as fcsv:
    escreve = csv.writer(fcsv,delimiter=',')
    escreve.writerow(('Nome',"Sobrenome","Idade"))
    escreve.writerow(('João',"Marimon","16"))
    escreve.writerow(('Lucas',"Silva","16"))
    escreve.writerow(('Bernardo',"Nsei","17"))

#Ler o arquivo CSV criado
    
with open('Arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1 = list(ler)
    print(lista1)
    for c in lista1:
        print(c)

#Transformar a saida em dicionario com o metodo dictreader

with open('arquivos/nomes.csv','r',encoding='utf-8') as fcsv2:
    ler_dic = csv.DictReader(fcsv2)
    #Iterar os valores
    for d in ler_dic:
        print(d["Nome"])