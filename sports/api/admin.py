from django.contrib import admin
from .models import  Game, Bets, Ante, Pregamestats, Preview

@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('team','opposition') 
    ordering = ('start_time',)

@admin.register(Pregamestats)
class PregameAdmin(admin.ModelAdmin):
    list_display = ('field','computed') 

@admin.register(Bets)
class BetsAdmin(admin.ModelAdmin):
    list_display = ('match_id',) 
    ordering = ('created_date',)

@admin.register(Ante)
class AnteAdmin(admin.ModelAdmin):
    list_display = ('description',) 
    list_filter = ( 'pl',)
    search_fields = ('description',)
    ordering = ('created_date',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id','team', 'opposition', 'start_time')
    list_filter = ('match_status', 'sport')
    search_fields = ('match_id',)
    ordering = ('start_time',)