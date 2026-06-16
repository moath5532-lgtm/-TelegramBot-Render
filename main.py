import os
from telegram.ext import ApplicationBuilder, CommandHandler

# هذا السطر يقرأ التوكن من الإعدادات التي حفظناها في موقع Render
TOKEN = os.environ.get('TOKEN')

async def hello(update, context):
    await update.message.reply_text('أنا بوت الارنب، أعمل الآن!')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", hello))
    print("البوت بدأ العمل...")
    app.run_polling()
