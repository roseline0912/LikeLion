import datetime     #datetime : python 표준 모듈
from django.utils import timezone       #django.utils.timezone : django 시간대 관련 유틸리티

from django.db import models



# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published') #사람이 읽기 좋은 형식의 필드 이름 지정
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
        
