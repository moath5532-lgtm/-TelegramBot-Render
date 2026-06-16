from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'أهلاً {update.effective_user.first_name}، أنا بوت معاذ، أعمل الآن!')

if __name__ == '__main__':
    TOKEN = '8926831653:AAHbduupIWl0cirNsdi5cGm6-IqPlm2xtK0'
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", hello))
    
    print("البوت بدأ العمل...")
    app.run_polling()
