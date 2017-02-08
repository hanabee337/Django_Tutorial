import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        '''
        최근에 발생된 Question 메소드인지 판단해주는 메서드
        :return: Boolean
        '''
        # 자신의 발생일자 >= 현재시각 - 하루만큼의 시간
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name="Question Title")
    c_text = models.CharField(max_length=200, verbose_name="Question Text")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text
