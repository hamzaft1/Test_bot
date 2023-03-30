import os

import updater as updater
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ChatPermissions
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes, MessageHandler
from telegram.ext import CommandHandler
import mysql.connector
import time
import telegram
from mysql.connector import OperationalError


import tracemalloc
import datetime

from telegram.ext.filters import CHAT

tracemalloc.start()

# images
netflix_img = "https://www.canva.com/design/DAFdkkmiZPA/O1viqoSlKRM2mEDnVV2ePw/view?utm_content=DAFdkkmiZPA&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
shahidvip_img = "https://www.canva.com/design/DAFdkg7O5pw/kfqLl6bC3u3n5XAPZSD1eg/view?utm_content=DAFdkg7O5pw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
hbomax_img = "https://www.canva.com/design/DAFdki8Wc2Y/FgSnsnOh7zqoTXNgmOMdpw/view?utm_content=DAFdki8Wc2Y&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
hulu_img = "https://www.canva.com/design/DAFdksOBdWA/qgBmR0-_39xc1OZfgSqtzQ/view?utm_content=DAFdksOBdWA&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
disney_img = "https://www.canva.com/design/DAFdkrEcwME/ZLJQd_ZlzMx6dFxPNE_-hA/view?utm_content=DAFdkrEcwME&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
spotify_img = "https://www.canva.com/design/DAFdko33T9A/5O09AfN_b8E2XK_Mtfl3pg/view?utm_content=DAFdko33T9A&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
deezer_img = "https://www.canva.com/design/DAFdkgYAbDg/XymsPHdaiPQmZ25RVHXbqg/view?utm_content=DAFdkgYAbDg&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
ufc_img = "https://www.canva.com/design/DAFdkvOJATI/Xl37iyObTLnX7oS-uMZRYA/view?utm_content=DAFdkvOJATI&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
nba_img = "https://www.canva.com/design/DAFdkiuF26Q/3q8arvuMX_SlyLUMkw-cfA/view?utm_content=DAFdkiuF26Q&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
canva_img = "https://www.canva.com/design/DAFdkk3pnuQ/Q2ViZWkNIEmm_-JKA7Fefg/view?utm_content=DAFdkk3pnuQ&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"
# TODO(Add bg removale)
# TODO(Add movies downloader)


#Prices
netflix_price= 12
hulu_price= 15
hbomax_price= 14
disney_price= 13
spotify_price= 19
ufc_price= 17
nba_price= 19
shahidvip_price= 14
deezer_price= 11
canva_price= 10


Products = [
    [
        InlineKeyboardButton("❤Netflix🍿", callback_data='netflix'),
        InlineKeyboardButton("💚Hulu📺", callback_data='hulu'),
    ],
    [
        InlineKeyboardButton("💚Shahid VIP🎬", callback_data='shahid vip'),
        InlineKeyboardButton("💜Hbo max🔥", callback_data='hbo max')
    ],
    [

        InlineKeyboardButton("💙Disney +🏰", callback_data='disney +'),
        InlineKeyboardButton("💚Spotify🎧", callback_data='spotify')
    ],
    [
        InlineKeyboardButton("❤UFC🥊", callback_data='ufc'),
        InlineKeyboardButton("💙NBA🏀", callback_data='nba')
    ],
    [
        InlineKeyboardButton("🤍Deezer🎶", callback_data='deezer'),
        InlineKeyboardButton("💙Canva Pro🎨", callback_data='canva'),
    ]
]

# Navigations
NavigationNetflix_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_netflix')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationNetflix_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_netflix')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationShahid_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_shahid')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationShahid_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_shahid')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationHbo_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_hbo')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationHbo_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_hbo')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationHulu_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_hulu')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationHulu_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_hulu')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationDisney_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_disney')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationDisney_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_disney')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationSpotify_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_spotify')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationSpotify_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_spotify')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationDeezer_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_deezer')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationDeezer_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_deezer')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationUfc_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_ufc')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationUfc_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_ufc')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationNba_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_nba')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationNba_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_nba')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

NavigationCanva_eng = [
    [
        InlineKeyboardButton("Purchase", callback_data='purchase_canva')
    ],
    [
        InlineKeyboardButton("Back", callback_data='menu')

    ]
]
NavigationCanva_ar = [
    [
        InlineKeyboardButton("شراء", callback_data='purchase_canva')
    ],
    [
        InlineKeyboardButton("رجوع", callback_data='menu')

    ]
]

# Inline buttons keyboard
Check_eng = [
    [
        InlineKeyboardButton("Check ✅", url='https://t.me/YourPlatinum'),
    ],
    [
        InlineKeyboardButton("Start", callback_data='/start'),
    ]
]
Check_ar = [
    [
        InlineKeyboardButton("تحقق ✅", url='https://t.me/YourPlatinum'),
    ],
    [
        InlineKeyboardButton("بدأ", callback_data='/start'),
    ]
]

