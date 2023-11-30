from aiogram import *
from transformers import pipeline
from time import *
 
bot = Bot(token ='6105952763:AAF0kAeNO2eqZ4NUc-SFRiM8kB7KkH3T50Q')
dp = Dispatcher(bot)

model = pipeline('text-generation',
                model='/content/drive/MyDrive/Innopolis/итоговая аттестация/Model',
                tokenizer='Nehc/gpt2_lovecraft_ru',
                )

@dp.message_handler(commands='start')
async def hello(message:types.message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}, я сейчас попробую придумать, какой-нибудь анекдот ^.^')
    await bot.send_message(message.from_user.id, 'Но мне нужна твоя помощь, напиши мне начало анекдота')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAEKk3dlNOGmi6e0NpzJg-Fz8A4GqZpWFQAChQADS2nuELg_1TGNapL_MAQ')
 
@dp.message_handler(content_types='text')
async def get_text_messages(message:types.message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAEKk3llNOH1Q9qtpAm8A8utOjdzrC-AbgACpQADS2nuEJpkmbQXbXlOMAQ')
    await bot.send_message(message.from_user.id, model(message.text, do_sample=True, max_new_tokens=100)[0]['generated_text'].split('\n')[0])
    sleep(1)
    await bot.send_message(message.from_user.id, f'Давай попробуем еще раз!')

     

if __name__ == '__main__':
    executor.start_polling(dp)