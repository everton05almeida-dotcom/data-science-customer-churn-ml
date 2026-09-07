from pathlib import Path
import csv
import math
import random

random.seed(808)

BASE_DIR = Path(__file__).resolve().parents[1]
OUT = BASE_DIR / "dados" / "clientes_churn.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

headers = [
    "id","cliente","tempo_cliente_meses","mensalidade","tipo_contrato",
    "contatos_suporte","tickets_abertos","dias_atraso_pagamento","satisfacao",
    "uso_mensal_horas","forma_pagamento","segmento","indicacoes","churn"
]

rows = []
for i in range(1, 1201):
    tenure = random.randint(1, 72)
    mensalidade = round(random.uniform(49, 249), 2)
    contrato = random.choices(["Mensal", "Anual", "Bienal"], weights=[58, 27, 15])[0]
    suporte = random.randint(0, 8)
    tickets = random.randint(0, 10)
    atraso = random.randint(0, 45)
    satisfacao = random.choices([1, 2, 3, 4, 5], weights=[7, 15, 30, 31, 17])[0]
    uso = round(random.uniform(2, 60), 1)
    pagamento = random.choice(["Cartão", "Pix", "Boleto", "Débito automático"])
    segmento = random.choice(["Básico", "Intermediário", "Premium"])
    indicacoes = random.randint(0, 5)

    z = -1.8
    z += 0.95 if contrato == "Mensal" else -0.35 if contrato == "Anual" else -0.7
    z += 0.025 * atraso
    z += 0.20 * tickets
    z += -0.55 * (satisfacao - 3)
    z += -0.018 * tenure
    z += 0.004 * (mensalidade - 120)
    z += -0.12 * indicacoes
    z += -0.012 * min(uso, 50)
    prob = 1 / (1 + math.exp(-z))
    churn = 1 if random.random() < prob else 0

    rows.append([
        i, f"CLI-{i:05d}", tenure, mensalidade, contrato, suporte, tickets,
        atraso, satisfacao, uso, pagamento, segmento, indicacoes, churn
    ])

with OUT.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"Base sintética criada: {OUT}")
print(f"Registros: {len(rows)}")
