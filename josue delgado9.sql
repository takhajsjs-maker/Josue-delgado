/*Agrupación por Cliente*
- _Enunciado:_ Calcular cuántos pedidos ha hecho cada cliente.
- _Requerimientos:_
  1. Usar `COUNT(order_id)` y `GROUP BY*/

  SELECT customer_id, COUNT(order_id) as total_pedidos
  FROM Orders
  GROUP by customer_id;