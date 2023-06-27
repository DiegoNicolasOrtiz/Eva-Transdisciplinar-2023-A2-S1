# Eva-Transdisciplinar-2023-A2-S1

**Integrantes:**

-Diego Ortiz

-Débora Vizama

-Marcelo Vidal


## Descripción

Este es nuestro proyecto de Física y Programación 1, una simulación con interfaz de un evento físico dado por nuestros profesores para nuestra próxima evaluación. En nuestro caso, tenemos que simular el *Movimiento Rectilíneo Uniformemente Acelerado (MRUA)*. Este archivo da más detalle de cómo funciona nuestro algoritmo y algunos datos importantes sobre el fenómeno mencionado. 
  
  

## Evento Físico a Simular

**Origen**

La persona que descubrió el **MRUA** fue el gran matemático *Galileo Galilei*, logrando evidenciarlo mediante diversos experimentos (con bolas cayendo desde pendientes y dejando caer objetos desde la torre de pizza). Le fue de gran dificultad que su entorno social entendiera esto, ya que aunque la teoría que había hecho Aristóteles acerca de la caída libre era duramente criticada, ésta era fuertemente apoyada por la iglesia, lo que le causó varias discusiones al respecto a Galilei. Él consideraba que era mas importante describir el movimiento que averiguar sus causas, y se concentró en encontrar los principios matemáticos que explicaran lo que hoy en día llamamos movimiento uniformemente acelerado.

**Matemática Empleada**

Consiste básicamente en el cambio constante de la velocidad de un cuerpo en movimiento. Puede ser un auto acelerando, una pelota cayendo, etc. Cada segundo (**t**), el objeto en cuestión tendrá una posición (**x**) y velocidad (**v**) distintas, dando lugar a una recopilación de datos fascinante para los interesados en la física y matemática.
Debido a la cantidad de variables que están presentes en el evento físico, existen varias fórmulas que ayudan a calcular datos matemáticos para el trabajo, siendo las principales:

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/7f420f8d-5281-4a11-95da-f0140042ef44)

Siendo la primera la **ecuación de itinerario**.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/ead8ab43-e2f5-4596-9f59-9f55b4a970a9)

La segunda la **ecuación de la rapidez**.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/911cdf26-a023-4425-8f3c-bb79f37cd91f)

Y la tercera, la **ecuación de la aceleración**.

La posición del cuerpo en movimiento es clave en el proceso, porque ésta es constantemente modificada.

Teniendo sobre todo el foco en la *aceleración* (**a**) en cada expresión, ya que es la principal causante del fenómeno, y agrega la parte "Acelerado" a su nombre. La aceleración provoca que la velocidad cambie cada instante del proceso en movimiento del cuerpo, siendo un concepto realmente conocido cuando nos referimos a esa modificación de rapidez. La propia gravedad de la Tierra cuenta como una aceleración a la que somos sometidos en todo momento, correspondiendo a 9.8 metros partidos por segundos al cuadrado.
Cabe destacar que esta matemática enseñada es usada incluso en nuestro código para simular el proceso físico.

**¿Cómo se resuelve?**

