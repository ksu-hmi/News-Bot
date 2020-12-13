from VIAA_Database import *

#Insert into database
def create_keyword(user_id,new_keywords):
    
    #Create a new url into the url table
    #:param conn:
    #:param url:
    #:return: url id
    
    sql =  '''INSERT INTO keyword(user_id ,keyword)
              VALUES(?,?) '''
              
    conn = create_connection(r"dbVIAA.db")      
    cur = conn.cursor()
    cur.execute(sql, (user_id, new_keywords))
    conn.commit()
    return cur.lastrowid

#Get keywords per userID to populate table 
def keyword_table(userID): 
    conn = create_connection(r"dbVIAA.db")
    cur = conn.cursor()
    cur.execute("SELECT keyword FROM keyword where user_id = '" + userID + "';")
    keywords = cur.fetchall()

    return keywords