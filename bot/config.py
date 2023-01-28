from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class WebHook:
    host: str
    path: str
    web_host: str
    web_port: int


@dataclass
class Server:
    ip: str
    port: int


@dataclass
class Config:
    bot: TgBot
    webhook: WebHook
    server: Server


def load_config(path: str) -> Config:
    config = ConfigParser()
    config.read(path)

    bot = config["bot"]
    webhook = config["webhook"]
    server = config["server"]

    return Config(
        bot=TgBot(
            token=bot.get("token"),
            admin_id=bot.getint("admin_id")
        ),
        webhook=WebHook(
            host=webhook.get("host"),
            path=webhook.get("path"),
            web_host=webhook.get("web_host"),
            web_port=webhook.getint("web_port")
        ),
        server=Server(
            ip=server.get("ip"),
            port=server.getint("port")
        )
    )
