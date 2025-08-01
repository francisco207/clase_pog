class estudiante:
    def __init__(self,nombre,edad,nota1,nota2,nota3):
            self.nombre = nombre
            self.edad = edad
            self.nota1 = nota1
            self.nota2 = nota2
            self.nota3 = nota3

    def mostrar_datos(self):
          print("nombre",self.nombre)
          print("edad",self.edad)
          print("nota1",self.nota1)  
          print("nota2",self.nota2)   
          print("nota3",self.nota3)  

    def calcular_promedio(self):
          promedio = (self.nota1 + self.nota2 + self.nota3) / 3
          return promedio     
print("Bienvenido al sistemas estudiantes")
lista_estudiante = []
while True:   
    print("selecciones la opcion deseada")
    print("1.agregar estudiante")
    print("2.Mostrar informacion del estudiante")
    print("0.Salir")
    opcion = int(input())
    if opcion == 1:
        print("ingrese el nombre del estudiante")
        nombre = input()
        print("ingrese la edad del estudiante")
        edad = int(input())
        print("ingrese la primera nota")
        nota1 = float(input())
        print("ingrese la segunda nota")
        nota2 = float(input())
        print("ingrese la tercera nota")
        nota3 = float(input())
        estudiante = estudiante(nombre,edad,nota1,nota2,nota3)
        lista_estudiante.append(estudiante)
        print("Estudiante registrado correctamente")
    elif opcion == 2:
         numero_estudiantes =len(lista_estudiante)
         print("El numero de estudiante es:",numero_estudiantes)    
         for estudiante in lista_estudiante:
              print("el nombre del estudiante es",estudiante.nombre)
              print("el promedio del estudiante es",estudiante.calcular_promedio())
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
         print("Opcion no valida") 