# text messages
text_messages_ar = {
    'welcome_1': "<b><u>مرحباً <a href='tg://user?id={}'>{}</a></u></b> !\n\nانضم إلى مجموعتنا <a href='https://t.me/YourPlatinum'><u>Your-Platinum</u></a> لكسب النقاط من خلال دعوة أصدقائك  🙋‍♂️🙋‍♀️ وشراء حسابات مدفوعة مقابل نقاطك💰.\n\nانقر على '<b>تحقق ✅</b>'\n •انضم للمجموعة.\n• اضغط على بدأ",

    'welcome_2': '<u>مرحباً مجددًا <a href="tg://user?id={}">{}</a></u> !\n\nخدماتنا:\n├❤️ Netflix ─➤ <b>{}</b>\n├💚 Hulu ─➤ <b>{}</b>\n├💚 Shahid VIP ─➤ <b>{}</b>\n├💜 HBO Max ─➤ <b>{}</b>\n├💙 Disney + ─➤ <b>{}</b>\n├💚 Spotify ─➤  <b>{}</b>\n├❤️ UFC ─➤ <b>{}</b>\n├💙 NBA ─➤ <b>{}</b>\n├🤍 Deezer ─➤ <b>{}</b>\n├💙 Canva PRO ─➤ <b>{}</b>\n\n<u><b>ستحصل على نقطة عند دعوتك لشخص واحد عبر رابطك الخاص</b></u> !🌟',

    'congrats': "🎉👏<b><u> تهانينا! </u></b>👏🎉\nصديقك (<a href='tg://user?id={}'>{}</a>) انضم إلى <a ref='https://t.me/YourPlatinum'><u>Your-Platinum</u></a> !\n<b>لقد حصلت على نقطة إضافية</b> 🤑.\n\n<b><u>عدد نقاطك الآن: {}</u></b>.\nاستمر في دعوة الأصدقاء وشاهد نقاطك تحلق 🚀.",

    'oops': "✋<u>عذرًا</u>، يبدو أنك غير مستعد حتى الآن لبدء استخدام بوت<a href='https://t.me/YourPlatinum'><b><u> Your-Platinum</u></b></a> !! للوصول إلى جميع الميزات، انضم إلى مجموعتنا.\n\n • انقر على'<b>تحقق ✅</b>'\n •انضم للمجموعة.\n• اضغط على بدأ",

    'successful_purchase': "<b>تهانينا على عملية الشراء 🎉</b>!\n أنت على بعد لحظات من الحصول على <u>حسابك الخاص</u>. توصيلنا السريع يضمن وصول الطلب في غضون <u><b>5 دقائق</b></u> ⏱️. اجلس و <b>استرح</b> 🛋️.\n رضاك هو <b>أولويتنا الأولى</b> ونحن نفتخر بتقديم خدمة استثنائية 👌.",

    'cant_purchase': "🚫 <b>لا يمكن الشراء حالياً</b>.\n🗓️  لا يزال لديك اشتراك  <u>{} يومًا</u>.\n💳 آخر عملية شراء لهذا المنتج كانت في <b>{}</b>\n\n📞 <a href='https://t.me/hamza_farahat'>تواصل مع الدعم الفني في حالة وجود أي استفسار</a>. 👩‍💻",

    'product_solde': "• <s>سعر المنتج الأصلي: {}</s><b><u> 🚫\n• السعر الحالي: {}</u></b> 💰\n\n• نقاطك: {} \n• قابلية شرائه: {}",

    'product': "• <b><u>سعر المنتج: {}\n</u></b>\n• نقاطك: {}\n• قابلية شرائه: {}",

    'pick_favorite': "||spoiler||  *\!اختر المفضل لديك*  ||spoiler||",

    'not_enogh_score': "عذراً <a href='tg://user?id={id}'>{fname}</a> 😕، إنّ نقاطك ({score}) لا تكفي لشراء المنتج.",

    'try_reffer': "حاول استدعاء أصدقاء أكثر.",

    'referral_link': "✅<b><u>سوف تربح نقطة مكافأة من كل شخص تقوم بدعوته عبر رابطك الخاص</u>, إنسخ الرابط ثم قم بمشاركته مع أصدقائك.</b>\n\n🔗رابطك الخاص بك:\n<b><u>https://t.me/your_platinum_bot?start={id}</u></b>",

    'balance': "<b><u> 👋 مرحبًا <a href='tg://user?id={id}'>{fname}</a></u></b>.\n\n•  👥 عدد مشاركتك لرابط الدعوة: {users_rfferred} \n•  📈 عدد المعاملات: {user_purchases} \n\n•  💰<b><u> عدد النقاط: {score}</u></b> ",

    'infos': "<b>•  عند دعوتك لشخص واحد عبر رابطك الخاص سوف تحصل على نقطة مكافأةً  </b>\n\n•  ✅ <u>إثباتات البوت</u>:\n<a href='https://t.me/YourPlatinum'><u>Your-Platinum</u></a>",

    'support': "📞 <a href='https://t.me/hamza_farahat'>تواصل مع الدعم الفني في حالة وجود أي استفسار أو إشكالية</a>. 👩‍💻",

    'soon': "ssss",

    'winners_message': '\n\n\n•  <b>المستخدمين الأكثر مشاركة لرابط الدعوى</b>🔥🏆\n',

    'buyers': '\n\n<b>•  🛒🛍 المستخدمين الأكثر شراء لحساباتنا</b>\n'
}
text_messages_eng = {
    'welcome_1': "<b><u>Welcome <a href='tg://user?id={}'>{}</a></u></b> !\n\nJoin <a href='https://t.me/YourPlatinum'><u>Your-Platinum</u></a> to earn 🏆 by referring 🙋‍♂️🙋‍♀️ and buying 🎬 accounts with 💰. Click <u>/start</u> to activate the 🤖, and unlock 🎁 to get 🏆. Thank you!",

    'welcome_2': '👋 <u>Welcome back <a href="tg://user?id={}">{}</a></u> !\n\n╭─➤𝗦𝗲𝗿𝘃𝗶𝗰𝗲𝘀 𝗠𝗲𝗻𝘂\n├❤️ Netflix ─➤ <b>{}</b>\n├💚 Hulu ─➤ <b>{}</b>\n├💚 Shahid VIP ─➤ <b>{}</b>\n├💜 HBO Max ─➤ <b>{}</b>\n├💙 Disney + ─➤ <b>{}</b>\n├💚 Spotify ─➤  <b>{}</b>\n├❤️ UFC ─➤ <b>{}</b>\n├💙 NBA ─➤ <b>{}</b>\n├🤍 Deezer ─➤ <b>{}</b>\n├💙 Canva PRO ─➤ <b>{}</b>\n╰─➤<u><b>1 FRIEND REFERD = 1 POINT</b></u> !🌟',

    'congrats': "🎉👏<b><u>Congrats!</u></b>👏🎉\nYour friend (<a href='tg://user?id={}'>{}</a>) joined <a href='https://t.me/YourPlatinum'><u>Your-Platinum</u></a>!\n<b>You earn 1 point</b> 🤑 towards your score.\n<b><u>Your score: {}</u></b>.\nKeep inviting friends and watch your score soar 🚀.",

    'oops': "😕 Oops, it looks like you're not ready to start using <a href='https://t.me/YourPlatinum'><b><u>Your-Platinum</u></b></a> bot yet! To access all features, join our group. Click 'CHECK ✅' and follow instructions to get started. We're excited to see you there! 💻🎉",

    'successful_purchase': "<b>Congrats on your 🎉 purchase</b>! You're moments away from accessing <u>your account</u>. Our fast delivery ensures receipt in <u>under <b>5 minutes</b></u> ⏱️. Sit back and <b>relax</b> 🛋️. Your satisfaction is our top <b>priority</b> and we take pride in exceptional service 👌",

    'cant_purchase': "🚫 <b>Can't purchase yet</b>.\n🗓️ Subscription still has ⏳<u>{} days left</u>.\n💳 Your last purchase of this product is <b>{}</b>\n\n📞 <a href='https://t.me/hamza_farahat'>Contact support with any questions</a>. 👩‍💻",

    'product_solde': "• <s>Product price : {}</s><b><u> 🚫\n• Purchase coast : {}</u></b> 💰\n\n• Your score : {} \n• Your possibility for buying it: {}",

    'product': "• <b><u>Product price : {}\n</u></b>\n• Your score : {}\n• Your possibility for buy it: {}",

    'pick_favorite': "||spoiler|| *Pick your favorite\!* ||spoiler||",

    'not_enogh_score': "Sorry {fname} 😕,Your score ({score}) is not enough to purchase the product.",

    'try_reffer': "Try to refferr more friends.",

    'referral_link': '🔗 Your Refferral Link:\n\n https://t.me/your_platinum_bot?start={id}',

    'balance': "<u><b>👋 Hello <a href='tg://user?id={id}'>{fname}</a></b></u>.\n\n•  👥 Your number of referrals: {users_rfferred} \n•  📈 Transaction numbers: {user_purchases} \n\n•  💰<b><u> Numbers of points: {score}</u></b> ",

    'infos': "<b>• When you invite one person through your own link, you will receive a reward point</b> \n\n• ✅ <u>Bot proofs</u>: <a href='https://t.me/YourPlatinum'><u><b>Your-Platinum</b></u></a>",

    'support': "📞 <a href='https://t.me/hamza_farahat'>Contact support with any questions</a>. 👩‍💻",

    'soon': "ssss",

    'winners_message': '\n\n•  🔥🏆 <b>Highest scores </b>\n',

    'buyers': '\n\n<b>• ✅ The most buying users of our accounts 🛒🛍️</b>\n'

}

