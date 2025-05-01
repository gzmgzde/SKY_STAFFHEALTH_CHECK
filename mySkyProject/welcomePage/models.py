from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# This is the model for the Administrator table
class Administrator(models.Model):
    admin_id = models.TextField(db_column='Admin_Id', primary_key=True, blank=True, null=False)
    email = models.TextField(db_column='Email', unique=True, blank=True, null=True)
    password = models.TextField(db_column='Password', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Administrator'


# This is the model for the Department table
class Department(models.Model):
    department_id = models.TextField(db_column='Department_Id', primary_key=True, blank=True, null=False)
    department_name = models.TextField(db_column='Department_Name')

    class Meta:
        managed = True
        db_table = 'Department'

    def __str__(self):
        return self.department_name

# This is the model for the Team table
class Team(models.Model):
    team_id = models.TextField(db_column='Team_Id', primary_key=True, blank=True, null=False)
    team_name = models.TextField(db_column='Team_Name')
    department = models.ForeignKey(
    Department, 
    on_delete=models.CASCADE, 
    db_column='Depart_Id',
    blank=True, 
    null= True,   
    related_name='teams'
)

    class Meta:
        managed = True
        db_table = 'Team'

    def __str__(self):
        return self.team_name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# This is the model for the User table
class User(AbstractBaseUser):
    user_id = models.TextField(db_column='User_Id', primary_key=True, blank=True, null=False)
    name = models.TextField(db_column='Name')
    email = models.TextField(db_column='Email', unique=True, blank=True, null=True)
    password = models.TextField(db_column='Password', blank=True, null=True)
    role = models.CharField(db_column='Role', max_length=50, blank=True, null=True)
    admin = models.ForeignKey(Administrator, on_delete=models.SET_NULL, db_column='admin_id', blank=True, null=True, related_name='users')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, db_column='Depart_Id', blank=True, null=True, related_name='users')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, db_column='Team_Id', blank=True, null=True, related_name='users')


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'User'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True