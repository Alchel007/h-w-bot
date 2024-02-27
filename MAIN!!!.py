import telebot
from telebot import types


bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание")
    btn2 = types.KeyboardButton('Д/З')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "выберите раздел", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Д/З':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("задать д/з")
        btn2 = types.KeyboardButton('посмотреть д/з')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "выберите раздел", reply_markup=markup)

    elif message.text == 'задать д/з':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Математика')
        btn2 = types.KeyboardButton('Химия')
        btn3 = types.KeyboardButton('Биология')
        btn4 = types.KeyboardButton('Физика')
        btn5 = types.KeyboardButton('Английский язык')
        btn6 = types.KeyboardButton('История')
        btn7 = types.KeyboardButton('География')
        btn8 = types.KeyboardButton('Информатика')
        btn9 = types.KeyboardButton('Обществознание')
        btn10 = types.KeyboardButton('Русский язык')
        btn11 = types.KeyboardButton('Литература')
        btn12 = types.KeyboardButton('Индивидуальный проект')
        btn13 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
        bot.send_message(message.from_user.id, 'Выберите предмет', reply_markup=markup)
# МАТЕША
    elif message.text == 'Математика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Алгебра')
        btn2 = types.KeyboardButton('Геометрия')
        btn3 = types.KeyboardButton('Практикум')
        btn4 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id,
                         'выберите раздел',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Алгебра':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Алг. Профиль')
        btn2 = types.KeyboardButton('Алг. База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Алг. Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.chat.id, 'Отправьте д/з в формате текста')

    elif message.text == 'Алг. База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геометрия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Геом. Профиль')
        btn2 = types.KeyboardButton('Геом. База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геом. Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геом. База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Практикум Профиль')
        btn2 = types.KeyboardButton('Практикум База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')
# МАТЕША
# АНГЛ ЯЗ
    elif message.text == 'Английский язык':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Англ. Профиль')
        btn2 = types.KeyboardButton('Англ. База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Англ. Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Англ. База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')
# АНГЛ ЯЗ
# ОБЩЕСТВО
    elif message.text == 'Обществознание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Общ. Профиль')
        btn2 = types.KeyboardButton('Общ. База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Общ. Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Общ. База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')
# ОБЩЕСТВО
# ИНФОРМАТИКА
    elif message.text == 'Информатика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Инф. Профиль')
        btn2 = types.KeyboardButton('Инф. База')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Инф. Профиль':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Инф. База':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')
# ИНФОРМАТИКА
    elif message.text == 'Химия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Физика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'История':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'География':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Индивидуальный проект':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Литература':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Русский язык':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Отправьте д/з в формате текста',
                         reply_markup=markup, parse_mode='Markdown')



# ОТПРАВКА Д/З



    elif message.text == 'посмотреть д/з':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Математика.')
        btn2 = types.KeyboardButton('Химия.')
        btn3 = types.KeyboardButton('Биология.')
        btn4 = types.KeyboardButton('Физика.')
        btn5 = types.KeyboardButton('Английский язык.')
        btn6 = types.KeyboardButton('История.')
        btn7 = types.KeyboardButton('География.')
        btn8 = types.KeyboardButton('Информатика.')
        btn9 = types.KeyboardButton('Обществознание.')
        btn10 = types.KeyboardButton('Русский язык.')
        btn11 = types.KeyboardButton('Литература.')
        btn12 = types.KeyboardButton('Индивидуальный проект.')
        btn13 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
        bot.send_message(message.from_user.id, 'Выберите предмет', reply_markup=markup)
        # МАТЕША
    elif message.text == 'Математика.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Алгебра.')
        btn2 = types.KeyboardButton('Геометрия.')
        btn3 = types.KeyboardButton('Практикум.')
        btn4 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id,
                         'выберите раздел',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Алгебра.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Алг. Профиль.')
        btn2 = types.KeyboardButton('Алг. База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Алг. Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Алг. База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геометрия.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Геом. Профиль.')
        btn2 = types.KeyboardButton('Геом. База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геом. Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Геом. База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Практикум Профиль.')
        btn2 = types.KeyboardButton('Практикум База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Практикум База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')
        # МАТЕША
        # АНГЛ ЯЗ
    elif message.text == 'Английский язык.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Англ. Профиль.')
        btn2 = types.KeyboardButton('Англ. База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Англ. Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Англ. База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')
        # АНГЛ ЯЗ
        # ОБЩЕСТВО
    elif message.text == 'Обществознание.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Общ. Профиль.')
        btn2 = types.KeyboardButton('Общ. База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Общ. Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Общ. База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')
        # ОБЩЕСТВО
        # ИНФОРМАТИКА
    elif message.text == 'Информатика.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Инф. Профиль.')
        btn2 = types.KeyboardButton('Инф. База.')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'База или профиль?',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Инф. Профиль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Инф. База.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')
        # ИНФОРМАТИКА
    elif message.text == 'Химия.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Физика.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'История.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'География.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Индивидуальный проект.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Литература.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Русский язык.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Д/З:',
                         reply_markup=markup, parse_mode='Markdown')

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Расписание")
        btn2 = types.KeyboardButton('Д/З')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "выберите раздел", reply_markup=markup)

    elif message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Суббота')
        btn7 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'Укажите день недели', reply_markup=markup)

    elif message.text == 'Понедельник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.Физика\n2.Сочинение\n3.Англ. язык\n4.Англ. язык\n5.История/ИКТ\n6.История/ИКТ\n7.Икт/Обществознание",
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Вторник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.История \n2.Химия \n3.Русский язык \n4.Литература \n5.Математика \n6.Математика\n7.Нем/франц",
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Среда':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.Икт/Обществознание\n2.Икт/Обществознание\n3.Физ-ра\n4.Англ. язык\n5.Физика\n6.Практикум по математике\n7.Обществознание/Англ. язык (профиль)",
                         reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Четверг':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.Нем/франц\n2.ОБЖ\n3.Русский язык\n4.Литература\n5.Математика\n6.Математика\n7-8.Физ-ра/3D моделирование",
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Пятница':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.География\n2.Инд.проект\n3.Англ. язык\n4.Обществознание/Англ. язык\n5.Икт/Обществознание\n6.Икт/Обществознание\n7.Физика/Биология",
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Суббота':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('назад')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         "1.История\n2.Биология\n3.Литература\n4.Математика\n5.Математика\n6.Математика\n7.Математика(профиль)",
                         reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Суббота')
        btn7 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'Укажите день недели', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
