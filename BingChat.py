import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


async def test_ask() -> None:
    cookies = json.loads(open("C:/Users/USER/Downloads/bing_cookies.json", encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(
        prompt="(請用中文回答我)假設你是一位財務專家而且您是一位具有股票推薦經驗的金融專家，如果以下新聞標題是好消息請只回答#yes，而如果是壞消息則只回答#no，如果不確定則只回答#unknown，然後於下一行用簡短的句子進行詳細說明，這個標題對公司股價是好還是壞呢? 而以下為要分析的新聞標題:年底確定來不及！台積電中科2奈米廠用地延至明年交地",
        conversation_style=ConversationStyle.creative,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, ensure_ascii=False, indent=2))  # 加入 ensure_ascii=False
    assert response

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())