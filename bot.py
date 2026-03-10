from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8380321396:AAENKq3iXH0nAzudkEYhUw-CSQspF6SuxKE"

# Menu buttons
keyboard = [
    ["📅 Timetable", "👨‍🏫 Staff"],
    ["📝 Exams", "🏫 Department"],
    ["📢 Notice", "📍 Location"],
    ["ℹ️ Help"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Welcome to AVS AI & DS Student Assistant*\n\n"
        "This bot helps students with:\n"
        "📅 Timetable\n"
        "👨‍🏫 Staff Information\n"
        "📝 Exam Schedule\n"
        "🏫 Department Details\n"
        "📢 Notices\n"
        "📍 College Location\n\n"
        "Please choose an option below.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Reply handler
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "timetable" in text:
        await update.message.reply_text(
            "📅 *AI & DS 1st Year Timetable*\n\n"
            "*Monday*\nPython\nAllied\nTAM\nPython\nHTML\n\n"
            "*Tuesday*\nAllied\nTAM\nPython\nMSD\nLIB\n\n"
            "*Wednesday*\nAllied\nENG\nHTML\nPython\nMSD\n\n"
            "*Thursday*\nTAM\nENG\nAllied\nHTML\nPython\n\n"
            "*Friday*\nLAB\nLAB",
            parse_mode="Markdown"
        )

    elif "staff" in text:
        await update.message.reply_text(
            "👨‍🏫 *AI & DS Staff*\n\n"
            "👩‍🏫 Haripriya Mam\nAllied Paper\nA Section Class Incharge\n\n"
            "👩‍🏫 Ishwarya Mam\nEnglish Paper\nB Section Class Incharge\n\n"
            "👩‍🏫 Mangala Priya Mam\nTamil Paper\n\n"
            "👩‍🏫 Mahalakshmi Mam\nPython Paper\n\n"
            "👩‍🏫 Gunavathi Mam\nHTML Paper\n\n"
            "👨‍🏫 HOD: Selvagovindarajan\n"
            "🎓 Vice Principal: Raghu Nath",
            parse_mode="Markdown"
        )

    elif "exam" in text:
        await update.message.reply_text(
            "📝 *Model Exam Schedule*\n\n"
            "🧪 Model Practical: *11 – 14*\n"
            "📚 Model Semester: *17 – 22*",
            parse_mode="Markdown"
        )

    elif "department" in text:
        await update.message.reply_text(
            "🏫 *Department of AI & Data Science*\n\n"
            "AVS College of Arts & Science\n"
            "Ramalingapuram\n"
            "Tamil Nadu – 636106\n\n"
            "Subjects include:\n"
            "• Python Programming\n"
            "• Artificial Intelligence\n"
            "• Data Science\n"
            "• Web Development",
            parse_mode="Markdown"
        )

    elif "notice" in text:
        await update.message.reply_text(
            "📢 *Important Notice*\n\n"
            "Model Practical: 11 – 14\n"
            "Model Semester Exam: 17 – 22",
            parse_mode="Markdown"
        )

    elif "location" in text:
        await update.message.reply_location(
            latitude=11.6643,
            longitude=78.1460
        )

    elif "help" in text:
        await update.message.reply_text(
            "ℹ️ *Bot Help*\n\n"
            "📅 Timetable – View class schedule\n"
            "👨‍🏫 Staff – View staff details\n"
            "📝 Exams – View exam schedule\n"
            "🏫 Department – Department info\n"
            "📢 Notice – Important announcements\n"
            "📍 Location – College location",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text("Please select an option from the menu.")

# Build bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()