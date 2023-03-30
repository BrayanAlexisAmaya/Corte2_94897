# Realice una función recursiva que calcule el factorial o el número de fibonacci
# (dependiendo del ejercicio que le salió en el parcial).
try:
    def Factorial(N):
        if N == 1:
            return 1
        else:
            return N*Factorial(N-1);

    def app():
        N = int(input("Ingrese el numero al que le quiere sacar factorial: "));
        print(Factorial(N))

    if __name__ == "__main__":
        app()

except Exception as e:
    print(e);