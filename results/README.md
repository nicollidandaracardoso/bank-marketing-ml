# Resultados

As figuras da exploração inicial, avaliação e interpretação são salvas em `results/figures/`. Os três pipelines treinados no conjunto de treino estão em `results/models/` e a comparação final no teste está em `results/tables/model_comparison.csv`.

Arquivos da avaliação:

- `figures/model_confusion_matrices.png`
- `figures/model_roc_curves.png`
- `figures/model_precision_recall_curves.png`
- `tables/model_comparison.csv`

Arquivos da interpretação:

- `figures/logistic_regression_top_coefficients.png`
- `figures/random_forest_grouped_importance.png`
- `tables/logistic_regression_coefficients.csv`
- `tables/random_forest_feature_importance.csv`

Os artefatos de modelo ficam em `models/`. A avaliação foi executada no conjunto de teste reservado; os hiperparâmetros e limiares não foram ajustados com esses resultados. A interpretação usa os parâmetros dos pipelines treinados, não o conjunto de teste. Os coeficientes e as importâncias são associações do modelo, não causas.
