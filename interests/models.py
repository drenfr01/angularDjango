from django.db import models

class Subject(models.Model):
  subject_name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.subject_name

class Book(models.Model):
  title = models.CharField(max_length=300)
  date_read = models.DateTimeField()
  subject = models.ManyToManyField(Subject, through='Membership')

  def __unicode__(self):
    return self.title

class Membership(models.Model):
  subject = models.ForeignKey(Subject)
  book = models.ForeignKey(Book)
  reason = models.CharField(max_length=500)

  def __unicode__(self):
    return self.reason
