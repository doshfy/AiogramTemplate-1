from aiogram.types import BotCommand


def default() -> list[BotCommand]:
    return [
        BotCommand("start", description="Restart the bot")
    ]
