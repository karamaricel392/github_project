import numpy as np
import pandas as pd

def create_dataframe():
    # Generate 10 random integers between 5 and 20
    num_values = np.random.randint(5, 20, size=10)
    
    # Create a DataFrame with the generated values
    df = pd.DataFrame({'values': num_values})
    
    return df

if __name__ == "__main__":
    print(create_dataframe())
