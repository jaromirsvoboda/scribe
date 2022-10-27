from importlib.resources import path
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
@click.option('--path', default=".", help='Path to the folder containing kindle notes (in .html format)')
def main(path):
    print(path)
    scribe = Scribe()
    scribe.run(path)

if __name__ == '__main__':
    main()  # type: ignore