from pyrogram import Client
from pyrogram.handlers import MessageHandler
import datetime
import logging


api_id = 00000  # CHANGE ME
api_hash = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"   # CHANGE ME
app = Client("Session", api_id, api_hash)
logging.basicConfig(filename='meesage_log.log', level=logging.INFO)


def new_message(client, message):
    """
        new message
    """
    if message["chat"]["type"] == "private":
        out = f"{message['message_id']} | {datetime.datetime.fromtimestamp(message['date'])} | chat: '{message['chat']['username']}' | "
        out += message_format(message)
        logging.info(out)


def message_format(message):
    """
     format message for log
    :param message:
    :return:
    """
    out = ""
    if message["reply_to_message"]:
        out += f"> [{message_format(message['reply_to_message'])}] "
    if message["forward_sender_name"]:
        out += f"| forward from: {message['forward_sender_name']} | "
    if message["forward_from"]:
        out += f"forward from: {message['forward_from']['id']} @{message['forward_from']['username']} {message['forward_from']['first_name']} {message['forward_from']['last_name']} | "
    out += f"{message['from_user']['id']} @{message['from_user']['username']} {message['from_user']['first_name']} {message['from_user']['last_name']}: "
    if message['photo']:
        out += f"(photo: {message['photo']['file_id']}) "
    if message['document']:
        out += f"({message['document']['file_name']}: {message['document']['file_id']} {message['document']['mime_type']}) "
    if message['voice']:
        out += f"(Voice: {message['voice']['file_id']}) "
    if message['video_note']:
        out += f"(video_note: {message['video_note']['file_id']}) "
    if message['video']:
        out += f"(video: {message['video']['file_id']}) "
    if message.text:
        out += message.text
    if message['caption']:
        out += f"| caption: {message['caption']} "
    return out


app.add_handler(MessageHandler(new_message))
app.run()
