import pandas as pd
import numpy as np

def load_climate_data(file_path):
"""
Load climate data from a CSV file.
"""
try:
data = pd.read_csv(file_path)
return data
except FileNotFoundError:
print(f"File not found: {file_path}")
return None

def clean_climate_data(data):
"""
Clean and prepare climate data for analysis.
"""

```
if data is None:
    return None

# Remove duplicate records
data = data.drop_duplicates()

# Convert column names to lowercase
data.columns = data.columns.str.lower().str.strip()

# Replace missing values with NaN
data = data.replace(["", "NA", "N/A", "null"], np.nan)

# Remove rows where all values are missing
data = data.dropna(how="all")

return data
```

def summarize_climate_data(data):
"""
Generate basic statistical information about climate data.
"""

```
if data is None or data.empty:
    return None

return data.describe()
```

if **name** == "**main**":
print("AtmoSync data processing module")
print("Ready to process micro-climate data.")
