from flask import Flask,render_template,request,jsonify
from flask_mysqldb import MySQL
from microservice.converter_adapter import Converter
from microservice.storage_data import BDRedisConnetion, BDmySQLConnetion





def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['MYSQL_HOST'] = 'DBmySQL'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'uno'
    app.config['MYSQL_DB'] = 'mysql'
    mysql = MySQL(app)

    @app.route('/', methods=['POST', 'GET'])
    def savedata():
         
        if(request.method == 'POST'):
            Temperat = request.form['temperature']
            tiemp = request.form['timeup']
            
            if( Temperat and tiemp):
                DtaB = Converter( Temperat , tiemp )  #Objeto tipo adaptador (adapter & strategy pattern)               
                
                Json = DtaB.HTML_To_Json() #Ejecutando adapter pattern 

                conecting_mySQL = BDmySQLConnetion( Json, mysql.connection.cursor(), mysql ) #Objeto de tipo conexión que manipula DBmySQL
                conecting_mySQL.Create_table()
                conecting_mySQL.Insert_data()


                conecting_Redis = BDRedisConnetion("redis",Json)
                conecting_Redis.Insert_data()

        return render_template("form.html")
          
    @app.route("/IoT", methods=['GET', 'POST'])
    def IoT():
        Json = request.get_json()
        conecting_mySQL = BDmySQLConnetion( mysql.connection.cursor(), Json, mysql ) #Objeto tipo conexion que manipula DBmySQL
        conecting_mySQL.Create_table()
        conecting_mySQL.Insert_data()


        conecting_Redis = BDRedisConnetion("redis",Json)
        conecting_Redis.Insert_data()
        
    
    return app

