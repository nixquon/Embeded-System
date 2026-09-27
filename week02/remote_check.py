import platform
import socket
import sys
from datetime import datetime
from pathlib import Path

print("Host:", socket.gethostname())
print("OS:", platform.system())
print("CPU:", platform.machine())
print("Project:", Path.cwd())
print("File:", Path(__file__).resolve())
print("Python:", sys.executable)
print("Virtual environment:", sys.prefix != sys.base_prefix)
print("Time:", datetime.now().isoformat(timespec="seconds"))