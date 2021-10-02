def chargementniv(chiffre) :  # pour charger à partir du fichier correspondant au numéro du niveau (chiffre) les blocs du niveau
    niveau=[]


    fichier = open("niveauxTXT/niveau"+str(chiffre)+".txt","r")
    c= "&"
    n=1
    compteurX=0
    compteurY=0
    while c != "":
        c= fichier.read(1)
        if c !="":
            niveau.append((compteurX,compteurY,c))
            n=n+1
            compteurX=compteurX+1
            if n==16:
                compteurX=0
                n=1
                compteurY=compteurY+1
                c= fichier.read(1)

    fichier.close()
    return(niveau)


niv = input("Niveau à transformer? ")
res =chargementniv(niv)

for element in res:
    print(element)

fichier = open("niveauxJSON/niveau"+niv+".json","w") #On peut choisir le niveau à modifier en changeant le nombre au début
fichier.write("{\n\t\"niveau"+niv+"\": {\n")
fichier.write("\t\t\""+str(res[0][0])+","+str(res[0][1])+"\": "+str(res[0][2]))
i=0
for element in res:
    if i !=0:
        fichier.write(",\n")
        fichier.write("\t\t\""+str(element[0])+","+str(element[1])+"\": "+str(element[2]))
    else:
        i=1
fichier.write("\n\t}\n}")
fichier.close()

