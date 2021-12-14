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
                        " /remindlesson - 🔔 напомнить о занятии \n /reminddeadline - 🔔 напомнить о дедлайне \n "
                        "/educationresult - 🎓 успеваемость\n"
                        " /educationmaterial - 📚️ учебный материал \n"
                        " /testcheck - 🧩 тесты для самоподготовки\n"
                        " /congratsstudent -  🏆 топ учащихся\n", reply_markup=nav.mainMenu)

# команды
@dp.message_handler(commands="help")  #  помощь
async def cmd_test1(message: types.Message):
    await helpOut(message)


@dp.message_handler(commands="faq")  # типичные вопросы
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await faqOut(message)


@dp.message_handler(commands="remindlesson")  # напомнить о занятии
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await remlesOut(message)


@dp.message_handler(commands="reminddeadline")  # напомнить о дедлайне
async def cmd_test1(message: types.Message):  # await теперь обязателен
    await remdeadOut(message)


@dp.message_handler(commands="testcheck")   # тесты для самопроверки
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await testcheckOut(message)


@dp.message_handler(commands="educationresult")   # об успеваемости
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await eduresOut(message)


@dp.message_handler(commands="educationmaterial")  # учебный материал
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await edumatOut(message)


@dp.message_handler(commands="congratsstudent")  # поздравление если ты харош
async def cmd_test1(message: types.Message):  # await тeперь обязателен
    await congstuOut(message)


@dp.message_handler()
async def cmd_test1(message: types.Message):
    if message.text == '🛠 Помощь':  #кнопочки, текст внутри message  не трогать
        await helpOut(message)
    elif message.text == '⁉ Частые вопросы':
        await faqOut(message)
    elif message.text == '🧩 Тесты':
        await testcheckOut(message)
    elif message.text == '🔔 Напомнить о занятии':
        await remlesOut(message)
    elif message.text == '🔔 Напомнить о дедлайне':
        await remdeadOut(message)
    elif message.text == '🎓 Успеваемость':
        await eduresOut(message)
    elif message.text == '📚️ Учебный материал':
        await edumatOut(message)
    elif message.text == '🏆 Топ':
        await congstuOut(message)
    elif message.text == 'Другое ➡':
        await message.reply("Другое ➡", reply_markup=nav.otherMenu)
    elif message.text == '⬅ Главное меню':
        await message.reply("⬅ Главное меню", reply_markup=nav.mainMenu)


# чтобы работало и меню и команды
async def helpOut(message):
    await message.reply("help  is working")


async def faqOut(message):
    await message.reply("faq is working")


async def remlesOut(message):
    await message.reply("remind lesson is working")


async def remdeadOut(message):
    await message.reply("remind deadline is working")


async def testcheckOut(message):
    await message.reply("test is working:")


async def eduresOut(message):
    await message.reply("education result is working")


async def edumatOut(message):
    await message.reply("education material is working")


async def congstuOut(message):
    await message.reply("congrats is working")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)



