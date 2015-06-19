from django.db import models

class Article(models.Model): 
  content = models.TextField()
  recorded = models.DateTimeField('date record created')

class Binding(models.Model):
  referenced_article = models.ForeignKey(Article)
  name = models.CharField(max_length=20)
  recorded = models.DateTimeField('date record created')
  

