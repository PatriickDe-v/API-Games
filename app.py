from resource.game import Game, Games

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Games, '/games')
api.add_resource(Game,'/games/<string:game_id>')
if __name__ == '__main__':
    app.run(debug=True)

