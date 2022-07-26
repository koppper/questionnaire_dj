# Generated by Django 4.0.6 on 2022-07-24 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.date_model.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='utils.date_model.updated_at')),
                ('title', models.CharField(max_length=255, verbose_name='Название вопроса')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.date_model.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='utils.date_model.updated_at')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание вопросника')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Вопросник',
                'verbose_name_plural': 'Вопросники',
            },
        ),
        migrations.CreateModel(
            name='UserQuestionnaire',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.date_model.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='utils.date_model.updated_at')),
                ('right_answers', models.PositiveIntegerField(default=0, verbose_name='Правильные ответы')),
                ('wrong_answers', models.PositiveIntegerField(default=0, verbose_name='Неправильные ответы')),
                ('not_answered', models.PositiveIntegerField(default=0, verbose_name='Неотвеченные ответы')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор варианта вопросника')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.questionnaire', verbose_name='Вопросник')),
            ],
            options={
                'verbose_name': 'UserQuestionnaire',
                'verbose_name_plural': 'UserQuestionnaires',
                'order_with_respect_to': 'author',
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.date_model.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='utils.date_model.updated_at')),
                ('right', models.BooleanField(default=False, verbose_name='Правильный ответ пользователя')),
                ('not_answered', models.BooleanField(default=False, verbose_name='Не отвеченный')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question', verbose_name='Вопрос')),
                ('user_questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.userquestionnaire', verbose_name='Вариант пользователя')),
            ],
            options={
                'verbose_name': 'UserAnswer',
                'verbose_name_plural': 'UserAnswers',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.questionnaire', verbose_name='Номер вопросника'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='question',
            order_with_respect_to='questionnaire',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='utils.base_model.uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='utils.date_model.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='utils.date_model.updated_at')),
                ('text', models.CharField(max_length=1000, verbose_name='Ответ')),
                ('right', models.BooleanField(default=False, verbose_name='Правильно')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question', verbose_name='Номер вопроса')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'order_with_respect_to': 'question',
            },
        ),
    ]
