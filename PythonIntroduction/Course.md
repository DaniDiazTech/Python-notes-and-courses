
# For better details in code

if __name__ == '__main__':
    unittest.main(verbosity=2)

Ramification:
comparations 0 < 1,  0 != 0, etc

# Cristal boxes

La diferencia entre las pruebas de Caja Negra y Caja de Cristal es que en las pruebas de caja negra se escriben primero los test para ayudarnos a implementar nuevo código. 

En las pruebas de caja de cristal se asume que se tiene código escrito y las pruebas se escriben para verificar todas las ramificaciones del programa y probar todos los diferentes caminos posibles.

# How to fight with bugs
Debuggear: skill que es aprendible


Procedimiento:

1. NO usar tanto el debugger. Crea y usa los print()

2. Estudiar los datos que tenemos disponibles

3. Usar metodo cientifico, crear hipotesis y experimentar

Tip: Un proograma no falla, simplemente funciona de una manera diferente a la deseada

4.  Llevar un registro de los Bugs que han ocurrido, preferentemente con test

Diseñar experimentos: 
 
1. Buscar el pedazo de codigo que esta fallando. Se analiza una parte de programa, para ver si se comporta adecuadamente, y se continua hasta hayar donde esta el bug.

Errores comunes:

1. Encontrar errores comunes: Syntax Error, etc..

2.  Si no es un error comun revisa el flujo del codigo, con paciencia, y trata de mostrarselo a otras personas

3.  IMPORTANTE: Llevar un registro de los procedimientos y los resultados de estos que has usado

4. NO TE RINDAS

# Exceptions 

Un error en el interprete del codigo sucede.

1. Son realmente comunes
2. Normalmente se asocian a errores de Semantica:
    Excepciones comunes:
    ImportError : una importación falla;
    IndexError : una lista se indexa con un número fuera de rango;
    NameError : se usa una variable desconocida ;
    SyntaxError : el código no se puede analizar correctamente
    TypeError : se llama a una función en un valor de un tipo inapropiado;
    ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

3. Cuando hay una excepción el interprete termina el programa.

# Manage exception

1. Keywords:
try:
except:
finally:

2. No se deben silenciar excepciones

3. Para llamar una excepsión se usa:
raise:

# Affirmations:

Programación defensiva:
Se prepara el codigo para recibir los inputs deseados, mas que todo los tipos.

# Assert:
used for manage exceptions


