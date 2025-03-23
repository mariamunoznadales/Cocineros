## Descripción
El sistema simula el flujo de trabajo en un restaurante con múltiples clientes haciendo pedidos y cocineros procesándolos. Cada cliente realiza un pedido que se coloca en una cola de prioridad, y los cocineros los procesan de acuerdo con la prioridad del pedido. El número de cocineros puede ajustarse dinámicamente para adaptarse a la cantidad de pedidos, y se usa un semáforo para evitar condiciones de carrera y garantizar que los recursos sean gestionados de manera eficiente.

## Características
Programación Concurrente: El sistema usa hilos (threads) para gestionar la concurrencia de clientes y cocineros, permitiendo que se procesen múltiples pedidos simultáneamente sin bloqueos innecesarios.

Cola de Prioridad: Los pedidos se gestionan en una cola de prioridad, donde los cocineros procesan primero los pedidos más urgentes o rápidos de preparar.

Semáforo de Cocineros: Se utiliza un semáforo para limitar el número de cocineros que pueden trabajar al mismo tiempo, evitando condiciones de carrera y gestionando los recursos de manera eficiente.

Ajuste Dinámico de Cocineros: El sistema permite agregar cocineros si la demanda de pedidos aumenta, mejorando la capacidad de respuesta y eficiencia.

Simulación Realista de Pedidos: Los clientes realizan pedidos de manera aleatoria, y los cocineros los procesan en función de la disponibilidad y la prioridad.

## Dificultades Abordadas
Coordinación entre Múltiples Productores (Clientes) y Consumidores (Cocineros)
Se ha utilizado la programación concurrente mediante hilos para permitir que los clientes realicen pedidos y los cocineros los procesen de manera simultánea. La coordinación se maneja utilizando un semáforo que limita el acceso concurrente a la cola de pedidos, evitando condiciones de carrera y garantizando que solo un número limitado de cocineros acceda a los recursos compartidos al mismo tiempo.

Optimización del Tiempo de Espera
La optimización del tiempo de espera se ha logrado mediante el uso de una cola de prioridad, que permite que los cocineros procesen los pedidos más rápidos de preparar antes. Además, el número de cocineros es dinámico, lo que permite añadir más cocineros en caso de alta demanda, mejorando la capacidad de respuesta del sistema y reduciendo los tiempos de espera de los pedidos.

