import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(archivo):
    """
    Lee el archivo de gramática y devuelve un diccionario con las producciones.
    """
    gramatica = {}
    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if '->' in linea:
                izq, der = linea.split('->')
                izq = izq.strip()
                der = [x.strip() for x in der.split()]
                if izq not in gramatica:
                    gramatica[izq] = []
                gramatica[izq].append(der)
    return gramatica

def leer_cadenas(archivo):
    """
    Lee un archivo de texto que contiene las cadenas de aceptación.
    """
    cadenas = []
    with open(archivo, 'r') as f:
        for linea in f:
            cadenas.append(linea.strip())  # Elimina espacios en blanco y saltos de línea
    return cadenas

def construir_arbol(gramatica, simbolo_inicial, cadena, max_profundidad=10):
    """
    Construye un grafo de derivación a partir de la gramática y una cadena.
    """
    G = nx.DiGraph()  # Usamos un grafo dirigido para el árbol de derivación
    index_cadena = 0  # Índice para rastrear el progreso en la cadena
    profundidades = {simbolo_inicial: 0}  # Controlar la profundidad para evitar recursión infinita

    def agregar_nodo(padre, simbolo, visitados):
        """
        Función recursiva que añade nodos al grafo de derivación.
        """
        nonlocal index_cadena
        profundidad_actual = profundidades.get(simbolo, 0)

        if simbolo == 'lambda':  # Si la producción es vacío (lambda), no añadimos más nodos
            G.add_edge(padre, 'lambda')
            return
        
        if index_cadena >= len(cadena):  # Si hemos alcanzado el final de la cadena
            return

        if simbolo == cadena[index_cadena]:  # Si el símbolo coincide con el actual de la cadena
            G.add_edge(padre, simbolo)
            index_cadena += 1
        elif simbolo.islower():  # Si es un terminal (minúscula) pero no coincide, no es válida
            return
        else:  # Si es un no terminal
            if profundidad_actual >= max_profundidad:
                return  # Evitar recursión infinita por demasiada profundidad

            producciones = gramatica.get(simbolo, [])
            for produccion in producciones:
                for s in produccion:
                    G.add_edge(padre, s)
                    profundidades[s] = profundidad_actual + 1
                    agregar_nodo(s, s, visitados.copy())  # Copiar el conjunto visitados para no afectar otras ramas

    agregar_nodo(simbolo_inicial, simbolo_inicial, set())  # Iniciar con un conjunto vacío de visitados
    return G

def dibujar_arbol(G, cadena):
    """
    Dibuja el árbol de derivación usando matplotlib.
    """
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, node_size=3000, font_weight='bold', arrows=True)
    plt.title(f'Árbol de derivación para la cadena: {cadena}')
    plt.show()

# Programa principal
if __name__ == '__main__':
    archivo_gramatica = 'gramatica.txt'  # Archivo de gramática
    archivo_cadenas = 'cadenas.txt'  # Archivo con las cadenas de aceptación
    simbolo_inicial = 'A'  # Simbolo inicial de la gramática

    # Leer la gramática
    gramatica = leer_gramatica(archivo_gramatica)

    # Leer las cadenas
    cadenas = leer_cadenas(archivo_cadenas)

    # Procesar cada cadena
    for cadena in cadenas:
        print(f'Procesando la cadena: {cadena}')
        # Construir el árbol de derivación
        arbol = construir_arbol(gramatica, simbolo_inicial, cadena)

        # Dibujar el árbol
        dibujar_arbol(arbol, cadena)

