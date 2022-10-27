from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class Course(models.Model):
    MONTHS = [
        ('січня', 'січня'),
        ('лютого', 'лютого'),
        ('березня', 'березня'),
        ('квітня', 'квітня'),
        ('травня', 'травня'),
        ('червня', 'червня'),
        ('липня', 'липня'),
        ('серпня', 'серпня'),
        ('вересня', 'вересня'),
        ('жовтня', 'жовтня'),
        ('листопада', 'листопада'),
        ('грудня', 'грудня')
    ]
    title = models.CharField("Заголовок курса", max_length=200)
    language = models.CharField("Язык программирования", max_length=50)
    direction = models.CharField("Направление курса", max_length=100)
    certification = models.CharField("Информация об сертификате", max_length=250)
    description = models.CharField("Описание курса", max_length=10000)
    ua_price = models.CharField("Стоимость курса грн.", max_length=20)
    rus_price = models.CharField("Стоимость курса рубл.", max_length=20)
    usa_price = models.CharField("Стоимость курса дол.", max_length=20)
    hours = models.IntegerField("Сколько часов курс займёт")
    lections = models.IntegerField("Количество лекций в курсе")
    skill = models.CharField("Необходимый уровень знаний", max_length=50)
    start_month = models.CharField("Месяц начала курса", max_length=10, choices=MONTHS)
    start_day = models.IntegerField("День начала курса",
                                    validators=[MinValueValidator(0), MaxValueValidator(31)])
    end_month = models.CharField("Конец курса", max_length=10, choices=MONTHS)
    end_day = models.IntegerField("День начала курса",
                                  validators=[MinValueValidator(0), MaxValueValidator(31)])

    def __str__(self):
        return self.title

class Request(models.Model):
    TIME_AVAILABLE = [
        ('9:00-11:00', '9:00-11:00'),
        ('11:00-13:00', '11:00-13:00'),
        ('13:00-15:00', '13:00-15:00'),
        ('15:00-17:00', '15:00-17:00'),
        ('17:00-19:00', '17:00-19:00'),
        ('19:00-21:00', '19:00-21:00'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField(region="UA")
    email = models.EmailField(unique=True, max_length=150)
    time = models.CharField(max_length=15,
                            choices=TIME_AVAILABLE,
                            blank=True,
                            null=True)
    course = models.ForeignKey(Course, related_name="requests",
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)



