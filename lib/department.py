from __init__ import CURSOR, CONN
        
class Department:
    
    def __init__(self, name, location, id= None):
        self.name = name
        self.location = location
        self.id = None
        
    def __repr__(self):
            return f"<Department {self.id}: {self.name}' '{self.location}>"
        
    @classmethod   
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS davie(
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT);
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod   
    def drop_table(cls):
        sql = """DROP TABLE IF NOT EXIST davie;"""
        
        CURSOR.execute(sql)
        CONN.commit()
        
    def insert(self):
        sql = """INSERT INTO davie(name, location) VALUES (?, ? )"""
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        
    @classmethod   
    def save(cls, name, location):
        davie = cls(name,location)
        davie.insert()
        return davie
    
    
    def update(self):
        sql = """UPDATE davie SET name = ? location = ? WHERE id = ?"""
        
        CURSOR.execute(sql, (self.name,self.location, self.id))
        CONN.commit()
        
    def delete(self):
        sql = """DELETE FROM davie WHERE id = ? """
        
        CURSOR.execute(sql, id = None)
        CONN.commit()
        
        
        
    
        
