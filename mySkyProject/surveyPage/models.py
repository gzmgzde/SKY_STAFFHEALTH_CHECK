from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from welcomePage.models import User, Team, Department, Administrator

class Badge(models.Model):
    badge_id = models.TextField(db_column='Badge_Id', primary_key=True, blank=True, null=False)
    tier_level = models.TextField(db_column='Tier_Level', blank=True, null=True)

    class Meta:
        managed = True



class HealthCard(models.Model):
    health_card_id = models.AutoField(db_column='Health_Card_Id', primary_key=True)  # Changed to AutoField
    health_card_name = models.TextField(db_column='Health_Card_Name')
    health_card_description = models.TextField(db_column='Health_Card_Description', blank=True, null=True)

    class Meta:
        managed = True



class HealthRecord(models.Model):
    record_id = models.AutoField(db_column='Record_Id', primary_key=True)
    record_time = models.DateTimeField(db_column='Record_Time', blank=True, null=True)
    record_date = models.DateField(db_column='Record_Date', blank=True, null=True)
    team_sum = models.ForeignKey('TeamSummary', on_delete=models.CASCADE, db_column='Team_Sum_Id', blank=True, null=True, related_name='health_records')
    session_id = models.IntegerField(db_column='Session_Id', unique=True)
    session_duration = models.DurationField(db_column='Session_Duration', blank=True, null=True)
    session_date = models.DateField(db_column='Session_Date', blank=True, null=True)
    health_card = models.ForeignKey(HealthCard, on_delete=models.CASCADE, db_column='Health_Card_Id', blank=True, null=True, related_name='health_records')
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='Depart_Id', blank=True, null=True, related_name='health_records')

    class Meta:
        managed = True
    


class SkyeAi(models.Model):
    chat_id = models.TextField(db_column='Chat_Id', primary_key=True, blank=True, null=False)
    prompt = models.TextField(db_column='Prompt', blank=True, null=True)
    response = models.TextField(db_column='Response', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User_Id', blank=True, null=True, related_name='skye_ai')

    class Meta:
        managed = True
        db_table = 'SKYE-AI'


class TeamSummary(models.Model):
    team_sum_id = models.TextField(db_column='Team_Sum_Id', primary_key=True, blank=True, null=False)
    vote_average = models.FloatField(db_column='Vote_Average', blank=True, null=True)
    progress_trend = models.TextField(db_column='Progress_Trend', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='Team_Id', blank=True, null=True, related_name='team_summaries')
    record = models.ForeignKey(HealthRecord, on_delete=models.CASCADE, db_column='Record_Id', blank=True, null=True, related_name='team_summaries')

    class Meta:
        managed = True
   


class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_Id', primary_key=True)
    vote_value = models.IntegerField(

        blank=True, 
        null=True, 
        choices=((1, 'Bad'), (2, 'Neutral'), (3, 'Good')),
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    progress_status = models.TextField(db_column='Progress_Status', blank=True, null=True)
    vote_comment = models.TextField(db_column='Vote_Comment', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User_Id', blank=True, null=True, related_name='votes')
    health_card = models.ForeignKey(HealthCard, on_delete=models.CASCADE, db_column='Health_Card_Id', blank=True, null=True, related_name='votes')

    class Meta:
        managed = True

