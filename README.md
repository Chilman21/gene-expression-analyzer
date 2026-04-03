🧬 Gene Expression Analyzer (Pandas + Matplotlib)

📌 Overview

This project analyzes gene expression data using Python. It compares control and treated samples, calculates fold change, and visualizes the results using graphs.

🚀 Features

- Load gene expression data from CSV file
- Calculate fold change (Treated / Control)
- Identify:
  - Upregulated genes
  - Downregulated genes
- Visualize data using:
  - Bar plots
  - Fold change plots
  - Scatter plots

📂 Project Structure

gene-project
│
├── main.py
└── gene_expression.csv

📊 Sample Data

Gene,Control,Treated
GeneA,10,15
GeneB,8,7
GeneC,5,20
GeneD,12,9
GeneE,3,18

⚙️ Installation

Install required libraries:
pip install pandas matplotlib

▶️ How to Run

Run the Python script:
python main.py

📈 Output

The program will:
- Print analysis results in terminal
- Show graphs:
  - Control vs Treated comparison
  - Fold change per gene
  - Scatter plot

🧠 Concepts Used

- Data analysis with Pandas
- Data visualization with Matplotlib
- Biological concept: Gene expression & fold change

🎯 Use Cases

- RNA-seq data analysis
- Gene expression comparison
- Biological data visualization

✨ Future Improvements

- Add log2 fold change
- Add volcano plot
- Support multiple samples
- Export results to file

👩‍💻 Author

Chilman Bishnoi

