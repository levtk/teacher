from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from logging import Logger
from uuid import UUID

class Kind(Enum):
    """The kind represents the kind of exercise for each within a lesson plan"""
    VIDEO = "VIDEO"
    QUESTION = "QUESTION"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    READING_COMPREHENSION = "READING_COMPREHENSION"

class Level(Enum):
    """Level is the international language level being taught"""
    A1 = auto()
    A2 = auto()
    B1 = auto()
    B2 = auto()
    C1 = auto()
    C2 = auto()

@dataclass
class Exercise():
    id: UUID
    instructor_id: UUID
    kind: Kind
    level: Level
    description: str
    question: str
    link: str|None
    answer_choices: list[str]|None
    free_form_answer: str|None

@dataclass
class Lesson():
    """Class for a lesson which holds exercises, assignment due date, language, etc..."""
    id: UUID
    instructor_id: UUID
    level: Level
    title: str
    language: str
    assigned_to: list[str]
    assigned_on: date
    due_by: date = field(
        metadata={"validate": lambda instance, value: value >= instance.assigned_on}
    )
    exercises: list[Exercise]