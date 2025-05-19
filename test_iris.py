import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_dataset(file_path):
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Plot scatter plots
    sns.pairplot(df)
    plt.suptitle("Pairplot of the Dataset")
    plt.show()

    # Plot bar chart for categorical column (assuming the first column is categorical)
    if df.column.dtype == 'object':
        sns.countplot(x=df.columns, data=df)
        plt.title("Bar Chart of Categorical Column")
        plt.xlabel(columns)
        plt.ylabel("Count")
        plt.show()
    else:
        print("No categorical column found to plot bar chart.")

# Example usage
file_path = r'C:\Users\smita\Downloads\test\archive\Iris.csv'  # Ensure this file exists in the same directory
visualize_dataset(file_path)
