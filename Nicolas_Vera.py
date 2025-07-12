import os
os.system("cls")

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD,procesador, video]}

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def stock_marca():
    global i
    global marca
    marca = 0
    for i in productos.items():
        print(i[1])
        for marca in i:
             if marca in i:
                  print(i)
             
  
    #marca = input("Ingrese marca a consultar: ")
    #for marca in productos.items:
        #input(productos[0])
  



def opcione():
    try:
        opcion = int(input("Ingrese opcion: "))
        if opcion <=4 and opcion >= 1:
            if opcion == 1:
                input("Stock marca")
                stock_marca()
            if opcion == 2:
                input("Busqueda de precio")
            if opcion == 3:
                 input("Actualizar precio")
            if opcion == 4:
                 input("Salir")
        else:
            input("Debe ingresar una opcion valida!!")
            opcione()
                      
    except:
        input("Debe ingresar una opcionnnn valida!!")
        opcione()

def menu():
    
        os.system("cls")
        print("***MENU PRINCIPAL***")
        print("1. Stock marca")
        print("2.Búsqueda por precio")
        print("3.Actualizar precio")
        print("4.Salir")
        opcione()
        


stock_marca()