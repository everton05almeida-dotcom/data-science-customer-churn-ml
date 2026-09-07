# 🤖 Data Science — Customer Churn Prediction

Projeto de portfólio focado em **Data Science e Machine Learning**, utilizando Python, Pandas, scikit-learn, SQL e Power BI para prever a probabilidade de cancelamento de clientes.

> **Importante:** todos os dados utilizados neste projeto são sintéticos e foram criados exclusivamente para fins educacionais e de portfólio.

## 🎯 Objetivo

Construir um processo de Machine Learning capaz de identificar clientes com maior risco de churn, comparar modelos e gerar uma base de scoring para apoiar estratégias de retenção.

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

`Geração dos Dados → EDA → Tratamento → Train/Test Split → Pré-processamento → Machine Learning → Avaliação → Scoring → Power BI`

## 📁 Estrutura

```text
dados/
└── amostra_clientes_churn.csv

python/
├── gerar_dados.py
├── analise_exploratoria.py
├── treinar_modelos.py
├── scoring_clientes.py
└── run_pipeline.py

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

powerbi/
└── COMO_MONTAR_POWER_BI.md
```

Os arquivos completos `dados/clientes_churn.csv`, `dados/clientes_churn_score.csv` e `modelos/modelo_churn.pkl` são gerados automaticamente ao executar o pipeline. Isso mantém o repositório mais limpo e torna o projeto reproduzível.

## ▶️ Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o fluxo completo:

```bash
python python/run_pipeline.py
```

Ou execute as etapas individualmente:

```bash
python python/gerar_dados.py
python python/analise_exploratoria.py
python python/treinar_modelos.py
python python/scoring_clientes.py
```

## 📈 Resultados atuais

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Regressão Logística | 0.737 | 0.605 | 0.295 | 0.397 | 0.746 |
| Random Forest | 0.723 | 0.600 | 0.170 | 0.265 | 0.726 |

A **Regressão Logística** apresentou o melhor ROC AUC neste experimento.

## 💡 Valor de Negócio

O scoring pode ajudar uma empresa a priorizar clientes com maior risco de cancelamento, direcionando campanhas de retenção e atendimento preventivo.

## 🚀 Evoluções futuras

- ajuste de hiperparâmetros
- validação cruzada
- feature engineering
- XGBoost / LightGBM
- API de inferência
- deploy em cloud
- MLflow
