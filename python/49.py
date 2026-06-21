from collections import defaultdict
from typing import List


def run(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in words:
        signature = "".join(sorted(word))
        groups[signature].append(word)

    return list(groups.values())