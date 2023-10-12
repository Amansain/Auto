#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "15951945"))
    API_HASH = os.environ.get("API_HASH", "7b82b801d197921e54cf404799ae5b3f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5951942864:AAE_sZsQG9vo1NUQc8oTDzxBwD-veRcBWEE") 
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
    SESSION = os.environ.get("SESSION", "BQDzaEkAs9UhTzXX-uRHZQD0Dh-paB_U16uZalgLN_IoMEZB-PSNFO8wO-a610oSYMvD7JQ1r61bc_toZR5FOYATHY2IQuulFVFl9_xqP7uwg52HpwZZEGGgb6NjYCpqb1vppXF4orhDxwJwKT11VxFQZvrDAnrZ0qVPFKKDQR9RgodMgueF-P2FwW4E8mPgV9juEr63RkqwwqKx6CvHbJdCZ87JyA6K6i8zlaIq0UcGGmiXKU8eiAz3iaZh8_g8r8_gekEmblMh-TvjHFoi2-GaI2p8HtNbAyEkhkjaEOQS4lLcGcTJGYYguTbq6zyCJvrxRiXmJjQwU7rTF83uxQs0QUuyPAAAAAFEMvphAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
