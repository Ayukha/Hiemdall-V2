from django.db import models

# Create your models here.
class labStatus(models.Model):
	Date = models.DateTimeField(auto_now=True)
	Day_no = models.AutoField()

	# storing choices
	LAB_HELD = 'yes'
	LAN_NOT_HELD = 'no'

	Status_choice = (
		(LAB_HELD,'Lab held'),
		(LAB_NOT_HELD,'Lab not held'),
	)

	Status = models.CharField(
		max_length=3,
		choices=Status_choice,
		default=LAB_HELD,
	)

	Message = models.TextField(blank=True,default='')


class daildAttendance(models.Model):
	#User = models.ForiegnKey(user)
	#status choices
	PRESENT = 'p'
	ABSENT = 'a'
	ON_LEAVE = 'l'

	Status_choice = (
		(PRESENT,'Present'),
		(ABSENT,'Absent'),
		(ON_LEAVE,'On leave'),
	)

	Status = models.CharField(
		max_length=1,
		choices=Status_choice,
		)

	Reason = models.TextField(blank=True)

	#Informed = models.


class userAttendance(models.Model):
	#User = models.onetooneField()
	Present_days = models.IntegerField()
	Absent_days = models.IntegerField()
	Consecutive_absent = models.IntegerField()





