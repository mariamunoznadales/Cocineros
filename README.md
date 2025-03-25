# Sistema de Gestión de Pedidos para Restaurante

## Descripción del Problema

Necesitamos simular un sistema de gestión de pedidos para un restaurante que debe:
- Recibir pedidos de múltiples clientes simultáneamente
- Priorizar pedidos urgentes sobre los normales
- Limitar el número de cocineros trabajando al mismo tiempo
- Mostrar el estado de los pedidos en tiempo real

## Solución Implementada

### Componentes Principales

```python
# Estructuras de datos
order_queue = queue.PriorityQueue()  # Cola de pedidos prioritarios
waiting_orders = []                  # Pedidos en espera
completed_orders = []                # Pedidos completados

# Mecanismos de control
cook_semaphore = threading.Semaphore(num_cooks)  # Limita cocineros activos

## Flujo del Sistema

1- Clientes realizan pedidos:

Cada pedido recibe una prioridad (1=urgente, 3=normal)

Se almacenan en la cola de prioridad

2- Cocineros procesan pedidos:

Máximo 5 cocineros pueden trabajar simultáneamente

Atienden primero los pedidos con prioridad más alta (valor más bajo)

Simulan tiempo de preparación (2-5 segundos)

3- Visualización:

Muestra listas actualizadas de pedidos en espera y pedidos completados
