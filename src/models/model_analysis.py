import statsmodels.api as sm
from scipy.stats import ttest_ind, shapiro

def normality_test(series, name="Variable"):
    stat, p = shapiro(series)
    result = "normally distributed" if p > 0.05 else "NOT normally distributed"
    print(f"{name} - Shapiro-Wilk Test: stat={stat:.3f}, p={p:.3f} --> {result}")
    return stat, p

def run_ttest(group1, group2, name="Variable"):
    t_stat, p_val = ttest_ind(group1, group2)
    print(f"T-test ({name}): t = {t_stat:.3f}, p = {p_val:.3f}")
    return t_stat, p_val

def run_ols(X, y):
    X_const = sm.add_constant(X)
    model = sm.OLS(y, X_const).fit()
    print(model.summary())
    return model