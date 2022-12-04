import telebot
from config import TOKEN
from telebot import types
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])


def adim(message):
    knopki = types.ReplyKeyboardMarkup(resize_keyboard=True)
    knopka1 = types.KeyboardButton('Курс криптовалют')
    knopka2 = types.KeyboardButton('Основы майнинга')
    knopka3 = types.KeyboardButton('Курс валют')
    knopki.row(knopka1, knopka2, knopka3)
    vib = bot.send_message(message.chat.id, 'Выберите опцию', reply_markup=knopki)
    bot.register_next_step_handler(vib, rasp)
k1 = "adim"
k2 = "adim"
def rasp(message):
    if message.text == 'Курс криптовалют':
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)
    elif message.text == "Основы майнинга":
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = types.KeyboardButton('Что такое майнинг?')
        knopka2 = types.KeyboardButton('Основные принципы работы')
        knopka3 = types.KeyboardButton('Майнинг биткоинов и других криптовалют')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        osn = bot.send_message(message.chat.id, 'Что Вас интересует?', reply_markup=knopki)
        bot.register_next_step_handler(osn, mine)
    elif message.text == "/close":
        adem(message)
    elif message.text == "Курс валют":
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
        k = bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs)
    elif message.text == "/close":
        adem(message)
def kurs(message):
    global k1
    global k2
    if message.text == "RUB":
        k1 = "RUB"
        k2 = "₽"
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "USD":
        k1 = "USD"
        k2 = "$"
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "EUR":
        k1 = "EUR"
        k2 = "€"
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "CNY":
        k1 = "CNY"
        k2 = "¥"
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "Меню":
        adim(message)
    elif message.text == "/close":
        adem(message)
k32 = "adim"
def kurs2(message):
    global k32
    if message.text == "RUB":
        k32 = "RUB"
        price = convert(base = k1, amount = 1, to=['RUB'])
        bot.send_message(message.chat.id, f'{k1} = {price["RUB"]} ₽')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "USD":
        k32 = "USD"
        price = convert(base = k1, amount = 1, to=['USD'])
        bot.send_message(message.chat.id, f'{k1} = {price["USD"]} $')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "EUR":
        k32 = "EUR"
        price = convert(base = k1, amount = 1, to=['EUR'])
        bot.send_message(message.chat.id, f'{k1} = {price["EUR"]} €')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "CNY":
        k32 = "CNY"
        price = convert(base = k1, amount = 1, to=['CNY'])
        bot.send_message(message.chat.id, f'{k1} = {price["CNY"]} ¥')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka = "Назад"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka, knopka5)
        k = bot.send_message(message.chat.id, "Во что конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs2)
    elif message.text == "Назад":
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = "RUB"
        knopka2 = "USD"
        knopka3 = "EUR"
        knopka4 = "CNY"
        knopka5 = "Меню"
        knopki.add(knopka1, knopka2, knopka3, knopka4, knopka5)
        k = bot.send_message(message.chat.id, "Какую валюту Вы хотите конвертировать?", reply_markup=knopki)
        bot.register_next_step_handler(k, kurs)
    elif message.text == "Меню":
        adim(message)







def crypto(message):

    if message.text == 'RUB':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether', vs_currencies='rub')
        mes = bot.send_message(message.chat.id, f'Bitcoin == {price["bitcoin"]["rub"]} ₽\n \n'
                                          f'Ethereum == {price["ethereum"]["rub"]} ₽\n \n'
                                          f'Litecoin == {price["litecoin"]["rub"]} ₽\n \n'
                                          f'Tether == {price["tether"]["rub"]} ₽\n \n')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)

    elif message.text == 'USD':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether', vs_currencies='usd')
        mes = bot.send_message(message.chat.id, f'Bitcoin == {price["bitcoin"]["usd"]} $\n \n'
                                          f'Ethereum == {price["ethereum"]["usd"]} $\n \n'
                                          f'Litecoin == {price["litecoin"]["usd"]} $\n \n'
                                          f'Tether == {price["tether"]["usd"]} $\n \n')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)
    elif message.text == 'EUR':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether', vs_currencies='eur')
        mes = bot.send_message(message.chat.id, f'Bitcoin == {price["bitcoin"]["eur"]} €\n \n'
                                          f'Ethereum == {price["ethereum"]["eur"]} €\n \n'
                                          f'Litecoin == {price["litecoin"]["eur"]} €\n \n'
                                          f'Tether == {price["tether"]["eur"]} €\n \n')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)
    elif message.text == 'CNY':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, tether', vs_currencies='cny')
        mes = bot.send_message(message.chat.id, f'Bitcoin == {price["bitcoin"]["cny"]} ¥\n \n'
                                                f'Ethereum == {price["ethereum"]["cny"]} ¥\n \n'
                                                f'Litecoin == {price["litecoin"]["cny"]} ¥\n \n'
                                                f'Tether == {price["tether"]["cny"]} ¥\n \n')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        knopka1 = types.KeyboardButton('RUB')
        knopka2 = types.KeyboardButton('USD')
        knopka3 = types.KeyboardButton('EUR')
        knopka = types.KeyboardButton('CNY')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka, knopka4)
        cr = bot.send_message(message.chat.id, 'Во что конвертировать?', reply_markup=knopki)
        bot.register_next_step_handler(cr, crypto)
    elif message.text == 'Меню':
        adim(message)
    elif message.text == "/close":
        adem(message)

