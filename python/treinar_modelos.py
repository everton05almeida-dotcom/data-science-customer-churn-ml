from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

BASE_DIR = Path(__file__).resolve().parents[1]
DATA = BASE_DIR / "dados" / "clientes_churn.csv"
OUT = BASE_DIR / "outputs" / "metricas_modelos.csv"
MODEL = BASE_DIR / "modelos" / "modelo_churn.pkl"

df = pd.read_csv(DATA)

X = df.drop(columns=["id","cliente","churn"])
y = df["churn"]

num_cols = [
    "tempo_cliente_meses","mensalidade","contatos_suporte","tickets_abertos",
    "dias_atraso_pagamento","satisfacao","uso_mensal_horas","indicacoes"
]
cat_cols = ["tipo_contrato","forma_pagamento","segmento"]

preprocess = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

models = {
    "Regressao_Logistica": LogisticRegression(max_iter=1000, random_state=42),
    "Random_Forest": RandomForestClassifier(
        n_estimators=220, random_state=42, max_depth=8, min_samples_leaf=4
    )
}

results = []
trained = {}

for name, model in models.items():
    pipe = Pipeline([("prep", preprocess), ("model", model)])
    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)
    prob = pipe.predict_proba(X_test)[:,1]

    results.append({
        "modelo": name,
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, prob),
    })
    trained[name] = pipe

metrics = pd.DataFrame(results).sort_values("roc_auc", ascending=False)
metrics.to_csv(OUT, index=False, encoding="utf-8-sig")

best_name = metrics.iloc[0]["modelo"]
joblib.dump(trained[best_name], MODEL)

print(metrics)
print(f"\nMelhor modelo por ROC AUC: {best_name}")
