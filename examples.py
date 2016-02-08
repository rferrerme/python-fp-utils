"""
Some examples that show how to use the Collection helper.
"""

from fp_utils import Collection

# Output: "[100, 80, 60, 40, 20, 0]"
print Collection(range(0, 11)) \
    .filter(lambda x: x%2==0) \
    .map(lambda x: x*10) \
    .comment("Sort descending") \
    .apply(lambda list: sorted(list, reverse=True)) \
    .getValue()

# Output: "Collection(55)"
print Collection(range(1, 11)) \
    .reduce(lambda a,b: a+b, initial=0)

def show(value): print value

# Output: one character per line: "o", "n", "e", "t", "w", "o", "t", "h", "r", "e", "e"
Collection(["one", "two", "three"]) \
    .flatMap(lambda word: list(word)) \
    .forEach(show)