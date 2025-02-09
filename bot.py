import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7598938996:AAFf3Rv4r82KzQm6Hgku_-goWMNLxQ8tKJQ"  # Bu joyga bot tokeningizni yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug‘iga javob
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Salom! Ushbu bot guruhda link tashlashni bloklaydi!")

# ❌ Linklarni o‘chirish
@dp.message()
async def filter_links(message: Message):
    if "t.me/" in message.text or "http" in message.text:
        await message.delete()
        await message.answer("❌ Guruhda link tashlash taqiqlangan!")

# 👋 Yangi a'zolarni kutib olish
@dp.message()
async def welcome_message(message: Message):
    if message.new_chat_members:
        for user in message.new_chat_members:
            await message.answer(f"👋 Xush kelibsiz, {user.full_name}!")

# 🔄 Botni ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
