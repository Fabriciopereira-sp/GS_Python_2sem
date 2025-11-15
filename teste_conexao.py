import oracledb

try:
    conn = oracledb.connect(
        user="rm563065",
        password="191298",
        dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oracle.fiap.com.br)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=ORCL)))"
    )
    print("Conectou no banco da FIAP.")
    conn.close()
except Exception as e:
    print("Erro:", e)
