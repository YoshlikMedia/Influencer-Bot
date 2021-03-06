from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.texts import (influencers_category,
                        services,
                        user_menu_text,
                        create_post,
                        comment_post
                        )


async def user_menu_keyboard(lang):
    user_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=user_menu_text[lang]["influencers"],
                    callback_data="influencers",
                ),
                InlineKeyboardButton(
                    text=user_menu_text[lang]["brand_buyer"],
                    callback_data="brand_buyer",
                ),
            ],
        ]
    )
    return user_menu


async def influencers_seller_categories(lang):
    keyboard = InlineKeyboardMarkup()
    for item, value in influencers_category[lang].items():
        keyboard.add(InlineKeyboardButton(text=value, callback_data=item))
    return keyboard


async def services_categories(lang):
    keyboard = InlineKeyboardMarkup()
    for item, value in services[lang].items():
        keyboard.add(InlineKeyboardButton(text=value, callback_data=item))
    return keyboard


async def create_post_categories(lang):
    keyboard = InlineKeyboardMarkup()
    for item, value in create_post[lang].items():
        keyboard.add(InlineKeyboardButton(text=value, callback_data=item))
    return keyboard


async def comment_post_categories(lang):
    keyboard = InlineKeyboardMarkup()
    for item, value in comment_post[lang].items():
        keyboard.add(InlineKeyboardButton(text=value, callback_data=item))
    return keyboard