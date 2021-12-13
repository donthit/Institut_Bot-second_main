import logging
import asyncio
from aiogram.utils.exceptions import BotBlocked
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher
from os import getenv
from sys import exit
import bot as nav
import Responses as R
import time

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

print("PROGRAM START")
# пример обработчика ошибки


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


@dp.message_handler(commands="start")  # новый обработчик
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await message.reply("\t Здравствуй!🤖 Бот для учебы, вот список команд:"
                        " \n /start - начало работы \n /help - 🛠 помощь \n /faq - ⁉ часто задаваемые вопросы \n"
                        " /remind-lesson - 🔔 напомнить о занятии \n /remind-deadline - 🔔 напомнить о дедлайне \n "
                        "/education-result - 🎓 успеваемость\n"
                        " /education-material - 📚️ учебный материал \n"
                        " /test-check - 🧩 тесты для самоподготовки\n"
                        " /congrats-student -  🏆 топ учащихся\n", reply_markup=nav.mainMenu)


@dp.message_handler(commands="help")  #  помощь
async def cmd_test1(message: types.Message):
    await message.reply("help is working")


@dp.message_handler(commands="faq")  # типичные вопросы
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await message.reply("faq is working")


@dp.message_handler(commands="remind-lesson")  # напомнить о занятии
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await message.reply("remind-lesson is working")


@dp.message_handler(commands="remind-deadline")  # напомнить о дедлайне
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await message.reply("remind-deadline  is working")


@dp.message_handler(commands="test-check")   # тесты для самопроверки
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await message.reply("test-check is working")


@dp.message_handler(commands="education-result")   # об успеваемости
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await message.reply("education-result is working")


@dp.message_handler(commands="education-material")  # учебный материал
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await message.reply("education-material is working")


@dp.message_handler(commands="congrats-student")  # поздравление если ты харош
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await message.reply("congrats-student is working")


@dp.message_handler()  #пока что попытки не обращайте внимания
async def cmd_test1(message: types.Message):
    if message.text == '🛠 Помощь':  #
        await message.reply("помощь")

    elif message.text == '⁉ Частые вопросы':  #
        await message.reply("частые вопросы")

    elif message.text == '🔔 Напомнить о занятии':  #
        await message.reply("напомнить о занятии")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)



