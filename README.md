# discord-ext-typed-commands

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/bryanforbes/discord-ext-typed-commands/blob/master/LICENSE)
[![Unit tests](https://github.com/bryanforbes/discord-ext-typed-commands/workflows/Unit%20tests/badge.svg)](https://github.com/bryanforbes/discord-ext-typed-commands/actions?query=workflow%3A%22Unit+tests%22)
[![CodeQL Analysis](https://github.com/bryanforbes/discord-ext-typed-commands/workflows/CodeQL%20Analysis/badge.svg)](https://github.com/bryanforbes/discord-ext-typed-commands/actions?query=workflow%3A%22CodeQL+Analysis%22)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This package contains a discord.py extension to provide classes to more easily use typed commands

## Installation

```
pip install discord-ext-typed-commands
```

**NOTE:** Because `discord.py` uses namespace packages for its extensions, `mypy` must be configured to use namespace packages either with the `--namespace-packages` command line flag, or by setting `namespace_packages = True` in your `mypy` configuration file. See the [import discovery](https://mypy.readthedocs.io/en/stable/command_line.html#import-discovery) section of the `mypy` documentation for more details.

## Usage

The most common usage will be in connection with [discord.py-stubs](https://pypi.org/project/discord.py-stubs/) in order to allow bot authors to use the command classes from discord.py while also using the generics defined in the stubs:

```python
from typing import Any, Type, TypeVar, Union, cast, overload

import discord
from discord.ext import typed_commands

OtherContextType = TypeVar('OtherContextType', bound=typed_commands.Context)


class MyContext(typed_commands.Context):
    async def send_with_hello(self, text: str) -> None:
        await self.send(f'Hello! {text}')


class MyCog(typed_commands.Cog[MyContext]):
    @typed_commands.command()
    async def speak(self, ctx: MyContext, text: str) -> None:
        await ctx.send_with_hello(text)


class MyBot(typed_commands.Bot[MyContext]):
    @overload
    async def get_context(self, message: discord.Message) -> MyContext:
        ...

    @overload
    async def get_context(
        self, message: discord.Message, *, cls: Type[OtherContextType]
    ) -> OtherContextType:
        ...

    async def get_context(
        self,
        message: discord.Message,
        *,
        cls: Type[OtherContextType] = cast(Any, MyContext),
    ) -> Union[MyContext, OtherContextType]:
        return await super().get_context(message, cls=cls)


my_bot = MyBot('$')
my_bot.add_cog(MyCog())
my_bot.run('...')
```
**NOTE**: Because it is not a runtime dependency, [discord.py-stubs](https://pypi.org/project/discord.py-stubs/) will need to be explicitly installed to type check a bot while it is being developed. It is recommended that the stubs be added as a development dependency using your preferred method of package management.

## Development

Make sure you have [poetry](https://python-poetry.org/) installed.

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type post-checkout
```
