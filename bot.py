from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#  ------main menu-------- главное меню
btnHelp = KeyboardButton('🛠 Помощь')
btnFaq = KeyboardButton('⁉ Частые вопросы')
btnRemLes = KeyboardButton('🔔 Напомнить о занятии')
btnRemDead = KeyboardButton('🔔 Напомнить о дедлайне')
btnTestCheck = KeyboardButton('🧩 Тесты')
btnOther = KeyboardButton('Другое ➡')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFaq, btnHelp, btnRemLes, btnRemDead, btnTestCheck, btnOther)
#  добавление кнопок выше в Главное меню

#  ----other menu ---- подМеню
btnEduRes = KeyboardButton('🎓 Успеваемость')
btnEduMat = KeyboardButton('📚️ Учебный материал')
btnCongStu = KeyboardButton('🏆 Топ')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEduRes, btnCongStu, btnEduMat)

# кнопка возврата в Главное меню
btnMain = KeyboardButton('⬅ Главное меню')

# ----------- end menu ----------------- конец меню

