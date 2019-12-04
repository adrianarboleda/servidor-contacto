from flask import Flask, jsonify, request
import mysql.connector

app = Flask (__name__)

bd = mysql.connector.connect(host='localhost', user='alumno',
                            passwd='12345', database='contactos')

cursor = bd.cursor()

@app.route('/contactos/', methods=["GET", "POST", "PATCH", "DELETE"])

def peliculas():
    if request.method=="GET":
        contactos = []
        query = "SELECT * FROM contacto"
        cursor.execute(query)

        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'nombre': contacto[1],
                'telefono': contacto[2],
                'correo': contacto[3],
                'facebook': contacto[4],
                'twitter': contacto[5],
                'instagram': contacto[6],
                'img': contacto[7]
            }
            contactos.append(d)

        print(contactos)

        return jsonify(contactos)
    elif request.method =="POST":
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto (nombre, telefono,correo,facebook, twitter, instagram, img) VALUES(%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (data['nombre'], data['telefono'],data['correo'],data['facebook'],data['twitter'],data['instagram'], data['img']))

        bd.commit()

        if cursor.rowcount:
            return jsonify({'data': 'Ok'})
        else:
            return jsonify({'data': 'Error'})
    elif request.method == "DELETE":
        data = request.get_json()
        print(data)

        query = "DELETE FROM contacto WHERE id = %s"

        cursor.execute(query, data)

        bd.commit()

    else:
        data = request.get_json()
        print(data)

        query = "UPDATE contacto SET nombre =%s, telefono = %s, correo = %s, facebook = %s, twitter = %s, instagram = %s, img = %s WHERE id = %s"

        cursor.execute(query, (data['nombre'], data['telefono'],data['correo'],data['facebook'],data['twitter'],data['instagram'], data['img'], data['id']))

        bd.commit()



app.run(debug=True)