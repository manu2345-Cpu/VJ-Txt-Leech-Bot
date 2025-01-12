# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\n I Am A Bot For Download Links From Your **.TXT** File And Then Upload That File On Telegram So Basically If You Want To Use Me First Send Me /upload Command And Then Follow Few Steps..\n\nUse /stop to stop any ongoing task.</b>")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('𝕤ᴇɴᴅ ᴛxᴛ ғɪʟᴇ ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n144,240,360,480,720,1080 please choose quality")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg » https://graph.org/file/ce1723991756e48c35aa1.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']
        

        
            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] Vid_ID:** {str(count).zfill(3)}.** {𝗻𝗮𝗺𝗲𝟭}{MR}.mkv\n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                cc1 = f'**[📁] Pdf_ID:** {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{MR}.pdf \n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


# -*- coding: utf-8 -*-

'''
For Educational Purposes Only.

-------------- Vdocipher Downloader -------------

first time run: 

1) pip install aiohttp sqlite3 requests json pytz datetime shlex
2) sudo apt install -y git cmake make build-essential; git clone https://github.com/axiomatic-systems/Bento4.git; cd Bento4; mkdir cmakebuild; cd cmakebuild/; cmake -DCMAKE_BUILD_TYPE=Release ..; make; sudo make install

Dependencies: yt-dlp, aria2c, mp4decrypt, ffmpeg
Usage: python decipher_dl.py -t "TOKEN"

For custom name add: -o "LUMD"
For custom resl add: -r "1/2/3" where 1 is highest and 3 is lowest available rsl

'''

import re
import json
import pytz
import sqlite3
import requests
import datetime
import asyncio, shlex
from aiohttp import ClientSession
from typing import Tuple, Union, List
import subprocess, os, argparse, base64

__version__ = 1.0
__author__ = "Daddy Yankee"

os.makedirs("Videos/", exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("-o",
                    '--output',
                    dest="name",
                    help="Specify output file name with no extension",
                    default=None,
                    required=False)
parser.add_argument("-t",
                    '--token',
                    dest="token",
                    help="Vdocipher Token",
                    required=True)
parser.add_argument("-r",
                    '--resl',
                    dest="resl",
                    help="Video Resolution",
                    default="1",
                    required=False)

args = parser.parse_args()


class Vdocipher:

    def __init__(self, token):
        self.token = token
        self.vid = self.decode_b64(
            self.decode_b64(self.token)["playbackInfo"])["videoId"]
        session = requests.Session()
        session.headers.update({
            "authority":
            "dev.vdocipher.com",
            "user-agent":
            "Dalvik/2.1.0 (Linux; U; Android 9;  Pixel 6)",
        })
        self.mpd_link, self.name = self.detail(session)
        self.pssh = self.parse_mpd(session)
        session.close()

    def detail(self, session):
        response = session.get(
            f"https://dev.vdocipher.com/api/meta/{self.vid}").json()
        mpd = response["dash"]["manifest"]
        title = self.c_name(response["title"]).rsplit(".", 1)[0]
        return mpd, title

    @staticmethod
    def decode_b64(data):
        return json.loads(base64.urlsafe_b64decode(data).decode())

    def c_name(self, name):
        newname = name.replace("'", "").replace("/", "-").replace(
            "%",
            "").replace('"', '').replace("[", "(").replace("]", ")").replace(
                "`", "").replace("\n", "").replace("\t", "").replace(
                    ":", "-").replace(":", "").replace("||", "")
        return newname

    def parse_mpd(self, session):
        resp = session.get(self.mpd_link)
        pssh = re.findall(r'pssh>(.*)</cenc', resp.text)[0]
        return pssh

    def get_date(self):
        tz = pytz.timezone('Asia/Kolkata')
        ct = datetime.datetime.now(tz)
        return ct.strftime("%d %b %Y - %I:%M%p")

    async def get_keys(self):
        keys = await self.get_from_db(self.pssh)
        if not keys:
            async with ClientSession() as session:
                async with session.post("https://api.newdomainhai.gq/free",
                                        data={"link": self.token}) as resp:
                    keys = await resp.json(content_type=None)
            try:
                keys = keys["KEY_STRING"]
            except (KeyError, ValueError):
                return 1
            await self.add_to_db(self.pssh, keys)
        return keys

    async def init_db(self):
        query = 'CREATE TABLE IF NOT EXISTS "DATABASE" ( "pssh" TEXT, "keys" TEXT, PRIMARY KEY("pssh") )'
        await self.async_db(query)

    async def add_to_db(self, pssh, keys):
        query = "INSERT or REPLACE INTO DATABASE VALUES (?, ?)"
        await self.async_db(query, (pssh, keys))

    async def get_from_db(self, pssh):
        query = "SELECT keys FROM DATABASE WHERE pssh = ?"
        result = await self.async_db(query, (pssh, ))
        keys = result[0][0] if result and len(result) > 0 else None
        return keys

    async def async_db(self, query, parameters=None):

        def executor():
            connection = sqlite3.connect(f"{self.dirPath}/database.db")
            cursor = connection.cursor()
            cursor.execute(query,
                           parameters) if parameters else cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            return result

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, executor)


