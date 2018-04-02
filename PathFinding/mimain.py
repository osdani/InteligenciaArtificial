from claseE import formato
import ast

o= raw_input('Ciudad de Origen: ')                                                   # Tomamos la ciudad
#Ciudad = formato('Ciudad',[h de los vecinos],[Vecinos],[g con los vecinos]) # estructura para crear la ciudad
# ---- Ciudades .....
Arad = formato('Arad',[374,253,329],['Zerind','Sibiu','Timisoara'],[75,140,118])
Bucarest = formato('Bucarest',[77,80,176,100],['Giurgiu','Urziceni','Fagaras','Pitesti'],[90,85,211,101])
Craiova = formato('Craiova',[242,193,100],['Dobreta','RimnicuVilcea','Pitesti'],[120,146,138])
Dobreta = formato('Dobreta',[241,160],['Mehadia','Craiova'],[75,120])
Eforie = formato('Eforie',[151],['Hirsova'],[86])
Fagaras = formato('Fagaras',[253,0],['Sibiu','Bucarest'],[99,211])
Giurgiu = formato('Giurgiu',[0],['Bucarest'],90)
Hirsova = formato('Hirsova',[80,161],['Urziceni','Eforie'],[98,86])
Iasi = formato('Iasi',[234,199],['Neamt','Vaslui'],[87,92])
Lugoj = formato('Lugoj',[329,241],['Timisoara','Mehadia'],[11,70])
Mehadia = formato('Mehadia',[242,244],['Dobreta','Lugoj'],[75,70])
Neamt = formato('Neamt',[226],['Iasi'],[87])
Oradea = formato('Oradea',[374,253],['Zerind','Sibiu'],[71,151])
Pitesti = formato('Pitesti',[193,0,160],['RimnicuVilcea','Bucarest','Craiova'],[97,101,138])
RimnicuVilcea = formato('RimnicuVilcea',[253,100,160],['Sibiu','Pitesti','Craiova'],[80,97,146])
Sibiu = formato('Sibiu',[176,193,380,366],['Fagaras','RimnicuVilcea','Oradea','Arad'],[99,80,151,140])
Timisoara = formato('Timisoara',[366,244],['Arad','Lugoj'],[118,111])
Urziceni = formato('Urziceni',[0,151,199],['Bucarest','Hirsova','Vaslui'],[85,98,142])
Vaslui = formato('Vaslui',[226,80],['Iasi','Urziceni'],[92,142])
Zerind = formato('Zerind',[380,366],['Oradea','Arad'],[71,75])

#----- PROGRAMA ----
p= eval(o)                    # convertir a objeto
u=[]                          # crear lista cerrada
x=0
u.append(o)                 #Agregar ciudad origen
while(x==0):
    y=0
    d=p.Fa()               # Encontrar ciudad con menor f
    for i in range(len(u)):
        m=u[i]
        if d ==m:   # Comparar lista cerrada con la ciudad con menor f
            y=1
    if y!=1:
        u.append(d)
    else:
        a= p.re()
    o=d
    p=eval(d)
    if d=='Bucarest':
        x= 1                #Si llega a Bucarest termina el programa
print u                     # imprimir ruta
