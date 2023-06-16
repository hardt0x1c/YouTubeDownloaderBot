from aiogram.fsm.state import StatesGroup, State


class UserSendURL(StatesGroup):
    send_url = State()
