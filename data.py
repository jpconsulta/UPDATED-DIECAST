import sqlite3

db_path = "diecast.db"

# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns restaurant by their location
def read_diecast_by_carbrand(carbrand):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM diecasts WHERE carbrand = ?'
    value = carbrand
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_diecast_by_manufacturer(manufacturer):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM diecasts WHERE manufacturer = ?'
    value = manufacturer
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 pet by pet_id
def read_diecast_by_id(id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM diecasts WHERE id = ?'
    value = id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

# This function inserts 1 pet data
def insert_diecast(diecast_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO diecasts (manufacturer, carbrand, carname, series, releaseyear, color, material, price, url, scale) VALUES (?,?,?,?,?,?,?,?,?,?)'
    values = (diecast_data['manufacturer'], diecast_data['carbrand'],
              diecast_data['carname'], diecast_data['series'],
              diecast_data['releaseyear'], diecast_data['color'],
              diecast_data['material'], diecast_data['price'],
              diecast_data['url'], diecast_data['scale'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_diecast(diecast_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE diecasts SET manufacturer=?, carbrand=?, carname=?, series=?, releaseyear=?, color=?, material=?, price=?, url=?, scale=? WHERE id=?"
    values = (diecast_data['manufacturer'], diecast_data['carbrand'],
              diecast_data['carname'], diecast_data['series'],
              diecast_data['releaseyear'], diecast_data['color'],
              diecast_data['material'], diecast_data['price'],
              diecast_data['url'], diecast_data['scale'], diecast_data['id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_diecast(diecast_id):
    con, cur = connect_to_db(db_path)
    query = "DELETE FROM diecasts WHERE id = ?"
    values = (diecast_id,)  # Note the comma to create a single-element tuple
    cur.execute(query, values)
    con.commit()
    con.close()


def search_diecast(query):
    conn, cur = connect_to_db(db_path)
    sql_query = "SELECT * FROM diecasts WHERE carbrand LIKE ? OR manufacturer LIKE ? OR carname LIKE ?"
    value = "%{}%".format(query)
    print(value)
    results = cur.execute(sql_query, (value, value, value)).fetchall()
    conn.close()
    return results