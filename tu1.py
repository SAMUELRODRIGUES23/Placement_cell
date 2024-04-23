from flask import Flask, url_for,render_template,request,redirect,session,flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key='samuel'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='te'


mysql=MySQL(app)

'''@app.route('/viewadmin')
def viewadmin():
    if 'username' in session:
        return render_template("viewadmin.html",username=session['username'])
    else:
         return render_template("login.html")'''

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        password=userDetails['password']
        sr=userDetails['sr']
        pin=userDetails['pin']
        cur=mysql.connection.cursor()
        if pin=="officialplayer123":
            cur.execute("INSERT INTO users(name,email,password,sr) VALUES(%s,%s,%s,%s)",(name,email,password,sr))
            mysql.connection.commit()
            cur.close()
           
            return render_template('register.html',error='YOU ARE REGISTERED.PLEASE LOG IN')
                 
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        
        username=request.form['name']
        
        password=request.form['password']
        
       
       
        cur=mysql.connection.cursor()
        
        cur.execute(f"select name,password from users where name='{username}'")
        user=cur.fetchone()
        cur.close() 
        if user and password==user[1]:
            session['username']=user[0]
            return render_template("viewadmin.html",username=session['username'])
        else:
            return render_template("login.html",error='login failed')
    return render_template("login.html")

@app.route('/userlogin',methods=['GET','POST'])
def userlogin():
     if request.method=='POST':
        username=request.form['name']
        password=request.form['password']
        cur=mysql.connection.cursor()
        cur.execute(f"select Name,Password from students where Name='{username}'")
        user=cur.fetchone()
        cur.close() 
        if user and password==user[1]:
            session['username']=user[0]
            return render_template("view.html")
        else:
            return render_template("userlogin.html",error='login failed')
     return render_template("userlogin.html")
    
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        phone=userDetails['phone']
        msg=userDetails['message']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO contact(name,email,phone,message) VALUES(%s,%s,%s,%s)",(name,email,phone,msg))
        mysql.connection.commit()
        cur.close()
        return render_template("contact.html",message='SENT.THANK YOU')
    return render_template("contact.html")

@app.route('/details',methods=['GET','POST'])
def details():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['c_name']
        branch=userDetails['branch']
        num=userDetails['num']
        date=userDetails['date']
        des=userDetails['descp']
        cur=mysql.connection.cursor()
        if branch=="computer" or branch =="Computer" or branch =="COMPUTER":
            cur.execute("INSERT INTO c_details(c_name,branch,Phone_number,date,description) VALUES(%s,%s,%s,%s,%s)",(name,branch,num,date,des))
            mysql.connection.commit()
            cur.close()
            return render_template('details.html',error='Details Saved')
        if branch=="Electronics" or branch =="ELECTRONICS" or branch =="ETC" or branch=="electronics" or branch=="etc":
            cur.execute("INSERT INTO etc_info(c_name,branch,ph_no,date,description) VALUES(%s,%s,%s,%s,%s)",(name,branch,num,date,des))
            mysql.connection.commit()
            cur.close()
            return render_template('details.html',error='Details Saved')
        if branch=="IT" or branch =="it" or branch =="Infromation Technology" or branch=="information technology":
            cur.execute("INSERT INTO it_info(c_name,branch,ph_no,date,description) VALUES(%s,%s,%s,%s,%s)",(name,branch,num,date,des))
            mysql.connection.commit()
            cur.close()
            return render_template('details.html',error='Details Saved')
        if branch=="mechanical" or branch =="mech" or branch =="MECHANICAL" or branch==" Mechanical":
            cur.execute("INSERT INTO mech_info(c_name,branch,ph_no,date,description) VALUES(%s,%s,%s,%s,%s)",(name,branch,num,date,des))
            mysql.connection.commit()
            cur.close()
            return render_template('details.html',error='Details Saved')
                 
    return render_template('details.html')

@app.route("/usercreate",methods=['GET','POST'])
def usercreate():
    if request.method=='POST':
        us=request.form
        roll=us['roll']
        name=us['name']
        password=us['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO students(sr_no,Name,Password)values(%s,%s,%s)",(roll,name,password))
        mysql.connection.commit()
        cur.close()
        return render_template("usercreate.html",error="User registered")
    return render_template("usercreate.html",error="User registered")

    
@app.route('/users',methods=['GET','POST'])
def users():

    if request.method == 'POST':
            id_data = request.form['id']
            name = request.form['name']
            email = request.form['email']
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE users
                SET name=%s, email=%s
                WHERE sr=%s
                """, (name, email, id_data))
            mysql.connection.commit()
            cur=mysql.connection.cursor()
            val=cur.execute("Select *from users")
            if val>0:
                userDetails=cur.fetchall()
                return render_template('users.html',userDetails=userDetails)
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from users")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

    
@app.route('/it')
def it():
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from it_info")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('it.html',userDetails=userDetails)
    
@app.route('/view')
def view():
        return render_template('view.html')

@app.route('/viewadmin')
def viewadmin():
        return render_template('viewadmin.html')

@app.route('/aboutus')
def aboutus():
        return render_template('aboutus.html')


    
@app.route('/comp')
def comp():
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from c_details")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('comp.html',userDetails=userDetails)
    
@app.route('/etc')
def etc():
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from etc_info")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('etc.html',userDetails=userDetails)
    
@app.route('/mech')
def mech():
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from mech_info")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('mech.html',userDetails=userDetails)

@app.route('/logout')
def logout():
    session.clear()
    return render_template("homepage.html")

@app.route('/response')
def response():
    cur=mysql.connection.cursor()
    val=cur.execute("Select *from contact")
    if val>0:
        userDetails=cur.fetchall()
        return render_template('response.html',userDetails=userDetails)

    

  

if __name__=="__main__":
    app.run(debug=True)

