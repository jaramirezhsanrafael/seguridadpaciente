import oracledb
import platform

# SOLO en Windows/macOS se pasa lib_dir; en Linux no se debe pasar (ahí se usa PATH/ldconfig)
if platform.system() == "Windows":
    oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_0")

conn = oracledb.connect(
    user="EMPRESA04",
    password="EMPRESA04",
    dsn="10.10.1.67:1521/dina2"  # p.ej. 10.0.0.5:1521/ORCL
)
""" with conn.cursor() as cur:
    cur.execute("SELECT * FROM EMPRESA04.adningreso WHERE AINCONSEC IN (460527,460526,460525,460524)")
    print(cur.fetchall()) """