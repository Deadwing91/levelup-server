from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, Game_Type


class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        games = Game.objects.get(pk=pk)
        serializer = GameSerializer(games)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        gametype = Game_Type.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            name=request.data["name"],
            designer=request.data["designer"],
            description=request.data["description"],
            number_of_players=request.data["number_of_players"],
            skill_level=request.data["skill_level"],
            gamer=gamer,
            gametype=gametype
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.name = request.data["name"]
        game.designer = request.data["designer"]
        game.description = request.data["description"]
        game.number_of_players = request.data["number_of_players"]
        game.skill_level = request.data["skill_level"]
        gametype = Game_Type.objects.get(pk=request.data["gametype"])
        game.gametype = gametype
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class GameGameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Type
        fields = ('id', 'label')
    

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    gametype = GameGameTypeSerializer(many=False)

    class Meta:
        model = Game
        fields = ('id', 'gamer', 'gametype', 'name', 'description', 'designer', 'number_of_players', 'skill_level')