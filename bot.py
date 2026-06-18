import telebot
from telebot import types

TOKEN = '8666296987:AAH0L5W2hsErd1R4JCORh9mT5CuuBrARHR8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_pubg = types.InlineKeyboardButton("🎮 PUBG Mobile (UC)", callback_data="pubg")
    btn_ff = types.InlineKeyboardButton("🔥 Free Fire (Diamonds)", callback_data="freefire")
    btn_clash = types.InlineKeyboardButton("🏰 Clash of Clans", callback_data="clash")
    btn_admin = types.InlineKeyboardButton("👨‍💻 Admin bilan bog'lanish", callback_data="admin")
    markup.add(btn_pubg, btn_ff, btn_clash, btn_admin)
    bot.send_message(message.chat.id, "Salom! **All Games Donate** botiga xush kelibsiz. Kerakli o'yinni tanlang:", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    m_id = call.message.message_id
    if call.data == "pubg":
        text = "🛒 **PUBG Mobile UC tariflari:**\n\n🔹 60 UC — 12 000 so'm\n🔹 325 UC — 55 000 so'm\n🔹 660 UC — 110 000 so'm\n\n💳 To'lov qilish va sotib olish uchun @ziroc0 bilan bog'laning."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=m_id, text=text, parse_mode="Markdown")
    elif call.data == "freefire":
        text = "🛒 **Free Fire Olmos tariflari:**\n\n🔹 100 Olmos — 15 000 so'm\n🔹 310 Olmos — 40 000 so'm\n\n💳 To'lov uchun @ziroc0 bilan bog'laning."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=m_id, text=text, parse_mode="Markdown")
    elif call.data == "clash":
        text = "🛒 **Clash of Clans tariflari:**\n\n🔹 Gold Pass — 65 000 so'm\n\n💳 To'lov uchun @ziroc0 bilan bog'laning."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=m_id, text=text, parse_mode="Markdown")
    elif call.data == "admin":
        text = "👨‍💻 Savollar va takliflar bo'yicha adminga yozing: @ziroc0"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=m_id, text=text, parse_mode="Markdown")

bot.infinity_polling()