class Download(Vdocipher):

    def __init__(self, name, resl, token):
        super().__init__(token)
        currentFile = __file__
        if name:
            self.name = name
        realPath = os.path.realpath(currentFile)
        self.dirPath = os.path.dirname(realPath)
        self.vid_format = f'bestvideo.{resl}/bestvideo.2/bestvideo'
        self.encrypt_video = self.dirPath + '/vid_enc.mp4'
        self.encrypt_audio = self.dirPath + '/aud_enc.m4a'
        self.decrypt_video = self.encrypt_video.replace('enc', 'dec')
        self.decrypt_audio = self.encrypt_audio.replace('enc', 'dec')
        self.merged = f"{self.dirPath}/Videos/{self.name} DL: {self.get_date()}.mkv"

    async def x(self):

        self.key = await self.get_keys()
        if self.key == 1:
            print("Could'nt Get decryption Keys.")
            return

        adtext = lambda text: text.rjust(30)

        print(adtext("[Downloading] Video ➡️"), self.name)
        returncode = await self.yt_dlp_drm()
        if returncode != 0:
            return 1

        print(adtext("[Decrypting] Video ➡️"), self.name)
        returncode = await self.decrypt()
        if returncode != 0:
            return 1

        print(adtext("[Merging] Video ➡️"), self.name)
        returncode = await self.merge()
        if returncode != 0:
            return 1

        print(adtext("[Cleaning Directory...]"))
        await self.delete()
        if returncode == 0:
            print(adtext("[Done] Video ➡️"), self.name)
            return self.merged

    async def subprocess_call(self, cmd: Union[str, List[str]]):
        if isinstance(cmd, str):
            cmd = shlex.split(cmd)
        elif isinstance(cmd, (list, tuple)):
            pass
        else:
            return None, None
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await process.communicate()
        error = stderr.decode().strip()
        output = stdout.decode().strip()

        return output, error, process.returncode

    async def yt_dlp_drm(self) -> List[str]:
        xhr = []
        xhr.append(
            self.subprocess_call(
                f'yt-dlp -k --allow-unplayable-formats -f "{self.vid_format}" --fixup never "{self.mpd_link}" --external-downloader aria2c --external-downloader-args "-x 16 -s 16 -k 1M" -o "{self.encrypt_video}" --exec echo'
            ))

        xhr.append(
            self.subprocess_call(
                f'yt-dlp -k --allow-unplayable-formats -f ba --fixup never "{self.mpd_link}" --external-downloader aria2c --external-downloader-args "-x 16 -s 16 -k 1M" -o "{self.encrypt_audio}" --exec echo'
            ))
        await asyncio.gather(*xhr)
        return 0

    async def decrypt(self):
        _, _, returncode = await self.subprocess_call(
            f'mp4decrypt --show-progress {self.key} "{self.encrypt_audio}" "{self.decrypt_audio}"'
        )
        if returncode != 0: return 1

        _, _, returncode = await self.subprocess_call(
            f'mp4decrypt --show-progress {self.key} "{self.encrypt_video}" "{self.decrypt_video}"'
        )
        if returncode != 0: return 1
        return 0

    async def merge(self):
        _, _, returncode = await self.subprocess_call(
            f'ffmpeg -i "{self.decrypt_video}" -i "{self.decrypt_audio}" -reserve_index_space 512k -c copy "{self.merged}"'
        )
        if returncode != 0: return 1
        return 0

    async def delete(self):
        try:
            listx = [
                self.encrypt_video, self.encrypt_audio, self.decrypt_audio,
                self.decrypt_video
            ]
            for x in listx:
                try:
                    if os.path.isfile(x):
                        os.remove(x)
                except:
                    print("Failed to delete:- ", x)
                    pass

        except:
            pass


async def main(name, resl, token):
    try:
        if isinstance(resl, str):
            resl = int(resl)
    except:
        resl = 1
    x = Download(name, resl, token)
    await x.init_db()
    await x.x()


if __name__ == "__main__":
    toke = str(args.token)
    name = str(args.name)
    resl = str(args.resl)
    asyncio.run(main(name=name, resl=resl, token=toke))


bot.run()
