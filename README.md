# Reto Tecnico
Juego de preguntas

El juego de preguntas fue realizado con python y la libreria tkinter. 

INGRESAR DATOS DEL JUEGADOR: Inicia mostrando al jugador una ventana en la cual debera ingresar el nombre de usuario y oprimir la tecla aceptar, si el nombre no fue digitalizado de manera correcta (Sin caracteres o solo espacios), mostrara una ventana indicando que el nombre es errado y debera  ingresar un nombre valido. 

CUESTIONARIO DE PREGUNTAS: Al insertar el nombre del jugador de manera correcta, se abrira la ventana del cuestionario de preguntas y tendra solo 30 segundos para seleccionar la respuesta correcta, si el usuario demora mas del tiempo estipulado se finalizara el juego y mostrara un mensaje de tiempo acabado, de lo contrario, si responde correctamente aumentara el puntaje y la ronda del juego. Si la respuesta no es correcta emergera un mensaje mostrando que ha perdido. 

BOTONES SALIR - SIGUIENTE: El jugador tendra la opcion de elegir si continua el juego (oprimiendo el boton siguiente) o si prefiere salir (oprimiendo el boton salir). Si la respuesta no es correcta emergera un mensaje mostrando que ha perdido. 

BOTON DE PUNTAJES: Si desea observar la lista de puntajes de los jugadores, debera oprimir el boton puntajes que esta ubicada en la ventana de cuestionarios de preguntas llamada "Puntajes".

PERSISTENCIA: Se utilizo la persistencia de datos para guardar el nombre del jugador y el puntaje obtenido hasta la finalizacion de su juego, si este es mayor a 0. Los datos son guardados en un archivo txt, el cual sera creado automaticamente por medio de Python.  
