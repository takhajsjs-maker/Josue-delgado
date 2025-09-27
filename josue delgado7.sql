/*Ordenamiento de Pedidos*
- _Enunciado:_ Mostrar todos los pedidos, del más reciente al más antiguo.
- _Requerimientos:_
  1. Seleccionar todo de `Orders`.
  2. Usar `ORDER BY order_id DESC`.*/

SELECT * FROM Orders
ORDER BY order_id DESC;
