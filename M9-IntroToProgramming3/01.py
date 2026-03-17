"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations


def normalize_username(name: str) -> str:
    normalized_name = name.strip().lower().replace(" ", "_")
    return normalized_name
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    raise NotImplementedError


def is_valid_age(age: int) -> bool:
    if age < 18 or age > 120:
        return False
    return True
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    return list(filter(None, values))
    """Return a new list containing only truthy values from input."""
    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    return sum(pos for pos in numbers if pos >= 0)
    """Return sum of numbers until the first negative value (exclusive)."""
    raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 3 != 0]
    """Return numbers excluding values divisible by 3."""
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    return next((num for num in numbers if num % 2 == 0), None)
    """Return the first even number, or None if no even number exists."""
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    return [num**2 for num in numbers if num % 2 == 0]
    """Return squares of all even numbers in input order."""
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}
    """Return dict mapping each word to its length."""
    raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    return list(zip(keys, values))
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    return {"name": name, "role": role, "active": active }
    """Build and return {'name': name, 'role': role, 'active': active}."""
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    tags.append(tag)
    return tags
    """Append tag to tags safely (no shared mutable default across calls)."""
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    return {value: key for key, value in mapping.items()}
    """Invert mapping. Assume values are unique."""
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    return sorted(set(tags))
    """Return unique tags sorted ascending."""
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))
    """Count occurrences of each word using collections.Counter."""
    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    groups = defaultdict(list)
    for name, score in records:
        groups[name].append(score)
    return dict(groups)
    """Group scores by student name using collections.defaultdict(list)."""
    raise NotImplementedError


def rotate_queue(items: list[str], steps: int) -> list[str]:
    d = deque(items)
    d.rotate(steps)
    return list(d)
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None
    """Convert string to int, returning None if conversion fails."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip()]
    """Read a text file with a context manager and return non-empty stripped lines."""
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    return sorted(scores, reverse=True)[:n]
    """Return top `n` scores in descending order."""
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    return all(score >= threshold for score in scores)
    """Return True if every score is >= threshold."""
    raise NotImplementedError