# Cast navigation buttons
Products = InlineKeyboardMarkup(Products)
Check_eng = InlineKeyboardMarkup(Check_eng)
Check_ar = InlineKeyboardMarkup(Check_ar)
NavigationNetflix_eng = InlineKeyboardMarkup(NavigationNetflix_eng)
NavigationNetflix_ar = InlineKeyboardMarkup(NavigationNetflix_ar)
NavigationShahid_eng = InlineKeyboardMarkup(NavigationShahid_eng)
NavigationShahid_ar = InlineKeyboardMarkup(NavigationShahid_ar)
NavigationHbo_eng = InlineKeyboardMarkup(NavigationHbo_eng)
NavigationHbo_ar = InlineKeyboardMarkup(NavigationHbo_ar)
NavigationHulu_eng = InlineKeyboardMarkup(NavigationHulu_eng)
NavigationHulu_ar = InlineKeyboardMarkup(NavigationHulu_ar)
NavigationDisney_eng = InlineKeyboardMarkup(NavigationDisney_eng)
NavigationDisney_ar = InlineKeyboardMarkup(NavigationDisney_ar)
NavigationSpotify_eng = InlineKeyboardMarkup(NavigationSpotify_eng)
NavigationSpotify_ar = InlineKeyboardMarkup(NavigationSpotify_ar)
NavigationDeezer_eng = InlineKeyboardMarkup(NavigationDeezer_eng)
NavigationDeezer_ar = InlineKeyboardMarkup(NavigationDeezer_ar)
NavigationUfc_eng = InlineKeyboardMarkup(NavigationUfc_eng)
NavigationUfc_ar = InlineKeyboardMarkup(NavigationUfc_ar)
NavigationNba_eng = InlineKeyboardMarkup(NavigationNba_eng)
NavigationNba_ar = InlineKeyboardMarkup(NavigationNba_ar)
NavigationCanva_eng = InlineKeyboardMarkup(NavigationCanva_eng)
NavigationCanva_ar = InlineKeyboardMarkup(NavigationCanva_ar)

