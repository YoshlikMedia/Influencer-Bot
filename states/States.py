from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    post = State()
    comment = State()