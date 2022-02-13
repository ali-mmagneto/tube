""" !/usr/bin/env python3
    -*- coding: utf-8 -*-
    Name     : inline-tube-mate [ Telegram ]
    Repo     : https://github.com/m4mallu/inine-tube-mate
    Author   : Renjith Mangal [ https://t.me/space4renjith ]
    Credits  : https://github.com/SpEcHiDe/AnyDLBot """

from presets import Presets
from urllib.parse import quote
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Buttons used
start_btn = [
    [
        InlineKeyboardButton('🎖 Geliştirici', url=Presets.SOURCE_URL),
        InlineKeyboardButton('🔰 Destek', url=Presets.SUPPORT_URL)
    ],
    [
        InlineKeyboardButton('📸 Thumbnail', callback_data='view_btn'),
        InlineKeyboardButton('❓ Yardım', callback_data='help_btn')
    ],
    [
        InlineKeyboardButton('❌ Kapat', callback_data='close_btn'),
        InlineKeyboardButton('🔎 Satır İçi Arama', switch_inline_query_current_chat='')
    ]
    ]


del_thumb = [
            [
                InlineKeyboardButton("⛔️ THUMB'ı Sil", callback_data="thumb_del_conf_btn"),
                InlineKeyboardButton("⬅️ Geri", callback_data="a_back_btn")
            ]
            ]


back_button = [
              [
                    InlineKeyboardButton('⬅️ Geri', callback_data='back_btn')
              ]
              ]

close_button = [
               [
                    InlineKeyboardButton('❌ Kapat', callback_data='close_btn'),
                    InlineKeyboardButton('🏠 Ana Sayfa', callback_data='home_btn')
               ]
               ]

cancel_button = [
                [
                    InlineKeyboardButton('❌ İptal ❌', callback_data='cancel_btn')
                ]
                ]

prompt_thumb_btn = [
                   [
                        InlineKeyboardButton('👍🏻 Evet', callback_data='set_thumb_btn'),
                        InlineKeyboardButton('👎🏻 Hayır', callback_data='close_btn')
                   ]
                   ]

# Markups Used
reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_del_thumb = InlineKeyboardMarkup(del_thumb)
reply_markup_start = InlineKeyboardMarkup(start_btn)
reply_markup_thumb = InlineKeyboardMarkup(prompt_thumb_btn)


def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Inline", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share


def get_chat_invite_link(link):
    buttons = [
              [
                  InlineKeyboardButton('❌ Kapat', callback_data='close_btn'),
                  InlineKeyboardButton('Şimdi Katıl', url='{}'.format(link))
              ]
              ]
    reply_markup_invite_link = InlineKeyboardMarkup(buttons)
    return reply_markup_invite_link


def get_public_chat_link(username):
    buttons = [
              [
                  InlineKeyboardButton('❌ Kapat', callback_data='close_btn'),
                  InlineKeyboardButton('Şimdi Katıl', url='https://t.me/{}'.format(username))
              ]
              ]
    reply_markup_public_url = InlineKeyboardMarkup(buttons)
    return reply_markup_public_url
