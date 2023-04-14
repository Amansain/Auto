#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "7822571"))
    API_HASH = os.environ.get("API_HASH", "067329e70bfc5b3022f77080703da788")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2089413356:AAFkYhLxRqwQaR0QHk2czfYQHWI8TAy-Hf0") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", """<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <code>{file_name}</code>

=========== • ✠ • ===========

<b>▫️ ɢʀᴏᴜᴘ : @CinimaBranthen 

▫️ ᴄʜᴀɴɴᴇʟ : @CoBLinks</b>

=========== • ✠ • ===========</b>""")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQCenDdoZsPgoohWSS4Up3743sPNtcVEZ2-QUDsWzstPQD-JL-KjqRvbCEQqEeailA-q4Jid-8bLYKbVl7xGVWZTD8YugCHjpoSlTE4Wm6uWZRCC3Eut4iP0MoyysR19OMdC1ZRabY_AzW0QEj8N-Xmvd9G1dy82TvSSV-HTUNS5gOpTBXCXi3xXt9Y0X1gXlODz4wA9hNl8UsulpAzuNIEE6tdRwmyFgtf41MTrc-FXwxQyq0pq2A1fOo0V2JiWmwrD1ID1gAF-xRILOgkAmeHu43cZPyUjqnSTng-hOKAZah94TQCVH2EhZ-qhyNocWtap1lBmx_LU_ZxdW6cpI8PBccJeTwA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
