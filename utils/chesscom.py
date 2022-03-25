import aiohttp
from datetime import datetime


class ChessComError(Exception):
    def __init__(self, status_code: int):
        self.message = f"Chess.com Request failed with status code: {status_code}"
        self.status_code = status_code
        super().__init__(self.message)


async def get_player_games(username: str) -> list[dict]:
    username = username.lower()
    async with aiohttp.ClientSession() as session:
        url = f"https://api.chess.com/pub/player/{username}/games/" \
              f"{datetime.today().year}/{'0' if datetime.today().month < 10 else ''}{datetime.today().month}"
        async with session.get(url) as response:
            if response.status == 200:
                return (await response.json())["games"]
            else:
                raise(ChessComError(response.status))
