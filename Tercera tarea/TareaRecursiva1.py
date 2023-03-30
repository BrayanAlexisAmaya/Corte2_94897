# Realice una función recursiva que calcule la siguiente función:
#K(n,p) = 1*p +2*p+3*p + ... + n*p
try:
    def Recursiva(K,N,P):
        if N != 0:
            J = N * P
            K.append(J)
            Recursiva(K,N-1, P)
            return sum(K)

    def app():
        N = int(input("ingrese hasta que numero desea realizar la funcion: "));
        P = int(input("Ingrese el numero base para la funcion: "));
        K = [];
        print(Recursiva(K,N,P));

    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);