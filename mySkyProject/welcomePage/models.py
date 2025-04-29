from django.db import models

class Administrator(models.Model):
    admin_id = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Administrator'

class Badge(models.Model):
    # Use Django's implicit auto-incrementing ID as the primary key
    badge_id = models.CharField(max_length=255, null=True, unique=True)  # Allow NULL to match SQL
    tier_level = models.CharField(max_length=50)

    class Meta:
        db_table = 'Badge'

class Department(models.Model):
    department_id = models.CharField(max_length=255, primary_key=True)
    department_name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='departments')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='department_teams')

    class Meta:
        db_table = 'Department'

class HealthCard(models.Model):
    # Use Django's implicit auto-incrementing ID as the primary key
    health_card_id = models.CharField(max_length=255, null=True, unique=True)  # Allow NULL to match SQL
    health_card_name = models.CharField(max_length=255)
    health_card_description = models.TextField()

    class Meta:
        db_table = 'Health_Card'

class HealthRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    record_time = models.CharField(max_length=255, null=True)
    record_date = models.CharField(max_length=255, null=True)
    team_summary = models.ForeignKey('TeamSummary', on_delete=models.CASCADE, null=True, related_name='health_records')
    session_id = models.IntegerField(unique=True)
    session_duration = models.FloatField(null=True)
    session_date = models.CharField(max_length=255, null=True)
    health_card = models.ForeignKey('HealthCard', on_delete=models.CASCADE, null=True, related_name='health_records')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, related_name='health_records')

    class Meta:
        db_table = 'Health_Record'

class SKYEAI(models.Model):
    chat_id = models.CharField(max_length=255, primary_key=True)
    prompt = models.TextField(null=True)
    response = models.TextField(null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='skye_ai_chats')

    class Meta:
        db_table = 'SKYE-AI'

class Team(models.Model):
    team_id = models.CharField(max_length=255, primary_key=True)
    team_name = models.CharField(max_length=255)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, related_name='teams')
    team_summary = models.ForeignKey('TeamSummary', on_delete=models.CASCADE, null=True, related_name='teams')

    class Meta:
        db_table = 'Team'

class TeamSummary(models.Model):
    team_sum_id = models.CharField(max_length=255, primary_key=True)
    vote_average = models.FloatField(null=True)
    progress_trend = models.CharField(max_length=255, null=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, related_name='team_summaries')
    record = models.ForeignKey('HealthRecord', on_delete=models.CASCADE, null=True, related_name='team_summaries')

    class Meta:
        db_table = 'Team_Summary'

class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255)
    admin = models.ForeignKey('Administrator', on_delete=models.CASCADE, null=True, related_name='users')
    session_id = models.IntegerField(unique=True, null=True)
    session_duration = models.FloatField(null=True)
    session_date = models.CharField(max_length=255, null=True)
    badge = models.ForeignKey('Badge', on_delete=models.CASCADE, null=True, related_name='users')
    view_profile = models.CharField(max_length=255, null=True)
    profile_picture = models.BinaryField(null=True)
    login_error_times = models.IntegerField(null=True)

    class Meta:
        db_table = 'User'

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    vote_value = models.FloatField(null=True)
    progress_status = models.CharField(max_length=255, null=True)
    vote_comment = models.TextField(null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='votes')
    health_card = models.ForeignKey('HealthCard', on_delete=models.CASCADE, null=True, related_name='votes')

    class Meta:
        db_table = 'Vote'