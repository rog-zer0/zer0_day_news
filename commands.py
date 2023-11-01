# Создание двух пользователей
user1 = User.objects.create_user(username='Biba', password='12345')
user2 = User.objects.create_user(username='Boba', password='54321')

# Создание двух объектов модели Author, связанных с пользователями
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Создание 4 категорий в модели Category
Category.objects.bulk_create([
    Category(name='В мире'),
    Category(name='Войти в IT'),
    Category(name='Спорт'),
    Category(name='Технологии'),
])

# Создание 2 статей и 1 новости
article1 = Article.objects.create(title='Как я с курсами связался', author=author1)
article2 = Article.objects.create(title='Нейронка и кодинг', author=author2)
news1 = News.objects.create(title='Chat_gpt захватил PornHub', author=author1)

# Присвоение категорий статьям и новостям
article1.categories.add(Category.objects.get(name='Войти в IT'), Category.objects.get(name='Технологии'))
article2.categories.add(Category.objects.get(name='Войти в IT'))
news1.categories.add(Category.objects.get(name='Технологии'))

# Создание 4 комментариев к разным объектам модели Post
comment1 = Comment.objects.create(post=article1, text='Автор жжет!')
comment2 = Comment.objects.create(post=article2, text='фантазия кончается')
comment3 = Comment.objects.create(post=news1, text='RIP PornHub')
comment4 = Comment.objects.create(post=comment1, text='AI захватила все')

# Изменение рейтингов с помощью функций like() и dislike()
article1.like()
article1.dislike()
article2.like()
article2.dislike()
news1.like()
news1.dislike()
comment1.like()
comment1.dislike()
comment2.like()
comment2.dislike()
comment3.like()
comment3.dislike()
comment4.like()
comment4.dislike()

# Обновление рейтингов пользователей
user1.update_rating()
user2.update_rating()

# Получение лучшего пользователя (на основе рейтинга)
best_user = User.objects.order_by('-rating').first()

# Получение лучшей статьи на основе лайков/дислайков
best_article = Article.objects.filter(post__like=True).order_by('-date_added').first()

# Получение всех комментариев для конкретной статьи
comments = Comment.objects.filter(post=best_article)

# Вывод результатов
print(f"Лучший пользователь: {best_user.username}, Рейтинг: {best_user.rating}")
print(f"Лучшая статья: {best_article.title}, Автор: {best_article.author.user.username}, Рейтинг: {best_article.rating}, Превью: {best_article.preview}")
print("Все комментарии:")
for comment in comments:
    print(f"Дата: {comment.date}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}")