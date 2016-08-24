import re


def match_rule(pattern, word):
    return re.search(pattern, word)


def apply_rule(search, replace, word):
    return re.sub(search, replace, word)


rules = []
words = ["coach", "wax", "vacancy", "day"]
for word in words:
    with open("plural.txt", encoding="utf-8") as plural_file:
        for line in plural_file:
            pattern, search, replace = line.split(None, 3)
            if match_rule(pattern, word):
                rules.append(apply_rule(search, replace, word))
                break
print(rules)
