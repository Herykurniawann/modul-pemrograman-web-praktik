# import library third party
from flask import Flask,render_template
from flask_mysqldb import MySQL

# init main app
app = Flask(__name__)

# database config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB']='flask_praktikum'

# init mysql
mysql = MySQL(app)

# set route default
@app.route('/')
# function name
def home():
#   cursor koneksi mysql
    cur = mysql.connection.cursor()
#   execute query
    cur.execute("SELECT * FROM users")
#   fetch hasil query masukkan ke variable data
    data = cur.fetchall()
#   close koneksi mysql
    cur.close()

#   render array data sebagai users
