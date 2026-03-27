"""Lecture 09 exercises (Python internals).

Implement each function as a small experiment.

Use this mental model:
names -> references -> objects
"""

from __future__ import annotations

from collections.abc import Callable
 

def extract_opnames(source: str) -> list[str]:
    return [instr.opname for instr in dis.Bytecode(source)]


def aliasing_after_append() -> tuple[list[int], list[int], bool]:
    a = [1, 2]
    b = a
    b.append(3)
    return a, b, id(a) == id(b)


def copy_after_append() -> tuple[list[int], list[int], bool]:
    a = [1, 2]
    b = a.copy()
    b.append(3)
    return a, b, id(a) == id(b)


def rebind_after_concat() -> tuple[list[int], list[int], bool]:
    a = [1, 2]
    b = a
    b = b + [3]
    return a, b, id(a) == id(b)


def refcount_steps() -> tuple[int, int, int]:
    obj = []
    start_count = sys.getrefcount(obj)
    
    alias = obj
    with_alias_count = sys.getrefcount(obj)
    
    del alias
    after_delete_count = sys.getrefcount(obj)
    
    return start_count, with_alias_count, after_delete_count


def make_incrementer(start: int = 0) -> Callable[[], int]:
    count = start

    def inc() -> int:
        nonlocal count
        count += 1
        return count

    return inc


def inject_with_exec(namespace: dict[str, object], statement: str) -> dict[str, object]:
    exec(statement, namespace)
    return namespace


def function_locals_snapshot() -> dict[str, int]:
    def inner() -> dict[str, int]:
        a = 10
        b = 20
        return dict(locals())
    
    return inner()


def cycle_collected() -> bool:
    class Node:
        pass

    n1 = Node()
    n2 = Node()
 
    n1.ref = n2
    n2.ref = n1

    w1 = weakref.ref(n1)
    w2 = weakref.ref(n2)

    del n1
    del n2

    gc.collect()

    return w1() is None and w2() is None


def shallow_vs_deep_copy_state() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    original = [[1], [2]]
    shallow = original.copy()
    deep = copy.deepcopy(original)
    
    shallow[0].append(99)

    return original, shallow, deep
