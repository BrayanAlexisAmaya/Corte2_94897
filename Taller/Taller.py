
try:
    def Lista():
        L = open("organization_data.csv","r");
        ListaPaises = L.readlines();
        Matriz = [];
        L.seek(0);
        for i in range(len(ListaPaises)):
            Matriz.append([]);
            Datos = L.readline().rstrip("\n").split(",");
            for j in range(len(Datos)):
                Matriz[i].append(Datos[j]);
        L.close();

        Paises = [Matriz[0]];

        Matriz = sorted(Matriz, key= lambda x: x[4]);

        Lis = [];
        for i in range(len(Matriz)):
            if i + 1 != 10000:
                if Matriz[i][4] == Matriz[i+1][4]:
                    pass
                elif Matriz[i][4] == "Country":
                    pass
                else:
                    Lis.append(Matriz[i][4])
            else:
                Lis.append(Matriz[i][4]);
                break;

        for i in range(243):
            Paises.append([])
            for j in range(len(Matriz)):
                if Lis[i] == Matriz[j][4]:
                        Paises[i+1].append(Matriz[j]);

        return Paises;

    def Busqueda(Matriz,Buscar):
        Matriz = sorted(Matriz, key=lambda x: int(x[8]));
        return Matriz

    def app():
        Paises = Lista();
        Buscar = "";
        print("Para salir ingrese 0")
        while Buscar != 0:

            Buscar = int(input("\nIndice del pais de busqueda: "));
            if Buscar != 0:

                Empresas = Busqueda(Paises[Buscar], Buscar);
                print(f"\nPais:{Paises[Buscar][0][4]}");

                print("\nEmpresa con mayor # de empleados: ");
                for i in range(len(Paises[0])):
                    print(f"- {Paises[0][i]}:{Empresas[-1][i]}");

                print("\nEmpresa con menor # de empleados: ");
                for i in range(len(Paises[0])):
                    print(f"- {Paises[0][i]}:{Empresas[0][i]}");

                Empleados = [];
                for i in range(len(Empresas)):
                    Empleados.append(int(Empresas[i][8]));

                Promedio = sum(Empleados)/len(Empresas);
                print(f"\nPromedio empreados {format(Promedio, '.2f')}");
                print(f"Cantidad de empresas: {len(Empresas)}");

    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);