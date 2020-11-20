import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=projeto-iris-db.database.windows.net;'
                      'Database=IrisDB;'
                      'UID=iris;'
                      'PWD=sql2020@;')

cursor = conn.cursor()

def list_all_users():
    return  cursor.execute("SELECT UserId, Name FROM dbo.Users").fetchall()

def get_user_by_id(user_id):
    cursor.execute("SELECT UserId, Name FROM dbo.Users WHERE UserId=?", user_id)
    row = cursor.fetchone()
    if row:
        return row.Name

def get_image_by_id(user_id):
    cursor.execute("SELECT UserId, PhotoBase64Location FROM dbo.Users WHERE UserId=?", user_id)
    row = cursor.fetchone()
    if row:
        return row.PhotoBase64Location
