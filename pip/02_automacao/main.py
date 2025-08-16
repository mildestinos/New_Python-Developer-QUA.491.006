import pyautogui
import time
import subprocess
import math

# 1. Abre o Paint
subprocess.Popen('mspaint')
time.sleep(2.5)  # tempo para o Paint abrir

# 2. Move o mouse para uma área em branco do Paint
# (ajuste conforme a sua tela/resolução)
center_x = 600
center_y = 400
radius = 100
pyautogui.moveTo(center_x + radius, center_y)

# 3. Pressiona o botão esquerdo e desenha um círculo
pyautogui.mouseDown()

for angle in range(0, 361, 2):  # passo de 2 graus
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    pyautogui.moveTo(x, y, duration=0.01)

pyautogui.mouseUp()
