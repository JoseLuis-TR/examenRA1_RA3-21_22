def comprobar_edad(e):
    """[Comprueba si la edad esta dentro del rango]

    :param e: [Edad introducia por el usuario]
    :type e: int
    :return: [True si esta dentro del rango y False si se encuentra fuera de este]
    :rtype: resultado booleano
    """
    if e in [6, 7, 8, 9, 10, 11, 12]:
        return True
    else:
        return False


def comprobar_mes(m):
    """[Comprueba que el mes introducido es correcto]

    :param m: [Mes introducido por el usuario]
    :type m: int
    :return: [True si es un mes correcto y False si no lo es]
    :rtype: resultado booleano
    """
    if m in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return True
    else:
        return False


def comprobar_numero_multiplicar(edadtabla, mestabla):
    """[Sabiendo la edad y el mes, devuelve en número que tablas le pertencen al usuario]

    :param edadtabla: [Edad introducida por el usuario]
    :type edadtabla: int
    :param mestabla: [Mes introducido por el usuario]
    :type mestabla: int
    :return: [Numero de cada una de las tablas a generar]
    :rtype: lista de enteros
    """
    rango_1 = [6, 7, 8]
    rango_2 = [9, 10]
    rango_3 = [11, 12]
    if edadtabla in rango_1:
        if mestabla % 2 == 0:
            return [2, 4]
        else:
            return [1, 3, 5]
    elif edadtabla in rango_2:
        if mestabla % 2 == 0:
            return [6, 8, 10]
        else:
            return [7, 9]
    elif edadtabla in rango_3:
        return [11, 12, 13]


def rango_edad(er):
    """[Devuelve un string del rango de edad al que pertenece el usuario]

    :param er: [Edad introducida por el usuario]
    :type er: int
    :return: [El rango al que pertenece el usuario]
    :rtype: string
    """
    if er in (6, 7, 8):
        return "[6-8]"
    elif er in (9, 10):
        return "[9-10]"
    elif er in (11, 12):
        return "[11-12]"


def par_o_impar(mesip):
    """[Comprueba si el mes es par o impar]

    :param mesip: [Mes introducido por el usuario]
    :type mesip: int
    :return: [La cadena par o impar dependiendo del resultado]
    :rtype: string
    """
    if mesip % 2 == 0:
        return "par"
    else:
        return "impar"


def tabla_multiplicar(base):
    """[Imprime en pantalla las tablas de multiplicar que le toca al usuario]

    :param base: [Numeros que le tocan al usuario según la tabla]
    :type base: lista de enteros
    :return: [No devuelve nada, cuando acaba el bucle de la función vuelve a la función pantalla_generacion_tablas]
    """
    for n in base:
        print(f"TABLA DEL {n}" + "\n" + "*" * 12)
        for i in range(1, 10 + 1):
            print(f"{n} x {i} = {n * i}")
            if i == 10:
                if n == base[-1]:
                    print("*" * 72)
                else:
                    print("\n")


def pantalla_generacion_tablas(nom, ed, me, num):
    """[Representa el programa de generación de tablas, recoge los datos introducidos por el usuario y la lista de
    números que le toca al usuario]

    :param nom: [Nombre introducido por el usuario]
    :type nom: string
    :param ed: [Edad introducida por el usuario]
    :type ed: int
    :param me: [Mes introducido por el usuario]
    :type me: int
    :param num: [numeros que le tocan al usuario segun la tabla]
    :type num: lista de enteros
    :return: [Se usa para salir del programa en caso de que el ususario no quiera repetir]
    """
    print("\n" + "*" * 72 + "\n" + f"PROGRAMA DE GENERACIóN DE TABLA: {nom}" + "\n" + "-" * 72)
    if not comprobar_edad(ed):
        print(f"Edad: {ed}. No se contempla esta edad" + "\n" + "*" * 72)
        repetir()
        return
    elif not comprobar_mes(me):
        print(f"Mes: {me}. El mes es erroneo")
        repetir()
        return

    print(f"Edad: {ed}. El alumno esta dentro del rango {rango_edad(ed)}" + "\n" +
          f"Mes: {me}. El mes es {par_o_impar(me)}, corresponden las tablas siguientes:" + str(num[0:]) + "\n"
          + "-" * 72 + "\n")
    tabla_multiplicar(num)
    repetir()


def repetir():
    """[Función usada para saber si repetir el programa o no]

    :return: [Si dice que sí vuelve a la función de inicio, en caso de que no vuelve a la función anterior que cerrara
    el programa]
    """
    while True:
        repeat = input("¿Quieres revisar las tablas de otro alumno? S/N" + "\n" + ">")
        if repeat.upper() == "S":
            print("\n")
            inicio()
        elif repeat.upper() == "N":
            break
        else:
            print("Introduce S o N")
            continue


def inicio():
    """[Pide al usuario su nombre, edad y el mes en el que está]

    :return: [No devuelve nada si no que desde ella se llama a otra función]
    """
    nombre = input("Esriba su nombre: ")
    while True:
        try:
            edad = int(input("Edad: "))
            mes = int(input("Mes en el que estás: "))
            break
        except ValueError:
            print("Escriba un número para la edad y el nacimiento")
            continue
    numeros = comprobar_numero_multiplicar(edad, mes)
    pantalla_generacion_tablas(nombre, edad, mes, numeros)


if __name__ == "__main__":
    inicio()
