from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8380321396:AAHY5dmxoGkBpXQvNWWmBJs-VSMqwcQ6Das"

# MENU BUTTONS
keyboard = [
    ["📅 Timetable", "👨‍🏫 Staff"],
    ["📝 Exams", "🏫 Department"],
    ["📢 Notices", "📍 Location"],
    ["❓ Help", "👨‍💻 Developer"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# AI Knowledge Base
knowledge = {
    "hod": "👨‍🏫 The HOD of AI & DS department is *Dr. Selvagovindarajan*.",
    "vice principal": "🏫 The Vice Principal of AVS College is *Raghu Nath*.",
    "model exam": "📝 Model Semester Exams will be conducted from *17 to 22*.",
    "model practical": "🧪 Model Practical exams will be conducted from *11 to 14*.",
    "department": "🏫 AI & DS focuses on *Artificial Intelligence, Data Science, Machine Learning and Web Development*.",
    "college": "📍 AVS College of Arts & Science is located in *Salem, Tamil Nadu*.",
    "developer": "👨‍💻 This bot was developed by *Khathir Ahamed* (AI & DS Student)."
}

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 *Welcome to AVS AI & DS Student Assistant Bot*\n\n"
        "This smart bot helps students with academic information.\n\n"
        "✨ Available Services:\n"
        "📅 Timetable\n"
        "👨‍🏫 Staff Information\n"
        "📝 Exam Schedule\n"
        "🏫 Department Details\n"
        "📢 College Notices\n"
        "📍 College Location\n\n"
        "💬 You can also ask questions about the college.\n\n"
        "👨‍💻 Developed by *Khathir Ahamed*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# MESSAGE HANDLER
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "timetable" in text:
        await update.message.reply_text(
            "📅 *AI & DS Class Timetable*\n\n"
            "🟢 *Monday*\n"
            "Python\nAllied\nTAM\nPython\nHTML\n\n"
            "🔵 *Tuesday*\n"
            "Allied\nTAM\nPython\nMSD\nLibrary\n\n"
            "🟡 *Wednesday*\n"
            "Allied\nEnglish\nHTML\nPython\nMSD\n\n"
            "🟣 *Thursday*\n"
            "TAM\nEnglish\nAllied\nHTML\nPython\n\n"
            "🔴 *Friday*\n"
            "🧪 Lab Day",
            parse_mode="Markdown"
        )

    elif "staff" in text:
        await update.message.reply_text(
            "👨‍🏫 *AI & DS Department Staff*\n\n"
            "👨‍💼 *HOD*: Dr. Selvagovindarajan\n"
            "🏫 *Vice Principal*: Raghu Nath\n\n"
            "Faculty members are available in the department office.",
            parse_mode="Markdown"
        )

    elif "exam" in text:
        await update.message.reply_text(
            "📝 *Exam Information*\n\n"
            "🧪 Model Practical: *11 - 14*\n"
            "📚 Model Semester Exam: *17 - 22*\n\n"
            "📖 Prepare well and good luck!",
            parse_mode="Markdown"
        )

    elif "department" in text:
        await update.message.reply_text(
            "🏫 *Department of AI & Data Science*\n\n"
            "Focus Areas:\n"
            "🤖 Artificial Intelligence\n"
            "📊 Data Science\n"
            "🧠 Machine Learning\n"
            "💻 Web Technologies\n\n"
            "Students learn modern technologies used in industry.",
            parse_mode="Markdown"
        )

    elif "notice" in text:
        await update.message.reply_text(
            "📢 *Latest Notices*\n\n"
            "📌 Submit assignments before model exams.\n"
            "📌 Lab records must be submitted before practical exams.",
            parse_mode="Markdown"
        )

    elif "location" in text:
        await update.message.reply_text(
            "📍 *AVS College of Arts & Science*\n\n"
            "Salem, Tamil Nadu\n\n"
            "🌐 Google Maps:\n"
            "https://maps.google.com",
            parse_mode="Markdown"
        )

    elif "help" in text:
        await update.message.reply_text(
            "❓ *Help Menu*\n\n"
            "Use the menu buttons to get information:\n"
            "📅 Timetable\n"
            "👨‍🏫 Staff\n"
            "📝 Exams\n"
            "🏫 Department\n"
            "📢 Notices\n"
            "📍 Location",
            parse_mode="Markdown"
        )

    elif "developer" in text:
        await update.message.reply_text(
            "👨‍💻 *Developer*\n\n"
            "Name: Khathir Ahamed\n"
            "Department: AI & DS\n"
            "College: AVS College of Arts & Science\n\n"
            "This bot was developed to help students access academic information easily.",
            parse_mode="Markdown"
        )

    elif "hi" in text or "hello" in text:
        await update.message.reply_text(
            "👋 Hello! How can I help you today?"
        )

    else:
        for key in knowledge:
            if key in text:
                await update.message.reply_text(knowledge[key], parse_mode="Markdown")
                return

        await update.message.reply_text(
            "🤖 Sorry, I couldn't understand your question.\n"
            "Please ask about *timetable, exams, staff, department or college.*",
            parse_mode="Markdown"
        )

# RUN BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

print("🤖 Bot is running...")
app.run_polling()
