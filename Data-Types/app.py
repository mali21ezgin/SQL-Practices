from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine

# 1. CSV read
df = pd.read_csv("train.csv", encoding="utf-8")

# 2. 2. Make column names SQL-friendly (replace spaces and hyphens with '_', convert to uppercase)
df.columns = [
    col.strip().replace(" ", "_").replace("-", "_").upper()
    for col in df.columns
]

# 3. SQL Server connection settings
server = r"localhost\SQLEXPRESS"  # Replace with your own server/instance name
database = "ETRADE3"

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={quote_plus(conn_str)}", fast_executemany=True
)

# 4. Transfer to table (overwrites if it exists
df.to_sql("RAW_SUPERSTORE", con=engine, if_exists="replace", index=False)

print(f"Yükleme tamamlandı. Toplam satır: {len(df)}")
print("Sütunlar:", list(df.columns))