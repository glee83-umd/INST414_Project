import matplotlib.pyplot as plt
import seaborn as sns

def plot_depression_anxiety_trends(df):
    plt.figure(figsize=(8,5))
    sns.lineplot(x="Age", y="Depressive Symptom", marker="o", label="Depressive Symptom", data=df)
    sns.lineplot(x="Age", y="Anxiety", marker="s", label="Anxiety", data=df)
    plt.title("Depression & Anxiety Trends in Adolescents")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_social_media_usage(df):
    plt.figure(figsize=(8,5))
    sns.lineplot(x="Age", y="Social Media Usage", data=df)
    plt.title("Age vs Social Media Usage")
    plt.xlabel("Age")
    plt.ylabel("Social Media Usage")
    plt.grid(True)
    plt.show()

def plot_relationship(df, x, y, title):
    plt.figure(figsize=(8,5))
    sns.regplot(x=x, y=y, data=df, ci=None, line_kws={"color":"r"})
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_correlation(df):
    plt.figure(figsize=(8,5))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Between Variables")
    plt.show()