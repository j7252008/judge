from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Question(models.Model):
	qid=models.IntegerField();
	qname=models.CharField(max_length=100)
	qdescription=models.CharField(max_length=300)

	def __str__(self):
		return self.qname

# class ResloveStat(models.Model):
# 	rid=models.IntegerField(User)
# 	rqid=models.IntegerField();
# 	rstate=models.CharField(max_length=20)

# 	def __unicode__(self):
# 		return self.rid