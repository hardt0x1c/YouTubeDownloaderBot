import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import bot_token
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import FSInputFile
import messages as msg
from States import UserSendURL
from main import youtube_downloader


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer(msg.greet)
    await state.set_state(UserSendURL.send_url)


# Обработчик состояния
@dp.message(UserSendURL.send_url)
async def download(message: types.Message, state: FSMContext):
    url = message.text
    video_dowloaded = youtube_downloader(url)
    video = FSInputFile('downloads/videos/video.mp4')
    await message.answer_video(video, caption=f'Видео по ссылке {url}')


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())