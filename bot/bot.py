import os
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
import httpx

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def handle(msg: Message):
    user_id = msg.from_user.id
    text = msg.text.strip()

    if text.lower() == "/start":
        await msg.answer("🌿 Welcome! Send your TON wallet address to prove NFT ownership.")
    elif text.lower() == "/ping":
        await msg.answer("pong!")
    elif text.lower() == "/mint":
        await msg.answer("Minting not implemented yet.")
    elif text.startswith("EQ") or text.startswith("UQ"):
        await msg.answer("✅ Address received. Verifying NFT ownership...")
        owns_nft = await check_nft_ownership(text)
        if owns_nft:
            await msg.answer("🎉 NFT ownership verified!")
        else:
            await msg.answer("❌ No NFT found for this wallet.")
    else:
        await msg.answer("❓ Unknown command. Send your wallet address.")

async def check_nft_ownership(wallet_address: str) -> bool:
    url = f"https://tonapi.io/v2/accounts/{wallet_address}/nfts"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            return False
        data = resp.json()
        # Check if there are any NFTs (or filter for a specific collection)
        return bool(data.get("nft_items"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
