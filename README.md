1. Descripción del Problema
En un entorno de restaurante con alta demanda, se necesita un sistema eficiente para:

Gestionar múltiples pedidos concurrentes de diferentes clientes.

Priorizar pedidos urgentes sobre los regulares.

Controlar el número de cocineros activos para evitar sobrecarga del sistema.

Mostrar el estado de los pedidos (en espera, en preparación y completados) en tiempo real.

Problemas específicos a resolver:

Concurrencia: Múltiples clientes realizando pedidos simultáneamente.

Priorización: Algunos pedidos deben prepararse antes que otros.

Límite de recursos: No se pueden tener infinitos cocineros trabajando al mismo tiempo.

Sincronización: Evitar condiciones de carrera al acceder a estructuras de datos compartidas.

2. Solución Implementada
2.1. Estructuras de Datos y Mecanismos
Cola de Prioridad (PriorityQueue)
Almacena los pedidos pendientes.

Prioridad: Los pedidos con menor valor (1 = urgente, 3 = normal) se atienden primero.

Semáforo (threading.Semaphore)
Limita el número máximo de cocineros activos (inicialmente 3, máximo 5).

Evita la sobrecarga del sistema.

Listas de Seguimiento
waiting_orders: Pedidos en espera de ser procesados.

completed_orders: Pedidos ya preparados.

Clase Order
Representa un pedido con:

customer_id (identificador del cliente).

order_details (descripción del pedido).

priority (1=urgente, 2=media, 3=normal).

order_id (identificador único autoincremental).

2.2. Funcionamiento del Sistema
Generación de Pedidos (place_order)

Los clientes (hilos) crean pedidos con prioridad aleatoria.

Cada pedido se encola en order_queue y se añade a waiting_orders.

Procesamiento por Cocineros (process_order)

Cada cocinero (hilo) toma un pedido de la cola (si hay disponibilidad en el semáforo).

Simula un tiempo de preparación (2-5 segundos).

Mueve el pedido de waiting_orders a completed_orders.

Visualización en Tiempo Real

Muestra constantemente:

Pedidos en espera.

Pedidos completados.

2.3. Manejo de Concurrencia
Semáforo: Controla que no trabajen más de 5 cocineros a la vez.

Cola thread-safe (PriorityQueue): Garantiza que no haya condiciones de carrera al extraer pedidos.

Mutex implícito en listas: Evita corrupción de datos al modificar waiting_orders y completed_orders.

3. Análisis de Rendimiento
3.1. Métricas Clave
Parámetro	Valor	Descripción
Cocineros base	3	Número inicial de cocineros activos.
Cocineros máximos	5	Límite superior de cocineros permitidos.
Tiempo de preparación	2-5 seg	Aleatorio para simular variabilidad.
Timeout de inactividad	5 seg	Si no hay pedidos en 5 seg, el cocinero se detiene.
3.2. Ventajas del Diseño
✔ Priorización eficiente:

Los pedidos urgentes (prioridad 1) siempre se atienden primero.

✔ Balance de carga:

El semáforo evita saturar la cocina con demasiados cocineros.

✔ Escalabilidad controlada:

Puede aumentar hasta 5 cocineros si hay muchos pedidos.

✔ Monitoreo en tiempo real:

Las listas waiting_orders y completed_orders permiten ver el estado actual.

✔ Seguridad en concurrencia:

No hay condiciones de carrera gracias a PriorityQueue y el semáforo.

3.3. Posibles Mejoras
🔧 Tiempo de espera dinámico:

Ajustar automáticamente el timeout según la carga de trabajo.

🔧 Balance de carga inteligente:

Añadir más cocineros solo si la cola de pedidos supera un umbral.

🔧 Persistencia de datos:

Guardar pedidos en una base de datos para recuperación ante fallos.

🔧 Interfaz gráfica (GUI):

Reemplazar la salida por consola con un panel visual más amigable.

🔧 Métricas de desempeño:

Tiempo promedio de preparación, pedidos urgentes atendidos, etc.

4. Conclusión
El sistema implementado resuelve eficientemente el problema de gestión de pedidos en un restaurante con las siguientes características:

✅ Gestión priorizada: Los pedidos urgentes no esperan.
✅ Control de recursos: No se satura la cocina con demasiados cocineros.
✅ Concurrencia segura: No hay corrupción de datos por accesos simultáneos.
✅ Monitoreo en tiempo real: Permite saber qué pedidos están en espera y cuáles ya están listos.

Próximos pasos:

Implementar persistencia para guardar el historial de pedidos.

Desarrollar una interfaz gráfica para mejor visualización.

Añadir métricas de rendimiento para optimizar tiempos de preparación.

Este sistema es escalable y puede adaptarse a restaurantes con diferentes niveles de demanda.
