from flask import Flask, render_template, request
import pymysql


def sql_connector():
    conn = pymysql.connect(user='root', password='password', db='pehla', host='localhost')
    c = conn.cursor()
    return conn, c


app = Flask(__name__)
          
        
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        batsman = request.form.get('batsman')
        runs = request.form.get('runs')
        conn, c = sql_connector()
        c.execute("INSERT INTO batsmans VALUES ('{}', {})".format(batsman, int(runs)))
        conn.commit()
        conn.close()
        c.close()
    return render_template('index.html')
                             

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# pymysql, mysql-connector, mysql-connector-python
