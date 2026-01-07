import pyautogui
import time
import random

time.sleep(5)  # Tempo para o amigo se afastar do computador 😈

# Exibe a mensagem final como caixa de diálogo
pyautogui.alert(
    title='⚠️ ALERTA CRÍTICO ⚠️',
    text='VOCÊ LIGOU O SOM DO COMPUTADOR SEM USAR FONES\n\n AGORA VOU LIGAR SEU MOUSE 😈',
    button='Entendi'
)

for i in range(100):
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    pyautogui.moveTo(x, y, duration=0.5)
