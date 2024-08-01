from django.db import models, connection
from django.db.utils import DatabaseError

# Create your models here.
class Category:
    def all():
        # Step2 SQL語法
        sql = 'SELECT * FROM category'
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                tuple_categories = cursor.fetchall()
                print(tuple_categories)
                # 將 tuple 轉成 list
                categories = [{'id': category[0],'name': category[1]} for category in tuple_categories]
                print(categories)
                return categories
        except DatabaseError as e:
            print(f'讀取資料錯誤：{ e }')
            return None
        
    def single():
        pass
    def create():
        pass
    def update():
        pass
    def delete():
        pass
