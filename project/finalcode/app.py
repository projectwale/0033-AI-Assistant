# pip install rasa==2.0.2
# rasa run actions
# rasa run --cors "*" --enable-api
# pip install rasa-nlu==0.11.5
# greenlet==0.4.16
# pip install slackclient==1.3.1

# rasa train


from flask import Flask, render_template, request, session, url_for, redirect,jsonify,flash
import pymysql
from werkzeug.utils import secure_filename
import pathlib
import os
import json
import requests

app = Flask(__name__)
output=[]#("message stark","hi")]
app.secret_key = 'any random string'
app.config['UPLOAD_FOLDER1'] = 'static/Users'

def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="033_ailegalchatbot")
    return connection


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
        
                
con = dbConnection()
cursor = con.cursor()


@app.route('/')
def main():
    return render_template('index.html')




@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        telephone = request.form.get("telephone")
        message = request.form.get("message")
        sql = "INSERT INTO feedbacks(NAME, EMAIL, PHONE, MASSAGE) VALUES (%s, %s, %s, %s)"
        val = (name, email, telephone, message)
        cursor.execute(sql, val)
        con.commit()
        
        flash('Message sent successfully!', 'success')  # Flash a success message
        return redirect(url_for('contact'))  # Redirect to the contact page
        
  
    return render_template('contact.html')

@app.route('/logout')
def logout():
    session.pop('user1')

    return redirect(url_for('main'))


@app.route('/login1',methods=['POST','GET'])
def login1():
    if request.method == 'POST':
        email = request.form.get("email")
        Password = request.form.get("password")
        print(email)
        print(Password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM registration WHERE email = %s AND password = %s', (email, Password))
        print(result_count)
        
        if result_count == 1:
            res = cursor.fetchone()
            print(res)
            session['user1'] = res[1]
            session['uidmail'] = res[2]
            session['image1'] = res[6]
            # Successful login logic
            # return jsonify({'message': 'Login successful', 'user_id': res[0]})
            return "success"
        else:
            # Failed login logic
            # return jsonify({'message': 'Login failed'})
            return "fail"

        con.close()
    


@app.route('/register1',methods=['POST'])
def register1():
    
    print("ouy")
    if request.method =='POST':
        print("in record")
        details = request.form
      
        Username = details['name']
        email = details['email']
        Mobile = details['Moblie'] 
        Password = details['password']
        addresss = details['addresss']
        age = details['Age']
        uploadimg = request.files['file']
        
        
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM registration WHERE email = %s', (email))
        res = cursor.fetchone()
      
        
        filename_secure = secure_filename(uploadimg.filename)
        uploadimg.save(os.path.join(app.config['UPLOAD_FOLDER1'], filename_secure))
        filenamepath = os.path.join(app.config['UPLOAD_FOLDER1'], filename_secure)
        
        if not res:
            sql = "INSERT INTO registration(name, email, password, mobile, address,Age,image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (Username, email, Password, Mobile, addresss, age, filenamepath)
            cursor.execute(sql, val)
            con.commit()
    
            message = "Registration USER successfully added by USER side. Username: " + Username
            # return redirect(url_for('index'))
            return jsonify({'message': message})
            message = "Already available"
            
        else:
            message = "Registration USER not  added by USER side. Username: " + Username
            dbClose()
            # return redirect(url_for('index'))
            return jsonify({'message': message})

################################################################################################################################
@app.route('/home')
def home():
    if 'user1' in session:
        return render_template('home.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')
@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/userdetails')
def userdetails():
    uidmail=session['uidmail']
    print(uidmail)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM registration WHERE email = %s', (uidmail))
    data = cursor.fetchall()
    print(data)
    
    return render_template('userdetails.html',data=data)

@app.route('/profile')
def profile():
    return render_template('profile.html')

####################################################################CHATBOT############################################################
@app.route('/getRequest1', methods=['POST'])
def getRequest1():
    print("GET")
    if request.method =='POST':
        print("Post")
     
        data = request.get_json()
        userText = data.get('userMessage')
   
        print(userText)
        data = json.dumps({"sender": "Rasa","message": userText})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()
        print()
        print("Output")
        print(res)
        print()
        val = res[0]['text']
        output.append(val)
        print()
        print("val")
        print(val)
        print()
        responses = val
        print("=====================")
        print(responses)
        print("=====================")
        
        return responses
  

if __name__ == '__main__':
    app.run(debug=True)
    # app.run('0.0.0.0')