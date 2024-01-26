# Vamos abrir um arquivo TXT

arq1 = open('Arquivos/arquivo.txt','r')

# Ler o arquivo TXT

print(arq1.read())

arq1.seek(0,0)

print(arq1.read())

arq1.close()

#Usar um arquivo em modo gravação

arq2 = open('Arquivos/arquivo.txt',"w+")

#Gravar

arq2.write("Tem novo conteudo\n",)
arq2.write("Gravei outra linha\n",)

arq2.seek(0,0)
print(arq2.read())

#Feche o arquivo
arq2.close()

#Abrir uma nova manipulação de alteração de arquivos

arq3 = open('Arquivos/arquivo.txt','a+')
arq3.write("Novo conteudo sem apagar o antigo\n")
arq3.seek(0,0)
print(arq3.read())

# Gerenenciador de contexto de arquivos

with open("Arquivos/arquivo1.txt","w+") as f:
    f.write('Primeira linha\n')
    f.write('Segunda linha\n')
    f.seek(0,0)
    grava = str(f.read())
    f.seek(0,0)
    print(f.read())
 
#Gravar informaçoes em 2 arquivos
with open("Arquivos/arquivo1.txt","w+") as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())

    