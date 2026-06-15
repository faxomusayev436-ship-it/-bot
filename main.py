import telebot
import os

# 读取 Render 环境里设置的 API_TOKEN
TOKEN = os.getenv('API_TOKEN')

if not TOKEN:
    print("Error: API_TOKEN environment variable is not set.")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "机器人已在云端运行！")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"你刚才说的是: {message.text}")

if __name__ == "__main__":
    print("Bot is starting with polling mode...")
    # 使用 infinity_polling() 它是 pyTelegramBotAPI 中实现轮询的推荐方式
    bot.infinity_polling()
