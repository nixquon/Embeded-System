from datetime import datetime
import platform
import socket

print("Hello, Raspberry Pi!")
print("Host:", socket.gethostname())
print("Python:", platform.python_version())
print("Time:", datetime.now())