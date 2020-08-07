from discord.ext import typed_commands


class MyContext(typed_commands.Context):
    ...


def test_bot() -> None:
    class MyBot(typed_commands.Bot[MyContext]):
        ...


def test_autosharded_bot() -> None:
    class MyBot(typed_commands.AutoShardedBot[MyContext]):
        ...


def test_cog() -> None:
    class MyCog(typed_commands.Cog[MyContext]):
        ...


def test_command() -> None:
    class MyCommand(typed_commands.Command[MyContext]):
        ...


def test_group_mixin() -> None:
    class MyGroupMixin(typed_commands.GroupMixin[MyContext]):
        ...


def test_group() -> None:
    class MyGroup(typed_commands.Group[MyContext]):
        ...


def test_help_command() -> None:
    class MyHelpCommand(typed_commands.HelpCommand[MyContext]):
        ...


def test_default_help_command() -> None:
    class MyDefaultHelpCommand(typed_commands.DefaultHelpCommand[MyContext]):
        ...


def test_minimal_help_command() -> None:
    class MyMinimalHelpCommand(typed_commands.MinimalHelpCommand[MyContext]):
        ...
