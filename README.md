# Bank Marketing — Predicting Customer Subscription

Projeto educacional de classificação binária com Python e Scikit-learn. O objetivo é estudar padrões históricos de campanhas telefônicas de marketing bancário e estimar se houve adesão (`yes`) ou não (`no`) a um depósito a prazo. As previsões representam estimativas baseadas nos dados históricos, não certezas nem uma solução pronta para uso bancário.

## Dataset

Usamos `bank-additional-full.csv`, a versão completa do dataset Bank Marketing, obtida do pacote oficial da [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing). Ela contém 41.188 registros, 20 variáveis preditoras e o alvo `y`; o CSV usa `;` como separador. Fonte, atribuição, licença e hash SHA-256 estão em [`data/README.md`](data/README.md). Preserve a atribuição aos autores originais.

## Progresso

**Etapa atual: exploração dos dados (EDA).** O notebook examina a estrutura do CSV, tipos, nulos, valores `unknown`, duplicatas, classes do alvo, variáveis numéricas e distribuições relevantes. As figuras geradas ficam em `results/figures/`.

Ainda não foram treinados modelos e, portanto, este README não apresenta métricas de desempenho.

## Decisões importantes

- **`duration`:** será removida dos preditores do modelo principal. A duração da ligação só é conhecida depois do contato; usá-la para decidir antes de ligar seria data leakage (vazamento de informação).
- **`unknown`:** será mantido como categoria própria, pois é um valor textual explícito no dataset e não um `NaN`.
- **`pdays`:** o valor `999` indica ausência de contato em campanhas anteriores nesta versão. Não é um número literal de dias. A EDA compara a média bruta com os dias entre clientes previamente contatados; o tratamento final será implementado na etapa de pré-processamento.
- **Causalidade:** associações nos gráficos não demonstram que uma variável cause a adesão. O projeto é experimental e pode refletir limitações ou vieses dos dados históricos.

## Tecnologias

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook e joblib. As dependências estão listadas em [`requirements.txt`](requirements.txt).

## Como executar a EDA

No PowerShell, a partir da pasta raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook
```

Abra `notebooks/01_exploratory_data_analysis.ipynb` no Jupyter. O notebook espera encontrar o CSV em `data/bank-additional-full.csv`.

Para executar e salvar as saídas no notebook:

```powershell
jupyter nbconvert --to notebook --execute --inplace notebooks/01_exploratory_data_analysis.ipynb
```

## Referência

Moro, S., Rita, P. & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. [DOI: 10.24432/C5K306](https://doi.org/10.24432/C5K306). A UCI indica licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
