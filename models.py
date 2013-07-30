from django.db import models
from mezzanine.core.models import RichTextField
from mezzanine.core.fields import FileField
from django.contrib.auth.models import User


class UserResume(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=50)
	short_description = RichTextField()
	photo = FileField(upload_to="user_resume")

	def __unicode__(self):
		return self.user.username + "'s resume"



class CareerHistory(models.Model):
	resume = models.ForeignKey(UserResume)
	name = models.CharField(max_length=50)
	from_date = models.DateField()
	to_date = models.DateField(null=True, blank=True)
	description = RichTextField()
	link = models.URLField(blank=True)
	logo = FileField(upload_to="user_resume", blank=True)

	def __unicode__(self):
		return self.name


class SkillCategory(models.Model):
	resume = models.ForeignKey(UserResume)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Skill(models.Model):
	resume = models.ForeignKey(UserResume)
	name = models.CharField(max_length=100)
	link = models.URLField(blank=True)
	category = models.ForeignKey(SkillCategory)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	resume = models.ForeignKey(UserResume)
	title = models.CharField(max_length=100)
	description = RichTextField()
	link = models.URLField(blank=True)
	image = FileField(upload_to="user_resume")

	def __unicode__(self):
		return self.title

class School(models.Model):
	resume = models.ForeignKey(UserResume)
	title = models.CharField(max_length=100)
	qualification_attained = models.CharField(max_length=100)
	year_started = models.DateField()
	year_completed = models.DateField(blank=True)

	def __unicode__(self):
		return self.title






