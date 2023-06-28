# Eva-Transdisciplinar-2023-A2-S1

**Integrantes:**

-Diego Ortiz

-Débora Vizama

-Marcelo Vidal


## Descripción

Este es nuestro proyecto de **Física** y **Programación 1**, una simulación con interfaz de un evento físico dado por nuestros profesores para nuestra próxima evaluación. En nuestro caso, tenemos que simular el *Movimiento Rectilíneo Uniformemente Acelerado (MRUA)*. Este archivo da más detalle de cómo funciona nuestro algoritmo y algunos datos importantes sobre el fenómeno mencionado, además de una guía de instalación, guía de uso, entre otros detalles, todo con el objetivo de dar mayor comodidad y disponibilidad. 
  


## Evento Físico a Simular

**Origen**

La persona que descubrió el **MRUA** fue el gran matemático *Galileo Galilei*, logrando evidenciarlo mediante diversos experimentos (con bolas cayendo desde pendientes y dejando caer objetos desde la torre de pizza). Le fue de gran dificultad que su entorno social entendiera esto, ya que aunque la teoría que había hecho Aristóteles acerca de la caída libre era duramente criticada, ésta era fuertemente apoyada por la iglesia, lo que le causó varias discusiones al respecto a Galilei. Él consideraba que era más importante describir el movimiento que averiguar sus causas, y se concentró en encontrar los principios matemáticos que explicaran lo que hoy en día llamamos movimiento uniformemente acelerado.

**Matemática Empleada**

Consiste básicamente en el cambio constante de la velocidad de un cuerpo en movimiento **en línea recta**. Puede ser un auto acelerando, una pelota cayendo, etc. Cada segundo (**t**), el objeto en cuestión tendrá una posición (**x**) y velocidad (**v**) distintas, dando lugar a una recopilación de datos fascinante para los interesados en la física y matemática.
Debido a la cantidad de variables que están presentes en el evento físico, existen varias fórmulas que ayudan a calcular datos matemáticos para el trabajo, siendo las principales:

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/7f420f8d-5281-4a11-95da-f0140042ef44)

Siendo la primera la **ecuación de itinerario**.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/ead8ab43-e2f5-4596-9f59-9f55b4a970a9)

La segunda, la **ecuación de la rapidez**.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/911cdf26-a023-4425-8f3c-bb79f37cd91f)

Y la tercera, la **ecuación de la aceleración**.

La posición del cuerpo en movimiento es clave en el proceso, porque ésta es constantemente modificada.

Teniendo sobre todo el foco en la *aceleración* (**a**) en cada expresión, ya que es la principal causante del fenómeno, y agrega la parte "Acelerado" a su nombre. La aceleración provoca que la velocidad cambie cada instante del proceso en movimiento del cuerpo, siendo un concepto realmente conocido cuando nos referimos a esa modificación de rapidez. La propia gravedad de la Tierra cuenta como una aceleración a la que somos sometidos en todo momento, correspondiendo a 9.8 metros divididos por segundos al cuadrado.

Cabe destacar que esta matemática enseñada es usada incluso en nuestro código para simular el proceso físico.

**¿Cómo se resuelve?**

Si tuviéramos que dar una solución a cómo resolver en sí la ecuación y proceso, sería averiguar la aceleración en la fórmula, la cual, es constante en este fenómeno, cada segundo siempre aumentará o disminuirá (La seguimos tratando cómo aceleración en términos correctos, ya que sigue siendo un cambio de la rapidez) a la velocidad en una misma cantidad. Con esta información, podemos obtenerla dividiendo la variación de la velocidad (**Δv**) por la variación del tiempo (**Δt**). Es de importancia considerar que, gracias a que la aceleración nunca cambia en este proceso, simular los datos tomados sería ir de cuesta arriba, literalmente. Si la velocidad aumenta y aumenta (Si disminuye eventualmente el cuerpo se detendría), significaría que el cuerpo, a cierto punto, iría tan rápido que por cada segundo, recorrería miles de kilómetros. Esto es, por supuesto, poco realista, pero matemáticamente correcto. Por este hecho, solo se suelen considerar los datos más racionales a la hora de graficar este proceso, ya que como puede ver, en un gráfico de posición por tiempo, la recta avanza cada vez más por el eje *y* que en el eje *x*:

