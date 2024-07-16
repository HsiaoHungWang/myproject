from django.db import models, connection

# Create your models here.
class Sakila:
    def countries():
        with connection.cursor() as cursor:
            cursor.execute('SELECT country_id, country FROM country')
            countries = cursor.fetchall()
            return countries
    
    def categories():
        with connection.cursor() as cursor:
            cursor.execute('SELECT category_id, name FROM category')
            categories = cursor.fetchall()
            return categories

