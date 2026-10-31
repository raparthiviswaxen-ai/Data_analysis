import pandas as pd
from sqlalchemy import create_engine, URL

# Location of the CSV file
file_path = r"C:\upgraded_onedrive\OneDrive\Documents\My Tableau Repository\Datasources\2024.2\en_US-US\Superstore00.csv"

# Read CSV file
df = pd.read_csv(file_path)

# Display first 5 records
print(df.head())

# Display number of rows and columns
print(df.shape)

# Display column names
print(df.columns.tolist())

# Check the number of rows and columns
print("Dataset Shape:", df.shape)

# Check the data types of each column
print("\nColumn Data Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Convert Order Date into date format
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d-%m-%Y"
)

# Convert Ship Date into date format
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%d-%m-%Y"
)

# Check the updated data types
print("\nUpdated Date Types:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Display the first 5 records
print("\nUpdated Dataset:")
print(df.head())

# MySQL database connection details
connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="MyPassword",
    host="localhost",
    port=3306,
    database="powerbi"
)

# Create the connection
engine = create_engine(connection_url)

# Test the connection
try:
    with engine.connect() as connection:
        print("Successfully connected to MySQL!")
except Exception as e:
    print("Connection failed:", e)

# Import dataset into MySQL
df.to_sql(
    name="superstore",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)

print("Superstore dataset imported successfully!")