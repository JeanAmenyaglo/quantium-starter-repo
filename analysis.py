# import pandas as pd
# import glob

# # Load all CSV files
# files = glob.glob("data/*.csv")
# df_list = [pd.read_csv(f) for f in files]

# # Combine into one DataFrame
# df = pd.concat(df_list, ignore_index=True)

# # Convert date column to datetime
# df['date'] = pd.to_datetime(df['date'])

# # Filter for Pink Morsel only
# pink = df[df['product'] == "pink morsel"]

# # Calculate sales (price * quantity)
# pink['sales'] = pink['price'] * pink['quantity']

# # Create final output with only Sales, Date, Region
# output = pink[['sales', 'date', 'region']]

# # Save to CSV
# output.to_csv("pink_morsel_sales.csv", index=False)

# print("Output file created: pink_morsel_sales.csv")


import pandas as pd
import glob

# Load all CSV files
files = glob.glob("data/*.csv")
df_list = [pd.read_csv(f) for f in files]

# Combine into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter for Pink Morsel only
pink = df[df['product'] == "pink morsel"]

# CLEAN PRICE COLUMN (IMPORTANT FIX)
pink['price'] = pink['price'].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales
pink['sales'] = pink['price'] * pink['quantity']

# Create final output
output = pink[['sales', 'date', 'region']]

# Save to CSV
output.to_csv("pink_morsel_sales.csv", index=False)

print("Output file created: pink_morsel_sales.csv")