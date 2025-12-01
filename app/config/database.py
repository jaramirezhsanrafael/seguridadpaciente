import cx_Oracle
import oracledb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# FORMATO:
# oracle+cx_oracle://usuario:password@host:puerto/servicio

ORACLE_USER = "EMPRESA04"
ORACLE_PASS = "EMPRESA04"
ORACLE_HOST = "10.10.1.67"
ORACLE_PORT = "1521"
ORACLE_SERVICE = "dina2"  # O el nombre que uses (ej: ORCL, DINA2, PROD)

DATABASE_URL = (
    f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASS}@10.10.1.67:1521/?service_name=dina2"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,               # Para ver errores en consola
    pool_pre_ping=True       # Evita pérdida de conexión
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#inspector = inspect(engine)
#tablas = inspector.get_table_names(schema="EMPRESA04")
#print(tablas)


try:
    conn = cx_Oracle.connect(
        user="EMPRESA04",
        password="EMPRESA04",
        dsn="10.10.1.67:1521/dina2"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM dual")
    result = cursor.fetchone()

    print("Conexión exitosa:", result)

except cx_Oracle.Error as e:
    print("Error al conectar:", e)

finally:
    if 'conn' in locals():
        conn.close()