![Movimiento rectilíneo uniformemente acelerado (MRUA) - Didactalia: material  educativo](https://www.matesfacil.com/fisica/cinematica/MRUA/Z3.png)

Como se puede apreciar, la solución del fénomeno correspondería a cuánto recorrería el cuerpo cada segundo. Teniendo todavía en cuenta que esto sería en una línea recta, nunca cambiando la dirección del movimiento. Por lo que, si el ejemplo fuera una caída, cuando el cuerpo toque el suelo, ya no se considerarían más datos, debido al cambio drástico de velocidad, aceleración, entre otras cosas.

**Aplicaciones**

El Movimiento Rectilíneo Uniformemente Acelerado se puede ver en situaciones donde un objeto se mueve en línea recta y su velocidad cambia de manera constante. A continuación, algunos ejemplos de como se puede ver en la vida cotidiana:

*Saltar desde una silla*: Cuando saltas desde una silla, experimentas un MRUA. Al principio, tu velocidad es cero, pero a medida que caes, tu velocidad aumenta constantemente debido a la gravedad.

*Acelerar en un automóvil*: Cuando un automóvil acelera desde una posición de reposo, experimenta un MRUA. La velocidad del automóvil aumenta de manera constante hasta que alcanza la velocidad deseada.

*Frenar en una bicicleta*: Si aplicas los frenos en una bicicleta, experimentas un MRUA negativo (desaceleración). Tu velocidad disminuye constantemente hasta que te detienes por completo.

*Lanzar una pelota hacia arriba*: Si lanzas una pelota hacia arriba, experimentará un MRUA. Al principio, la pelota se mueve rápidamente hacia arriba, pero su velocidad disminuye debido a la gravedad hasta que finalmente cae hacia abajo.

Estos ejemplos representan situaciones en las que puedes observar el movimiento rectilíneo uniformemente acelerado en tu vida diaria. El MRUA implica un cambio constante en la velocidad de un objeto en línea recta.


## Código

**Herramientas Utilizadas**

En el aspecto de programación, para realizar este trabajo necesitamos la ayuda de ciertas aplicaciones como **Python 3** y **Visual Studio Code** con la extensión de Python.

-Python es un lenguaje de alto nivel de programación interpretado que al ser más básico, es ideal para empezar a aprender a programar, siendo utilizado para desarrollar aplicaciones de todo tipo.

-Visual Studio Code es un editor de código fuente desarrollado por Microsoft. Básicamente te da la posibilidad de escribir y ejecutar código en cualquier lenguaje de programación, esto gracias a sus extensiones y amplia cantidad de opciones.

También hay que mencionar las librerías de Python usadas, siendo ellas: **Pygame**, **Tkinter**, **Matplotlib** y **Pillow**. 

-*Pygame* consiste en una manera sencilla de tratar con sprites y colocarlos en una ventana para crear simulaciones o videojuegos en dos dimensiones. Sus funciones ayudan a la resolución de figuras simples, movimientos que pueden registrar datos, entre otras cosas. En nuestro caso, nos ayudó para crear la simulación de cómo se debería mover un objeto respecto a los ejes de un gráfico con el MRUA.

-*Tkinter* se trata de un creador de interfaces para ventanas abiertas por código. Sus funciones incluyen botones, campos en los que se pueden colocar datos y poder tenerlos guardados, simplemente texto, entre otras cosas. Para nuestro equipo, la librería fue de ayuda para que el proyecto se vea más ordenado y con sentido para que se pueda comprender su estructura, siendo el menú principal la interfaz que creamos.

-*Matplotlib* es definido como la librería ideal para generar gráficos en dos dimensiones. Sus funciones incluyen lo más básico en gráficos, teniendo diferentes tipos de éstos, capacidad de colocar nombres a cada parámetro, colocar valores a ellos y demás. En este caso, ayudó en la creación del gráfico de nuestro evento físico, el cual se diferencia en gran medida con otros fenómenos por cómo funciona la recta en curva.

-*Pillow* corresponde a nuestra librería más reciente, la cual agrega soporta a la manipulación, guardado, entre otras funciones con archivos de formato de imagen. Para nuestro caso, fue de enorme utilidad para hacer la incrustación de la simulación de pygame en la interfaz de Tkinter mediante el tomar fotos cada cierto tiempo de la animación.

Siendo honestos como grupo, hay que mencionar sobre el gran uso de *Internet* para este proyecto. Sin las búsquedas numerosas sobre las funciones y librerías, enorme parte del trabajo estaría completo y pobre de información, por lo que, no podemos atribuirnos todo el crédito de redacción y funcionalidad a nosotros.

**Guía de Instalación**

Nuestro algoritmo es simple de instalar y usar. Si gusta probarlo, el proceso empieza descargando las aplicaciones mencionadas, siendo más que suficiente la última versión de Python, siendo Python 3, y Visual Studio Code.

Luego, son necesarias las librerías. Éstas se pueden descargar rápidamente ingresando en el buscador de tu computadora, el nombre de una aplicación que debería venir de fábrica en ella, llamándose "Símbolo del Sistema". Una vez se abra, se verá una gran caja para ingresar comandos. Esto correspondería al terminal cmd de tu dispositivo. La ventana debería verse así:

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/357713bd-cb26-4e4c-89a1-132e57e1edbf)

Para instalar las librerías de esa forma, se necesita el programa "pip3". Para poder instalarlo, es necesario tener Python3 (Puedes escribir "python --version" en la caja de comandos, y si está instalado, saldrá la versión que posees). Si cumples con ese requisito, escribe en la caja de comandos: 

*curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py*

Y después presiona el botón "enter" como si fuera un mensaje. Algo de texto debería aparecer. 

