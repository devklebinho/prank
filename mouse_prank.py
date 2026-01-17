#import pyautogui
import time
import random

time.sleep(5)  # Tempo para o amigo se afastar do computador 😈
'''
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
'''

import sounddevice as sd
import numpy as np

# Configurações
VOLUME_LIMITE = 0.05   # ajuste esse valor
SAMPLE_RATE = 44100
DURACAO = 0.1          # segundos por leitura

def acao():
    print("🔊 Volume alto detectado! Ação executada.")

print("🎤 Ouvindo o microfone... (Ctrl+C para parar)")

while True:
    audio = sd.rec(
        int(DURACAO * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32'
    )
    sd.wait()

    volume = np.sqrt(np.mean(audio**2))  # RMS

    print(f"Volume: {volume:.4f}")

    if volume > VOLUME_LIMITE:
        acao()
