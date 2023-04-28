from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
import parse
import time
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
class Form(StatesGroup):
    peremennaya = State()
def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    spisok = []
    spisok2 = []
    @dp.message_handler(commands=["start"])
    async def begin(message: types.Message):
        await bot.send_message(message.chat.id, "Посмотреть текущие курсы известных криптовалют - /cryptocheck \nВыбрать криптовалюту для указания нижнего и верхнего порогра стоимости - /limit")


    @dp.message_handler(commands=['help'])
    async def process_help_command(message: types.Message):
        await bot.send_message(message.chat.id, '1')


    @dp.message_handler(commands=['cryptocheck'])
    async def listcrypt(message: types.Message):
        curen = parse.currency()
        await bot.send_message(message.chat.id, curen)

    @dp.message_handler(commands=['limit'])
    async def handle_message(message: types.Message):
        await message.reply("Введите сначала верхний предел, затем нижний и название криптовалюты ( 30350 30270 BTC)")

        @dp.message_handler()
        async def handle_message(message: types.Message):
            string = message.text
            spisok = string.split()

            f = open('limits.txt', 'w+')
            for element in spisok:
                f.write(str(element))
                f.write('\n')
            f.close()
            f = open('limits.txt', 'r')
            lines = f.readlines()
            spisok2 = []
            for line in lines:
                spisok2.append(line.replace('\n',''))
            print(spisok, spisok2)
            while (parse.limitcheck(spisok2[2]) < float(spisok2[0]) and parse.limitcheck(spisok2[2]) > float(spisok2[1])):
                print(parse.limitcheck(spisok2[2]))
                time.sleep(2)
            if (parse.limitcheck(spisok2[2]) < float(spisok2[1])):
                await message.reply('Курс доллара вышел за нижний предел!')
            else:
                await message.reply('Курс доллара вышел за верхний предел!')

    if __name__ == "bot":
        executor.start_polling(dp, skip_updates=True)