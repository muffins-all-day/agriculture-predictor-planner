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


## 🔄 RandomizedSearchCV Results (May 2025)

### 1. One-Hot Encoded Model (10 Trials)
- **Preprocessing**: OneHotEncoder on district, crop, and month
- **Model**: XGBRegressor with RandomizedSearchCV (10 iterations)
- **Best CV RMSE**: 656.02
- **Test RMSE**: 647.61
- **Test R²**: 0.547

---

### 2. One-Hot Encoded Model (30 Trials)
- **Preprocessing**: OneHotEncoder on district, crop, and month
- **Model**: XGBRegressor with RandomizedSearchCV (30 iterations)
- **Best CV RMSE**: 421.04
- **Test RMSE**: 399.60
- **Test R²**: 0.828

---

📝 *Observation*: Performance improved significantly with more trials. One-hot encoding still performs slightly worse than categorical modeling (RMSE ~315), but is more portable for deployment.


