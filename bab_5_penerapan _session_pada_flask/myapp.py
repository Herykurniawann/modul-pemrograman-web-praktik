from flask import Flask, render_template ,request ,session ,redirect ,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)


# db config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

# init db
mysql = MySQL(app)
app.secret_key = 'secret'


@app.route("/")
def index():
    if 'is_log_in' in session:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()

        return render_template('index.html',users=data,userName = session['user_name'])
    else:
        return redirect(url_for('login'))
    


@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET" :
        return render_template('login.html')
    else:
        email = request.form['userEmail']
        password = request.form['userPassword']

        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s",(email,password))
        
        user = cur.fetchone()

        if user :
            session['is_log_in'] = True
            session['user_name'] = user[1]

            # redirect
            return redirect(url_for('index')) #patokannya nama function
        else:
            errMessage = "Login Failed"
            return render_template('login.html',errMessage=errMessage)

        cur.close()
        

        print("POST")
        return "POST" + email + password


@app.route('/logout')
def logout():
    session.pop('is_log_in',None)
    session.pop('user_name',None)

    return redirect(url_for('login'))
        

if __name__ == "__main__":
    app.run(debug=True)