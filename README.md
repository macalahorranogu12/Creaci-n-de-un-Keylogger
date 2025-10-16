Para iniciar el programa, primero toca asegurarse de tener instalada la libreria del keyboard, para eso se debe ejecutar en la terminal de VScode el comando, "pip install keyboard"
Si se quiere verificar si keyboard ya esta descargado, usar el comando "keyboad version "

Usé la liberia keyboard para poder leer todo lo que se ingrese por el teclado ya que esta libreria se usa para simular y controlar el teclado. Ya sea grabar una combinación o solo ver las letras
primero cree una función la cual se ejecutará cada que se use una tecla, la cual tiene como proposito capturar el nombre de la letra que se presiona, aqui se usa el parametro event, el cual  contiene información sobre el evento de tecla presionada. En este caso, nos interesa el atributo name del evento, que contiene el nombre de la tecla

Y por último usamos keyboard.on_press, la cual es una función de la biblioteca keyboard que toma una función de callback como argumento, en este caso, on_press es la función de callback. 
Cada vez que se presiona una tecla, on_press se ejecutará con el evento de tecla como argumento.
Y de ahi ya solo añadi una tecla para finalizar el programa con la telca esc
