

class formato():
    def __init__(self, n, h, veci,g):     # Se crean caracteristicas de una ciudad

        self.n =n                #Nombre
        self.h = h                    #distancia de la ciudades vecinas a Bucarest
        self.veci = veci            # vector de vecinos
        self.g = g             # los g

    def Fa(self):                # Encuentra el min f
        t=0
        z=0
        c=[]
        for i in range(len(self.g)):         # Encontrar f's
            d = self.g[i]
            suma= d+self.h[i]
            c.append(suma)
        t=min(c)
        for i in range(len(c)):
            if t == c[i]:
                z=i
        return str(self.veci[z])            # retorna ciudad min

    def re(self):                                    # elimina el fmin con su respectiva ciudad, h, y g
        t=0
        z=0
        c=[]
        for i in range(len(self.g)):   #Hallar f
            d = self.g[i]
            suma= d+self.h[i]
            c.append(suma)         #Agrega f a una lista de F's
        t=min(c)                     #encuentra el min f
        for i in range(len(c)):   
            if t == c[i]:
                z=i

        a= self.veci
        a.pop(z)          # eliminar vecino
        c.pop(z)          #elminar f
        self.g.pop(z)              # elminar g
        self.h.pop(z)          # eliminar h
        return c
