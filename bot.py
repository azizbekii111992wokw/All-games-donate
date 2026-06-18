import telebot
from telebot import types

TOKEN = '8666296987:AAH0L5W2hsErd1R4JCORH'
bot = telebot.TeleBot(TOKEN)

# Bosh menyu tugmalarini yaratish funksiyasi
def get_main_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn_pubg = types.InlineKeyboardButton(text="🎮 PUBG Mobile", callback_data="pubg")
    btn_ff = types.InlineKeyboardButton(text="🔥 Free Fire", callback_data="freefire")
    btn_clash = types.InlineKeyboardButton(text="🏰 Clash of Clans", callback_data="clash")
    btn_admin = types.InlineKeyboardButton(text="👨‍💻 Admin", url="https://t.me/ziroc0")
    
    markup.add(btn_pubg, btn_ff)
    markup.add(btn_clash)
    markup.add(btn_admin)
    return markup

# /start bosilganda
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 
        "👋 Assalomu alaykum! O'yin turlari va tariflarini ko'rish uchun quyidagi tugmalardan birini tanlang:", 
        reply_markup=get_main_keyboard()
    )

# Ichki tugmalar bosilganda ishlaydigan qism
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Orqaga tugmasi bosilsa bosh menyuni qayta ko'rsatadi
    if call.data == "back_to_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="👋 O'yin turlari va tariflarini ko'rish uchun quyidagi tugmalardan birini tanlang:",
            reply_markup=get_main_keyboard()
        )
        return

    # Tariflar ichidagi sotib olish va ORQAGA tugmalari
    sub_markup = types.InlineKeyboardMarkup()
    contact_btn = types.InlineKeyboardButton(text="✍️ Sotib olish", url="https://t.me/ziroc0")
    back_btn = types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main")
    sub_markup.add(contact_btn)
    sub_markup.add(back_btn)

    if call.data == "pubg":
        text = "🛒 **PUBG Mobile UC tariflari:**\n\n🔹 60 UC — 12 000 so'm\n🔹 325 UC — 55 000 so'm\n🔹 660 UC — 110 000 so'm\n\n💳 To'lov qilish va sotib olish uchun adminga yozing."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=sub_markup, parse_mode="Markdown")
        
    elif call.data == "freefire":
        text = "🛒 **Free Fire Olmos tariflari:**\n\n🔹 100 olmos — 15 000 so'm\n\n💳 To'lov qilish va sotib olish uchun adminga yozing."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=sub_markup, parse_mode="Markdown")
        
    elif call.data == "clash":
        text = "🛒 **Clash of Clans tariflari:**\n\n🔹 Gold Pass — 65 000 so'm\n\n💳 To'lov qilish va sotib olish uchun adminga yozing."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=sub_markup, parse_mode="Markdown")

bot.polling(none_stop=True)

