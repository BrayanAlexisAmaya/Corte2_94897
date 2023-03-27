# Realice un programa donde se cree una matriz de 5x10, después se imprima en
# pantalla la matriz creada, indicando cuál es el número más alto y  más bajo dentro
# de la lista, incluyendo su respectiva posición.Finalmente se organice la matriz del
# número mayor al menor, empezando desde la posición[0, 0].
try:
    import random as r

    def MatrizRand():
        Matriz = [];
        for i in range(5):
            Matriz.append([]);
            for j in range(10):
                Matriz[i].append(r.randint(1,50));
        return Matriz;

    def MatrizOrdenada(Matriz):
        MatrizOr = [];
        for i in range(5):
            for j in range(10):
                MatrizOr.append(Matriz[i][j]);

        for k in range(1,50):
            n = 0;
            while n < (50-k):
                if MatrizOr[n] < MatrizOr[n+1]:
                    Aux = MatrizOr[n];
                    MatrizOr[n] = MatrizOr[n+1];
                    MatrizOr[n+1] = Aux;
                n += 1;

        MatrizMa = [];
        for i in range(5):
            MatrizMa.append([]);
            for f in range(((i+1)*10)-10,((i+1)*10)):
                MatrizMa[i].append(MatrizOr[f])
        return MatrizMa;

    def Mayor(Matriz,MatrizOR):
        for i in range(5):
            for j in range(10):
                if Matriz[i][j] == MatrizOR[0][0]:
                    Fila = str(i);
                    Columana = str(j);
                    Index = "["+Fila+","+Columana+"]";
        return Index;

    def Menor(Matriz,MatrizOR):
        for i in range(5):
            for j in range(10):
                if Matriz[i][j] == MatrizOR[4][9]:
                    Fila = str(i);
                    Columana = str(j);
                    Index = "["+Fila+","+Columana+"]";
        return Index;

    def app():
        Matriz = MatrizRand();
        MatrizOr = MatrizOrdenada(Matriz);
        IndexMayor = Mayor(Matriz,MatrizOr);
        IndexMenor = Menor(Matriz, MatrizOr);
        print(f"La matriz creada es:");
        for i in range(5):
            print(Matriz[i]);
        print(f"\nEl numero mas alto en la matriz es: {MatrizOr[0][0]} y esta ubicado en el indice: {IndexMayor}");
        print(f"El numero mas bajo en la matriz es: {MatrizOr[4][9]} y esta ubicado en el indice: {IndexMenor}");
        print(f"\nLa matriz ordenada es: ")
        for i in range(5):
            print(MatrizOr[i]);


    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);