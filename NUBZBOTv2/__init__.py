import os
import dotenv

bot_version = "2.0.0"
bot_release_status = "Alpha"

dotenv.load_dotenv()

TOKEN = str(os.environ["TOKEN"])