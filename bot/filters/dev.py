from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from typing import Union
from bot.config import Config


class DevFilter(BoundFilter):
    key = "dev"

    def __init__(self, dev: bool = None) -> None:
        self.dev = dev

    async def check(self, obj: Union[types.Message, types.CallbackQuery]) -> Union[bool, None]:
        if self.dev is None:
            return

        config: Config = obj.bot.get("config")
        admin_id = config.bot.admin_id
        user_id = obj.from_user.id

        return (user_id == admin_id) == self.dev
