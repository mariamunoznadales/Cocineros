import threading
import queue
import time
import random

# Cola de pedidos, se usa para almacenar los pedidos en espera
order_queue = queue.PriorityQueue()

# Semáforo para controlar el número de cocineros disponibles.
# El semáforo permite que solo un número limitado de cocineros trabajen a la vez.
num_cooks = 3
max_cooks = 5  # Límite máximo de cocineros que pueden estar trabajando
cook_semaphore = threading.Semaphore(num_cooks)

# Listas para simular las pantallas de pedidos en proceso y pedidos listos
waiting_orders = []  # Pedidos esperando a ser procesados
completed_orders = []  # Pedidos listos para ser entregados

# Variable para generar el ID de los pedidos secuencialmente
order_counter = 1

# Clase que representa un pedido realizado por un cliente
class Order:
    def __init__(self, customer_id, order_details, priority=1):
        global order_counter
        self.customer_id = customer_id
        self.order_details = order_details
        self.order_id = order_counter  # Usamos order_counter para asignar el ID del pedido secuencialmente
        self.priority = priority  # Prioridad de preparación del pedido (baja = más urgente)
        order_counter += 1  # Incrementamos el contador para el siguiente pedido

    def __str__(self):
        return f"Pedido {self.order_id} de Cliente {self.customer_id}: {self.order_details}"

    def __lt__(self, other):
        return self.priority < other.priority  # La cola de prioridad prioriza los pedidos con menor prioridad

# Función que simula la llegada de un pedido de un cliente
def place_order(customer_id, order_details, priority=1):
    # Crear un objeto Order con los detalles del pedido
    order = Order(customer_id, order_details, priority)
    
    # Colocar el pedido en la cola de prioridad
    order_queue.put(order)
    
    # Agregar el pedido a la lista de "esperando"
    waiting_orders.append(str(order))
    
    # Mostrar los pedidos esperando en la pantalla
    print("\nPedidos en espera:")
    for order in waiting_orders:
        print(order)

# Función que simula el proceso de cocinar un pedido
def process_order(cook_id):
    while True:
        # Adquirir el semáforo. Si hay cocineros disponibles, el semáforo permite que el hilo (cocinero) continúe.
        cook_semaphore.acquire()
        
        try:
            # Extraer un pedido de la cola con prioridad (espera máximo 5 segundos)
            order = order_queue.get(timeout=5)
            
            # Mostrar que el pedido se está preparando
            print(f"\nCocinero {cook_id} preparando {order}...")
            waiting_orders.remove(str(order))  # Remover el pedido de la lista de "esperando"
            
            # Simular el tiempo de preparación del pedido
            time.sleep(random.randint(2, 5))
            
            # Agregar el pedido a la lista de "listos para ser entregados"
            completed_orders.append(str(order))
            
            # Mostrar los pedidos listos en la pantalla
            print("\nPedidos listos para ser entregados:")
            for order in completed_orders:
                print(order)
            
            # Imprimir mensaje cuando el pedido esté listo
            print(f"{order} está listo para ser entregado.\n")
            
            # Marcar el pedido como procesado
            order_queue.task_done()
        
        except queue.Empty:
            # Si la cola está vacía después de 5 segundos, terminar el proceso
            print(f"Cocinero {cook_id}: No hay más pedidos en la cola.")
            break
        
        finally:
            # Liberar el semáforo, permitiendo que otro cocinero pueda tomar un pedido si hay alguno disponible
            cook_semaphore.release()

# Crear pedidos de clientes (simulando la llegada de 10 pedidos)
total_orders = 10
for i in range(total_orders):
    # Aleatoriamente asignamos prioridad a los pedidos (los de prioridad baja se preparan primero)
    priority = random.randint(1, 3)  # Prioridad 1 es urgente, 3 es baja
    # Crear un hilo para cada cliente que realiza un pedido
    threading.Thread(target=place_order, args=(i, f"Plato {random.randint(1, 5)}", priority), daemon=True).start()
    
    # Simular un tiempo de espera entre los pedidos
    time.sleep(0.5)

# Crear hilos para los cocineros, que van a procesar los pedidos de la cola
cook_threads = []
for cook_id in range(1, num_cooks + 1):
    # Crear un hilo para cada cocinero
    cook_thread = threading.Thread(target=process_order, args=(cook_id,))
    
    # Iniciar el hilo
    cook_thread.start()
    
    # Añadir el hilo a la lista de cocineros activos
    cook_threads.append(cook_thread)

# Si hay más pedidos que cocineros, añadir más cocineros hasta el límite
for cook_id in range(num_cooks + 1, max_cooks + 1):
    cook_thread = threading.Thread(target=process_order, args=(cook_id,))
    cook_thread.start()
    cook_threads.append(cook_thread)

# Esperar a que todos los cocineros terminen de procesar todos los pedidos
for cook_thread in cook_threads:
    cook_thread.join()

# Mensaje final cuando todos los pedidos han sido procesados
print("\nTodos los pedidos han sido procesados.")
