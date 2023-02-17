import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def read_data(file_path):
    """
    Reads the data from a csv file and returns a pandas dataframe
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} could not be found.")
        df = None
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {e}")
        df = None
    return df

def analyze_data(df):
    """
    Analyzes the data and identifies patterns in the values
    """
    try:
        if 'CrashPoint' not in df.columns:
            raise ValueError("The dataframe does not contain a column named 'CrashPoint'.")
        
        # Plot the data to visualize the pattern
        plt.plot(df['CrashPoint'])
        plt.show()
        
        # Fit a linear regression model to the data
        x = [[i] for i in range(len(df))]
        y = df['CrashPoint'].values
        reg = LinearRegression().fit(x, y)
    except ValueError as ve:
        print(ve)
        reg = None
    except Exception as e:
        print(f"Error: An unexpected error occurred while analyzing the data: {e}")
        reg = None
    return reg

def predict_values(reg, n=200):
    """
    Predicts the next n values of crashpoint using the linear regression model
    """
    try:
        if reg is None:
            raise ValueError("The linear regression model is not fit to the data.")
        
        # Use the fitted model to predict the next n crash points
        last_index = len(df) - 1
        future_index = [[i] for i in range(last_index + 1, last_index + 1 + n)]
        predictions = reg.predict(future_index)
    except ValueError as ve:
        print(ve)
        predictions = None
    except Exception as e:
        print(f"Error: An unexpected error occurred while making predictions: {e}")
        predictions = None
    return predictions


if __name__ == "__main__":
    # Load the data from the CSV file into a pandas dataframe
    file_path = "crash_data.csv"
    df = read_data(file_path)
    
    if df is not None:
        # Analyze the data and identify patterns
        reg = analyze_data(df)
        
        if reg is not None:
            # Predict the next n crash points
            predictions = predict_values(reg, 200)
            if predictions is not None:
                print(predictions)
                # Save the predictions to a CSV file
                df_pred = pd.DataFrame({'CrashPoint': predictions})
                df_pred.to_csv("generated.csv", index=False)
