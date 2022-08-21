# Generated by Django 3.2.7 on 2021-09-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('importance', models.CharField(choices=[('primary', 'important'), ('secondary', 'not important'), ('success', 'very important'), ('danger', 'urgent'), ('warning', 'temporary'), ('info', 'moderate'), ('dark', 'least important')], default='info', max_length=100)),
                ('code', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeblog.genre')),
            ],
        ),
    ]