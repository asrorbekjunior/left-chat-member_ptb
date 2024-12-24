from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Foydalanuvchi chiqib ketganida ishlovchi funksiya
def user_left(update: Update, context: CallbackContext):
    if update.message.left_chat_member:
        left_user = update.message.left_chat_member
        chat_title = update.message.chat.title
        update.message.reply_text(f"{left_user.first_name} guruhni tark etdi ({chat_title}).")

# Asosiy kod
def main():
    # Bot tokenini kiriting
    TOKEN = "SIZNING_BOT_TOKENINGIZ"
    updater = Updater(token=TOKEN, use_context=True)

    # Foydalanuvchi chiqib ketishini kuzatadigan handler
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, user_left))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

# Kodni ishga tushirish
if __name__ == "__main__":
    main()
