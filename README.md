# Тестовое задание для интернет-бизнес-системы


Задание состоит в том, чтобы создать метод который возвращает набор данных в json-формате

Результат работы [выглядит следующим образом](https://ibs-test-task.onrender.com/docs) и был развернут в сервисе render

Решение задания состоит из 2-х частей:

- Создание базы данных для хранения информации 
- Написание самого метода

Хотел бы разобрать каждую часть отдельно.

### База данных

База данных создана с помощью модуля `sqlite3` и состоит из 2-х таблиц: 

- workers
- posts

Ниже представлен код создания этих таблиц

```sql
CREATE TABLE workers (
  id INTEGER PRIMARY KEY,
  name TEXT,
  username TEXT,
  job TEXT,
  photo TEXT
);

CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  FOREIGN KEY (worker_id) REFERENCES workers(id),
  title TEXT,
  description TEXT,
  date TEXT,
);
```

После чего эти таблицы были заполнены тестовыми данными и выглядят следующим образом:
#### Таблица workers

id|name|username|job|photo
---: | :---: | :---: | :---: | :---:
1|Петрунин|Ян|Азбука|https://234
2|Иванов|Сергей|Дизайнер|https://...
3|Тильтевский|Виталий|Бездельник|https://...

#### Таблица posts

id | worker_id | title | description | date
---: | ---: | :---: | :---: | ---
1|1|Заголовок поста|Ян|2023-04-07T15:16:10+00:00
2|1|Ян поста|Lorem ipsum|2023-04-07T15:16:10+00:00
3|1|Заголовок Ян|Lorem ipsum dolor sit amet, consectetur adipiscing elit|2023-04-07T15:16:10+00:00
4|2|Заголовок поста|Lorem|2023-04-07T15:16:10+00:00
5|2|Заголовок поста|Lorem ipsum |2023-04-07T15:16:10+00:00
6|2|Заголовок поста|Lorem ipsum dolor sit amet, consectetur adipiscing elit|2023-04-07T15:16:10+00:00
7|3|Стас поста|Lorem|2023-04-07T15:16:10+00:00
8|3|Заголовок поста|dolor ipsum |2023-04-07T15:16:10+00:00
9|3|поста| ipsum dolor sit amet, consectetur adipiscing elit|2023-04-07T15:16:10+00:00