import os
from time import sleep

"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE     : PAUL JUNIOR ZAPANA VARGAS
"""

dic_empresas = {
    '00000001': {
        'razon_social': 'TECSUP',
        'direccion': 'JOSE LUIS BUSTAMANTE Y RIVERO'
    }
}

ANCHO = 50

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("*" * ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
    """)
    print("*" * ANCHO)

    opcion = input("ELIJA UNA  OPCIÓN : ")

    if not opcion.isdigit():
        print("Opción inválida")
        # input("Presione ENTER para continuar...")
        continue

    opcion = int(opcion)
    os.system("cls" if os.name == "nt" else "clear")

    # REGISTRAR
    if opcion == 1:
        print("*" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("*" * ANCHO)

        ruc = input("Ingrese RUC: ")

        if ruc in dic_empresas:
            print("La empresa ya existe")
        else:
            razon_social = input("Ingrese Razón Social: ")
            direccion = input("Ingrese Dirección: ")

            dic_empresas[ruc] = {
                'razon_social': razon_social,
                'direccion': direccion
            }
            print("Empresa fue registrada correctamente!")

    # MOSTRAR
    elif opcion == 2:
        print("*" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("*" * ANCHO)

        if not dic_empresas:
            print("No hay empresas registradas")
        else:
            for ruc, info in dic_empresas.items():
                print(f"RUC           : {ruc}")
                print(f"Razón Social  : {info['razon_social']}")
                print(f"Dirección     : {info['direccion']}")
                print("*" * ANCHO)

    # ACTUALIZAR
    elif opcion == 3:
        print("*" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("*" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a actualizar: ")

        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")

            nueva_razon = input(f"NUEVA RAZÓN SOCIAL ({dic_empresas[ruc]['razon_social']}): ")
            nueva_direccion = input(f"NUEVA DIRECCIÓN ({dic_empresas[ruc]['direccion']}): ")

            if nueva_razon:
                dic_empresas[ruc]['razon_social'] = nueva_razon
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_direccion

            print("Empresa actualizada correctamente!")
        else:
            print("No se encontró empresa")

    # ELIMINAR
    elif opcion == 4:
        print("*" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("*" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a eliminar: ")

        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada correctamente!")
        else:
            print("No se encontró la empresa")

    # SALIR
    elif opcion == 5:
        print("*" * ANCHO)
        print(" " * 10 + "FINALIZANDO EL PROGRAMA")
        print("*" * ANCHO)
        sleep(2)
        break

    else:
        print("Opción no válida")

    input("Presione ENTER para continuar!!")