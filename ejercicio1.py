class estudiante:
    def __init__(self,edad,nota1,nombre,nota2,nota3):
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
    
print("Bienvenido a la gestion estudiantes")
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

promedio_estudiante =estudiante.calcular_promedio()
print("el promedio de ",estudiante.nombre,"es",promedio_estudiante)