# 🤖 Data Science — Customer Churn Prediction

Projeto de portfólio focado em **Data Science e Machine Learning**, utilizando Python,
Pandas, scikit-learn, SQL e Power BI para prever a probabilidade de cancelamento de clientes.

> **Importante:** todos os dados utilizados neste projeto são sintéticos e foram criados
> exclusivamente para fins educacionais e de portfólio.

## 🎯 Objetivo

Construir um processo de Machine Learning capaz de identificar clientes com maior risco de churn,
comparar modelos e gerar uma base de scoring para apoiar estratégias de retenção.

## 🧠 Modelos

- Regressão Logística
- Random Forest

Melhor modelo no teste atual: **Regressão Logística**.

## 📊 Métricas avaliadas

- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- Matriz de confusão

## 🛠️ Tecnologias

- Python
- Pandas
- scikit-learn
- Matplotlib
- Jupyter Notebook
- SQL
- Power BI
- Excel
- Git / GitHub

## 🔄 Pipeline

`Dados → EDA → Tratamento → Train/Test Split → Pré-processamento → Machine Learning → Avaliação → Scoring → Power BI`

## 📁 Estrutura

```text
dados/
├── clientes_churn.csv
└── clientes_churn_score.csv

python/
├── analise_exploratoria.py
├── treinar_modelos.py
└── scoring_clientes.py

notebooks/
└── customer_churn_analysis.ipynb

sql/
└── consultas_churn.sql

docs/
├── perguntas_negocio.md
└── resultados_modelos.md

outputs/
├── metricas_modelos.csv
├── matriz_confusao.csv
└── classification_report.txt

modelos/
└── modelo_churn.pkl

powerbi/
└── COMO_MONTAR_POWER_BI.md

Dashboard_Customer_Churn_ML.xlsx
```

## ▶️ Como executar

```bash
pip install -r requirements.txt
python python/treinar_modelos.py
python python/scoring_clientes.py
```

## 💡 Valor de Negócio

O scoring pode ajudar uma empresa a priorizar clientes com maior risco de cancelamento,
direcionando campanhas de retenção e atendimento preventivo.

## 🚀 Evoluções futuras

- ajuste de hiperparâmetros
- validação cruzada
- feature engineering
- XGBoost / LightGBM
- API de inferência
- deploy em cloud
- MLflow
