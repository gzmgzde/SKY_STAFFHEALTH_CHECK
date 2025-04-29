# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Administrator(models.Model):
    admin_id = models.TextField(db_column='Admin_Id', primary_key=True, blank=True, null=False)
    email = models.TextField(db_column='Email', unique=True, blank=True, null=True)
    password = models.TextField(db_column='Password', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Administrator'

class Badge(models.Model):
    badge_id = models.TextField(db_column='Badge_Id', primary_key=True, blank=True, null=False)
    tier_level = models.TextField(db_column='Tier_Level', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Badge'

class Department(models.Model):
    department_id = models.TextField(db_column='Department_Id', primary_key=True, blank=True, null=False)
    department_name = models.TextField(db_column='Department_Name')
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='User_Id', blank=True, null=True, related_name='departments')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='Team_Id', blank=True, null=True, related_name='departments')

    class Meta:
        managed = False
        db_table = 'Department'

class HealthCard(models.Model):
    health_card_id = models.TextField(db_column='Health_Card_Id', primary_key=True, blank=True, null=False)
    health_card_name = models.TextField(db_column='Health_Card_Name')
    health_card_description = models.TextField(db_column='Health_Card_Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Health_Card'

class HealthRecord(models.Model):
    record_id = models.AutoField(db_column='Record_Id', primary_key=True, blank=True, null=False)
    record_time = models.DateTimeField(db_column='Record_Time', blank=True, null=True)
    record_date = models.DateField(db_column='Record_Date', blank=True, null=True)
    team_sum = models.ForeignKey('TeamSummary', on_delete=models.CASCADE, db_column='Team_Sum_Id', blank=True, null=True, related_name='health_records')
    session_id = models.IntegerField(db_column='Session_Id', unique=True)
    session_duration = models.DurationField(db_column='Session_Duration', blank=True, null=True)
    session_date = models.DateField(db_column='Session_Date', blank=True, null=True)
    health_card = models.ForeignKey(HealthCard, on_delete=models.CASCADE, db_column='Health_Card_Id', blank=True, null=True, related_name='health_records')
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='Depart_Id', blank=True, null=True, related_name='health_records')

    class Meta:
        managed = False
        db_table = 'Health_Record'

class SkyeAi(models.Model):
    chat_id = models.TextField(db_column='Chat_Id', primary_key=True, blank=True, null=False)
    prompt = models.TextField(db_column='Prompt', blank=True, null=True)
    response = models.TextField(db_column='Response', blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='User_Id', blank=True, null=True, related_name='skye_ai')

    class Meta:
        managed = False
        db_table = 'SKYE-AI'

class Team(models.Model):
    team_id = models.TextField(db_column='Team_Id', primary_key=True, blank=True, null=False)
    team_name = models.TextField(db_column='Team_Name')
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='Depart_Id', blank=True, null=True, related_name='teams')
    team_sum = models.ForeignKey('TeamSummary', on_delete=models.CASCADE, db_column='Team_Sum_Id', blank=True, null=True, related_name='teams')

    class Meta:
        managed = False
        db_table = 'Team'

class TeamSummary(models.Model):
    team_sum_id = models.TextField(db_column='Team_Sum_Id', primary_key=True, blank=True, null=False)
    vote_average = models.FloatField(db_column='Vote_Average', blank=True, null=True)
    progress_trend = models.TextField(db_column='Progress_Trend', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='Team_Id', blank=True, null=True, related_name='team_summaries')
    record = models.ForeignKey(HealthRecord, on_delete=models.CASCADE, db_column='Record_Id', blank=True, null=True, related_name='team_summaries')

    class Meta:
        managed = False
        db_table = 'Team_Summary'

class User(models.Model):
    user_id = models.TextField(db_column='User_Id', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')
    email = models.TextField(db_column='Email')
    username = models.TextField(db_column='Username', blank=True, null=True)
    password = models.TextField(db_column='Password', blank=True, null=True)
    role = models.TextField(db_column='Role')
    admin = models.ForeignKey(Administrator, on_delete=models.CASCADE, db_column='Admin_Id', blank=True, null=True, related_name='users')
    session_id = models.IntegerField(db_column='Session_Id', unique=True, blank=True, null=True)
    session_duration = models.DurationField(db_column='Session_Duration', blank=True, null=True)
    session_date = models.DateField(db_column='Session_Date', blank=True, null=True)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, db_column='Badge_Id', blank=True, null=True, related_name='users')
    view_profile = models.TextField(db_column='View_Profile', blank=True, null=True)
    profile_picture = models.BinaryField(db_column='Profile_Picture', blank=True, null=True)
    login_error_times = models.IntegerField(db_column='Login_Error_Times', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_Id', primary_key=True, blank=True, null=False)
    vote_value = models.IntegerField(
        db_column='Vote_Value', 
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
        managed = False
        db_table = 'Vote'
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
