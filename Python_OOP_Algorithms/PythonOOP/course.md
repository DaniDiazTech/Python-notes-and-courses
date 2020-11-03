# Tipos de datos
Datos abstractos:
En Python todo es un objeto, todo tiene un tipo.
Que todo sea objeto significa que, todo en nuestro programa tiene una representacion en memoria.

Que todo tenga un tipo, significa que podemos encapsular, datos y comportamiento adentro de un objeto.

# Interaccion de objetos

1. Creacion
2. Manipulacion
3. Destruccion

# Ventajas 

1. Decomposicion
2. Abstraccion
3. Encapsulacion

# Clases

Son moldes, utilizadas para la creación de objetos.

# Instancias

Las clases son moldes, mientras los objetos son llamados instancias

* Cuando se crea una instancia,se ejecuta el método __init__
* Todos los metodos de una clase reciben el parametro self

# Atributos de clase
Permiten
    *  Representan datos
    *  Procedimientos para interatuar con los datos (metodos = funciones escritas dentro de las clases)
    *  Mecanismos para esconder representacion interna

*  Se accede a los atributos con un punto (.)

*  Puede tener atributos privados, inician con (_)

# Decomposición

*  Partir un problema en problemas más chiquitos
*  Clases permiten crear abstracciones, en forma de componente
*  Cada clase se  encarga de una parte del problema. El programa es mas facil de mantener

# Abstracción 
* Nos enfocamos en información importante
*  Separamos la info central de los detalles secundarios
* Podemos usar variables y métodos (Públicos o privados)


# Encapsulacion

* Permite agrupar datos y su comportamiento
* Controla el acceso a dichos datos
* Previene modificaciones no autorizadas

# Herencia
* Nos permite generar una jerarquia de clases

* Nos permite comportamiento comun en la jerarquia
* El padre se le conoce como superclase,los hijos son llamados subclases

# Polimorfismo 

* Habilidad de tomar varias formas
* Cambiamos comportamiento de una superclass y adaprtarlo a una subclase