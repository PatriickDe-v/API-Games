from flask_restful import Resource, reqparse

games = [
    {
        'game_id': 'NFS',
        'nome': 'Need For Speed Most Wanted',
        'ano': 2005,
        'categoria': 'Corrida'
    },
    {
        'game_id': 'COD',
        'nome': 'Call Of Duty',
        'ano': 2019,
        'categoria': 'Battle Royal'
    },
    {
        'game_id': 'GOW',
        'nome': 'God Of War - Ragnarok',
        'ano': 2022,
        'categoria': 'História'
    }
]

class Games(Resource): 
    def get(self):
        return {'games': games}

class Game(Resource): 
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('ano')
    argumentos.add_argument('categoria')

    def findGames(game_id):
        for game in games:
            if game['game_id'] == game_id: 
                return game 
        return None

    def get(self, game_id):
        game = Game.findGames(game_id)
        if game:
            return game
        return {'message': 'Game not found!'}, 404 #error
    def post(self, game_id):
        dados = Game.argumentos.parse_args()

        novoGame = {'game_id': game_id, **dados}

        games.append(novoGame)
        return novoGame, 200 #sucess
    def put(self, game_id): 

        dados = Game.argumentos.parse_args()

        novoGame = {'game_id': game_id, **dados}

        game = Game.findGames(game_id)
        if game: 
            game.update(novoGame)
            return novoGame, 200 #sucess 
        games.append(novoGame)
        return novoGame, 201 #sucess  

    def delete(self, game_id): 
        global games 
        games = [games for game in games if game['game_id'] != game_id]
        return {'message': 'Game deleted!'}