# Keyboard buttons
choice_eng = [["💰 Balance", "👥 Refferr"], ["📝 Infos", "🆘 Support"], ["🚀 Soon"]]
choice_ar = [["أرباحي 💰", "رابط الدعوة 👥"], ["ما هذا البوت ⁉", "الدعم 🆘"], ["قريبا 🚀ً"]]
choice_eng = ReplyKeyboardMarkup(choice_eng, resize_keyboard=True)
choice_ar = ReplyKeyboardMarkup(choice_ar, resize_keyboard=True)

# MysQl connection
HOST = "sql8.freesqldatabase.com"
USER = "sql8606789"
PASSWORd = "NAIRBrYKxp"
DATABASE = "sql8606789"

config = {
    "host": HOST,
    "user": USER,
    "password": PASSWORd,
    "database": DATABASE
}

def connect():
    try:
        return mysql.connector.connect(**config)
    except Exception as e:
        print(e)
        time.sleep(2)
        connect()

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

TOKEN = os.getenv("TOKEN")
URL = "https://test-bot-fawn.vercel.app"
PORT = int(os.getenv('8080', '5000'))

def SELECT_ONE(query, conn=conn):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()

        else:
            # conn.reconnect()
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
        conn.commit()
        return row

    except OperationalError as e:
        print(f"Error connecting to MySQL: {e}")

    except Exception as e:
        print(f"Error executing query: {e}")

def SELECT_ALL(query, conn=conn):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
        else:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
        conn.commit()
        return row

    except OperationalError as e:
        print(f"Error connecting to MySQL: {e}")

    except Exception as e:
        print(f"Error executing query: {e}")

def EXECUTE(query, conn=conn):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
        else:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)

        conn.commit()
    except OperationalError as e:
        print(f"Error connecting to MySQL: {e}")

    except Exception as e:
        print(f"Error executing query: {e}")

def INSERT(query, conn=conn):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
        else:
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)

        conn.commit()
        return False
    except Exception as e:
        print(f"Error executing query: {e}")
        return True

