# Realice un programa donde permita crear una lista de
# 10 números aleatorios entre 1 y 50 (todos números enteros),
# después cree dos funciones donde se reciba la lista como
# parámetro para:
# mayor() - Función que imprima el número mayor de la lista
# (no puede usar el método max())
# primos() - función que imprima los números de la lista que
# son primos.
import random as r
try:

    def NumerosAleatorios():
        i = 0;
        Numeros = [];
        while i < 10:
            Numeros.append(r.randint(1,50));
            i += 1;
        return Numeros

    def Mayor(Numeros):
        k = 1;
        while k < 10:
            i = 0;
            while i < (10-k):
                if Numeros[i] > Numeros[i+1]:
                    Aux = Numeros[i];
                    Numeros[i] = Numeros[i+1];
                    Numeros[i+1] = Aux;
                i += 1;
            k += 1;
        return Numeros

    def Primos(Numeros):
        Primos = [];
        i = 0;
        while i < 10:
            n = 2;
            P = True
            while n < Numeros[i]:
                if Numeros[i]%n == 0:
                    P = False;
                n += 1;
            if P != False:
                Primos.append(Numeros[i]);
            i += 1;
        return Primos

    def app():
       Numeros = NumerosAleatorios();
       print(f"los numeros aleatorios son: {Numeros}");
       NumerosOrdenados = Mayor(Numeros);
       print(f"Los numeros aleatorios ordenados son: {NumerosOrdenados}");
       print(f"El numero mayor de la lista es: {NumerosOrdenados[-1]}");
       NumerosPrimos = Primos(NumerosOrdenados);
       print(f"Los numeros aleatorios primos son: {NumerosPrimos}");

    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);