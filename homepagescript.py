# Import the class `Flask` from the `flask` module
from flask import Flask, render_template, request
from Resultsfromkeywordsearch import *
# Instantiate a new web application called `app`, with `__name__` representing the current file
app=Flask(__name__)
#The@app.route commands define the URLs in the website. 
#The specific functions directly after@app.route define what happens when those URLs are visited 
@app.route('/greet', methods=['POST'])
#The greet() function sets up the response for the submission form in home.html returning the response to home.htm

def greet():
    inputName = request.form['myName']
    inputUserId = request.form['userID']
    results = url_table(inputUserId)
    ip = request.remote_addr
    #write data to file or to DB
    inputName = inputName.title()
    return render_template("results.html",myName=inputName, results=results)
@app.route('/')
#In home(), Python callsFlask’s render_template function, which looks in the “templates” folder for the file mentioned
#and passes the variable myName to the template as blank by default. The home.html file says
#it extends layout.html. So, the render_template function goes to layout.html and assembles
#the html response, inserting home.html as a block named “content” where indicated
def home():
    
    return render_template("home.html",myName="")

@app.route('/keyword/')
def about():
    return render_template("keyword.html")


if __name__=="__main__":
    app.run(debug=True)

# Button to select url to twitter
 