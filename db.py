import sqlite3

class database:    
    def __init__(Self, file):
        Self.conn = sqlite3.connect(file)

    def insertVacature(Self, title, bedrijf, link):
        values = [title, bedrijf, link] 
        Self.conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES (?, ?, ?)", values)
        Self.conn.commit()

    def closeDatabaseConnection(Self):
        Self.conn.close()

    def showTable(Self):
        result = Self.conn.execute("SELECT * FROM vacature")
        Self.conn.commit()
        return result;
        # for row in result:
        #     print(row)