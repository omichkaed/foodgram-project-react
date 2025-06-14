# Generated by Django 3.2 on 2023-10-31 20:13

import colorfield.fields
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название ингредиента', max_length=200, verbose_name='Название')),
                ('measurement_unit', models.CharField(help_text='Выберите единицу измерения', max_length=200, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название', max_length=200, unique=True, verbose_name='Название')),
                ('color', colorfield.fields.ColorField(default='#FF0000', help_text='Выберите цвет, нажмите на цветной квадрат', image_field=None, max_length=25, samples=(('#FFFFFF', 'white'), ('#000000', 'black')), verbose_name='Цвет')),
                ('slug', models.SlugField(help_text='Укажите слаг', max_length=200, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, help_text='Укажите логин', max_length=200, unique=True, verbose_name='Логин')),
                ('password', models.CharField(help_text='Укажите пароль', max_length=200, verbose_name='Пароль')),
                ('first_name', models.CharField(blank=True, help_text='Укажите имя', max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Укажите фамилию', max_length=200, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Укажите email', max_length=200, unique=True, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('username',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
