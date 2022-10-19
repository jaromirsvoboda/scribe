import logging
import time
import click

from pathlib import Path

from scribe.scribe import Scribe


timestamp = time.strftime("%Y-%m-%d_%H-%M-%S_%p")
logging.basicConfig(
    filename=fr"{timestamp}.log",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info(f"Starting Scribe at {timestamp}.")




@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()  # type: ignore

# `cwd`: current directory is straightforward
cwd = Path.cwd()

# `mod_path`: According to the accepted answer and combine with future power
# if we are in the `helper_script.py`
mod_path = Path(__file__).parent
# OR if we are `import helper_script`
# mod_path = Path(scribe.__file__).parent

# `src_path`: with the future power, it's just so straightforward
relative_path_1 = 'same/parent/with/helper/script/'
relative_path_2 = '../../or/any/level/up/'
src_path_1 = (mod_path / relative_path_1).resolve()
src_path_2 = (mod_path / relative_path_2).resolve()



scribe = Scribe()
scribe.run()