async def rewarding(code, red_flag, context, user, text_messages):
    if code is not None:
        if not red_flag:
            row1 = SELECT_ONE(f'SELECT * FROM users_data WHERE user_id = "{code}";')
            score = row1[2]

            row2 = SELECT_ONE(f'SELECT * FROM users_data WHERE user_id = "{user.id}";')
            id = row2[0]
            fname = row2[1]

            await context.bot.send_message(chat_id=code,
                                           text=text_messages['congrats'].format(id, fname, score + 1),
                                           parse_mode='HTML')
            EXECUTE(
                f'UPDATE users_data SET user_score = user_score + 1, users_rfferred = users_rfferred + 1 WHERE user_id = "{code}"')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    print("chat id -> "+ str(update.message.chat_id))
    await context.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
    print(f'{datetime.datetime.now()} -> some one starts the bot')
    # Basic Data
    user = update.message.from_user
    member = await context.bot.get_chat_member(chat_id="@YourPlatinum", user_id=user.id)
    id = user.id
    fname = user.first_name
    red_flag = False

    # Insert the user at db
    try:
        if not member.user.is_bot:
            red_flag = INSERT(
                f'INSERT INTO users_data (user_id, user_firstname, user_language) VALUES ("{id}", "{fname}", "{member.user.language_code}")')
    except Exception as e:
        red_flag = True

    row = SELECT_ONE(f'SELECT user_language FROM users_data WHERE user_id = "{id}";')

    # Language builder
    Check = Check_eng
    text_messages = text_messages_eng
    choice = choice_eng
    if row[0] in ['fr', 'ar']:
        text_messages = text_messages_ar
        choice = choice_ar
        Check = Check_ar

    # checking if start had referral link
    if len(update.message.text.split()) > 1:
        code = update.message.text.split()[1]
        await rewarding(code, red_flag, context, user, text_messages)

    # Check user if membership
    try:
        if member.status in ['member', 'creator']:
            await clear_previuos_messages(context, update, update.message.message_id)
        else:
            await update.message.reply_text(
                text=text_messages['welcome_1'].format(id, fname),
                parse_mode='HTML', reply_markup=Check)
            return
    except Exception as e:
        return

    await update.message.delete()

    # delete all previous messages
    await clear_previuos_messages(context, update, update.message.message_id)




    # welcome if user member
    await update.message.reply_text(
        text=text_messages['welcome_2'].format(id, fname, netflix_price, hulu_price,shahidvip_price, hbomax_price, disney_price, spotify_price, ufc_price, nba_price, deezer_price, canva_price),
        parse_mode='HTML')
    await update.message.reply_text(text_messages['pick_favorite'], reply_markup=Products,
                                    parse_mode='MARKDOWNV2')
    await update.message.reply_text("<a href='https://t.me/YourPlatinum'><b><u>Your-Platinum</u></b></a>",
                                    parse_mode='HTML', reply_markup=choice)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'{datetime.datetime.now()} -> inline')
    # Basic Data
    query = update.callback_query
    user = update.callback_query.from_user

    # User Data
    try:
        member = await context.bot.get_chat_member(chat_id="@YourPlatinum", user_id=user.id)
        row = SELECT_ONE(f'SELECT * FROM users_data WHERE user_id = "{user.id}";')
        id = row[0]
        score = row[2]
    except Exception as e:
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text='click /start')
        return

    # Language builder
    choice = choice_eng
    text_messages = text_messages_eng
    NavigationNetflix = NavigationNetflix_eng
    NavigationHulu = NavigationHulu_eng
    NavigationShahid = NavigationShahid_eng
    NavigationHbo = NavigationHbo_eng
    NavigationDisney = NavigationDisney_eng
    NavigationSpotify = NavigationSpotify_eng
    NavigationUfc = NavigationUfc_eng
    NavigationNba = NavigationNba_eng
    NavigationDeezer = NavigationDeezer_eng
    NavigationCanva = NavigationCanva_eng
    Check = Check_eng
    if row[5] in ['fr', 'ar']:
        text_messages = text_messages_ar
        choice = choice_ar
        NavigationNetflix = NavigationNetflix_ar
        NavigationHulu = NavigationHulu_ar
        NavigationShahid = NavigationShahid_ar
        NavigationHbo = NavigationHbo_ar
        NavigationDisney = NavigationDisney_ar
        NavigationSpotify = NavigationSpotify_ar
        NavigationUfc = NavigationUfc_ar
        NavigationNba = NavigationNba_ar
        NavigationDeezer = NavigationDeezer_ar
        Check = Check_ar
        NavigationCanva = NavigationCanva_ar

    # Check membership when user clicks start Button (not /start)
    if query.data == "/start" or member.status == "left":
        if query.data == "/start" and member.status != "left":
            await clear_previuos_messages(context, query, query.message.message_id + 1)
            await context.bot.send_message(chat_id=query.message.chat_id, text="/start")
        else:
            await clear_previuos_messages(context, query, query.message.message_id + 1)
            await context.bot.send_message(chat_id=query.message.chat_id,
                                           text=text_messages['oops'],
                                           reply_markup=Check, parse_mode='HTML')

    # Check tricky members
    if member.status == "left":
        await clear_previuos_messages(context, query, query.message.message_id)
        return
    if query.data in ['netflix', 'purchase_netflix']:
        possible = "✅" if score >= netflix_price else "❌"
        purchase = True if score >= netflix_price else False

        if query.data == 'netflix':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=netflix_img,
                                         caption="||spoiler|| 🎞️ *Netflix* 🎥 ||spoiler||", parse_mode='MARKDOWNV2')

            await context.bot.send_message(
                text=text_messages['product_solde'].format(netflix_price+3, netflix_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationNetflix, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -netflix_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['shahid vip', 'purchase_shahid']:
        possible = "✅" if score >= shahidvip_price else "❌"
        purchase = True if score >= shahidvip_price else False

        if query.data == 'shahid vip':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=shahidvip_img,
                                         caption="||spoiler|| 📱 *Shahid VIP* 🖥️ ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(shahidvip_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationShahid, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -shahidvip_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['hbo max', 'purchase_hbo']:
        possible = "✅" if score >= hbomax_price else "❌"
        purchase = True if score >= hbomax_price else False

        if query.data == 'hbo max':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=hbomax_img,
                                         caption="||spoiler|| 🔥 *HBO max* 💥 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(hbomax_price, score, possible), chat_id=query.message.chat_id,
                reply_markup=NavigationHbo, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -hulu_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['hulu', 'purchase_hulu']:
        possible = "✅" if score >= hulu_price else "❌"
        purchase = True if score >= hulu_price else False

        if query.data == 'hulu':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=hulu_img,
                                         caption="||spoiler|| 🍕 *Hulu* 🍿 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(hulu_price, score,
                                                     possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationHulu, parse_mode='HTML')
        else:
            if purchase:
                await purchase_item(context, query, id, -hulu_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['disney +', 'purchase_disney']:
        possible = "✅" if score >= deezer_price else "❌"
        purchase = True if score >= deezer_price else False

        if query.data == 'disney +':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=disney_img,
                                         caption="||spoiler|| 🎢 *Disney \+* 🌟 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(deezer_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationDisney, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -deezer_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['spotify', 'purchase_spotify']:

        possible = "✅" if score >= spotify_price else "❌"
        purchase = True if score >= spotify_price else False

        if query.data == 'spotify':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=spotify_img,
                                         caption="||spoiler|| 🔊 *Spotify* 🎼 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(spotify_price, score,
                                                           possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationSpotify, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -spotify_price, query.data, row[5])

            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['deezer', 'purchase_deezer']:
        possible = "✅" if score >= deezer_price else "❌"
        purchase = True if score >= deezer_price else False

        if query.data == 'deezer':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=deezer_img,
                                         caption="||spoiler|| 💿 *Deezer* 🎵 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(deezer_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationDeezer, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -deezer_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['ufc', 'purchase_ufc']:
        possible = "✅" if score >= ufc_price else "❌"
        purchase = True if score >= ufc_price else False

        if query.data == 'ufc':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=ufc_img,
                                         caption="||spoiler|| 🤼‍♂️ *UFC* 👊 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(ufc_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationUfc, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -ufc_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['nba', 'purchase_nba']:
        possible = "✅" if score >= nba_price else "❌"
        purchase = True if score >= nba_price else False

        if query.data == 'nba':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=nba_img,
                                         caption="||spoiler|| 🏆 *NBA* 🏀 ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product'].format(nba_price, score,
                                                           possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationNba, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -nba_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data in ['canva', 'purchase_canva']:
        possible = "✅" if score >= canva_price else "❌"
        purchase = True if score >= canva_price else False

        if query.data == 'canva':
            await query.delete_message()
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=canva_img,
                                         caption="||spoiler|| 🎨 *Canva Pro* ✏️ ||spoiler||", parse_mode='MARKDOWNV2')
            await context.bot.send_message(
                text=text_messages['product_solde'].format(canva_price+2, canva_price, score, possible),
                chat_id=query.message.chat_id,
                reply_markup=NavigationCanva, parse_mode='HTML')

        else:
            if purchase:
                await purchase_item(context, query, id, -canva_price, query.data, row[5])
            else:
                await not_enoth_score(context, query, id, row[5])
    elif query.data == 'menu':
        # delete all previous messages
        await clear_previuos_messages(context, query, query.message.message_id)
        await query.edit_message_text(text_messages['pick_favorite'], reply_markup=Products,
                                      parse_mode='MARKDOWNV2')
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="<a href='https://t.me/YourPlatinum'><b><u>Your-Platinum</u></b></a>",
                                       parse_mode='HTML', reply_markup=choice)
    elif query.data == 'refferr':
        await clear_previuos_messages(context, query, query.message.message_id)
        await query.edit_message_text(
            text=f'🔗 Your Refferral Link: <b><a href="https://t.me/your_platinum_bot?start={id}"><u>Your-Link</u></a></b>',
            parse_mode='HTML')

