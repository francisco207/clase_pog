class Banco:
    def __init__(self, numero_de_cuenta,titular,saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.titular = titular
        self.saldo = saldo

    def portal(self):
        print("numero de cuenta:", self.numero_de_cuenta)
        print("titular:", self.titular)
        print("saldo:", self.saldo)

print("Bienvenido al portal del banco")
lista_cuentas = []
while True:
    print("1. Crear cuenta")
    print("2. Ver cuentas")
    print("3. Realizar transacción")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        numero_de_cuenta = input("Ingrese el número de cuenta: ")
        for cuenta in lista_cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                print("El número de cuenta ya registrado.")
                break
        else:   
            titular = input("Ingrese el nombre del titular: ")
            saldo = float(input("Ingrese el saldo inicial: "))
            cuenta = Banco(numero_de_cuenta, titular, saldo)
            lista_cuentas.append(cuenta)
            print("Cuenta creada exitosamente.")
    elif opcion == "2":
        if not lista_cuentas:
            print("No hay cuentas registradas.")
        else:
            for cuenta in lista_cuentas:
                cuenta.portal()
                print("-" * 20)
   
    elif opcion == "3":
        numero_de_cuenta = input("Ingrese el número de cuenta para realizar la transacción: ")
        for cuenta in lista_cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                transaccion = input("Ingrese 'd' para depósito o 'r' para retiro: ").lower()
                if transaccion == 'd':
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuenta.saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: {cuenta.saldo}")
                elif transaccion == 'r':
                    monto = float(input("Ingrese el monto a retirar: "))
                    if monto > cuenta.saldo:
                        print("Saldo insuficiente.")
                    else:
                        cuenta.saldo -= monto
                        print(f"Retiro exitoso. Nuevo saldo: {cuenta.saldo}")
                else:
                    print("Transacción no válida.")
                break
        else:
            print("Número de cuenta no encontrado.")
   
   
    elif opcion == "0":
        print("Gracias por usar el portal del banco.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

