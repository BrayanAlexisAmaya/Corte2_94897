# Realice un función llamada Aleatorio() donde se retorne un número entre 100 y 120,
# excepto los números 110, 115 y 119. Al final se deben imprimir 10 números retornados
# de la función Aleatorio(), alternando el orden par, impar (Comenzando con número par).
import random as r
try:

    def Aleatorio():
        i = 0;
        while i < 10:
            num = r.randint(100,121);
            if num != 110 and num != 115 and num != 119:
                if i%2 == 0:
                    if num%2 == 0:
                        print(num);
                        i += 1;
                elif i%2 != 0:
                    if num%2 != 0:
                        print(num);
                        i += 1;

    if __name__ == "__main__":
        Aleatorio();

except Exception as e:
    print(e);