async def delete_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.effective_message.id)

    if update.message.new_chat_members:
            await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.effective_message.id)
    elif update.message.left_chat_member:
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.effective_message.id)

async def response_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'{datetime.datetime.now()} -> keyboard')
    if update.message.chat_id == -1001875313753:
        curent_message = update.message.text.lower()
        if curent_message and "@" in curent_message:
            for word in curent_message.split():
                if "@" in word:
                    group_username = word[1:]  # remove the "@" symbol
                    try:

                        chat = await context.bot.get_chat("@" + group_username)
                        print(1)
                        print(chat.type)
                        print(2)
                        if chat.type == "group":
                            context.bot.send_message(chat_id=update.message.chat_id, text='This message mentions a group!')
                            break
                    except telegram.error.BadRequest as e:
                        print(e)
                        pass
        black_list= ["fuck", "a vendre","shit"]
        for message in black_list:
            if message in curent_message:
                await update.message.reply_text("7imaariyyon")
                await update.message.delete()
                break



        '''time.sleep(2)
        ban_duration = datetime.datetime.now() + datetime.timedelta(seconds=10)



        time.sleep(3)
        permissions = ChatPermissions(can_send_messages=True)
        await context.bot.restrict_chat_member(chat_id=update.effective_chat.id, user_id=update.effective_user.id, permissions=permissions)
        '''

        return
    # Basic data
    curent_message = update.message.text.lower()
    user = update.message.from_user

    member = await context.bot.get_chat_member(chat_id="@YourPlatinum", user_id=user.id)

    # User Data
    try:
        row = SELECT_ONE(f'SELECT * FROM users_data WHERE user_id = "{user.id}";')
        print(user.id)
        print(0)
        id = int(row[0])
        print(1)
        fname = row[1]
        print(2)
        users_rfferred = row[3]
        user_purchases = row[4]
        score = row[2]
        admin = id == 1752221538
    except Exception as e:
        await context.bot.send_message(chat_id=update.message.chat_id,
                                       text='click /start')
        print(e)
        return

    # Language builder
    text_messages = text_messages_eng
    if row[5] in ['fr', 'ar']:
        text_messages = text_messages_ar

    if curent_message in ["💰 balance", "أرباحي 💰"]:

        winners = SELECT_ALL('Select user_id ,user_firstname ,users_rfferred FROM sql8606789.users_data where users_rfferred>0 and user_id not in ("5735481926", "1752221538", "6229141024") order by users_rfferred DESC limit 5;')

        winners_message= text_messages['winners_message']
        rewards= ['🥇','🥈','🥉','🏅','🎖']
        i = 0
        for winner in winners:
            winners_message += f"<a href = 'tg://user?id={winner[0]}' > {winner[1]}</a> -> {winner[2]} {rewards[i]}\n"
            i+= 1

        await context.bot.send_message(chat_id=update.message.chat_id,
                                       text=text_messages['balance'].format(id=id, fname=fname,
                                                                            users_rfferred=users_rfferred,
                                                                            user_purchases=user_purchases, score=score) + winners_message,
                                       parse_mode='HTML')

    elif curent_message in ["👥 refferr", "رابط الدعوة 👥"]:
        await context.bot.send_message(chat_id=update.message.chat_id,
                                       text=text_messages['referral_link'].format(id=id),
                                       parse_mode='HTML')

    elif curent_message in ["📝 infos", "ما هذا البوت ⁉"]:

        buyers = SELECT_ALL('SELECT user_id ,user_firstname ,user_purchases FROM sql8606789.users_data where user_purchases> 0 and user_id not in ("5735481926", "1752221538", "6229141024") order by user_purchases DESC limit 5;')

        buyers_message= text_messages['buyers']
        for buyer in buyers:
            buyers_message += f"<a href = 'tg://user?id={buyer[0]}' > {buyer[1]}</a> -> {buyer[2]}  🤝\n"


        await context.bot.send_message(chat_id=update.message.chat_id, text=text_messages['infos'] + buyers_message,
                                       parse_mode='HTML')

    elif curent_message in ["🆘 support", "الدعم 🆘"]:
        await context.bot.send_message(chat_id=update.message.chat_id, text=text_messages['support'],
                                       parse_mode='HTML')

    elif curent_message in ["🚀 soon", "قريبا 🚀ً"]:
        await context.bot.send_message(chat_id=update.message.chat_id, text='Soon')

    elif curent_message == 'dola' and admin:
        await context.bot.send_message(chat_id=update.message.chat_id, text='xh7al kayn\nnno9at')

    elif curent_message == 'xh7al kayn' and admin:
        how_much = SELECT_ONE(f'SELECT count(*) as "Members t zzeb" FROM sql8606789.users_data;')
        await context.bot.send_message(chat_id=update.message.chat_id, text=how_much[0])

    elif curent_message == 'nno9at' and admin:
        winners = SELECT_ALL(
            f"SELECT user_id ,user_firstname ,user_score FROM sql8606789.users_data where user_score > 0 and user_id not in ('5735481926', '1752221538') order by user_score DESC ;")

        list = ''
        i = 1
        for winner in winners:
            list += f"{i}- <a href = 'tg://user?id={winner[0]}' > {winner[1]}</a> -> {winner[2]} pts\n"
            i += 1

        await context.bot.send_message(chat_id=update.message.chat_id, text=list, parse_mode='HTML')

