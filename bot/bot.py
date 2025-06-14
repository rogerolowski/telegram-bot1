import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def handle(msg: Message):
    user_id = msg.from_user.id
    text = msg.text.strip()

    if text.lower() == "/start":
        await msg.answer("🌿 Welcome! Send your TON wallet address to prove NFT ownership.")
    elif text.startswith("EQ"):  # crude TON address check
        # Here you'd call tonapi.io or toncenter.com RPC
        await msg.answer("✅ Address received. Verifying NFT ownership...")
        # TODO: Implement actual NFT ownership check
    else:
        await msg.answer("❓ Unknown command. Send your wallet address.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
