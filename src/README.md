# Módulo `preprocessing.py`

Este módulo mantém em um só lugar as transformações compartilhadas pelos notebooks 02 a 05.

- `load_dataset(data_path=None)`: lê `data/bank-additional-full.csv` com `;` como separador.
- `prepare_features_target(dataframe)`: separa `X` e `y`, remove `duration`, cria `was_previously_contacted` e substitui `pdays=999` por `NaN` para imputação.
- `make_preprocessor(features)`: cria um `ColumnTransformer` com imputação e padronização numéricas e imputação e One-Hot Encoding categóricos. A função constrói o transformador, mas não o ajusta.
- `split_data(features, target, ...)`: divide os dados em treino e teste em proporção 80/20 por padrão, com `stratify=target` e `random_state=42`.

Para evitar vazamento, ajuste o pré-processador somente com `X_train` (`fit_transform`) e use `transform` em `X_test`. Nas etapas de treinamento e validação cruzada, o transformador deve ficar dentro do `Pipeline` do Scikit-learn para que cada dobra aprenda suas transformações apenas com a parte de treino.

Os valores categóricos `unknown` são mantidos como categorias. A imputação categórica usa a categoria mais frequente somente para valores realmente ausentes; não substitui o texto `unknown`.
