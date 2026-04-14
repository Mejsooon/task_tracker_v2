from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class User:
    id: str
    name: str
    username: str
    password: str


@dataclass
class Task:
    id: str
    user_id: str
    difficulty_level: int
    task_target: str
    task_description: str
    reflection_questions: List[str]
    status: str = "active"


@dataclass
class Reflection:
    task_id: str
    user_id: str
    answers: Dict[str, str]
    optional_notes: str = ""