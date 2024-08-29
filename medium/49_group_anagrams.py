from collections import defaultdict


def group_annagrams(strs):
    anagrams = defaultdict(list)

    for str in strs:
        anagrams["".join(sorted(str))].append(str)

    return anagrams.values()


if __name__ == "__main__":
    print(group_annagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_annagrams(["", ""]))
