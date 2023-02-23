myList = ["Jackson A. Rodrigues", "Elisama M. Melo"];
#myList1 = [1,2,3,4,5,6,7,8,9,10];
#myList2= [True, False, True];
#myList3 = ["abc", 34, True, 40.9, "Jackson"];

#print(myList); imprimir a lista no console;
#print(len(myList)); imprimir o número de itens de uma lista;
#print(type(myList)); imprimir o tipo de dados;

thisList = list(("Lista", "usando", "construtor", "list()"));
if "usando" in thisList:
    thisList[1] = "alterar valor da lista";
    print(thisList); #alterar um valor de um item, primeiro tem que buscar e depois reatribuir;
else:
    print("item não existe na lista thisList.");

thisList.insert(0,"banana"); #inserindo um item a lista e especificando onde a ordem;
thisList.append("morango"); #inserindo um item no final da lista;
thisList.extend(myList); #adicionar elementos de outra lista;
thisList.remove("alterar valor da lista"); #remove um item especifico;
thisList.pop(2); #remove um índice especifico. Obs.: se você não especificar o índice ele remove o útimo da lista;
'''
A palavra del também remove o índice especifico;
'''
del thisList[1];
#del thisList; exclui a lista inteira;
#thisList.clear(); # O método esvazia a lista porém a lista permanece.

'''

pecorrendo um lista;

for x in thisList:
    print(x);


for i in range(len(thisList)):
    print(thisList[i]);

[print(x) for x in thisList];

i = 0;
while i < len(thisList):
    print(thisList[i]);
    i = i + 1;
'''
thisList.sort(reverse=True); #Lista a list alfanum, classifica a lista em ordem alfabética;
'''
Para classificar de forma descendente, use o argumento de palavra-chave reverse = True:
'''
print("origin: ", thisList);

copyList = thisList.copy(); #copia de uma lista;
copyList1 = list(thisList); #outra maneira de copir uma lista;
print("copy: ", copyList);
print("copy1: {}".format(copyList1));