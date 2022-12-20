# import html2markdown
# from markdownify import markdownify as md
import logging
import os
import re
from timeit import default_timer

from bs4 import BeautifulSoup

from scribe.note import Note


class Scribe():
    def run(self, input_root_path: str, output_path: str):
        start = default_timer()
        notes = self.extract_note(input_root_path)
        self.write_notes(notes, output_path)

        end = default_timer()

        logging.info(f"Scribe: Finished in {end - start} seconds.")

    def extract_notes(self, input_path: str) -> list[Note]:
        """
        Args:
            input_path (str): Either path to a single HTML file or a directory (or a tree of directories) containing HTML files.

        Returns:
            list[Note]: _description_
        """
        assert os.path.isdir(input_path) or os.path.splitext(input_path)[1] == ".html"
        walk = list(os.walk(input_path))
        notes: list[Note] = []

        if len(walk) == 0 and input_path.endswith(".html"):
            notes.append(self.extract_note(input_path))
        else:
            for root, dirs, files in walk:
                html_files = [file for file in files if file.endswith(".html")]
                for html_file in html_files:
                    notes.append(self.extract_note(os.path.join(root, html_file)))
        return notes


    def extract_note(self, html_path: str) -> Note:
        assert os.path.splitext(html_path)[1] == ".html"
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

            note = Note(
                title=title.text if title else "",
                authors=authors.text if authors else "",
                citation=citation.text if citation else "",
                tags=self.extract_tags(title.text if title else ""),
                sections_to_notes=sections_to_notes
            )

            return note

    def write_notes(self, notes: list[Note], output_path: str):
        assert os.path.isdir(output_path)
        for note in notes:
            self.write_note(note, output_path)

    def write_note(self, note: Note, output_path: str):
        with open(os.path.join(output_path, self.remove_tags(note.title)), "w") as file:
            note_as_md = note.to_markdown()
            file.write(note_as_md)

        # # Read the HTML file
        # with open(r'C:\Projects\scribe\test_resources\exported notes\[Prediction] What war between the USA and China wo - Notebook.html', 'r') as f:
        #     html = f.read()

        # # Convert the HTML to Markdown
        # markdown1 = html2markdown.convert(html)
        # markdown2 = md(html)

        # # Save the Markdown to a file
        # with open('output.md', 'w') as f:
        #     f.write(markdown2)

    def remove_tags(self, string: str) -> str:
        last_index_of_opening_bracket = string.rfind('[')
        if last_index_of_opening_bracket == -1:
            return string.strip()
        else:
            return string[:last_index_of_opening_bracket].strip()

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

    def remove_leading_and_trailing_newlines(self, string: str):
        if string and string[0] == '\n':
            string = string[1:]
        if string and string[-1] == '\n':
            string = string[:-1]
        return string
