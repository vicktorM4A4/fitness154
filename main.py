import os
import random

from setup import bot, logger
from webhook import app
import markups as nav
# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(message.chat.id,'<b>Hello! This is a telegram bot template written by <a href="https://github.com/vicktorM4A4">zxvizi</a></b>',parse_mode='html',reply_markup = nav.mainMenu)
        
        
        
    


@bot.message_handler()
async def bot_message(message):
    if message.text == 'Личный кабинет':
        await bot.send_message(message.from_user.id, 'https://olimpiyasport.ru/#fitnesskit_personal',reply_markup=nav.mainMenu)

    elif message.text == 'Купить абонемент':
        await bot.send_message(message.from_user.id, 'Купить абонемент',)

    elif message.text == 'Наши услуги':
        await bot.send_message(message.from_user.id, 'Здесь услуги с сайта выведутся',)

    elif message.text == 'Записатсья на тренировку':
        await bot.send_message(message.from_user.id, 'линк с базой на тренировку',)

    elif message.text == 'Другое':
        await bot.send_message(message.from_user.id, 'Наши контакты:',reply_markup=nav.otherMenu)

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, ' Возврат ',reply_markup=nav.mainMenu)
    elif  message.text =='Информация':
        await bot.send_message(message.from_user.id, ' здесь высрется информация ')
    elif  message.text =='Адрес':
        await bot.send_message(message.from_user.id, ' здесь высрется Адрес ')
            


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()
