from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMainRuss = KeyboardButton("Главное меню")
btnMainTjk = KeyboardButton("Менюи асосӣ️")
btnMainEng = KeyboardButton("Main menu")
mainMenuuRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMainRuss)
mainMenuuEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMainEng)
mainMenuuTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMainTjk)

# --- Main Menu ---
btnPlaceRuss = KeyboardButton("Посетить популярные места 📍")
btnPlaceEng = KeyboardButton("Visit popular places 📍")
btnPlaceTjk = KeyboardButton("Ба ҷойҳои машҳур сафар кунед 📍")
btnInfoRuss = KeyboardButton("Информация о боте")
btnInfoTjk = KeyboardButton("Маълумоти бот")
btnInfoEng = KeyboardButton("Information about bot")
btnFoodEng = KeyboardButton("National food 🍗")
btnFoodRuss = KeyboardButton("Национальная еда 🍗")
btnFoodTjk = KeyboardButton("Хӯроки миллӣ 🍗")
btnLangRuss = KeyboardButton("Изменить язык 🇹🇯🇺🇸")
btnLangEng = KeyboardButton("Change the language 🇷🇺🇹🇯")
btnLangTjk = KeyboardButton("Забонро иваз кунед 🇺🇸🇷🇺")
btnHelpRuss = KeyboardButton("Помочь проекту 💵")
btnHelpEng = KeyboardButton("Help to project 💵")
btnHelpTjk = KeyboardButton("Лойиҳага ёрдам беринг 💵")
mainMenuRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPlaceRuss, btnInfoRuss, btnFoodRuss, btnLangRuss, btnHelpRuss)
mainMenuTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPlaceTjk, btnInfoTjk, btnFoodTjk, btnLangTjk, btnHelpTjk)
mainMenuEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPlaceEng, btnInfoEng, btnFoodEng, btnLangEng, btnHelpEng)

# --- Places ---
btnPmkRuss = KeyboardButton("Популярные достопремечательности 🏰")
btnPmkEng = KeyboardButton("Popular Attractions 🏰")
btnPmkTjk = KeyboardButton("Ҷойҳои машҳур 🏰")
btnProRuss = KeyboardButton("Прогулка 🚶")
btnProEng = KeyboardButton("Walk 🚶")
btnProTjk = KeyboardButton("Пиёда рафтан 🚶")
btnPokRuss = KeyboardButton("Покупки 🛍 ")
btnPokEng = KeyboardButton("Shopping 🛍")
btnPokTjk = KeyboardButton("Харид 🛍")
placesRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPmkRuss, btnProRuss, btnPokRuss, btnMainRuss)
placesEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPmkEng, btnProEng, btnPokEng, btnMainEng)
placesTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPmkTjk, btnProTjk, btnPokTjk, btnMainTjk)

# --- City ---
btnDushRuss = KeyboardButton("Душанбе 🏙")
btnHudRuss = KeyboardButton("Худжанд 🏙")
btnKulRuss = KeyboardButton("Куляб 🏙")
btnDushEng = KeyboardButton("Dushanbe 🌃")
btnHudEng = KeyboardButton("Khujand 🌃")
btnKulEng = KeyboardButton("Kulob 🌃")
btnDushTjk = KeyboardButton("Душанбе 🌆")
btnHudTjk = KeyboardButton("Хучанд 🌆")
btnKulTjk = KeyboardButton("Кулоб 🌆")
cityRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDushRuss, btnHudRuss, btnKulRuss, btnMainRuss)
cityEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDushEng, btnHudEng, btnKulEng, btnMainEng)
cityTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDushTjk, btnHudTjk, btnKulTjk, btnMainTjk)

# --- Language Menu ---
btnRuss = KeyboardButton("Русский 🇷🇺")
btnEng = KeyboardButton("English 🇺🇸")
btnTjk = KeyboardButton("Тоҷикӣ 🇹🇯")
langMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRuss, btnEng, btnTjk)

# --- Restoraunt Menu ---
btnRestorauntEng = KeyboardButton("Where I can eat this food? 🍗")
btnRestorauntRuss = KeyboardButton("Где я смогу поесть эту еду? 🍗")
btnRestorauntTjk = KeyboardButton("Дар куҷо ман метавонам ин хӯрокро бихӯрам? 🍗")
restoMenuTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRestorauntTjk, btnMainTjk)
restoMenuRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRestorauntRuss, btnMainRuss)
restoMenuEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRestorauntEng, btnMainEng)

# --- Taxi menu ---
btnTaxiRuss = KeyboardButton("Как мне добраться туда?")
btnTaxiEng = KeyboardButton("How can I get there?")
btnTaxiTjk = KeyboardButton("Чӣ тавр ман метавонам ба он ҷо расам?")
taxiMenuRuss = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTaxiRuss, btnMainRuss)
taxiMenuTjk = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTaxiTjk, btnMainTjk)
taxiMenuEng = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTaxiEng, btnMainEng)

# --- Other Menu ---
btnInfoEng = KeyboardButton("Information ")
btnInfoRuss = KeyboardButton("Информация")
btnInfoTjk = KeyboardButton("Маълумот")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfoTjk, btnInfoEng, btnInfoRuss)
