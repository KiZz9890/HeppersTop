import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для удобства в которой хранится наш токен от группы

token="5fa6dc75156247a81a546ffdea12329c4726c3488139cc38a35d6d0af4596d30cae26277fd86b833ed1e6" 


# Подключаем токен и longpoll
bh = vk_api.VkApi(token = "5fa6dc75156247a81a546ffdea12329c4726c3488139cc38a35d6d0af4596d30cae26277fd86b833ed1e6")
give = bh.get_api()
longpoll = VkLongPoll(bh)

# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы наш бот не слышал и не отвечал на самого себя
       if event.to_me:
        # Для того чтобы бот читал все с маленьких букв  
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id
    
    # Доисторическая логика общения на ифах
    # Перед вами структура сообщений на которые бот сможет ответить, elif можно создавать сколько угодно, if и else же могут быть только 1 в данной ситуации.
    # if - если, else - иначе(значит бот получил сообщение на которое не вызвана наша функция для ответа)

          if message in ('привет','начать','хай'):
            blasthack(id, 'Привет! Что бы начать пользоваться ботом напиши "Помощь".') 

          elif message == 'как дела?':
              blasthack(id, 'Хорошо, а твои как?' )
          
          elif message == 'помощь':
              blasthack(id, 'Бот в разработке. Дата окончания работы над ботом 16.02.2022 00:00 по МСК если хочешь узнать кто его пишет напиши команду "Разработчик".' )
               
          elif message == 'хуй':
              blasthack(id, 'пошел нахуй мразь ебанная, кидал твоих родителей в канаву' )
              
          elif message == 'разработчик':
              blasthack(id, 'Бот разрабатывается @senior_lolipop помогает ему в разработке великий человек @ne_pingui_menya_lox' )
         
          else:
             blasthack(id, 'Я вас не понимаю! :( напишите "помощь"')

             
