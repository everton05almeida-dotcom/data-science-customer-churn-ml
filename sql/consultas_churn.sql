-- Customer Churn Analytics

-- 1. Taxa geral de churn
SELECT
    AVG(CAST(churn AS FLOAT)) AS churn_rate
FROM clientes_churn;

-- 2. Churn por tipo de contrato
SELECT
    tipo_contrato,
    COUNT(*) AS clientes,
    AVG(CAST(churn AS FLOAT)) AS churn_rate
FROM clientes_churn
GROUP BY tipo_contrato
ORDER BY churn_rate DESC;

-- 3. Satisfação e churn
SELECT
    satisfacao,
    COUNT(*) AS clientes,
    AVG(CAST(churn AS FLOAT)) AS churn_rate
FROM clientes_churn
GROUP BY satisfacao
ORDER BY satisfacao;

-- 4. Alto risco previsto
SELECT *
FROM clientes_churn_score
WHERE risco_churn = 'Alto'
ORDER BY probabilidade_churn DESC;
