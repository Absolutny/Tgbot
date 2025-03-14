# Brawl Stars Telegram Bot
# @Absolutny_bot
Этот Telegram-бот предоставляет информацию о персонажах из игры Brawl Stars. Пользователи могут выбирать бойцов по их редкости и просматривать изображения выбранных персонажей.

## Как работает бот

1. Пользователь отправляет команду `/start`.
2. Бот предлагает выбрать редкость бойца (например, "Начальный", "Редкий", "Сверхредкий" и т.д.).
3. После выбора редкости бот показывает список бойцов.
4. Пользователь выбирает бойца, и бот отправляет его изображение.
5. Кнопка "Назад" позволяет вернуться к выбору редкости.

## Требования для запуска 

### Необходимая библиотека
Для работы бота потребуется следующая библиотека Python:

1. **aiogram 3.17.0** — библиотека для создания Telegram-ботов.  
   - Установка: `pip install aiogram==3.17.0`

#### Дополнительные требования:
- **Python 3.8+** : Убедитесь, что у вас установлена версия Python не ниже 3.8.

## 📝 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий.git
   cd ваш-репозиторий
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Добавьте свой токен в код:
   В файле `bot.py` замените `BOT_TOKEN = 'Og'` на ваш собственный токен, который можно получить у [BotFather](https://core.telegram.org/bots#botfather).

4. Запустите бота:
   ```bash
   python bot.py
   ```
   
## Контакты для обратной связи 
Если у вас есть вопросы или предложения по улучшению бота, свяжитесь с разработчиком через Telegram: @Abdhschba.
