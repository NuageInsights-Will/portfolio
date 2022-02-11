import pandas as pd

df = pd.read_csv('zillow.csv', index_col = 0)
df.columns = ["Living Space (sq ft)", "Beds", "Baths", "Zip", "Year", "List Price ($)"]

def clean(df: pd.DataFrame) -> pd.DataFrame:
    def is_greater_than_2000(size: int) -> bool:
            if size > 2000:
                return True
            else:
                return False
    df["LivingSpaceGreaterThan2000"] = df["Living Space (sq ft)"].apply(is_greater_than_2000)
    df["TotalRooms"] = df["Beds"] + df["Baths"]
    df["ListPriceInclTax"] = df["List Price ($)"] * 1.13
    df["EstMortgageFees"] = df["List Price ($)"] * 0.05
    df.drop(columns = "Zip", inplace = True)
    df.drop(df.index[df["Year"] < 1980], inplace = True)
    df.drop(df.index[df["ListPriceInclTax"] < 130000], inplace = True)
    
clean(df)

df.to_csv('zillow_cleaned.csv')