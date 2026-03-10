import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Secure token from Railway
TOKEN = os.getenv("8380321396:AAGZr_ezivJ84iD1-Deu1Il5uAzVskJ6u88")

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
    "hod": "👨‍🏫 The HOD of AI & DS department is Dr. Selvagovindarajan.",
    "vice principal": "🏫 The Vice Principal of AVS College is Raghu Nath.",
    "model exam": "📝 Model Semester Exams will be conducted from 17 to 22.",
    "model practical": "🧪 Model Practical exams will be conducted from 11 to 14.",
    "department": "🏫 AI & DS focuses on Artificial Intelligence, Data Science, Machine Learning and Web Development.",
    "college": "📍 AVS College of Arts & Science is located in Salem, Tamil Nadu.",
    "developer": "👨‍💻 This bot was developed by Khathir Ahamed (AI & DS Student)."
}

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Welcome to AVS AI & DS Student Assistant Bot\n\n"
        "Available Services:\n"
        "📅 Timetable\n"
        "👨‍🏫 Staff\n"
        "📝 Exams\n"
        "🏫 Department\n"
        "📢 Notices\n"
        "📍 Location\n\n"
        "👨‍💻 Developer: Khathir Ahamed",
        reply_markup=reply_markup
    )

# MESSAGE HANDLER
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "timetable" in text:
        await update.message.reply_text(
            "📅 AI & DS Timetable\n\n"
            "Monday\nPython\nAllied\nTAM\nPython\nHTML\n\n"
            "Tuesday\nAllied\nTAM\nPython\nMSD\nLibrary\n\n"
            "Wednesday\nAllied\nEnglish\nHTML\nPython\nMSD\n\n"
            "Thursday\nTAM\nEnglish\nAllied\nHTML\nPython\n\n"
            "Friday\nLab Day"
        )

    elif "staff" in text:
        await update.message.reply_text(
            "👨‍🏫 AI & DS Department Staff\n\n"
            "HOD: Dr. Selvagovindarajan\n"
            "Vice Principal: Raghu Nath"
        )

    elif "exam" in text:
        await update.message.reply_text(
            "📝 Exam Information\n\n"
            "Model Practical: 11 - 14\n"
            "Model Semester Exam: 17 - 22"
        )

    elif "department" in text:
        await update.message.reply_text(
            "🏫 Department of AI & Data Science\n\n"
            "Artificial Intelligence\n"
            "Data Science\n"
            "Machine Learning\n"
            "Web Technologies"
        )

    elif "notice" in text:
        await update.message.reply_text(
            "📢 Latest Notices\n\n"
            "Submit assignments before model exams.\n"
            "Submit lab records before practical exams."
        )

    elif "location" in text:
        await update.message.reply_text(
            "📍 AVS College of Arts & Science\n\n"
            "Salem, Tamil Nadu\n\n"
            "Google Maps:\nhttps://maps.google.com"
        )

    elif "help" in text:
        await update.message.reply_text(
            "❓ Help\n\n"
            "Use menu buttons to access:\n"
            "Timetable\nStaff\nExams\nDepartment\nNotices\nLocation"
        )

    elif "developer" in text:
        await update.message.reply_text(
            "👨‍💻 Developer\n\n"
            "Khathir Ahamed\n"
            "AI & DS Student\n"
            "AVS College of Arts & Science"
        )

    elif "hi" in text or "hello" in text:
        await update.message.reply_text("Hello! How can I help you today?")

    else:
        for key in knowledge:
            if key in text:
                await update.message.reply_text(knowledge[key])
                return

        await update.message.reply_text(
            "Sorry, I couldn't understand your question.\n"
            "Try asking about timetable, exams, staff or department."
        )

# BUILD BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot is running...")
app.run_polling()
