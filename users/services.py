from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

# postni olish
def get_posts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM add_page_annoncements""")
        posts = dictfetchall(cursor)
        return posts
# imagesni olish 
def get_image():  
    get = get_posts()
    imgs = []
    for i in get:
        imgs.append(i['image'])
    return imgs
