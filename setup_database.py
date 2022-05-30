import sqlite3

file = "database.sqlite"
try:
    conn = sqlite3.connect(file)
    print("database created")
except:
    print("database nog created")

conn = sqlite3.connect(file)
conn.execute("CREATE TABLE vacature (id INTEGER NOT NULL PRIMARY KEY, title TEXT NOT NULL, bedrijf TEXT NOT NULL, link TEXT NOT NULL);")

# conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES ('testtitle', 'testbedrijf', 'http://testlink.com')")
# conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES ('testtitle1', 'testbedrijf1', 'http://testlink.com1')")
# conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES ('testtitle2', 'testbedrijf2', 'http://testlink.com2')")
# conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES ('testtitle3', 'testbedrijf3', 'http://testlink.com3')")
# res = conn.execute("SELECT * from vacature")

conn.commit()

conn.close()