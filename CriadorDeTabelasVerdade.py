from prettytable import PrettyTable
import math

#  Declara variáveis, exibe o texto inicial para o usuário e recebe sua entrada
print("*As sentenças atômicas devem ser representadas apenas por uma letra*")
table = PrettyTable()
sBase = []
sComp = input("Digite uma sentença a ser analisada: ")
llCol = []
lF = []
nC = 0
nL = 0

#  Filtra a string inserida
temp = ""
for c in sComp:
    temp = temp + " " + c
print(temp)
sComp = temp

#  Separa as sentenças base em uma lista e conta o número de colunas base
sSplit = sComp.split()
for st in sSplit:
    if st.isalnum() and st != "v" and st not in sBase:
        sBase.append(st)
        nC = nC + 1

#  Calcula o número de linhas (excluindo cabeçalho)
nL = math.pow(2,nC)

#  Lista os valores das colunas base e popula a tabela-verdade
va = nL
for s in sBase:
    ls = []
    lsd = [] 
    cva = 0
    va = va/2
    vv = True
    for i in range(0,int(nL)):
        if cva == va:
            cva = 0
            vv = not vv
        lsd.append({s:vv})
        ls.append(vv)
        cva = cva + 1
    table.add_column(s,ls)
    llCol.append(lsd)

#  Calcula os valores da coluna final
for i in range(0,int(nL)):
    t = False
    exe = "t = "
    for st in sComp:
        if st.isalnum() and st != "v":
            exe = exe + str(llCol[sBase.index(st)][i][st])
        else:
            exe = exe + st
    exe = exe.replace("&", "and")
    exe = exe.replace("v", "or")
    exe = exe.replace("~", "not")
    exec(exe)
    lF.append(t)

#  Adiciona a coluna final
table.add_column(sComp, lF)

#  Mostra a tabela no console
print(table)