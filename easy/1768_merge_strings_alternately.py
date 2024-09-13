def mergeAlternately(word1: str, word2: str):
    i = 0
    j = 0
    response = ""

    while i < len(word1) and j < len(word2):
        response += word1[i] + word2[j]
        i += 1
        j += 1

    # if one of pointer is smaller than str len we append remaining char to the response
    if i < len(word1):
        response += word1[i:]
    if j < len(word2):
        response += word2[j:]

    return response


if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"

    print(mergeAlternately(word1, word2))
