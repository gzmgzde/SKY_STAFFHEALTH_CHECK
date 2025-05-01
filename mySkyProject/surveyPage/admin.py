from django.contrib import admin
from .models import  Badge, HealthCard, HealthRecord, SkyeAi,  TeamSummary,  Vote


# Register your models here.

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('badge_id', 'tier_level')
    search_fields = ('tier_level',)

@admin.register(HealthCard)
class HealthCardAdmin(admin.ModelAdmin):
    list_display = ('health_card_id', 'health_card_name')
    search_fields = ('health_card_name', 'health_card_description')

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'record_date', 'session_id')
    search_fields = ('session_id',)
    list_filter = ('record_date', 'session_date')

@admin.register(SkyeAi)
class SkyeAiAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'prompt')
    search_fields = ('prompt', 'response')


@admin.register(TeamSummary)
class TeamSummaryAdmin(admin.ModelAdmin):
    list_display = ('team_sum_id', 'vote_average')
    search_fields = ('progress_trend',)
    list_filter = ('vote_average',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_id', 'vote_value', 'user', 'health_card')
    search_fields = ('vote_comment',)
    list_filter = ('vote_value',)