from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎲 Roll Dice"),
            KeyboardButton(text="🧙 Create Character")
        ],
        [
            KeyboardButton(text="📜 My Character"),
            KeyboardButton(text="📖 D&D Rules")
        ],
        [
            KeyboardButton(text="❓ What is D&D")
        ]
    ],
    resize_keyboard=True
)

dice_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="D4"),
            KeyboardButton(text="D6")
        ],
        [
            KeyboardButton(text="D8"),
            KeyboardButton(text="D10")
        ],
        [
            KeyboardButton(text="D12"),
            KeyboardButton(text="D20")
        ],
        [
            KeyboardButton(text="D100")
        ]
    ],
    resize_keyboard=True
)