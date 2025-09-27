/*Conteo de Registros*
- _Enunciado:_ ¿Cuántos pedidos tenemos en total?
- _Requerimientos:_
  1. Usar `COUNT(*)`.
  2. Ponerle un alias chulo como `total_pedidos`.*/

SELECT COUNT(*) as total_pedidos FROM Orders;