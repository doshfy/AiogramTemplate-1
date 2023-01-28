import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot import config
from bot.handlers import start
from bot.filters import dev

from bot.utils import commands

logger = logging.getLogger(__name__)
config = config.load_config("config.ini")


async def on_startup(dp: Dispatcher) -> None:
    await dp.bot.delete_webhook()
    await dp.bot.set_webhook(
        f"{config.webhook.host}{config.webhook.path}",
        max_connections=10 ** 5
    )

    await dp.bot.set_my_commands(
        commands=commands.default(),
        # scope=...
    )


async def on_shutdown(dp: Dispatcher) -> None:
    await dp.bot.delete_webhook()


def register_all_handlers(dp: Dispatcher) -> None:
    start.register(dp)


def bound_all_filters(dp: Dispatcher) -> None:
    dp.bind_filter(dev.DevFilter)


def main() -> None:
    logging.basicConfig(level=logging.WARNING)

    server = TelegramAPIServer.from_base(f"{config.server.ip}:{config.server.port}")
    bot = Bot(token=config.bot.token, server=server)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    bot["config"] = config

    register_all_handlers(dp)
    bound_all_filters(dp)

    executor.start_webhook(
        dispatcher=dp,
        webhook_path=config.webhook.path,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=config.webhook.web_host,
        port=config.webhook.web_port
    )


if __name__ == '__main__':
    main()
