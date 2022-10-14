import logging
import time

# timestamp = time.strftime("%Y-%m-%d_%H-%M-%S_%p")
# logging.basicConfig(
#     filename=fr"\{timestamp}.log",
#     filemode='a',
#     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#     datefmt='%H:%M:%S',
#     level=logging.DEBUG
# )
# logging.getLogger().addHandler(logging.StreamHandler())


# Hope you don't be imprisoned by legacy Python code :)
from pathlib import Path

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