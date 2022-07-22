from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    location = State()


class Location(StatesGroup):
    location = State()
