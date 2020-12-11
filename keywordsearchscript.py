
while True:
    user_name = input("Enter your name: \n")
    
    if username.isalpha() == True:
        print("Hi", user_name, ", I'm VIAA. \n It's a pleasure to search for you!")
    
        
    else:
        print("Please only use letters.\n")

    user_id = input("Please enter an id number to use when searching: ")
        if user_id.isalnum() == True:
            print("Your user is is", user_id)
     else:
        print("Please enter a number\n")      

# [ ] create keyword()

def keywords(word):
    keyword = []
    if word.isalpha(): 
        keyword = ask
    else:
        print("This is not a word")
    
ask = input("What would you like to search? ")
keywords(ask)                 

#Insert into table
def create_keyword(conn,user_id,keyword):
    
    #Create a new url into the url table
    #:param conn:
    #:param url:
    #:return: url id
    
    sql =  '''#INSERT INTO keyword(user_id ,keyword)
              #VALUES(?,?,?,?) '''
'''          
    cur = conn.cursor()
    cur.execute(sql, (user_id, keyword))
    conn.commit()
    return cur.lastrowid