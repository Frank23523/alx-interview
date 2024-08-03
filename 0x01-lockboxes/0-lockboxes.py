#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list where each element is a list of a box.
                           Each box contains keys (integers) to other boxes.
                           boxes[i] is the list of keys found in box i.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = set([0])  # The first box is already unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
