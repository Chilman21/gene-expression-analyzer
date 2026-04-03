import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("gene_expression.csv")

print("Data:")
print(df)

# Fold change 
df["FoldChange"] = df["Treated"] / df["Control"]

print("\nWith Fold Change: ")
print(df)

# Top upregulated genes (>1.5)
upregulated = df[df["FoldChange"] > 1.5]
print("\nUpregulated Genes: ")
print(upregulated)

# Top downregulated genes (>0.7)
downregulated = df[df["FoldChange"] > 0.7]
print("\nDownregulated Genes: ")
print(downregulated)

# Bar plot
plt.figure()
x = range(len(df["Gene"]))

plt.bar(x, df["Control"],  width = 0.4, label="Control")
plt.bar([i + 0.4 for i in x] , df["Treated"] , width = 0.4, label="Treated")

plt.xticks([i + 0.2 for i in x], df["Gene"])
plt.title("Control vs Treated Expression")
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.legend()
plt.show()

# Fold change plot
plt.figure()
plt.bar(df["Gene"], df["FoldChange"])
plt.title("Fold Change per gene")
plt.xlabel("Genes")
plt.ylabel("Fold Change")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df["Control"], df["Treated"])
plt.title("Control vs Treated Scatter")
plt.xlabel("Control")
plt.ylabel("Treated")
plt.show()