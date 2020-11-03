# Introduccion a complejidad algoritmica

* Complejidad temporal:
    El tiempo que toma completar un algoritmo
    * Se define como T(n)

* Complejidad Espacial:
    Cuanto espacio necesitamos en memoria para completar un algoritmo

# Aproximación

* Contar los pasos que se ejecuten en un  algoritmo conforme se acercan al infinito

# Crecimiento asintotico
*  Conforme el dataset o el inputy se va al infinito
    * UN dataset no es mas que un conjunto de data

* No importan las variaciones pequeñas
* Se centra en lo que pasa conforme el tamaño del problema va llegando al infinito


* LO que mejor nos permite entenderla complejidad algoritmica es el peor de los casos

# Big O notation

* Importa el término de mayor tamaño

# Ley de la suma
* solo importa el termino de mayor tamaño, sin ningun coeficiente

* O(n) + O(n * n) = O(n + n´2) => O(n´2)

# Clases de Big O

*  O(1) = constante 
* O(n) = lineal (complejidad crece conforme se crece el input)
* O(log n) = logaritmica 
* O(n log n) = log lineal (se crece de manera logaritmica pero con una constante de por medio)
* O(n ´ x) = polinomico
* O(x ´ n) = se crece de manera exponencial
* O(n!) = se crece factorialmente
