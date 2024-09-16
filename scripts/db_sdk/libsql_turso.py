# https://docs.turso.tech/features/embedded-replicas/introduction#embedded-replicas

import os

import libsql_experimental as libsql

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("data/test_turso.db", sync_url=url, auth_token=auth_token)  # type: ignore
conn.sync()

conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
conn.execute("INSERT INTO users(id) VALUES (15);")
conn.commit()
conn.sync()

print(conn.execute("select * from users").fetchall())
