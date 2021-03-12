from django.db import models

class Contributors(models.Models):
	user_id = models.IntegerField()

class Projects(models.Models):
	project_id = models
	title = models.CharField()
	description = models.CharField()
	type = models.CharField()
	author_user_id = models.ForeignKey()

class Issues(models.Models)

class Comments(models.Models):
	comment_id
		