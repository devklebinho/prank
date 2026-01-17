import sounddevice as sd
import numpy as np
import webbrowser

# Configurações
VOLUME_LIMITE = 0.05
SAMPLE_RATE = 44100
DURACAO = 0.1

def acao():
    print("🔊 Volume alto detectado! Abrindo página...")
    webbrowser.open(
        "https://bibliotecajoaquimsuassuna.github.io/libpage/silenceplease.html"
    )

print("🎤 Ouvindo o microfone... (Ctrl+C para parar)")

while True:
    audio = sd.rec(
        int(DURACAO * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32'
    )
    sd.wait()

    volume = np.sqrt(np.mean(audio**2))
    print(f"Volume: {volume:.4f}")

    if volume > VOLUME_LIMITE:
        acao()
