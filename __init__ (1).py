import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "25344449"))
    API_HASH = os.environ.get("API_HASH", "24fd33596888304ec937b8130e73f48c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8089615242:AAHih-ud-Mge9_OVIZjgQz_GP2HEFD6a6U0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MybotAnyting_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
