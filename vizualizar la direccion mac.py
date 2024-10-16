import network, ubinascii
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print("ESSID:", ap_if.config("essid"))
print("Direccion MAC: ",ubinascii.hexlify(network.WLAN().config("mac"),":").decode())
# Dirección MAC en formato de texto
mac_str = "b0:a7:32:d7:5e:80"

# Convertir la dirección MAC en una lista de bytes
mac_bytes = bytes(int(b, 16) for b in mac_str.split(':'))

# Imprimir la dirección MAC en formato de bytes
print(mac_bytes)