# useful functions
async def purchase_item(context, query, id, price, product=None, language='en') -> None:
    row = SELECT_ONE(f'SELECT {product}, user_firstname FROM users_data WHERE user_id = "{id}"')
    last_purchase_date = row[0]
    fname = row[1]

    text_messages = text_messages_eng
    if language in ['fr', 'ar']:
        text_messages = text_messages_ar

    subscription_days = (datetime.date.today() - last_purchase_date).days
    if subscription_days >= 30:
        await context.bot.send_chat_action(chat_id=query.message.chat_id, action="typing")
        # Updating the purchase's data
        EXECUTE(
            f'UPDATE users_data SET user_score = user_score {price}, user_purchases = user_purchases + 1, {product} = "{datetime.date.today()}" WHERE user_id = "{id}"')
        await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                            text=text_messages['successful_purchase'],
                                            parse_mode='HTML')
        await context.bot.send_message(chat_id=1752221538,
                                       text=f"<a href='tg://user?id={id}'>{fname}</a> -> {product}",
                                       parse_mode='HTML')
        await context.bot.send_message(chat_id=5735481926,
                                       text=f"<a href='tg://user?id={id}'>{fname}</a> -> {product}",
                                       parse_mode='HTML')


    else:
        await context.bot.send_chat_action(chat_id=query.message.chat_id, action="typing")
        subscription_days = 30 - subscription_days
        await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                            text=text_messages['cant_purchase'].format(
                                                subscription_days,
                                                last_purchase_date),
                                            parse_mode='HTML')

