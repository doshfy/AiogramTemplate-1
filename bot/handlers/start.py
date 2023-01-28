from aiogram import Dispatcher, filters, types


async def process_start_cmd(message: types.Message) -> None:
    await message.answer("Hello!")


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(process_start_cmd, filters.CommandStart())
