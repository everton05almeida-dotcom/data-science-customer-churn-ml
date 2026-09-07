from pathlib import Path
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parents[1]
DATA = BASE_DIR / "dados" / "clientes_churn.csv"
MODEL = BASE_DIR / "modelos" / "modelo_churn.pkl"
OUT = BASE_DIR / "dados" / "clientes_churn_score.csv"

df = pd.read_csv(DATA)
model = joblib.load(MODEL)

X = df.drop(columns=["id","cliente","churn"])
df["probabilidade_churn"] = model.predict_proba(X)[:,1].round(4)

df["risco_churn"] = pd.cut(
    df["probabilidade_churn"],
    bins=[-0.01, 0.35, 0.65, 1.0],
    labels=["Baixo","Médio","Alto"]
)

df.to_csv(OUT, index=False, encoding="utf-8-sig")
print("Scoring concluído:", len(df), "clientes")
