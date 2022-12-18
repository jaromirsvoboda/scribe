from dataclasses import dataclass

@dataclass
class Note():
    title: str
    authors: str
    citation: str
    tags: list[str]
    sections_to_notes: dict[str, list[str]]
    
    # def __str__(self):
    #     return f"Title: {self.title}
    
    def to_markdown(self):
        text = ""
        text += f"# {self.title}\n"
        text += "\n"
        text += f"## {self.authors}\n"
        text += "\n"
        text += f"## {self.citation}\n"
        for tag in self.tags:
            text += f"#{tag}\n"
        
        for section, notes in self.sections_to_notes.items():
            text += f"### {section}\n"
            for note in notes:
                text += f"- {note}\n"