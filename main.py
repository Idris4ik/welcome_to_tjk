# --- Importing modules ---

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3
import markup as nav
import parser

# --- idk ---
bot = Bot(token="TOP SECRET")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


# --- Command /start, and connecting database ---
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            lang INT
    )""")

    await message.reply("🇷🇺 Привет! Выберите язык. \n\n🇺🇸 Hello! Select the language. \n\n🇹🇯 Салом! Забонро интихоб кунед. \n\n🇺🇿 Salom! Tilni tanlang.", reply_markup=nav.langMenu)

    cursor.execute(f"INSERT INTO users VALUES({message.chat.id}, 0)")
    connection.commit()


# --- Bot ---
@dp.message_handler()
async def process_start_command(message:types.Message):

    # --- Russian ---
    if message.text == "Русский 🇷🇺":
        cursor.execute(f"UPDATE users SET lang == 1 WHERE user_id = {message.chat.id}")
        connection.commit()
        await bot.send_message(message.from_user.id, "Добро пожаловать в Таджикистан! рады что вы посетили наши солнечные края 😊", reply_markup=nav.mainMenuRuss)
    elif message.text == "Национальная еда 🍗":
        await bot.send_photo(message.from_user.id, photo=open("photos/samsa-s-baraninoy.jpg", "rb"), caption="В Таджикистане очень много вкусной национальной еды, такие как: Самса, Курутоб, и т.д", reply_markup=nav.restoMenuRuss)
    elif message.text == "Изменить язык 🇹🇯🇺🇸🇺🇿":
        await message.reply("🇷🇺 Привет! Выберите язык. \n\n🇺🇸 Hello! Select the language. \n\n🇹🇯 Салом! Забонро интихоб кунед. \n\n🇺🇿 Salom! Tilni tanlang.", reply_markup=nav.langMenu)
    elif message.text == "Информация о боте ℹ️":
        await bot.send_message(message.from_user.id, "Данный бот предназначен для туристов которые решили посетить Таджикистан, и узнать о нем побольше. \n\nДанный бот подскажет где можно вкусно поесть национальную или любую другую еду, также поможет вам посетить популярные достопремечетельности Таджикистана, и т.д \n\nЕсли вы заметили в боте ошибку то пожалуйста обратитесть в тех.поддержку @Idrisishe")
    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, "Главное меню", reply_markup=nav.mainMenuRuss)
    elif message.text == "Где я смогу поесть эту еду? 🍗":
        await bot.send_message(message.from_user.id, "В каком городе вы сейчас находитесь?", reply_markup=nav.cityRuss)
    elif message.text == "Душанбе 🏙":
        await bot.send_message(message.from_user.id, "Рестораны с национальной едой в Душанбе (все ссылки указывают на гугл карты) \n\nРесторан Яккачинар: https://goo.gl/maps/HuC9BvUMB1gKdBh66 \n\nРесторан Самандар: https://goo.gl/maps/Dq1Jkhi6SjxTimi5A \n\nРесторан «Рохат»: https://goo.gl/maps/AH63i57jw3n9gQzi8", reply_markup=nav.taxiMenuRuss)
    elif message.text == "Худжанд 🏙":
        await bot.send_message(message.from_user.id, "Рестораны с национальной едой в Худжанде (все ссылки указывают на гугл карты) \n\nКафе Неъматҷон: https://goo.gl/maps/V7PqScyvGDAq9i2F9 \n\nЧайхана Набичон: https://goo.gl/maps/HDdcanVB5RvNLnUC6 \n\nСeхкабоби Мир: https://goo.gl/maps/6N6HKAXL66tAzjRf9", reply_markup=nav.taxiMenuRuss)
    elif message.text == "Куляб 🏙":
        await bot.send_message(message.from_user.id, "Рестораны с национальной едой в Кулябе (все ссылки указывают на гугл карты) \n\nЧайхана Истаравшан: https://goo.gl/maps/qMTAEXkLHukZsqTKA \n\nОшхана Дусти: https://goo.gl/maps/wvn2sTWGb9gWgu9C8 \n\nРесторан Tohir: https://goo.gl/maps/fUFS7dvLRVsFB9W98", reply_markup=nav.taxiMenuRuss)
    elif message.text == "Как мне добраться туда?":
        await bot.send_photo(message.from_user.id, photo=open("photos/taxi.png", 'rb'), caption="Вы можете заказать такси, по таким номерам как 3333, 1111, 888, 7000", reply_markup=nav.mainMenuRuss)
    elif message.text == "Посетить популярные места 📍":
        await bot.send_message(message.from_user.id, "Выберите что вы хотите", reply_markup=nav.placesRuss)
    elif message.text == "Популярные достопремечательности 🏰":
        await bot.send_photo(message.from_user.id, photo=open("photos/ational-library.jpg", 'rb'), caption="Национальная библиотека Таджикистана \n\nГлавное национальное книгохранилище Таджикистана, являющееся особо ценным объектом культурного наследия народов Республики Таджикистан. Находится на особом режиме охраны и использования. Национальная библиотека является государственным учреждением культуры, национальным хранилищем наследия науки и культуры, архивом национальной периодической печати, научно — исследовательским информационно — культурным центром республиканского значения, своими функциями соответствует основным требованиям ЮНЕСКО для библиотек данного вида.", reply_markup=nav.taxiMenuRuss)
        await bot.send_photo(message.from_user.id, photo=open("photos/von-vorne.jpg", 'rb'), caption="Памятник Исмоилу Сомони. \n\nГлавная достопримечательность на площади Дусти и главный символ города. Монумент был установлен в 1997 году, и его высота составляет 13 метров. \nА прямо над ним возвышается красивая арка, общая высота которой превышает 43 метра. В этом памятнике изображены главные символы таджикской государственности: корона и скипетр, украшенные семью звездами. \nЗа памятником Исмаилу Сомони располагается аллея фонтанов, которые вечером становятся светомузыкальными. А в конце каскада фонтанов находится еще одна достопримечательность – стела Независимости высотой 45 метров. \nКрасивую бело-золотую башню венчает герб Таджикистана. Этот памятник был возведен в 2011 году, в честь 20-летия Независимости Таджикистана.", reply_markup=nav.taxiMenuRuss)
        await bot.send_photo(message.from_user.id, photo=open("photos/caption.jpg", 'rb'), caption="Историко-краеведческий музей археологии и фортификации находится в городе Худжанд. \n\nОн был открыт 29 ноября 1986 года, в честь празднования 2500-летия города. Музей расположен в восточной части старой Худжандской крепости VIII-X веков, которая была восстановлено в 1999 году. \nКогда стены крепости были частью мощной фартыфікацыйнай системы города. Внешне музей имитирует вид средневекового сооружения с толстыми стенами из сырцового кирпича и высокими башнями. \nВ помещении, площадью 150 квадратных метров, расположенный зала средневековой истории города, архитектурных особенностей зданий и сооружений,  истории изучения Худжанд и его исследователей. \nЦенные находки, которые занимают почетные места в экспозиции, это керамика античного и средневекового периодов. Интересно тут также посмотреть на многочисленные карты и планы города Худжандразличних эпох. \nВсего в музее насчитывается более 1200 экспонатов.", reply_markup=nav.taxiMenuRuss)
    elif message.text == "Помочь проекту 💵":
        await bot.send_message(message.from_user.id, "Вы можете помочь нашему проекту с помощью DonationAlerts: https://www.donationalerts.com/r/idris4ik \nили же на карты:  \n4444 8888 1033 3538,   \n4890 4947 9688 1696 \n\nСпасибо!")
    elif message.text == "Покупки 🛍":
        await bot.send_photo(message.from_user.id, photo=open("photos/dm.jpeg", 'rb'), caption='Душанбе Молл \n\nТЦ "Душанбе Молл" самый крупный торгово-развлекательный центр в Таджикистане, соответствующий международным стандартам. Это прекрасное место, где можно не только совершать покупки, но и интересно провести время и вкусно покушать. \n\nГугл карты: https://goo.gl/maps/Kk2FCW16oin6tmKu6', reply_markup=nav.taxiMenuRuss)
        await bot.send_photo(message.from_user.id, photo=open("photos/siema.jpg", 'rb'), caption='Сиёма Молл \n\nТСРЦ Сиёма Молл это уникальный торгово-развлекательный центр, в который можно приехать и с удовольствием провести несколько часов. Это множество брендовых магазинов, размещенных в одном месте, а, значит, не придётся ездить по всему городу, чтобы сделать важные покупки. Здесь вы найдёте: бытовую технику, мебель, электронику, одежду, обувь и аксессуары.  \n\nГугл карты: https://goo.gl/maps/hb8zDVzLBGP6GSfW7', reply_markup=nav.taxiMenuRuss)
        await bot.send_photo(message.from_user.id, photo=open("photos/tsum.jpg", 'rb'), caption='ЦУМ (Центральный Универсальный Магазин) \n\nЦентральный Универсальный Магазин города Душанбе известный под сокращённому имени «ЦУМ». ЦУМ – является государственным учреждением и ее здания состоит из 3-х этажей которая было построена в 1970-е годы. Общая площадь здания составляет 7500 кв. м. где ширина 25 и длина 125 метров. На первом этаже ЦУМ последние годы (2010-2020) продаются в основном телефоны-смартфоны и в этой связи данная торговый центр известен в основном как место для покупки телефонов что не имеет аналога по масштабу в стране.  Где-то на 20% территории первого этажа продаётся другие товары в том числе компьютеры, фотоаппараты, сувениры, и сервис телефонов. \n\nГугл карты: https://goo.gl/maps/ydYddgLaZDGrw6cf6', reply_markup=nav.taxiMenuRuss)
    elif message.text == "Прогулка 🚶":
        await bot.send_photo(message.from_user.id, photo=open("photos/pobeda.jpg", 'rb'), caption='Парк Победы \n\nАрхитектурно-скульптурный мемориальный комплекс был сооружён в 1975 году по проекта авторского коллектива из института Душанбегипрогор (архитекторы Б. А. Зухурдинов, В. Щердинин, скульптор Д. Рябичев). Главный вход в лесопарк и к мемориалу предусмотрен со стороны улицы Дружбы Народов в виде широкой аллеи с лестницами. Для удобного сообщения и облегчения подъёма на вершину холма с мемориалом построена подвесная канатная дорога (архитектор проекта М. Исмаилов, конструктор Р. Хурсандов). Стоимость билета: бесплатно \n\nГугл карты: https://goo.gl/maps/wkFhHeAwpPm4mXXg7', reply_markup=nav.taxiMenuRuss)
        await bot.send_photo(message.from_user.id, photo=open("photos/botanicheskij-sad1.jpg", 'rb'), caption='Ботанический сад \n\nБотанический сад был открыт в 1933 году. Первоначально растения размещались в соответствии с зонами: Европа, Сибирь, Восточная и Средняя Азия, Средиземноморье, Северная Америка. Сегодня здесь собраны образцы деревьев и кустарников (более 4500 видов), произрастающих во многих уголках планеты, иной раз совершенно противоположных: пальмы соседствуют с секвойями, сирень — с магнолиями и т. д. Причем некоторые из видов уже находятся на грани исчезновения и занесены в Красную книгу.На территории парка есть два небольших водоема, беседки, скульптурные композиции. Отдельно обустроен городок ремесел с постройками в национальном стиле, где по праздникам проводятся выставки, ярмарки и другие общественные мероприятия. Стоимость билета: 2 сомони (11.32 рублей) \n\nГугл карты: https://goo.gl/maps/DHve6qFsTbnD3uT17', reply_markup=nav.taxiMenuRuss)
    elif message.text == "Новости 📰":
        await bot.send_message(message.from_user.id, f"{parser.post} \n\nИсточник: {parser.f_url}" )
    elif message.text == "Другое":
        await bot.send_message(message.from_user.id, "Другое", reply_markup=nav.otherMenuRuss)
    elif message.text == "Экстренные службы ⛑":
        await bot.send_message(message.from_user.id, "112 - Экстренный вызов \n\n101 - Пожарная охрана \n\n102 - Милиция \n\n103 - Скорая помощь \n\n104 - Служба газа")

    # --- English ---
    elif message.text == "English 🇺🇸":
        cursor.execute(f"UPDATE users SET lang == 2 WHERE user_id = {message.chat.id}")
        connection.commit()
        await bot.send_message(message.from_user.id, "Welcome to Tajikistan! We are glad that you visited our sunny lands 😊", reply_markup=nav.mainMenuEng)
    elif message.text == "National food 🍗":
        await bot.send_photo(message.from_user.id, photo=open("photos/samsa-s-baraninoy.jpg", "rb"), caption="There are a lot of delicious national foods in Tajikistan, such as: Samsa, Kurutob, etc.", reply_markup=nav.restoMenuEng)
    elif message.text == "Change the language 🇷🇺🇹🇯🇺🇿":
        await message.reply("🇷🇺 Привет! Выберите язык. \n\n🇺🇸 Hello! Select the language. \n\n🇹🇯 Салом! Забонро интихоб кунед. \n\n🇺🇿 Salom! Tilni tanlang.", reply_markup=nav.langMenu)
    elif message.text == "Information about bot ℹ️":
        await bot.send_message(message.from_user.id, "This bot is made for tourists who decide to visit Tajikistan and learn more about it. \n\nThis bot will tell you where you can eat delicious national or any other food, it will also help you visit the popular sights of Tajikistan, etc. \n\nIf you notice an error in the bot, please contact @Idrisishe technical support")
    elif message.text == "Main menu":
        await bot.send_message(message.from_user.id, "Main menu", reply_markup=nav.mainMenuEng)
    elif message.text == "Where I can eat this food? 🍗":
        await bot.send_message(message.from_user.id, "What city are you currently in?", reply_markup=nav.cityEng)
    elif message.text == "Dushanbe 🌃":
        await bot.send_message(message.from_user.id, "Restaurants with national food in Dushanbe (all links point to google maps) \n\nYakkachinar restaurant: https://goo.gl/maps/HuC9BvUMB1gKdBh66 \n\nSamandar restaurant: https://goo.gl/maps/Dq1Jkhi6SjxTimi5A \n \nRohat Restaurant: https://goo.gl/maps/AH63i57jw3n9gQzi8", reply_markup=nav.taxiMenuEng)
    elif message.text == "Khujand 🌃":
        await bot.send_message(message.from_user.id, "Restaurants with national food in Khujand (all links point to Google maps) \n\nCafe Nemathon: https://goo.gl/maps/V7PqScyvGDAq9i2F9 \n\nTeahouse Nabichon: https://goo.gl/maps/HDdcanVB5RvNLnUC6 \n \nSehkabobi World: https://goo.gl/maps/6N6HKAXL66tAzjRf9", reply_markup=nav.taxiMenuEng)
    elif message.text == "Kulob 🌃":
        await bot.send_message(message.from_user.id, "Restaurants with national food in Kulob (all links point to Google maps) \n\nIstaravshan teahouse: https://goo.gl/maps/qMTAEXkLHukZsqTKA \n\nOshkhan Dusti: https://goo.gl/maps/wvn2sTWGb9gWgu9C8 \n \nTohir Restaurant: https://goo.gl/maps/fUFS7dvLRVsFB9W98", reply_markup=nav.taxiMenuEng)
    elif message.text == "How can I get there?":
        await bot.send_photo(message.from_user.id, photo=open("photos/taxi.png", 'rb'), caption="You can order a taxi by such numbers as 3333, 1111, 888, 7000", reply_markup=nav.mainMenuEng)
    elif message.text == "Visit popular places 📍":
        await bot.send_message(message.from_user.id, "Choose what do you want", reply_markup=nav.placesEng)
    elif message.text == "Popular Attractions 🏰":
        await bot.send_photo(message.from_user.id, photo=open("photos/ational-library.jpg", 'rb'), caption="National Library of Tajikistan \n\nThe main national book depository of Tajikistan, which is a particularly valuable object of the cultural heritage of the peoples of the Republic of Tajikistan. It is in a special mode of protection and use. The National Library is a state institution of culture, a national repository of the heritage of science and culture, an archive of the national periodical press, a research information and cultural center of republican significance, and its functions meet the basic requirements of UNESCO for libraries of this type.", reply_markup=nav.taxiMenuEng)
        await bot.send_photo(message.from_user.id, photo=open("photos/von-vorne.jpg", 'rb'), caption="Monument to Ismoil Somoni. \n\nThe main attraction in Dusty Square and the main symbol of the city. The monument was installed in 1997, and its height is 13 meters. \nAnd right above it rises a beautiful arch, the total height of which exceeds 43 meters. This monument depicts the main symbols of Tajik statehood: the crown and scepter, decorated with seven stars. \nBehind the monument to Ismail Somoni is an alley of fountains, which are light and musical in the evening. And at the end of the cascade of fountains is another landmark - the 45-meter high Independence Stela. The beautiful white and gold tower is crowned with the coat of arms of Tajikistan. \nThis monument was erected in 2011, in honor of the 20th anniversary of Tajikistan's independence.", reply_markup=nav.taxiMenuEng)
        await bot.send_photo(message.from_user.id, photo=open("photos/caption.jpg", 'rb'), caption="The Historical Museum of Archaeology and Fortification is located in Khujand. \n\nIt was opened on November 29, 1986 in honor of the 2500th anniversary of the city. It is located in the eastern part of the old fortress of Khujand VIII-X centuries, which was restored in 1999. \nWhen the walls of the fortress were part of the powerful system of the city. Externally, the museum imitates the appearance of a medieval structure with thick walls of raw bricks and high towers. \nIn the room, area of 150 square meters, located hall of the medieval history of the city, the architectural features of buildings and structures, the history of the study of Khujand and its explorers. \nThe main findings, which occupy places of honor in the exposition, are ceramics of antique and medieval periods. It is also interesting to look at the numerous maps and plans of Khujand of different epochs. \nIn total, the museum has more than 1200 exhibits.", reply_markup=nav.taxiMenuEng)
    elif message.text == "Help to project 💵":
        await bot.send_message(message.from_user.id, "You can help our project with DonationAlerts: https://www.donationalerts.com/r/idris4ik \nor on debit cards: \n4444 8888 1033 3538, \n4890 4947 9688 1696 \n\nThank you!")
    elif message.text == "Shopping 🛍":
        await bot.send_photo(message.from_user.id, photo=open("photos/dm.jpeg", 'rb'), caption='Dushanbe Mall \n\nShopping center "Dushanbe Mall" is the largest shopping and entertainment center in Tajikistan, suitable for RMTC. This is a great place where you can not only shop, but also have fun and have a delicious meal. \n\nGoogle maps: https://goo.gl/maps/Kk2FCW16oin6tmKu6', reply_markup=nav.taxiMenuEng)
        await bot.send_photo(message.from_user.id, photo=open("photos/siema.jpg", 'rb'), caption='Shiyoma Mall \n\nTSRC "Shiyoma Mall" is a unique shopping and entertainment center where you can come and enjoy spending a few hours. This is a lot of branded stores located in one place, which means you don’t have to travel all over the city to make important purchases. Here you will find: household appliances, furniture, electronics, clothes, shoes and accessories. \n\nGoogle maps: https://goo.gl/maps/hb8zDVzLBGP6GSfW7', reply_markup=nav.taxiMenuEng)
        await bot.send_photo(message.from_user.id, photo=open("photos/tsum.jpg", 'rb'), caption='TSUM (Central Department Store) \n\nThe Central Department Store of the city of Dushanbe is known under the abbreviated name "TSUM". TSUM is a government institution, and its building consists of three floors, built in the 1970s. The total area of ​​the building is 7500 sq. m. where the width is 25 and the length is 125 meters. On the first floor of the Central Department Store of recent years (2010–2020), mainly smartphones are sold, and in this regard, in shopping centers, mainly as a place to buy phones that have no analogues in terms of scale in the country. Somewhere on 20% of the territory of the first floor, other goods are sold, including computers, cameras, souvenirs and phone service. \n\nGoogle maps: https://goo.gl/maps/ydYddgLaZDGrw6cf6', reply_markup=nav.taxiMenuEng)
    elif message.text == "Walk 🚶":
        await bot.send_photo(message.from_user.id, photo=open("photos/pobeda.jpg", 'rb'), caption='Victory Park \n\nThe architectural and sculptural memorial complex was built in 1975 according to the project of the team of authors from the Dushanbegiprogor Institute (architects B. A. Zukhurdinov, V. Shcherdinin, sculptor D. Ryabichev). The main entrance to the forest park and to the memorial is provided from Druzhby Narodiv Street in the form of a wide alley with stairs. For convenient communication and facilitating the ascent to the top of the hill with the memorial, a cable car was built (project architect M. Ismailov, designer R. Khursandov). Ticket price: free\n\nGoogle maps: https://goo.gl/maps/wkFhHeAwpPm4mXXg7', reply_markup=nav.taxiMenuEng)
        await bot.send_photo(message.from_user.id, photo=open("photos/botanicheskij-sad1.jpg", 'rb'), caption='The Botanical Garden was opened in 1933. Originally the plants were placed according to zones: Europe, Siberia, East and Central Asia, the Mediterranean, North America. Today there are samples of trees and shrubs (over 4500 species), growing in many parts of the world, sometimes completely opposite: palms are next to sequoias, lilacs - to magnolias, etc. There are two small ponds, arbors and sculptures in the park. There is a separate handicrafts town with buildings in the national style, where exhibitions, fairs and other public events are held on holidays. Ticket price: 2 somoni (0.16 Dollar USA) \n\nGoogle Maps: https://goo.gl/maps/DHve6qFsTbnD3uT17', reply_markup=nav.taxiMenuEng)
    elif message.text == "News 📰":
        await bot.send_message(message.from_user.id, "Sorry, in this language this function isn't working :(")
    elif message.text == "Other":
        await bot.send_message(message.from_user.id, "Other", reply_markup=nav.otherMenuEng)
    elif message.text == "Emergency services ⛑":
        await bot.send_message(message.from_user.id, "112 - Emergency Call \n\n101 - Fire Department \n\n102 - Police \n\n103 - Ambulance \n\n104 - Gas Service")

    # --- Tajik ---
    elif message.text == "Тоҷикӣ 🇹🇯":
        cursor.execute(f"UPDATE users SET lang == 3 WHERE user_id = {message.chat.id}")
        connection.commit()
        await bot.send_message(message.from_user.id, "Хуш омадед ба Тоҷикистон! Мо шодем, ки шумо ба сарзаминҳои офтобии мо ташриф овардед 😊", reply_markup=nav.mainMenuTjk)
    elif message.text == "Хӯроки миллӣ 🍗":
        await bot.send_photo(message.from_user.id, photo=open("photos/samsa-s-baraninoy.jpg", "rb"), caption="Дар Тоҷикистон бисёр хӯрокҳои болаззати миллӣ мавҷуданд, аз қабили: Самса, Қурутоб ва ғайра.", reply_markup=nav.restoMenuTjk)
    elif message.text == "Забонро иваз кунед 🇺🇸🇷🇺🇺🇿":
        await message.reply("🇷🇺 Привет! Выберите язык. \n\n🇺🇸 Hello! Select the language. \n\n🇹🇯 Салом! Забонро интихоб кунед. \n\n🇺🇿 Salom! Tilni tanlang.", reply_markup=nav.langMenu)
    elif message.text == "Маълумоти бот ℹ️":
        await bot.send_message(message.from_user.id, "Ин бот барои сайёҳоне тарҳрезӣ шудааст, ки тасмим гирифтанд ба Тоҷикистон сафар кунанд ва дар бораи он маълумоти бештар гиранд. \n\nИн бот ба шумо мегӯяд, ки шумо метавонед аз куҷо таомҳои болаззати миллӣ ё дигар хӯрокҳоро бихӯред, инчунин барои дидан аз ҷойҳои ҷолиби диққати Тоҷикистон ва ғайра кумак мекунад. \n\nАгар шумо хатоеро дар бот мушоҳида кунед, лутфан бо дастгирии техникии @Idrisishe тамос гиред")
    elif message.text == "Менюи асосӣ️":
        await bot.send_message(message.from_user.id, "Менюи асосӣ️", reply_markup=nav.mainMenuTjk)
    elif message.text == "Дар куҷо ман метавонам ин хӯрокро бихӯрам? 🍗":
        await bot.send_message(message.from_user.id, "Шумо ҳоло дар кадом шаҳр ҳастед?", reply_markup=nav.cityTjk)
    elif message.text == "Душанбе 🌆":
        await bot.send_message(message.from_user.id, "Тарабхонаҳо бо таомҳои миллӣ дар Душанбе (ҳама пайвандҳо ба харитаҳои Google ишора мекунанд) \n\nТарабхонаи Яккачинор: https://goo.gl/maps/HuC9BvUMB1gKdBh66 \n\nТарабхонаи Самандар: https://goo.gl/maps/Dq1Jkhi6SjxTimi5A \n \nТарабхонаи «Роҳат»: https://goo.gl/maps/AH63i57jw3n9gQzi8", reply_markup=nav.taxiMenuTjk)
    elif message.text == "Хучанд 🌆":
        await bot.send_message(message.from_user.id, "Тарабхонаҳо бо таомҳои миллӣ дар Хуҷанд (ҳамаи истинодҳо ба харитаҳои Google ишора мекунанд) \n\nКафе Неъматхон: https://goo.gl/maps/V7PqScyvGDAq9i2F9 \n\nЧойхонаи Набичон: https://goo.gl/maps/HDdcanVB5RvNLnUC6 \n \nСехкабоби Ҷаҳон: https://goo.gl/maps/6N6HKAXL66tAzjRf9", reply_markup=nav.taxiMenuTjk)
    elif message.text == "Кулоб 🌆":
        await bot.send_message(message.from_user.id, "Тарабхонаҳо бо таомҳои миллӣ дар Кӯлоб (ҳама пайвандҳо ба харитаҳои Google ишора мекунанд) \n\nЧойхонаи Истаравшан: https://goo.gl/maps/qMTAEXkLHukZsqTKA \n\nОшхони Дӯстӣ: https://goo.gl/maps/wvn2sTWGb9gWgu9C8 \n \nТарабхонаи Тоҳир: https://goo.gl/maps/fUFS7dvLRVsFB9W98", reply_markup=nav.taxiMenuTjk)
    elif message.text == "Чӣ тавр ман метавонам ба он ҷо расам?":
        await bot.send_photo(message.from_user.id, photo=open("photos/taxi.png", 'rb'), caption="Шумо метавонед бо рақамҳои 3333, 1111, 888, 7000 такси фармоиш диҳед.", reply_markup=nav.mainMenuTjk)
    elif message.text == "Ба ҷойҳои машҳур сафар кунед 📍":
        await bot.send_message(message.from_user.id, "Он чизеро, ки шумо мехоҳед, интихоб кунед", reply_markup=nav.placesTjk)
    elif message.text == "Ҷойҳои машҳур 🏰":
        await bot.send_photo(message.from_user.id, photo=open("photos/ational-library.jpg", 'rb'), caption="Китобхонаи миллии Тоҷикистон \n\nАмонатхонаи асосии миллии китобҳои Тоҷикистон, ки объекти махсусан пурарзиши мероси фарҳангии халқҳои Ҷумҳурии Тоҷикистон мебошад. Он дар ҳолати махсуси муҳофизат ва истифода қарор дорад. Китобхонаи миллӣ муассисаи давлатии фарҳанг, хазинаи миллии мероси илму фарҳанг, бойгонии матбуоти даврии миллӣ, маркази иттилоотӣ-тадқиқотӣ ва фарҳангии аҳамияти ҷумҳуриявӣ буда, вазифаҳои он ба талаботи асосии ЮНЕСКО нисбат ба китобхонаҳо ҷавобгӯ мебошад. аз ин намуд.", reply_markup=nav.taxiMenuTjk)
        await bot.send_photo(message.from_user.id, photo=open("photos/von-vorne.jpg", 'rb'), caption="Муҷассамаи Исмоили Сомонӣ. \n\nАтракциони асосӣ дар майдони Дӯстӣ ва рамзи асосии шаҳр. Муҷассама соли 1997 гузошта шуда, баландии он 13 метр аст. \nВа рост аз болои он камари зебое мебарояд, ки баландии умумии он аз 43 метр зиёд аст. Дар ин муҷассама рамзҳои асосии давлатдории тоҷикон: тоҷ ва асо, ки бо ҳафт ситора оро дода шудаанд, тасвир ёфтааст. \nДар паси муҷассамаи Исмоили Сомонӣ як гулгашти фаввораҳое ҷойгир аст, ки шомгоҳон рӯшан ва мусиқиро фаро мегиранд. Ва дар охири каскади фавворахо боз як манзараи дигар — стела 45-метраи Истиқлолият мавҷуд аст. Манораи зебои сафеду тиллоро герби Точикистон зеб додааст. \nИн муҷассама соли 2011 ба ифтихори 20-умин солгарди истиқлоли Тоҷикистон гузошта шуда буд.", reply_markup=nav.taxiMenuTjk)
        await bot.send_photo(message.from_user.id, photo=open("photos/caption.jpg", 'rb'), caption="Осорхонаи таърихии бостоншиносӣ ва истиқлол дар шаҳри Хуҷанд ҷойгир аст. \n\n29 ноябри соли 1986 ба шарафи 2500-солагии шахр кушода шуд. Он дар қисмати шарқии қалъаи кӯҳнаи Хуҷанди асрҳои VIII-X, ки соли 1999 барқарор карда шудааст, ҷойгир шудааст. \nВақте ки деворҳои қалъа як қисми низоми тавонои шаҳр буданд. Дар берун, осорхона ба намуди сохтори асримиёнагӣ бо деворҳои ғафси хишти хом ва манораҳои баланд тақлид мекунад. \nДар ҳуҷра, масоҳати 150 метри мураббаъ, толори таърихи асримиёнагии шаҳр, хусусияти меъмории биною иншоот, таърихи омӯзиши Хуҷанд ва муҳаққиқони он. \nБозёфтҳои асосие, ки дар экспозиция ҷойҳои ифтихориро ишғол мекунанд, сафолҳои давраҳои антиқа ва асрҳои миёна мебошанд. Аз назар гузарондани харитаю накшахои сершумори Хучанд дар даврахои гуногун низ шавковар аст. \nУмуман дар музей зиёда аз 1200 экспонат мавчуд аст.", reply_markup=nav.taxiMenuTjk)
    elif message.text == "Лойиҳага ёрдам беринг 💵":
        await bot.send_message(message.from_user.id, "Шумо метавонед ба лоиҳаи мо бо DonationAlerts: https://www.donationalerts.com/r/idris4ik \nё харитаҳо кӯмак кунед: \n4444 8888 1033 3538 \n4890 4947 9688 1696 \n\nРахмат!")
    elif message.text == "Харид 🛍":
        await bot.send_photo(message.from_user.id, photo=open("photos/dm.jpeg", 'rb'), caption='Маркази савдои Душанбе \n\nМаркази савдои "Душанбе Молл" бузургтарин маркази савдо ва фароғатии Тоҷикистон буда, барои RMTC мувофиқ аст. Ин ҷои хубест, ки дар он шумо метавонед на танҳо харид кунед, балки хурсандӣ кунед ва хӯроки болаззат хӯред. \n\nХаритаҳои Google: https://goo.gl/maps/Kk2FCW16oin6tmKu6', reply_markup=nav.taxiMenuTjk)
        await bot.send_photo(message.from_user.id, photo=open("photos/siema.jpg", 'rb'), caption='Сиёма Молл \n\nТСРЦ "Сиёма Молл" як маркази беназири савдо ва фароғатӣ мебошад, ки дар он шумо метавонед омада, аз чанд соат лаззат баред. Ин бисёр мағозаҳои бренди дар як ҷо ҷойгиранд, яъне ба шумо лозим нест, ки барои хариди муҳим дар тамоми шаҳр сафар кунед. Дар ин ҷо шумо метавонед: асбобҳои рӯзгор, мебел, электроника, либос, пойафзол ва лавозимот. \n\nХаритаҳои Google: https://goo.gl/maps/hb8zDVzLBGP6GSfW7', reply_markup=nav.taxiMenuTjk)
        await bot.send_photo(message.from_user.id, photo=open("photos/tsum.jpg", 'rb'), caption='ТСУМ (Универмаги марказӣ) \n\nУнивермаги марказии шаҳри Душанбе бо номи мухтасари "ТСУМ" маъруф аст. "ТСУМ" як муассисаи давлатӣ буда, бинои он аз се ошёна иборат буда, солҳои 70-ум сохта шудааст. Масоҳати умумии бино 7500 кв. м, ки бараш 25 ва дарозиаш 125 метр аст. Дар ошёнаи якуми Универмаги марказӣ солҳои охир (2010–2020) асосан смартфонҳо ва аз ин лиҳоз дар марказҳои савдо асосан ҳамчун ҷои хариди телефонҳое ба фурӯш гузошта мешаванд, ки аз ҷиҳати миқёс дар ҷумҳурӣ ҳамто надоранд. . Тақрибан 20% майдони ошёнаи якум молҳои дигар, аз ҷумла компютерҳо, камераҳо, сувенирҳо ва хадамоти телефониро мефурӯшанд. \n\nХаритаҳои Google: https://goo.gl/maps/ydYddgLaZDGrw6cf6', reply_markup=nav.taxiMenuTjk)
    elif message.text == "Пиёда рафтан 🚶":
        await bot.send_photo(message.from_user.id, photo=open("photos/pobeda.jpg", 'rb'), caption='Боғи Ғалаба \n\nМаҷмааи ёдгории меъморӣ ва ҳайкалтарошӣ соли 1975 аз рӯи лоиҳаи гурӯҳи муаллифони Институти Душанбегипрогор (меъморон Б. А. Зухурдинов, В. Щердинин, ҳайкалтарош Д. Рябичев) сохта шудааст. Даромадгохи асосии боги чангал ва ёдгорй аз кучаи Дружбы Народив дар шакли хиёбони васеъ бо зинапоя кушода мешавад. Барои муоширати кулай ва осон кардани баромадан ба куллаи теппа бо ёдгории ёдгорй троллейбус сохта шуд (меъмори лоиха М. Исмаилов, лоихакаш Р. Хурсандов). Нархи чипта: ройгон \n\nХаритаҳои Google: https://goo.gl/maps/wkFhHeAwpPm4mXXg7', reply_markup=nav.taxiMenuTjk)
        await bot.send_photo(message.from_user.id, photo=open("photos/botanicheskij-sad1.jpg", 'rb'), caption='Боғи ботаники соли 1933 кушода шуд. Дар ибтидо растаниҳо аз рӯи минтақаҳо ҷойгир карда шуданд: Аврупо, Сибир, Осиёи Шарқӣ ва Марказӣ, Баҳри Миёназамин, Амрикои Шимолӣ. Имрӯзҳо намунаҳои дарахту буттаҳо (зиёда аз 4500 намуд), ки дар бисёр гӯшаву канори ҷаҳон мерӯянд, баъзан комилан муқобил: хурмоҳо дар паҳлӯи секвоияҳо, лилакҳо — ба магнолияҳо ва ғ. парк. Дар ин чо шахрчаи алохидаи хунармандй сохта шудааст, ки бинохои бо услуби миллй доранд, ки дар он рузхои ид выставкаю ярмарка ва дигар чорабинихои оммавй гузаронда мешаванд. Нархи билет: 2 сомонӣ (сомонӣ) \n\nХаритаҳои Google: https://goo.gl/maps/DHve6qFsTbnD3uT17', reply_markup=nav.taxiMenuTjk)
    elif message.text == "Ахбор 📰":
        await bot.send_message(message.from_user.id, f"{parser.post_tjk} \n\nСарчашма: {parser.f_url_tj}")
    elif message.text == "Дигар":
        await bot.send_message(message.from_user.id, "Дигар", reply_markup=nav.otherMenuTjk)
    elif message.text == "Хадамоти фавқулодда ⛑":
        await bot.send_message(message.from_user.id, "112 - Даъвати таъҷилӣ \n\n101 - Шӯъбаи оташнишонӣ \n\n102 - Полис \n\n103 - Ёрии таъҷилӣ \n\n104 - Хадамоти газ")

    # --- O'zbek ---
    elif message.text == "O'zbek 🇺🇿":
        cursor.execute(f"UPDATE users SET lang == 4 WHERE user_id = {message.chat.id}")
        connection.commit()
        await bot.send_message(message.from_user.id, "Tojikistonga xush kelibsiz! serquyosh yerlarimizga tashrif buyurganingizdan xursandman 😊", reply_markup=nav.mainMenuUzb)
    elif message.text == "Milliy taomlar 🍗":
        await bot.send_photo(message.from_user.id, photo=open("photos/samsa-s-baraninoy.jpg", "rb"), caption="Tojikistonda juda ko'p mazali milliy taomlar mavjud, masalan: samsa, qurutob va boshqalar.", reply_markup=nav.restoMenuUzb)
    elif message.text == "Tilni o'zgartirish 🇹🇯🇺🇸🇷🇺":
        await message.reply("🇷🇺 Привет! Выберите язык. \n\n🇺🇸 Hello! Select the language. \n\n🇹🇯 Салом! Забонро интихоб кунед. \n\n🇺🇿 Salom! Tilni tanlang.", reply_markup=nav.langMenu)
    elif message.text == "Bot haqida ma'lumot ℹ️":
        await bot.send_message(message.from_user.id, "Ushbu bot Tojikistonga tashrif buyurishga va u haqida ko'proq ma'lumot olishga qaror qilgan sayyohlar uchun mo'ljallangan. \n\nUshbu bot sizga milliy yoki boshqa taomlarni qayerda tanovul qilish mumkinligini aytib beradi, shuningdek, Tojikistonning mashhur diqqatga sazovor joylariga borishga yordam beradi va hokazo. \n\nAgar botda xatolikni sezsangiz, @Idrisishe texnik yordamiga murojaat qiling.")
    elif message.text == "Asosiy menyu":
        await bot.send_message(message.from_user.id, "Asosiy menyu️", reply_markup=nav.mainMenuUzb)
    elif message.text == "Bu taomni qayerda yeyishim mumkin? 🍗":
        await bot.send_message(message.from_user.id, "Siz hozir qaysi shahardasiz?", reply_markup=nav.cityUzb)
    elif message.text == "Koʻlob 🏙":
        await bot.send_message(message.from_user.id, "Ko'lobdagi milliy taomlar bilan ta'minlangan restoranlar (barcha havolalar Google xaritalariga ishora qiladi) \n\nIstaravshan choyxonasi: https://goo.gl/maps/qMTAEXkLHukZsqTKA \n\nOshxon Do'sti: https://goo.gl/maps/wvn2sTWGb9gWgu9C8 \n \nTohir restorani: https://goo.gl/maps/fUFS7dvLRVsFB9W98", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Dushanbe 🏙":
        await bot.send_message(message.from_user.id, "Dushanbedagi milliy taomlar bilan jihozlangan restoranlar (barcha havolalar Google xaritalariga ishora qiladi) \n\nYakkachinar restorani: https://goo.gl/maps/HuC9BvUMB1gKdBh66 \n\nSamandar restorani: https://goo.gl/maps/Dq1Jkhi6SjxTimi5A \n \nRohat restorani: https://goo.gl/maps/AH63i57jw3n9gQzi8", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Xo'jand 🏙":
        await bot.send_message(message.from_user.id, "Xo'janddagi milliy taomlar bilan ta'minlangan restoranlar (barcha havolalar Google xaritalariga ishora qiladi) \n\nNemathon kafesi: https://goo.gl/maps/V7PqScyvGDAq9i2F9 \n\nNabichon choyxonasi: https://goo.gl/maps/HDdcanVB5RvNLnUC6 \n \nSehkabobi dunyosi: https://goo.gl/maps/6N6HKAXL66tAzjRf9", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Qanday qilib u erga borishim mumkin?":
        await bot.send_photo(message.from_user.id, photo=open("photos/taxi.png", 'rb'), caption="3333, 1111, 888, 7000 kabi raqamlar orqali taksiga buyurtma berishingiz mumkin.", reply_markup=nav.mainMenuUzb)
    elif message.text == "Mashhur joylarga tashrif buyuring 📍":
        await bot.send_message(message.from_user.id, "O'zingiz xohlagan narsani tanlang", reply_markup=nav.placesUzb)
    elif message.text == "Mashhur diqqatga sazovor joylar 🏰":
        await bot.send_photo(message.from_user.id, photo=open("photos/ational-library.jpg", 'rb'), caption="Kutubxonasi Milliy Tojikiston \n\nAsosiy milliy kitob depozitariysi Tojikiston, ki khususan obekti khususan qimmatbahoi merosi khalqhoi Jumhurii Tojikiston. U maxsus himoya va foydalanish rejimida. Milliy kutubxona davlat madaniyat muassasasi, fan va madaniyat merosining milliy ombori, milliy davriy matbuot arxivi, respublika ahamiyatiga molik ilmiy-tadqiqot axborot-madaniy markaz boʻlib, uning vazifalari YuNESKOning kutubxonalarga qoʻyiladigan asosiy talablariga javob beradi. bu turdagi.", reply_markup=nav.taxiMenuUzb)
        await bot.send_photo(message.from_user.id, photo=open("photos/von-vorne.jpg", 'rb'), caption="Ismoil Somoniy haykali. \n\nDusti maydonidagi asosiy diqqatga sazovor joy va shaharning asosiy ramzi. Yodgorlik 1997 yilda o'rnatilgan bo'lib, uning balandligi 13 metrni tashkil qiladi. \nUning toʻgʻridan-toʻgʻri tepasida umumiy balandligi 43 metrdan oshgan goʻzal archa koʻtariladi. Ushbu yodgorlikda tojik davlatchiligining asosiy ramzlari: yetti yulduz bilan bezatilgan toj va tayoq tasvirlangan. \nIsmoil Somoniy haykali ortida favvoralar xiyoboni joylashgan bo‘lib, ular kechki payt yorug‘ va musiqali. Va favvoralar kaskadining oxirida yana bir diqqatga sazovor joy - 45 metr balandlikdagi Mustaqillik Stela. Chiroyli oq va oltin minora Tojikiston gerbi bilan bezatilgan. \nUshbu yodgorlik 2011-yilda Tojikiston mustaqilligining 20 yilligiga bagʻishlab oʻrnatilgan.", reply_markup=nav.taxiMenuUzb)
        await bot.send_photo(message.from_user.id, photo=open("photos/caption.jpg", 'rb'), caption="Arxeologiya va istehkom tarixi muzeyi Xo‘jandda joylashgan. \n\n1986 yil 29 noyabrda shaharning 2500 yilligi munosabati bilan ochilgan. U 1999-yilda qayta tiklangan VIII-X asrlarga oid eski Xoʻjand qalʼasining sharqiy qismida joylashgan. \nOʻshanda qalʼa devorlari shaharning qudratli tizimining bir qismi boʻlgan. Tashqi tomondan, muzey xom g'ishtdan yasalgan qalin devorlar va baland minoralar bilan o'rta asrlar inshootining ko'rinishini taqlid qiladi. \n150 kvadrat metr maydondagi xonada shaharning oʻrta asrlar tarixi, bino va inshootlarning meʼmoriy xususiyatlari, Xoʻjand va uning tadqiqotchilarining oʻrganish tarixi aks ettirilgan zal joylashgan. \nEkspozitsiyada faxriy oʻrinlarni egallagan asosiy topilmalar antik va oʻrta asrlarga oid sopol buyumlardir. Shuningdek, Xo‘jandning turli davrlarga oid ko‘p sonli xarita va rejalarini ko‘rish qiziq. \nMuzeyda jami 1200 dan ortiq eksponatlar mavjud.", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Loyihaga yordam bering 💵":
        await bot.send_message(message.from_user.id, "Loyihamizga DonationAlerts orqali yordam berishingiz mumkin: https://www.donationalerts.com/r/idris4ik \nyoki xaritalarda: \n4444 8888 1033 3538, \n4890 4947 9688 1696 \n\nRahmat!")
    elif message.text == "Xarid qilish 🛍":
        await bot.send_photo(message.from_user.id, photo=open("photos/dm.jpeg", 'rb'), caption="Dushanbe Mall \n\n“Dushanbe Mall” savdo markazi Tojikistondagi eng yirik savdo va koʻngilochar markaz boʻlib, RMTC uchun mos keladi. Bu yerda siz nafaqat xarid qilishingiz, balki dam olishingiz va mazali taom qilishingiz mumkin bo'lgan ajoyib joy. \n\nGoogle xaritalari: https://goo.gl/maps/Kk2FCW16oin6tmKu6", reply_markup=nav.taxiMenuUzb)
        await bot.send_photo(message.from_user.id, photo=open("photos/siema.jpg", 'rb'), caption="""Shiyoma Mall \n\nTSRC "Shiyoma Mall" noyob savdo va ko'ngilochar markaz bo'lib, siz kelib, bir necha soat vaqt o'tkazishingiz mumkin. Bu bir joyda joylashgan ko'plab markali do'konlar, ya'ni muhim xaridlarni amalga oshirish uchun butun shahar bo'ylab sayohat qilishingiz shart emas. Bu yerda siz: maishiy texnika, mebel, elektronika, kiyim-kechak, poyabzal va aksessuarlar. \n\nGoogle xaritalari: https://goo.gl/maps/hb8zDVzLBGP6GSfW7""", reply_markup=nav.taxiMenuUzb)
        await bot.send_photo(message.from_user.id, photo=open("photos/tsum.jpg", 'rb'), caption="""TSUM (Markaziy univermag) \n\nDushanbe shahar markaziy univermagi “TSUM” qisqartirilgan nomi bilan mashhur. TSUM davlat muassasasi boʻlib, uning binosi 1970-yillarda qurilgan uch qavatdan iborat. Binoning umumiy maydoni 7500 kv.m. bu erda kengligi 25 va uzunligi 125 metr. Markaziy universal do‘konning birinchi qavatida so‘nggi yillarda (2010–2020) asosan smartfonlar sotilmoqda, shu munosabat bilan savdo markazlarida, asosan, mamlakatimizda ko‘lami bo‘yicha o‘xshashi bo‘lmagan telefonlar xarid qilish joyi sifatida . Birinchi qavat hududining 20 foizida boshqa tovarlar, jumladan, kompyuterlar, kameralar, suvenirlar va telefon xizmatlari sotiladi. \n\nGoogle xaritalari: https://goo.gl/maps/ydYddgLaZDGrw6cf6""", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Yurish 🚶":
        await bot.send_photo(message.from_user.id, photo=open("photos/pobeda.jpg", 'rb'), caption="Gʻalaba bogʻi \n\nArxitektura-haykaltaroshlik yodgorlik majmuasi 1975-yilda Dushanbegiprogor instituti mualliflar jamoasi (meʼmorlar B. A. Zuxurdinov, V. Shcherdinin, haykaltarosh D. Ryabichev) loyihasi boʻyicha qurilgan. O'rmon bog'iga va yodgorlikka asosiy kirish Drujby Narodiv ko'chasidan zinapoyali keng xiyobon shaklida taqdim etiladi. Qulay aloqa va yodgorlik bilan tepalik choʻqqisiga chiqishni osonlashtirish uchun teleferik qurilgan (loyiha meʼmori M. Ismoilov, loyihachi R. Xursandov). Chipta narxi: bepul\n\nGoogle xaritalari: https://goo.gl/maps/wkFhHeAwpPm4mXXg7", reply_markup=nav.taxiMenuUzb)
        await bot.send_photo(message.from_user.id, photo=open("photos/botanicheskij-sad1.jpg", 'rb'), caption="Botanika bog'i 1933 yilda ochilgan. Dastlab o'simliklar zonalarga ko'ra joylashtirilgan: Evropa, Sibir, Sharqiy va Markaziy Osiyo, O'rta er dengizi, Shimoliy Amerika. Bugungi kunda dunyoning ko'p joylarida o'sadigan, ba'zan butunlay qarama-qarshi bo'lgan daraxt va butalarning (4500 dan ortiq turlari) namunalari mavjud: palmalar sekvoyalar yonida, lilaklar - magnoliyalar va boshqalar. park. Bayram kunlarida ko‘rgazmalar, yarmarkalar va boshqa ommaviy tadbirlar o‘tkaziladigan milliy uslubdagi binolarga ega alohida hunarmandlar shaharchasi tashkil etilgan. Chipta narxi: 2 somoniy (1 788.68 so'm) \n\nGoogle Xaritalar: https://goo.gl/maps/DHve6qFsTbnD3uT17", reply_markup=nav.taxiMenuUzb)
    elif message.text == "Yangiliklar 📰":
        await bot.send_message(message.from_user.id, "Kechirasiz, bu tilda bu funksiya ishlamayapti :(")
    elif message.text == "Boshqa":
        await bot.send_message(message.from_user.id, "Boshqa", reply_markup=nav.otherMenuUzb)
    elif message.text == "Favqulodda xizmatlar ⛑":
        await bot.send_message(message.from_user.id, "112 - Favqulodda qo'ng'iroq \n\n101 - Yong'in bo'limi \n\n102 - Politsiya \n\n103 - Tez yordam \n\n104 - Gaz xizmati")

if __name__ == '__main__':
    executor.start_polling(dp)