Si tuviéramos que dar una solución a cómo resolver en sí la ecuación y proceso, sería averiguar la aceleración en la fórmula, la cual, es constante en este fenómeno, cada segundo siempre aumentará o disminuirá (La seguimos tratando cómo aceleración en términos correctos, ya que sigue siendo un cambio de la rapidez) a la velocidad en una misma cantidad. Con esta información, podemos obtenerla dividiendo la variación de la velocidad (**Δv**) por la variación del tiempo (**Δt**). Es de importancia considerar que, gracias a que la aceleración nunca cambia en este proceso, simular los datos tomados sería ir de cuesta arriba, literalmente. Si la velocidad aumenta y aumenta (Si disminuye eventualmente el cuerpo se detendría), significaría que el cuerpo, a cierto punto, iría tan rápido que por cada segundo, recorrería miles de kilómetros. Esto es, por supuesto, poco realista, pero matemáticamente correcto. Por este hecho, solo se suelen considerar los datos más racionales a la hora de graficar este proceso, ya que como puede ver, en un gráfico de posición por tiempo, la recta avanza cada vez más por el eje *y* que en el eje *x*:
![Movimiento rectilíneo uniformemente acelerado (MRUA) - Didactalia: material  educativo](https://www.matesfacil.com/fisica/cinematica/MRUA/Z3.png)

**Aplicaciones**

El Movimiento Rectilíneo Uniformemente Acelerado se puede ver en situaciones donde un objeto se mueve en línea recta y su velocidad cambia de manera constante. A continuación, algunos ejemplos de como se puede ver en la vida cotidiana:

Saltar desde una silla: Cuando saltas desde una silla, experimentas un MRUA. Al principio, tu velocidad es cero, pero a medida que caes, tu velocidad aumenta constantemente debido a la gravedad.

Acelerar en un automóvil: Cuando un automóvil acelera desde una posición de reposo, experimenta un MRUA. La velocidad del automóvil aumenta de manera constante hasta que alcanza la velocidad deseada.

Frenar en una bicicleta: Si aplicas los frenos en una bicicleta, experimentas un MRUA negativo (desaceleración). Tu velocidad disminuye constantemente hasta que te detienes por completo.

Lanzar una pelota hacia arriba: Si lanzas una pelota hacia arriba, experimentará un MRUA. Al principio, la pelota se mueve rápidamente hacia arriba, pero su velocidad disminuye debido a la gravedad hasta que finalmente cae hacia abajo.

Estos ejemplos representan situaciones en las que puedes observar el movimiento rectilíneo uniformemente acelerado en tu vida diaria. El MRUA implica un cambio constante en la velocidad de un objeto en línea recta.

## Código

**Herramientas Utilizadas**
En el aspecto de programación, para realizar este trabajo necesitamos la ayuda de ciertas aplicaciones como Python 3 y Visual Studio Code con la extensión de Python.

-Python es un lenguaje de alto nivel de programación interpretado que al ser más básico, es ideal para empezar a aprender a programar, siendo utilizado para desarrollar aplicaciones de todo tipo.

-Visual Studio Code es un editor de código fuente desarrollado por Microsoft. Básicamente te da la posibilidad de escribir y ejecutar código en cualquier lenguaje de programación, esto gracias a sus extensiones y amplia cantidad de opciones.

También hay que mencionar las librerías en Python usadas, siendo ellas: **Pygame**, **Tkinter** y **Matplotlib**. 

-Pygame consiste en una manera sencilla de tratar con sprites y colocarlos en una ventana para crear simulaciones o videojuegos en dos dimensiones. Sus funciones ayudan a la resolución de figuras simples, movimientos que pueden registrar datos, entre otras cosas. En nuestro caso, nos ayudó para crear la simulación de cómo se debería mover un objeto respecto a los ejes de un gráfico con el MRUA.

-Tkinter se trata de un creador de interfaces para ventanas abiertas por código. Sus funciones incluyen botones, campos en los que se pueden colocar datos y poder tenerlos guardados, simplemente texto, entre otras cosas. Para nuestro equipo, la librería fue de ayuda para que el proyecto se vea más ordenado y con sentido para que se pueda comprender su estructura.

-Matplotlib es definido como la librería ideal para generar gráficos en dos dimensiones. Sus funciones incluyen lo más básico en gráficos, teniendo diferentes tipos de éstos, capacidad de colocar nombres a cada parámetro, colocar valores a ellos y demás. En este caso, ayudó en la creación del gráfico de nuestro evento físico, el cual se diferencia en gran medida con otros fenómenos por cómo funciona la recta en curva.

Siendo honestos como grupo, hay que mencionar sobre el gran uso de *Internet* para este proyecto. Sin las búsquedas numerosas sobre las funciones y librerías, enorme parte del trabajo estaría completo y pobre de información, por lo que, no podemos atribuirnos todo el crédito de redacción y funcionalidad a nosotros.

**Guía de Instalación**

Nuestro algoritmo es simple de instalar y usar. Si gusta probarlo, una vez el código es descargado de nuestro repositorio en el que hemos contribuido, hay que ejecutarlo(Imagen). Si todo se ha realizado correctamente, hay que ingresar los datos pedidos por el programa, siendo la velocidad inicial y la aceleración, solamente colocando los valores numéricos (Imagen). Una vez se haya hecho esto, cuando se presiona el botón "Nombre de botón", una simulación de la trayectoria del objeto aparecerá a la derecha, repitiéndose una y otra vez para la apreciación detallada del proceso (Imagen). Si gusta de una forma más detallada de presentar esta información, si presiona el botón "Gráfico", una pestaña nueva se abrirá para usted en el que verá la posición del cuerpo en los primeros 10 segundos de la simulación en un gráfico con los ejes correctamente nombrados (Imagen).

**Guía de Uso**



**Explicación del Código en Video**

A continuación, un video que explica oralmente nuestro código desarrollado en sus aspectos más importantes, además de una definición en otras palabras del evento físico que hemos presentado:
[(Video)](https://www.youtube.com/watch?v=yO754VJ7deg)
 

## Conclusiones
Cómo pueden ver, este evento físico es toda una curiosidad, desde sus orígenes hasta su uso matemático en el día de hoy hasta en los casos más mundanos. Es todo un desafío seguir avanzando en tecnología y, con tanta disposición, se siga enseñando a cada generación sobre estos sucesos que nos rodean, de una manera u otra. Se espera que haya sido una presentación de su agrado y que cada punto haya quedado claro, siendo éste nuestro mayor objetivo al hacer este gran proyecto.
