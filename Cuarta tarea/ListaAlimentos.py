# Realice un programa para calcular el valor bruto de un producto alimenticio según la última reforma tributaria
# del IVA de la canasta familiar del año 2023.
# Primero se debe leer el archivo Alimentos.txt, para organizar cada uno de los artículos según el valor del IVA.
# El usuario ingresará un producto del listado, junto con el valor neto del mercado actual, entonces el programa
# retornará el valor base del producto y el valor del iva discriminados.
# El programa funcionará continuamente hasta que el usuario escriba "salir"
try:
    def Lista():
        L = open("Alimentos.txt","rt");
        Alimentos = L.readlines();
        ListaAlimentos = [];
        L.seek(0);
        for i in range(len(Alimentos)):
            ListaAlimentos.append([]);
            Valor = L.readline().strip("\n").split(",");
            for j in range(len(Valor)):
                ListaAlimentos[i].append(Valor[j]);
        L.close();
        return ListaAlimentos;

    def Busqueda(Matriz,Buscar):
        for i in range(len(Matriz)):
            for j in range(len(Matriz[i])):
                if " " in Buscar:
                    Buscar = Buscar.split(" ");
                    Buscar = Buscar[-1];
                if Buscar in Matriz[i][j].lower():
                    Iva = float(Matriz[i][-1]);
                    break;
        return Iva

    def app():
        ListaAlimentos = Lista();
        Alimento = "";
        while Alimento.lower() != "salir":
            Alimento = input("Ingrese el alimento: ").lower();
            if Alimento.lower() != "salir":
                Valor = float(input("Ingrese el valor neto del alimento: "))
                Iva = Valor * Busqueda(ListaAlimentos,Alimento);
                ValorSinIva = Valor-Iva;
                print(f"\nEl alimento ingresado: {Alimento} tiene un iva de: {Busqueda(ListaAlimentos,Alimento)}");
                print(f"El valor bruto del alimento es: {ValorSinIva} y el iva discriminado es: {Iva}\n");
 


    if __name__ == "__main__":
            app();

except Exception as e:
    print(e);