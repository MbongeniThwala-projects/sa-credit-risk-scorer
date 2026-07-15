import numpy as np
import pandas as pd

#without random.seed(42), every time you rerun the script, one would get a different dataset
np.random.seed(42)

N_CUSTOMERS = 100000

client_id = np.arange(1, N_CUSTOMERS + 1)

age = np.random.randint(18, 71, size=N_CUSTOMERS)

monthly_income = np.round(np.random.lognormal(mean=9.2, sigma=.6, size=N_CUSTOMERS), 2)

# debt that depends on income (no independent)
debt_to_income_ratio = np.clip(np.random.normal(loc=.35, scale=.15, size=N_CUSTOMERS), .01, .95)

active_debt = np.round(monthly_income * 12 * debt_to_income_ratio, 2)

#Credit utilization ratio
credit_utilization_ratio = np.round(np.clip(np.random.beta(a=2, b=3, size=N_CUSTOMERS), 0, 1), 4)

#employment status and arrears- tied to income tier
employment_status = np.where(
    monthly_income < 8000, 'unemployment',
    np.where(monthly_income < 25000, 'self-employment', 'employment')
)

days_in_arrears = np.where(
    credit_utilization_ratio > .7,
    np.random.randint(0, 120, size=N_CUSTOMERS),
    np.random.randint(0, 15, size=N_CUSTOMERS)
)

#The target- defaault_flag
default_risk_score = (
    .4 * (debt_to_income_ratio) + 
    .3 * (credit_utilization_ratio) +
    .3 * (days_in_arrears / 120)
)

default_flag = np.random.binomial(1, p=np.clip(default_risk_score, 0, 1))

df = pd.DataFrame({
    'client_id': client_id,
    'age': age,
    'monthly_income': monthly_income,
    'active_debt': active_debt,
    'credit_utilization_ratio': credit_utilization_ratio,
    'employment_status': employment_status,
    "days_in_arrears": days_in_arrears,
    'default_flag': default_flag,
    'record_date': pd.Timestamp.today().date()
})

df.to_csv('sa_credit_data.csv', index=False)
print(f"Generated {len(df)} rows")
print(f"Default rate: {df['default_flag'].mean():.2%}")
print(df.head())