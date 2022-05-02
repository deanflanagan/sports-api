from rest_framework import serializers
from .models import  Game, Pregamestats, Bets, Preview


class GameSerializer(serializers.ModelSerializer):
    # stats = PregamestatsSerializer(source='gamestats', read_only=True)
    class Meta:
        model = Game
        fields = '__all__'

class PreviewSerializer(serializers.ModelSerializer):
    # stats = PregamestatsSerializer(source='gamestats', read_only=True)
    class Meta:
        model = Preview
        fields = '__all__'

class PregamestatsSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    actual_ttl = serializers.SerializerMethodField()
    
    def get_actual_ttl(self, obj):
        return obj.game.ft1 + obj.game.ft2

    
    class Meta:
        model = Pregamestats
        fields = '__all__'

    def to_representation(self, obj):
        """Move fields from profile to user representation."""
        representation = super().to_representation(obj)
        game_representation = representation.pop('game')
        for key in game_representation:
            representation[key] = game_representation[key]

        return representation



class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bets
        fields = '__all__'

