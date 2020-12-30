# PLEASE STOP!
# DO NOT EDIT THIS FILE
# Create a new config.py file in same dir
# and import, then extend this class.
if not __name__.endswith("sample_config"):
    import sys
    print(
        "The README is there to be read. "
        "Extend this sample config to a config file, "
        "don't just rename and change values by. "
        "Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr
    )
    quit(1)

from tobrot.get_cfg import get_config


class Config:
    # get a token from @BotFather
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", 1456031638:AAEHjOeROrmCeF0pKK0gt6XHPnNNmtLFePU should_prompt=True)
    # The Telegram API things
    APP_ID = int(get_config("APP_ID", 1366324 should_prompt=True))
    API_HASH = get_config("API_HASH", 0d0274833b354d9223ca60b3e2f1e7c8 should_prompt=True)
    # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(
        int(x) for x in get_config(
            "AUTH_CHANNEL", -1001418321537
            should_prompt=True
        ).split()
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "./DOWNLOADS")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = int(get_config("MAX_FILE_SIZE", 50000000))
    TG_MAX_FILE_SIZE = int(get_config("TG_MAX_FILE_SIZE", 2097152000))
    FREE_USER_MAX_FILE_SIZE = int(
        get_config("FREE_USER_MAX_FILE_SIZE", 50000000)
    )
    # chunk size that should be used with requests
    CHUNK_SIZE = int(get_config("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config(
        "DEF_THUMB_NAIL_VID_S",
        "https://telegra.ph/file/c20505878345a9b95e313.jpg"
    )
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = int(get_config(
        "MAX_MESSAGE_LENGTH",
        4096
    ))
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(get_config(
        "PROCESS_MAX_TIMEOUT",
        3600
    ))
    #
    ARIA_TWO_STARTED_PORT = int(get_config(
        "ARIA_TWO_STARTED_PORT",
        6800
    ))
    EDIT_SLEEP_TIME_OUT = int(get_config(
        "EDIT_SLEEP_TIME_OUT",
        1
    ))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(get_config(
        "MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START",
        600
    ))
    MAX_TG_SPLIT_FILE_SIZE = int(get_config(
        "MAX_TG_SPLIT_FILE_SIZE",
        1900000000
    ))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = get_config("TG_OFFENSIVE_API", None)
    # URL for the rclone configuration
    R_CLONE_CONF_URI = get_config("R_CLONE_CONF_URI", None)
    # Destination folder for the rclone
    R_CLONE_DEST = get_config("R_CLONE_DEST", "/PublicLeech")
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
    #
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "PublicLeech.log")
    #
    SP_LIT_ALGO_RITH_M = get_config(
        "SP_LIT_ALGO_RITH_M",
        "hjs"
    )
    #
    DIS_ABLE_ST_GFC_COMMAND_I = get_config(
        "DIS_ABLE_ST_GFC_COMMAND_I",
        False
    )
    # array to store the users who will have control (permissions)
    # in the bot
    SUDO_USERS = set(
        int(x) for x in get_config(
            "SUDO_USERS",
            should_prompt=True
        ).split()
    )
