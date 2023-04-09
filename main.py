import sqlite3
import json
import fastapi
import fastapi.encoders

app = fastapi.FastAPI(
    title = 'Test task'
)

def get_data():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT workers.*, json_group_array(json_object(
            'title', posts.title,
            'description', posts.description,
            'date', posts.date
        )) AS posts_info
        FROM workers
        LEFT JOIN posts ON workers.id = posts.worker_id
        GROUP BY workers.id''')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({'id': row[0], 'name': row[1], 'username': row[2], 'job': row[3], 'photo': row[4], 'posts' : json.loads(row[5])})
    conn.close()
    return data

@app.get('/')
def get_info(limit_users: int = fastapi.Query(default=None, description='Лимит пользователей'), 
             limit_posts: int = fastapi.Query(default=None, description='Лимит постов для каждого пользователя'),
             sort_by: str = fastapi.Query(default=None, description='Сортировка вывода по ключу'),
             reversed: bool = fastapi.Query(default=False, description='Сортировка по убыванию')):
    data = get_data()
    if limit_posts != None:
        for user in data:
            user["posts"] = user["posts"][:limit_posts]
    if limit_users != None:
        data = data[:limit_users]
    if sort_by != None:
        try:
            data = sorted(data, key=lambda x: x[sort_by])
        except KeyError:
            return 'Ключ не найден'
    if reversed:
        data = data[::-1]
    return data
    # order = 1
    # if reversed:
    #     order = -1
    # if sort_by != None:
    #     if sort_by == 'posts':
    #         data[:limit_users] = sorted(data[:limit_users], key=lambda x: len(x))
    #     else:
    #         data[:limit_users] = sorted(data[:limit_users], key=lambda x: x[sort_by])
    # return fastapi.encoders.jsonable_encoder(data[:limit_users])[::order]



# @app.get('/users')
# def get_users(limit: int = fastapi.Query(default=None, description='Лимит пользователей для вывода'), 
#              sort_by: str = fastapi.Query(default=None, description='Сортировка вывода по ключу'),
#              reversed: bool = fastapi.Query(default=False, description='Сортировка по убыванию')):
#     data = get_json()
#     order = 1
#     if reversed:
#         order = -1
#     if sort_by != None:
#         data[:limit] = sorted(data[:limit], key=lambda x: x[sort_by])
#     return fastapi.encoders.jsonable_encoder(data[:limit], exclude={'posts'})[::order]

# @app.get('/posts')
# def get_posts(limit: int = fastapi.Query(default=None, description='Лимит пользователей для вывода'), 
#              reversed: bool = fastapi.Query(default=False, description='Сортировка по убыванию')): 
#     data = get_json()
#     order = 1
#     if reversed:
#         order = -1
#     return fastapi.encoders.jsonable_encoder(data[:limit], include={'id', 'posts'})[::order]