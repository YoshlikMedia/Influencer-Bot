from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import LanguageCallbackData

lang_list = [
    [
        InlineKeyboardButton(
            text="๐บ๐ธ English", callback_data=LanguageCallbackData.new("en")
        ),
        InlineKeyboardButton(
            text="๐ท๐บ ะ ัััะบะธะน", callback_data=LanguageCallbackData.new("ru")
        ),
        InlineKeyboardButton(
            text="๐บ๐ฟ O'zbekcha", callback_data=LanguageCallbackData.new("uz")
        ),
    ]
]

language_keyboard = InlineKeyboardMarkup(inline_keyboard=lang_list)
