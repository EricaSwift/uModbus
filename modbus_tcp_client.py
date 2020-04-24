import socket
from umodbus import conf
from umodbus.client import tcp

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

message = tcp.read_input_registers(
    slave_id=1, starting_address=0, quantity=10)
response = tcp.send_message(message, sock)
print('Response from reading vector is '  + str(response))

sock.close()