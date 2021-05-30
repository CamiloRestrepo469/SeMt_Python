# 1.	Diseñe una función que permita registrar la información de un grupo de 5 personas como los siguientes datos: identificación, nombre, salario, comisión, bonificaciones.
# 2.	La función antes de insertar a la lista debe permitir validar que el salario sea superior de 900000 que las comisiones mayores de 0 al igual que las bonificaciones.
# 3.	Deberá diseñar una segunda función donde esta permita mostrar la información contenida en la lista.
# 4.	Deberá realizar una función que permita buscar un dato en la lista.


for i in range(2):

    class Resgistrar:
        def __init__(self, identificacion, nombre , salario) :
            print('**** por favor llenar todos los campos ******')
            
            self.identificacion = input('  digite la identificacion : ')
            identificacion=identificacion
            self.nombre = input('  nombre completos : ' )
            nombre=nombre
            
            print(' ----si su salario es mayor de 900.000 tiene derecho a bonificacion')
            self.salario =  int(input('  ingrese el salirio : '))
            salario=salario


        def __str__(self):
            return "identificacion: " + self.identificacion + ", nombre: "+ str(self.nombre) + ", salario: " + str(self.salario)


    class Insertar(Resgistrar):
        def __init__(self, identificacion, nombre, salario, comision, bonificacion) :
            super().__init__(identificacion, nombre, salario) 
            total=0 
            self.comision =comision  
            self.bonificacion =  bonificacion
            if salario > "900000":
                total= bonificacion+comision
                print(f'tienen derecho a bonificacion {salario}') 
            else:
                total=salario
                print(f"No tiene derecho bonificacion {salario}")

            print(salario) 
            print("-----------------------------------------------")        
            print(f"esta es la total sin bonificacion {total}")         

        def __str__(self):
            return super().__str__() + ", comision: " + str(self.comision) + ", bonificacion: " + str(self.bonificacion)
        

    resgistrar = Resgistrar
    print("-----------------------------------------------")   
    print(resgistrar)

    print("-----------------------------------------------")   
    insertar = Insertar("","", "","12000","10000") 

    print(insertar)

resgistrar = Resgistrar
print("-----------------------------------------------")   
print(resgistrar)
print("-----------------------------------------------")   
insertar = Insertar("","", "","12000","10000") 
print(insertar)

print(f"lista de  {i}")







        




