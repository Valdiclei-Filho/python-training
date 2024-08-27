from repository import repository_base;

connection = repository_base.repository_base.connect();

cursor = connection.cursor();
cursor.execute("select * from cliente")

result = cursor.fetchall();
for r in result:
    print(r)