def longestWord(text):
    word_split = re.findall(r"[\w']+", text)
    longest_word = ''
    for word in word_split:
        if len(word) > len(longest_word) and word.isalpha():
            longest_word = word
    return longest_word