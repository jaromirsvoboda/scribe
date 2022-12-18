import os
import re
from timeit import default_timer

from bs4 import BeautifulSoup
# import html2markdown
# from markdownify import markdownify as md
import logging

from scribe.note import Note


class Scribe():
    def run(self, root_path: str):
        start = default_timer()
        walk = list(os.walk(root_path))
        notes: list[Note] = []
        if len(walk) == 0 and root_path.endswith(".html"):
            notes.append(self.extract_note(root_path))
            return
        else:
            for root, dirs, files in walk:
                html_files = [file for file in files if file.endswith(".html")]
                for html_file in html_files:
                    notes.append(self.extract_note(os.path.join(root, html_file)))
        end = default_timer()
        
        logging.info(f"Scribe: Finished in {end - start} seconds.")
        
        
    def extract_note(self, html_path: str) -> Note:
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

    def extract_tags(self, string: str) -> list[str]:
        pattern = r'\w+ \[(.*)\]\s*$'

        match = re.search(pattern, string)

        if match:
            extracted_text = match.group(1)
            parts = extracted_text.split(',')
            stripped_parts = [part.strip() for part in parts if part.strip() != '']
            return stripped_parts
        else:
            return []
