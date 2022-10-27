import os
from timeit import default_timer

from bs4 import BeautifulSoup


class Scribe():
    def run(self, root_directory_path: str):
        start = default_timer()
        for root, dirs, files in os.walk(root_directory_path):
            html_files = [file for file in files if file.endswith(".html")]
            for html_file in html_files:
                with open(os.path.join(root, html_file)) as fp:
                    soup = BeautifulSoup(fp, 'html.parser')
                    print(soup)
