from flask import Flask, jsonify, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.position import Position

#cria engine e localização do db
engine = create_engine('sqlite:///go-robot.db', echo=True)
Session = sessionmaker(bind=engine)

# caso a tabela n exista, é criada
Base.metadata.create_all(engine)

app = Flask(__name__)


@app.route("/")
def index():
    try:
        get_session = Session()
        get_position = get_session.query(Position)
        print(get_position)

        return render_template("index.html", nome_controlador='Mihaell', positions = get_position)

    except Exception as err:
        print(str(err))

# rota de post 
@app.route("/set_position", methods = ['POST'])
# @app.post("/set_position")
def setPosition():
    try:
        print('estou aqui')
        # requisitas os dados do forms
        x = request.form['x']
        y = request.form['y']
        z = request.form['z']
        r = request.form['r']

        # adiciona ao db
        post_session = Session()
        pos = Position(x, y, z, r)

        post_session.add(pos)
        post_session.commit()

        # redireciona ao index apos add ao banco
        return redirect('/')
    except Exception as err:
        print(str(err))
        # return jsonify({"message":"Error password or user not match"})

# get das informaççoes do db
@app.get("/get_position")
def getPosition():
    try:
        # Abre sessão e faz um query ao banco
        get_session = Session()
        pos = get_session.query(Position).order_by(Position.id.desc()).limit(1).one()
        print (pos)
        # retorna a informação em json
        return pos.pos_as_json()
    except Exception as err:
        print(str(err))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