Acto seguido, escribe:

*python get-pip.py*

Y después presiona el botón "enter" como si fuera un mensaje. Inmediatamente, se debería instalar pip en unos momentos. Si todo ha salido bien, se puede continuar al siguiente paso, las librerías.

Para instalar las librerías correspondientes, de forma similar al paso anterior, escribe los siguientes comandos por separado, ingresando con el botón "enter" para enviar la orden e instalarlo. Cada instalación debería tomar cierto tiempo. Los comandos son:

*pip3 install tk*

para instalar **Tkinter**, 

*pip3 install matplotlib* 

para instalar **Matplotlib**, 

*pip3 install pygame* 

para instalar **pygame**, y 

*python3 -m pip install --upgrade pip* 

para instalar **Pillow**. 

Gracias a "pip3", las librerías deberían instalarse para Python3 sin mayores problemas y se pueden usar en Visual Studio Code si son importadas correctamente (Como está escrito al inicio de de nuestro código).

Finalmente, hay que instalar el código "Maquetado.py" de nuestro repositorio. Una vez descargado, debe abrirse con Visual Studio Code para evitar cualquier problema ("Abrir con" y seleccionar Visual Studio Code).

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/ff133934-477d-4dd4-ad3c-cfcc31940321)

Es muy probable que cuando se instale y se abra, saldrá una ventana de advertencia en la se avisa que el archivo podría ser peligroso, por lo que se entraría en modo seguro, lo cual desactivaría las librerías del algoritmo (Esto llevaría a errores a la hora de ejecutar el código). Es solamente un protocolo común de Visual Studio Studio, somos de confianza. Para evitar entrar en modo seguro en el código, hay que seleccionar que se concede el permiso. A partir de eso, el código debería funcionar sin ningún problema.

**Guía de Uso**

Si todo lo anterior se ha realizado correctamente, se debe iniciar el código mediante el botón de la esquina superior derecha.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/5211945f-3c5e-487d-af73-e132aeef532e)

El código se iniciará y mostrará una ventana como esta:

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/6deefc0e-9ff3-44f7-b5b2-35a7bb3c5d99)

Ahora, para la simulación, hay que ingresar los datos pedidos por el programa en los campos correspondientes, siendo la velocidad inicial en metros por segundo y la aceleración en metros por segundo al cuadrado, solamente colocando los valores numéricos.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/cfed5db5-bec5-4213-9653-a706d1db46a8)

Una vez se haya hecho esto, cuando se presiona el botón "Iniciar Simulación", una simulación de la posición por el tiempo del objeto aparecerá a la derecha, repitiéndose una y otra vez para la apreciación detallada del proceso. Aquí se podrá ver cuánto incrementa la posición del cuerpo a medida que avanzan los segundos.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/3fef34b6-3948-4350-82e4-be387bb6d7d7)

Si gusta de una forma más detallada de presentar esta información, si presiona el botón "Mostrar Gráfico", una pestaña nueva se abrirá para usted en el que verá la posición del cuerpo en los primeros 10 segundos de la simulación en un gráfico con los ejes correctamente nombrados.

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/d12bf165-7331-454f-936f-6757c267f7ad)

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/70920a38-a5e6-4ba0-b260-a470ae7e7090)

Si es de su interés el por qué elegimos dedicar ambos gráficos a la posición y el tiempo, es debido a que, a la hora de representar el aspecto matemático mejor conocido del fenómeno físico, lo más usado es la curva de la posición cada vez lejana tras cada segundo del cuerpo en movimiento con aceleración. Siendo uno de los gráficos más interactivo al mostrar el movimiento del círculo como trayectoria del gráfico, y el otro enseñando los datos detallados con mayor comodidad.

En esta ventana se puede guardar la imagen, mover el gráfico, entre otras cosas. 

![image](https://github.com/DiegoNicolasOrtiz/Eva-Transdisciplinar-2023-A2-S1/assets/134817301/c721c05f-adae-4a4c-9edf-a34e9e08fe15)


**Explicación del Proyecto en Video**

A continuación, un video que explica oralmente nuestro código desarrollado en sus aspectos más importantes, además de una definición en otras palabras del evento físico que hemos presentado:

https://youtu.be/1YkGrz5NqDY


## Conclusiones
Cómo pueden ver, este evento físico es toda una curiosidad, desde sus orígenes hasta su uso matemático en el día de hoy hasta en los casos más mundanos. Es todo un desafío seguir avanzando en tecnología y, con tanta disposición, se siga enseñando a cada generación sobre estos sucesos que nos rodean, de una manera u otra. De igual manera, no fué fácil llegar a este resultado, pero creemos como equipo que hemos llegado al resultado deseado. Gracias a las herramientas existentes a día de hoy, la creación de estos documentos fue realmente posible. Se agradece su atención. Se espera que haya sido una presentación de su agrado y que cada punto haya quedado claro, siendo éste nuestro mayor objetivo al hacer este gran proyecto.
 
