from django.db import models
import jdatetime
import datetime
class Group(models.Model):
    name = models.CharField(max_length=100 , verbose_name='Group Name')
    standardEnter = models.TimeField()
    standardExit = models.TimeField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'گروه کاربری'
        verbose_name_plural = "گروه های کاربری"

class Person(models.Model):
    name = models.CharField(verbose_name='Full Name' , max_length=100)
    group = models.ForeignKey(Group,on_delete=models.SET(None))
    isIn = models.BooleanField(verbose_name='Is he in building ? ' , default=False)
    lastStatusChangeTime = models.TimeField(verbose_name="آخرین ساعت تغییر" , blank= True , null=True)

    def __str__(self):
        return str(self.id) + "-" + self.name
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = "کاربران"

class Timing(models.Model):
    TYPE = [(1 , 'ورود' ), (0 , 'خروج')]
    person = models.ForeignKey(Person , verbose_name='User' , on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE)
    date = models.DateField(default=datetime.datetime.now().date())
    time = models.TimeField(default=datetime.datetime.now().time())

    @property
    def persianDate(self):
        return jdatetime.datetime.fromgregorian(date=self.date).strftime("%Y/%m/%d")
    @property
    def formatedTime(self):
        return self.time.strftime("%H:%M")

    @property
    def operation(self):
        if self.type:
            return "ورود"
        else:
            return "خروج"

    def __str__(self):
        date = jdatetime.datetime.fromgregorian(datetime= self.date)
        if self.type:
            type = "ورود"
        else:
            type = "خروج"
        return date.strftime('%Y/%m/%d') + " - " + self.person.name + " : " + type

    class Meta:
        verbose_name = 'رکورد'
        verbose_name_plural = "رکورد ها"
