# 1.	Crear con el uso de diccionarios una cesta de Compras, que permita adicionar prendas de vestir como: camisetas, pantalones, short, camisas, pantalonetas para hombres, en la compra deberá limitar que no exceda más de 10 productos. Se debe ingresar la prenda el precio y la talla para cada uno. Luego deberá calcular el valor a pagar. 


Cesta = {}
for i in range(11):
    print('***************Tenemos estos productos*********** ')
    print('camisetas, pantalones, short, camisas, pantalonetas para hombres')
    print()
    clave= input('-introduccir el producto que deseas comprar  : ')
    print('ingrese el valor de la prenda')
    valor = int(input(clave+ '  :  '))
    Cesta[clave]= valor
    
total = 0
for null,precio in Cesta.items():
    total += precio
    print("-------------------------------------------")

print(f"Estos son los productos que lleva {Cesta}") 
print("******************************************")
print(f"El precio de la Compras es : {total}")
