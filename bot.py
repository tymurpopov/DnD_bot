import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import TOKEN
from keyboards import (
    main_keyboard,
    dice_keyboard
)
from states import CharacterForm
from database import (
    save_character,
    get_character
)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Welcome to D&D Bot!",
        reply_markup=main_keyboard
    )


@dp.message(F.text == "📖 D&D Rules")
async def rules(message: Message):
    await message.answer(
        "https://www.dndbeyond.com/sources/dnd/phb-2024"
    )


@dp.message(F.text == "❓ What is D&D")
async def what_is_dnd(message: Message):
    await message.answer(
        "Dungeons & Dragons is a fantasy tabletop role-playing game."
    )


@dp.message(F.text == "🎲 Roll Dice")
async def dice_menu(message: Message):
    await message.answer(
        "Choose a dice:",
        reply_markup=dice_keyboard
    )


@dp.message(
    F.text.in_([
        "D4",
        "D6",
        "D8",
        "D10",
        "D12",
        "D20",
        "D100"
    ])
)
async def roll_dice(message: Message):
    size = int(message.text[1:])
    result = random.randint(1, size)

    await message.answer(
        f"🎲 Result: {result}",
        reply_markup=main_keyboard
    )


# Character Creation

@dp.message(F.text == "🧙 Create Character")
async def create_character(
    message: Message,
    state: FSMContext
):
    await state.set_state(CharacterForm.name)
    await message.answer("Character name:")


@dp.message(CharacterForm.name)
async def get_name(
    message: Message,
    state: FSMContext
):
    await state.update_data(name=message.text)
    await state.set_state(CharacterForm.char_class)
    await message.answer("Character class:")


@dp.message(CharacterForm.char_class)
async def get_class(
    message: Message,
    state: FSMContext
):
    await state.update_data(char_class=message.text)
    await state.set_state(CharacterForm.race)
    await message.answer("Character race:")


@dp.message(CharacterForm.race)
async def get_race(
    message: Message,
    state: FSMContext
):
    await state.update_data(race=message.text)
    await state.set_state(CharacterForm.history)
    await message.answer("Character history:")


@dp.message(CharacterForm.history)
async def get_history(
    message: Message,
    state: FSMContext
):
    await state.update_data(history=message.text)
    await state.set_state(CharacterForm.skills)
    await message.answer("Character skills:")


@dp.message(CharacterForm.skills)
async def get_skills(
    message: Message,
    state: FSMContext
):
    await state.update_data(skills=message.text)
    await state.set_state(CharacterForm.items)
    await message.answer("Character items:")


@dp.message(CharacterForm.items)
async def get_items(
    message: Message,
    state: FSMContext
):
    await state.update_data(items=message.text)

    data = await state.get_data()

    save_character(
        message.from_user.id,
        data
    )

    await state.clear()

    await message.answer(
        "✅ Character saved!",
        reply_markup=main_keyboard
    )


# View Character

@dp.message(F.text == "📜 My Character")
async def show_character(message: Message):
    character = get_character(
        message.from_user.id
    )

    if not character:
        await message.answer(
            "You don't have a character yet."
        )
        return

    _, name, char_class, race, history, skills, items = character

    await message.answer(
        f"🧙 Name: {name}\n\n"
        f"⚔️ Class: {char_class}\n"
        f"🧝 Race: {race}\n\n"
        f"📖 History:\n{history}\n\n"
        f"✨ Skills:\n{skills}\n\n"
        f"🎒 Items:\n{items}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())