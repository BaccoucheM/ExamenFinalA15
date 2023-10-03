import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='gestionprojet'
        )
        self.cursor = self.conn.cursor()

    def create_project(self, code_projet, description):
        query = "INSERT INTO projects (Code_projet, Description) VALUES (%s, %s)"
        values = (code_projet, description)
        self.cursor.execute(query, values)
        self.conn.commit()
        return {'Code_projet': code_projet, 'Description': description}

    def get_project(self, code_projet):
        query = "SELECT * FROM projects WHERE Code_projet = %s"
        self.cursor.execute(query, (code_projet,))
        project = self.cursor.fetchone()
        if project:
            return {'Code_projet': project[0], 'Description': project[1]}
        return None
