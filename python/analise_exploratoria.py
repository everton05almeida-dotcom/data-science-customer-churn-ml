from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE_DIR / "dados" / "clientes_churn.csv")

print("Taxa de churn:", round(df["churn"].mean(), 4))
print("\nChurn por contrato:")
print(df.groupby("tipo_contrato")["churn"].mean().sort_values(ascending=False))

summary = df.groupby("tipo_contrato")["churn"].mean().sort_values(ascending=False)
summary.plot(kind="bar", figsize=(8,5))
plt.title("Taxa de Churn por Tipo de Contrato")
plt.ylabel("Taxa de Churn")
plt.xlabel("Contrato")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(BASE_DIR / "outputs" / "churn_por_contrato.png", dpi=150)
