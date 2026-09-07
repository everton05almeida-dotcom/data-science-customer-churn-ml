import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

steps = [
    "gerar_dados.py",
    "analise_exploratoria.py",
    "treinar_modelos.py",
    "scoring_clientes.py",
]

for step in steps:
    print(f"\n>>> Executando {step}")
    subprocess.run([sys.executable, str(HERE / step)], check=True)

print("\nPipeline de Data Science executado com sucesso.")
