import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Percorso base e cartella che vuoi analizzare
BASE_DIR = Path(r"C:\Users\Emanuele Picone\Downloads\code")
FOLDER_NAME = "Gruppo_4_stud_2_N"  # Cambia questo con la cartella che vuoi visualizzare

CSV_PATH = BASE_DIR / FOLDER_NAME / "Accelerometer.csv"

# Carica il CSV usando l'intestazione per accedere alle colonne per nome
# (nel file l'ordine delle colonne è time, seconds_elapsed, z, y, x)
data = np.genfromtxt(CSV_PATH, delimiter=",", names=True)
seconds = data["seconds_elapsed"]
x = data["x"]
y = data["y"]
z = data["z"]

if __name__ == "__main__":
    print(f"Campioni caricati: {len(x)}")
    print("seconds:", seconds[:5])
    print("x:", x[:5])
    print("y:", y[:5])
    print("z:", z[:5])

    # Visualizzazione dei tre assi in grafici separati con asse del tempo condiviso
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(12, 8))
    
    for ax, signal, label, color in zip(
        axes, (x, y, z), ("x", "y", "z"), ("tab:red", "tab:green", "tab:blue")
    ):
        ax.plot(seconds, signal, color=color, linewidth=0.8)
        ax.set_ylabel(f"acc {label} (m/s²)")
        ax.grid(True, alpha=0.3)
        
    axes[-1].set_xlabel("tempo (s)")
    fig.suptitle(f"Accelerometro - {FOLDER_NAME}")
    fig.tight_layout()
    
    plt.show()