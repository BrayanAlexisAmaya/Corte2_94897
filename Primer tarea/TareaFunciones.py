# Realice un programa donde se cree una función que permita
# calcular el seno, cose, tangente, exponencial y logaritmo
# natural. El usurio deberá ingresar como entrada el valor
# y la función a aplicar, mostrando por pantalla el valor
# ingresado seguido del resultado de la función matemática
# implementada.
import math as n
try:

    def Funciones(Funcion,Valor):

        if Funcion == 1:
            Seno = n.sin(Valor);
            print(Seno);
        elif Funcion == 2:
            Coseno = n.cos(Valor);
            print(Coseno);
        elif Funcion == 3:
            Tangente = n.tan(Valor);
            print(Tangente);
        elif Funcion == 4:
            Exponencial = n.exp(Valor);
            print(Exponencial);
        elif Funcion == 5:
            Logaritmo = n.log(Valor);
            print(Logaritmo);
        else:
            print("Esta funcion no esta definida");

    def app():

        print("Seleccione la funcion a realizar:\n1. Funcion seno");
        print("2. Funcion coseno\n3. Funcion tangente")
        print("4. Funcion exponencial\n5. Funcion logaritmo natural");
        print("Recuerde que los resultados estan dados en RAD")
        Funcion = int(input("funcion: "));
        Valor = float(input("Ingrese el numero a evaluar: "));
        Funciones(Funcion, Valor);

    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);