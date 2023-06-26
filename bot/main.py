import telebot
from django.conf import settings

from users.models import User

API_TOKEN = settings.BOT_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=["users"])
def get_users_handler(message):
    users = User.objects.values("id", "first_name", "last_name")  # [{"first_name": "A", "last_name": "B"}]
    msg = ""
    for i, user in enumerate(users):
        msg += f"{i + 1}. {user.get('first_name')} {user.get('last_name')} | ID: {user.get('id')}\n"
    bot.send_message(message.chat.id, text=msg)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Boshlash"),
        telebot.types.BotCommand("users", "Foydalanuvchilar")
    ],
)
