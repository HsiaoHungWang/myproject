from django.db import models, connection

# Create your models here.
class Sakila:
    def countries():
        with connection.cursor() as cursor:
            cursor.execute('SELECT country_id, country FROM country')
            countries = cursor.fetchall()
            return countries

