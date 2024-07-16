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
        
    # 根據國家編號讀取城市資料
    def cities(id=1):
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT city_id, city FROM sakila.city WHERE country_id={id}')
            cities = cursor.fetchall()
            return cities


