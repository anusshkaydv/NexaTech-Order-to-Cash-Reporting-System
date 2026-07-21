import pyodbc

server = "nexatech-anushka-sql.database.windows.net"
database = "NexaTechERP"
username = "nexatechadmin"
password = "Qwertyuiop@123"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(connection_string)
    print("✅ Connected to Azure SQL Database Successfully!")
    conn.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)
