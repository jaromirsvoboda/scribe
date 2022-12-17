import os
from timeit import default_timer

from bs4 import BeautifulSoup
# import html2markdown
# from markdownify import markdownify as md
import logging


class Scribe():
    def run(self, root_path: str):
        start = default_timer()
        walk = list(os.walk(root_path))
        if len(walk) == 0 and root_path.endswith(".html"):
            self.process_html_file(root_path)
            return
        else:
            for root, dirs, files in walk:
                html_files = [file for file in files if file.endswith(".html")]
                for html_file in html_files:
                    self.process_html_file(os.path.join(root, html_file))
        end = default_timer()
        
        logging.info(f"Scribe: Finished in {end - start} seconds.")
        
        
    def process_html_file(self, html_path: str) -> str:
        with open(html_path, encoding='utf-8') as fp:
            # content = fp.read()
            soup = BeautifulSoup(fp, 'html.parser')
            print(soup)
            
            title = soup.find('div', {'class': ['bookTitle']})
            authors = soup.find('div', {'class': ['authors']})
            citation = soup.find('div', {'class': ['citation']})
            # sectionHeadings = soup.find('div', {'class': ['sectionHeading']})
            
            all_notes = soup.find_all('div', {'class': ['noteText']})
            sections_to_notes: dict[str, list[str]] = {}
            for note in all_notes:
                section_heading = note.find_previous_sibling('div', {'class': {'sectionHeading'}}).text
                if section_heading not in sections_to_notes:
                    sections_to_notes[section_heading] = []
                sections_to_notes[section_heading].append(note.text)
            
            
            return "a"

        # # Read the HTML file
        # with open(r'C:\Projects\scribe\test_resources\exported notes\[Prediction] What war between the USA and China wo - Notebook.html', 'r') as f:
        #     html = f.read()

        # # Convert the HTML to Markdown
        # markdown1 = html2markdown.convert(html)
        # markdown2 = md(html)

        # # Save the Markdown to a file
        # with open('output.md', 'w') as f:
        #     f.write(markdown2)
