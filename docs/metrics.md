# Model Performance Baseline

**Date:** 2025-04-23  
**Model:** XGBoost regressor, default parameters  
**Data:** 25 years of district-level yield & weather features

| Metric       | Value        |
| ------------ | ------------ |
| Initial RMSE | 595.675      |
| Initial R²   | 0.61705      |


# Model Metrics

| Metric     | Value      |
|------------|------------|
| RMSE       | 315.44     |
| R²         | 0.893      |
| Mean Yield | 853.68     |

## Changes

- Switched from a scikit-learn Pipeline + OneHotEncoder to XGBoost’s native categorical support (`enable_categorical=True`), removing all object-dtype columns up front.
- Kept the `Year` column as a continuous numeric feature so the model can learn long-term yield trends.

