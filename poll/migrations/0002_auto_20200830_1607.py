# Generated by Django 3.1 on 2020-08-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Question_text',
            new_name='question_text',
        ),
    ]