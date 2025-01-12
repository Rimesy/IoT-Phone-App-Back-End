import asyncio
from WebSocket import WebSocketRuntime
import openAIconnection
import speechToText
import ButtonState
from dotenv import load_dotenv

def main():
    # initialise all your code from here if you want it to work
    client = openAIconnection.initialise()
    message = speechToText.convert("/Audio/peter-the-horse-is-here.flac")
    response = openAIconnection.query(client, message)
    print(response)


async def main():
    # This will infinitely run
    load_dotenv()
    wsocket = WebSocketRuntime.WebSocketRuntime()
    button = ButtonState.ButtonState()
    ai_client = openAIconnection.initialise()

    tasks_list = [
        wsocket.start_server("", 8675, button, ai_client),
        button.button_runtime()
    ]
    
    await asyncio.gather(*tasks_list)


if __name__ == "__main__":
    asyncio.run(main())