from discord.ext import typed_commands


class MyContext(typed_commands.Context):
    ...


def test_bot() -> None:
    class MyBot(typed_commands.Bot[MyContext]):
        ...


def test_autosharded_bot() -> None:
    class MyBot(typed_commands.AutoShardedBot[MyContext]):
        ...
