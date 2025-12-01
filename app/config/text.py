import oracledb
import platform
from dotenv import load_dotenv
import os
load_dotenv()

# SOLO en Windows/macOS se pasa lib_dir; en Linux no se debe pasar (ahí se usa PATH/ldconfig)
if platform.system() == "Windows":
    oracledb.init_oracle_client(lib_dir=os.getenv('LIB_DIR'))

conn = oracledb.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    dsn=os.getenv('DSN')
)
with conn.cursor() as cur:
    request =cur.execute("SELECT * FROM EMPRESA04.adningreso WHERE AINCONSEC IN (460527,460526,460525,460524)")
    print(type(request.fetchall()))
    print(cur.fetchall())