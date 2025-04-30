from django.db import models


class CompanyInfo(models.Model):
    phone = models.CharField('Телефон', max_length=20)
    address = models.CharField('Адрес', max_length=255)
    work_time = models.CharField('Режим работы', max_length=255)
    email = models.EmailField('Email', max_length=255) 
    whatsapp = models.CharField('Whatsapp', max_length=255)
    about_us = models.TextField('О нас')
    why_it_is_cheaper_to_repair = models.TextField('Почему выгоднее чинить')

    def __str__(self):
        return 'Информация о компании'

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    @classmethod
    def get_instance(cls) -> "CompanyInfo":
        instance, created = cls.objects.get_or_create(id=1)
        return instance


    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class CompanyStat(models.Model):
    number = models.CharField('Метрика', max_length=255)
    label = models.CharField('Подпись', max_length=255) 
    small_label = models.CharField('Подпись снизу', max_length=255)

    def __str__(self):
        return f'{self.number} {self.label} {self.small_label}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Service(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', upload_to='services/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class Work(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', upload_to='works/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Request(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=18)

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'



class PersonalDataPolicy(models.Model):
    file = models.FileField('Файл', upload_to='personal_data_policy/', null=True, blank=True)

    class Meta:
        verbose_name = 'Обработка персональных данных'
        verbose_name_plural = 'Обработка персональных данных'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod 
    def get_instance(cls) -> "PersonalDataPolicy":
        instance, created = cls.objects.get_or_create(id=1)
        return instance

    def __str__(self) -> str:
        return 'Обработка персональных данных'


class PrivacyPolicy(models.Model): 
    file = models.FileField('Файл', upload_to='privacy_policy/', null=True, blank=True)

    class Meta: 
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls) -> "PrivacyPolicy":
        instance, created = cls.objects.get_or_create(id=1)
        return instance
    
    def __str__(self) -> str: 
        return 'Политика конфиденциальности'