def mine(messange):
    if messange.text == 'Что такое майнинг?':
        m = bot.send_message(messange.chat.id, f'Слово «майнинг» пришло к нам из английского языка и в буквальном смысле означает добычу полезных ископаемых. В контексте финансов и информационных технологий таким «сырьем» считается криптовалюта. \n \n'
                                               f'Майнинг – это добыча цифровой валюты с помощью специального оборудования. \n \n'
                                               f'Если говорить на языке блокчейн-инженеров, майнинг представляет собой присоединение блоков, в которых хранится информация о проведенных транзакциях. В результате они образуют непрерывную и последовательную цепочку – блокчейн. \n \n'
                                               f'Чтобы присоединить блок, необходимо решить определенную математическую задачу, расшифровав алгоритм криптовалюты.  \n \n'
                                               f'Собственно, этим и занимаются майнеры, а точнее их специальные устройства. Если оборудование находит правильный ответ, его владелец получает вознаграждение в виде цифровых монет. \n \n'
                                               f'При этом чем больше майнеров нацелены на решение задачи, тем больше усложняются поиски верного ответа и падает стоимость. \n \n')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = types.KeyboardButton('Что такое майнинг?')
        knopka2 = types.KeyboardButton('Основные принципы работы')
        knopka3 = types.KeyboardButton('Майнинг биткоинов и других криптовалют')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka4)



        osn = bot.send_message(messange.chat.id, 'Что Вас интересует?', reply_markup=knopki)
        bot.register_next_step_handler(osn, mine)

    elif messange.text == 'Основные принципы работы':
        m = bot.send_message(messange.chat.id, f'За обработку информации владелец компьютерного ресурса получает вознаграждение в виде комиссии, назначаемой владельцем виртуальных денег, или вознаграждения в виде части эмитированной в процессе майнинга криптовалюты. Именно на этом основан один из главных принципов работы платежных систем, предусматривающих использования биткоинов и некоторых других виртуальных денег. В первую очередь обрабатываются и проводятся те транзакции, где установлена самая высокая комиссия. Поэтому сделки с нулевой комиссией могут проводиться очень долго.')
        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = types.KeyboardButton('Что такое майнинг?')
        knopka2 = types.KeyboardButton('Основные принципы работы')
        knopka3 = types.KeyboardButton('Майнинг биткоинов и других криптовалют')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        osn = bot.send_message(messange.chat.id, 'Что Вас интересует?', reply_markup=knopki)
        bot.register_next_step_handler(osn, mine)

    elif messange.text == 'Майнинг биткоинов и других криптовалют':

        m = bot.send_message(messange.chat.id, f'Для чего биткоину нужны майнеры? \n \n'
                                               f'Важно понимать, что распространенное мнение о том, что необходимость в майнинге и, как следствие, майнерах отпадет после выпуска последнего биткоина, крайне далеко от истины. Как уже было сказано, не менее важными функциями майнинга являются обработка информации, проведение транзакций и обеспечение безопасности функционирования платежной системы. Очевидно, что выполнение подобной работы будет требоваться всегда. \n \n'
                                               f'Майнинг Биткоинов \n \n'
                                               f'Безусловно, самой популярной криптовалютой на сегодня является биткоин (в англ. варианте написания – bitcoin), созданный в 2008-2009 годах Сатоси Накамото. Именно поэтому, чаще всего, принимается решение о майнинге именно этого вида виртуальных денег. Однако, необходимо понимать, что оборотной стороной популярности является огромное количество привлеченных для обработки информации ресурсов. Поэтому сегодня для того, чтобы реально заработать на майнинге биткоинов требуется наличие чрезвычайно больших вычислительных мощностей. \n \n'
                                               f'Схемы майнинга \n \n'
                                               f'Простейшая схема майнинга предусматривает установку на компьютер специального программного обеспечения, после чего осуществляется подключение его ресурсов к платежной системе. \n \n'
                                               f'Что такое майнинг ферма? \n \n'
                                               f'Майнинг ферма представляет собой объединенное в одну систему некоторое количество компьютеров или серверов. При этом в разное время и для различных криптовалют используется неодинаковое оборудование. В частности, для «добычи» биткоина несколько лет назад применялись, главным образом, видеокарты, затем их сменили специально разработанные процессоры (ASIC). Вместе с тем, майнинг некоторых криптовалют, например, второго по популярности Ethereum, до сих пор наиболее эффективен при использовании производительных видеокарт. \n \n'
                                               f'Оборудование для майнинга \n \n'
                                               f'Простые схемы майнинга, которые были эффективными несколько лет назад, предусматривали наличие следующего оборудования: 2-3 видеокарт, материнской платы, процессора, оперативной и постоянной памяти, а также блока питания. Естественно, для подключения к системе требовалось установить соответствующее программное обеспечение, которое находится в свободном доступе. Важным ресурсом, который расходуется в процессе майнинга в большом количестве, выступает электроэнергия. \n \n'
                                               f'Программы для майнинга \n \n'
                                               f'В настоящее время разработано множество различных программ, которые могут быть использованы для майнинга криптовалют. Выбор конкретного продукта определяется, прежде всего, возможностями компьютера пользователя. Очевидно, что для разных конфигураций и вычислительной мощности эффективность различных программ буде неодинаковой. Самым простым вариантом майнинга выступает использование облачного пула. В этом случае арендуются или покупаются мощности специализированной компании вместе с установленным на них программным обеспечением. Однако, в большинстве случаев стоимость аренды или приобретения ресурсов достаточно велика. \n \n'
                                               f'Майнинг других криптовалют \n \n'
                                               f'Популярность биткоина, которую он получил в последние годы, вовсе не означает того, что эта криптовалюта сохранит лидирующие позиции навсегда. Напротив, многие специалисты предсказывают появление новых виртуальных денег или выделение какой-либо из уже существующих криптовалют. Дополнительным аргументом в пользу этого выступает тот факт, что любая виртуальная платежная система базируется, прежде всего, на доверии со стороны пользователей. Очевидно, что это является крайне субъективным фактором, который в настоящее время выступает в пользу биткоина, но вполне может обернуться и против него.')

        knopki = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        knopka1 = types.KeyboardButton('Что такое майнинг?')
        knopka2 = types.KeyboardButton('Основные принципы работы')
        knopka3 = types.KeyboardButton('Майнинг биткоинов и других криптовалют')
        knopka4 = types.KeyboardButton('Меню')
        knopki.add(knopka1, knopka2, knopka3, knopka4)
        osn = bot.send_message(messange.chat.id, 'Что Вас интересует?', reply_markup=knopki)

        bot.register_next_step_handler(osn, mine)

    elif messange.text == 'Меню':
        adim(messange)
    elif messange.text == "/close":
        adem(messange)

def adem(message):
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'ок', reply_markup=a)



bot.polling()