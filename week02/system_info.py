import platform
import socket
from datetime import datetime

print("호스트:", socket.gethostname())
print("운영체제:", platform.system())
print("CPU:", platform.machine())
print("시간:", datetime.now().isoformat(timespec="seconds"))