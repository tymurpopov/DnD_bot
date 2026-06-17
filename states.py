from aiogram.fsm.state import State, StatesGroup


class CharacterForm(StatesGroup):
    name = State()
    char_class = State()
    race = State()
    history = State()
    skills = State()
    items = State()