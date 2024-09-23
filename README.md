* Manuel Cardenas
* Andres Toledo
* Bryan Ariza



1. Introduccion:
   
   En este trabajo se busca desarrollar un programa en Python que lea un archivo de texto con reglas gramaticales y genere un gráfico de árbol a partir de dichas reglas. Para ello, se deben seguir varios pasos que comienzan con la comprensión de la gramática y su estructura, la lectura y análisis del archivo para extraer las reglas gramaticales, y finalmente, la creación del árbol gráfico utilizando las reglas obtenidas.
   El programa debe implementar la lectura del archivo de gramática y, utilizando la librería NetworkX de Python, generar un gráfico que represente visualmente las relaciones jerárquicas descritas en las reglas gramaticales. Una vez desarrollado el programa, es esencial probarlo con diferentes archivos para garantizar que la generación del árbol gráfico sea precisa y acorde a las reglas de cada archivo. Finalmente, el gráfico generado debe ser mostrado como la salida final del programa.

2. Instalacion del NetworkX:
  
 2.1) Actualizar los repositorios de Ubuntu:

        sudo apt update

 2.2) Insta lar Pip con el siguiente comando:

       sudo apt install python3-pip
       
 2.3) Ya con el pip instalado se debe instalar la librería NetworkX:

      pip3 install networkx
      
2.4) Ahora verificar que la instalación fue exitosa ejecutando Python e importando la librería:

    python3
  Luego, dentro del entorno interactivo de Python, escribe:
 
    import networkx
Si la instalación fue exitosa, no debe aparecer ningún error después de ejecutar este comando.

3) Ejecucion

   3.1) Descargar el archivo Ejercicio y entrar a el

       Cd (lugar donde se encuentre el archivo normalmente se encontrara en Descargas "Dowloands")

   3.2) Ejecuta el archivo con el siguiente comando

         pyton3 Grafo.py
   3.3) si se quiere cambiar la gramatica solo se ejecuta el comando:

         nano gramatica.txt
         nano cadenas.txt
   esto es para cambiar tanto la estructura de la gramatica como las cadenas que se deban monstrar
        

   
