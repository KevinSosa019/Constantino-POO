"""
    crear un dict con la siguiente tabla
    SISTEMAS    CIVIL      MATEMATICAS
    PROGRA2     SUELOS        MM110
    ALGO        DIBUJO        MM111
    POO         CARGAS        CALCULO

    Crear
    Leer
    Actualizar
    Borrar

    Crear las carreras
    Crear las clases
"""

carreras = []
seguir = True

while seguir:
    print(carreras)
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Buscar carrera")
    print("6. Salir")
    
    opcion = int(input("Ingrese su opcion: "))

    print("----------------------------------")
    
    if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre : ")
        dicCarrera = {}
        dicCarrera["carrera"] = nombre
        carreras.append(dicCarrera)
       
    elif opcion == 2:
        print("Leer (mostrar) carreras")
        for carrera in carreras:
            print("- Nombre :" + carrera["carrera"])
            
            
    elif opcion == 3:
        carreraActualizar = input("Ingrese nombre de la carrera : ")
        nuevoValor = input("Ingrese nuevo nombre de la carrera : ")

        indice = 0
        for carrera in carreras:
            if carrera["carrera"] == carreraActualizar:
                carrera["carrera"] = nuevoValor
        """
        indice = 0
        for carrera in carreras:
            if carrera["carrera"] == carreraActualizar:
                break
            else:
                indice = indice + 1

        carreras[indice]["carrera"] = nuevoValor
        """
       
    elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera: ")
        indice = 0
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == carreraBorrar:
                encontrado = True
                break
            else :
                indice = indice + 1

        if encontrado :
            carreras.remove(carreras[indice])
            print("Elemento borrado")
        else:
            print("No existe")



    elif opcion == 5:        
        buscarCarrera=input("Ingrese la carrera ha buscar: ")
        indice=0
        alterar=""
        noEncontrado=False
        centinela=False
        for carrera in carreras:
          if carrera['carrera']== buscarCarrera:  
              print("Se ha encontrado la carrera satisfactoriamente")
              
              alterar=input("Desea alterar la carrera? Y/N: ")   
                
              if alterar=="Y" or alterar=="y":
              
                 carreraActualizar=input("Ingrese nuevo nombre de la carrera: ")
                 indice=0
                 for carrera in carreras:
                   if carrera["carrera"] ==buscarCarrera:
                       carrera["carrera"]=carreraActualizar
                       
              elif alterar=="N" or alterar=="n":
                 print("Esta bien")
                 break
           
              else:
                 print("Debe de ser Y/N no otra palabra o letra")    
                 break
              
          else:
              indice = indice + 1
              noEncontrado=True
          
        if noEncontrado:   
          print('No se ha encontrado la carrera')
      
        
    elif opcion == 6:
        print("Hasta la proxima")
        seguir = False
    print("----------------------------------")

"""
[0  {'carrera': 'IS'},
 1  {'carrera': 'CIVIL'},
 2  {'carrera': 'IND'}]

"""