# Realice un programa donde se pueda consultar su
# horario de clases, de modo que ingresando el nombre de la
# materia indique el día de clase, la hora, el salón y el
# nombre del profesor
try:

    def Horario(Materia):
        Materias = ["calculo integral","fisica mecanica","taller de fisica mecanica","circuitos dc","programacion"];
        Materias.append("constitucion y democracia");
        Materias.append("cultura ecologica");
        Dia = ["Martes y jueves","Martes y jueves","Lunes","Martes y jueves","Martes y jueves","lunes","lunes"];
        Hora = ["7 a 9 am","9 a 11 am","1 a 3 pm","11 am a 1 pm","1 a 3 pm","3 a 5 pm","11 am a 1 pm"];
        Salon = ["406DB","405DB","306DB","306DB","303GO","304DB","Virtual"];
        Profesor = ["Lalinde murrillo","Pineda hernan","Ortiz cardenas","Pineda hernan","Torres barrera"];
        Profesor.append("Gonzales sierra");
        Profesor.append("Gonzales sierra");

        i = 0;
        Confirmacion = False;
        while i < 7:
            if Materia == Materias[i]:
                print("tienes",Materias[i],"los",Dia[i],"de",Hora[i],"en el salon",Salon[i],"con el profesor",Profesor[i]);
                Confirmacion = True;
                break;
            i += 1;
        if Confirmacion == False:
            print("no se ha encontrado esta materia")
            app();

    def app():
        print("Las materias son: ");
        print("calculo integral, fisica mecanica, taller de fisica mecanica, circuitos dc, programacion, constitucion y democracia, cultura ecologica");
        Materia = input("Ingrese la materia de la cual desea ver el horario: ");
        Horario(Materia.lower());

    if __name__ == "__main__":
        app();

except Exception as e:
    print(e);