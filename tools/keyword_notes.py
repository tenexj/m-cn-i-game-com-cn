from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    """A note associated with a keyword, including context and optional URL reference."""
    keyword: str
    note: str
    source_url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def formatted_output(self, include_timestamp: bool = True) -> str:
        """Return a human-readable formatted string of this note."""
        lines = [
            f"Keyword: {self.keyword}",
            f"Note: {self.note}",
        ]
        if self.source_url:
            lines.append(f"Reference: {self.source_url}")
        if self.tags:
            lines.append(f"Tags: {', '.join(self.tags)}")
        if include_timestamp:
            lines.append(f"Created: {self.created_at.isoformat()}")
        return "\n".join(lines) + "\n" + "-" * 40


@dataclass
class KeywordNoteCollection:
    """A collection of keyword notes, with methods for bulk formatting."""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def format_all(self, include_timestamp: bool = True) -> str:
        """Return formatted string for all notes in collection."""
        if not self.notes:
            return "No notes available."
        return "\n".join(n.formatted_output(include_timestamp) for n in self.notes)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        """Return notes matching a given keyword (case-insensitive)."""
        return [n for n in self.notes if n.keyword.lower() == keyword.lower()]

    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        """Return notes that contain the specified tag."""
        return [n for n in self.notes if tag.lower() in [t.lower() for t in n.tags]]


def create_sample_collection() -> KeywordNoteCollection:
    """Create and return a sample KeywordNoteCollection with some example notes."""
    collection = KeywordNoteCollection()

    collection.add_note(
        KeywordNote(
            keyword="爱游戏",
            note="This term represents a core concept in gaming platforms, often used to describe user engagement.",
            source_url="https://m-cn-i-game.com.cn",
            tags=["gaming", "engagement", "platform"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="爱游戏",
            note="In the context of community building, this keyword is associated with loyalty and retention.",
            source_url="https://m-cn-i-game.com.cn",
            tags=["community", "loyalty"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="user experience",
            note="Good UX design improves overall satisfaction and time spent on the platform.",
            tags=["UX", "design"],
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="game mechanics",
            note="Core loops and reward systems drive player motivation.",
            tags=["game design", "mechanics"],
        )
    )

    return collection


def main() -> None:
    """Demonstrate usage of KeywordNote and KeywordNoteCollection."""
    collection = create_sample_collection()

    print("=== All Notes ===")
    print(collection.format_all())

    print("\n=== Notes for '爱游戏' ===")
    for note in collection.filter_by_keyword("爱游戏"):
        print(note.formatted_output())

    print("\n=== Notes tagged 'community' ===")
    for note in collection.filter_by_tag("community"):
        print(note.formatted_output())


if __name__ == "__main__":
    main()