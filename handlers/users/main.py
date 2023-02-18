from aiogram import types
from loader import dp,bot
from aiogram.types import InlineQueryResultArticle,InputTextMessageContent
import uuid

from search import search

@dp.inline_handler()
async def test1(query: types.InlineQuery):
    text = query.query
    links = search(key=text)
    articles = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title = f"{link['title']}", 
            url = f"https://www.youtube.com/watch?v={link['id']}",
            description = f"{link['views']}",
            thumb_url = f"{link['thumbnails'][0]}",
            input_message_content=InputTextMessageContent(
                message_text = f"https://www.youtube.com/watch?v={link['id']}"
            ),
        ) for link in links
            
    ]
    await query.answer(results=articles,cache_time=60,is_personal=True)