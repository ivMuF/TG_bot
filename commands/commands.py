from loader import dp
from aiogram import executor, types
from api.site_API import headers, url, site_api

bot_start = executor.start_polling
user_data = {}


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Введи город!')


async def handler_group(callback, data, group_name):
    for i in data['suggestions']:
        if i['group'] == group_name:
            if i['entities']:
                for j in i['entities']:
                    await callback.message.answer(j['name'])
            else:
                await callback.message.answer('Раздел в разработке')


@dp.callback_query_handler(text='Hotels')
async def answer_hotels(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await handler_group(callback, user_data[user_id], 'HOTEL_GROUP')


@dp.callback_query_handler(text='Landmark')
async def answer_landmark(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await handler_group(callback, user_data[user_id], 'LANDMARK_GROUP')


@dp.callback_query_handler(text='Transport')
async def answer_landmark(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await handler_group(callback, user_data[user_id], 'TRANSPORT_GROUP')


@dp.message_handler()
async def name_city(message: types.Message):
    locations = site_api.get_locations()
    params = {"query": message.text, "locale": "ru_RU"}
    response = locations("GET", url, headers=headers, params=params)
    user_data[message.from_id] = response.json()

    button = [
        types.InlineKeyboardButton(text='Отели', callback_data='Hotels'),
        types.InlineKeyboardButton(text='Места', callback_data='Landmark'),
        types.InlineKeyboardButton(text='Транспорт', callback_data='Transport')
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*button)

    await message.answer('Что вы хотите:', reply_markup=keyboard)


if __name__ == '__main__':
    bot_start()
