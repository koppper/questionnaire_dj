from django.db import models

from .questionnaire import Questionnaire
from django.contrib.auth.models import User
from utils.models import AbstractUUID, AbstractTimeTracker


class UserQuestionnaire(AbstractUUID, AbstractTimeTracker):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор варианта вопросника'
    )
    right_answers = models.PositiveIntegerField(
        default=0,
        verbose_name='Правильные ответы'
    )
    wrong_answers = models.PositiveIntegerField(
        default=0,
        verbose_name='Неправильные ответы'
    )
    not_answered = models.PositiveIntegerField(
        default=0,
        verbose_name='Неотвеченные ответы'
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name='Вопросник'
    )

    class Meta:
        verbose_name = 'UserQuestionnaire'
        verbose_name_plural = 'UserQuestionnaires'
        order_with_respect_to = 'author'