async def not_enoth_score(context, query, id, language='en') -> None:
    await context.bot.send_chat_action(chat_id=query.message.chat_id, action="typing")
    # User Data
    row = SELECT_ONE(f'SELECT * FROM users_data WHERE user_id = "{id}";')

    fname = row[1]
    score = row[2]

    # Inline Buttons keyboard
    Back_eng = [
        [
            InlineKeyboardButton("Refferr", switch_inline_query=f'https://t.me/your_platinum_bot?start={row[0]}')
        ],
        [
            InlineKeyboardButton("Back", callback_data='menu')
        ]
    ]
    Back_ar = [
        [
            InlineKeyboardButton("قم بدعوة أصدقائك 🙋‍♂️🙋‍♀️",
                                 switch_inline_query=f'https://t.me/your_platinum_bot?start={row[0]}')
        ],
        [
            InlineKeyboardButton("رجوع", callback_data='menu')
        ]
    ]
    Back_eng = InlineKeyboardMarkup(Back_eng)
    Back_ar = InlineKeyboardMarkup(Back_ar)

    # Language builder
    text_messages = text_messages_eng
    Back = Back_eng
    if language in ['fr', 'ar']:
        text_messages = text_messages_ar
        Back = Back_ar

    await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                        text=text_messages['not_enogh_score'].format(id=id, fname=fname,
                                                                                     score=score), parse_mode='HTML')
    time.sleep(4)
    await context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id,
                                        text=text_messages['try_reffer'], reply_markup=Back)

async def clear_previuos_messages(context, query, mssg_id) -> None:
    i = 1
    while (True):
        try:
            await context.bot.delete_message(chat_id=query.message.chat_id, message_id=mssg_id - i)
            i += 1

        except Exception as e:
            if str(e) == "Message to delete not found":
                i += 1
                if i >= 7:
                    break
            else:
                break




# bot connexion
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(MessageHandler(telegram.ext.filters.StatusUpdate.NEW_CHAT_MEMBERS | telegram.ext.filters.StatusUpdate.LEFT_CHAT_MEMBER, delete_member))
app.add_handler(MessageHandler(telegram.ext.filters.ALL, response_message))

webhook_url = '{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN)
app.bot.setWebhook(webhook_url)
app.run_polling()
