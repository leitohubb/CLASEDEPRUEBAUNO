
nombre_cliente = "Pedro Ramírez"
precio_jean = 125000
cantidad_jeans = 2
precio_camisa = 45000
cantidad_camisas = 2
precio_polo = 30000
cantidad_polo = 1
total_jeans = precio_jean * cantidad_jeans
total_camisas = precio_camisa * cantidad_camisas
total_polo = precio_polo * cantidad_polo
total_compra = total_jeans + total_camisas + total_polo
descuento_polo = 0
descuento_total = 0
if cantidad_polo > 0:
    descuento_polo = total_compra * 0.05
total_compra -= descuento_polo
if total_compra > 200000:
    descuento_total = total_compra * 0.30
total_pagar = total_compra - descuento_total
print(f"Factura para: {nombre_cliente}")
print(f"Total Jeans: ${total_jeans}")
print(f"Total Camisas: ${total_camisas}")
print(f"Total Camisa tipo Polo: ${total_polo}")
print(f"Descuento por Polo: ${descuento_polo}")
print(f"Descuento por compra superior a 200.000: ${descuento_total}")
print(f"Total a Pagar: ${total_pagar}")
