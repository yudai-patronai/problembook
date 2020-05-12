n = int(input())
words = dict()
for i in range(n):
    word = input()
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words.update({word: 1})
maxfreq = max(words.values())
for key in words:
    if words[key] == maxfreq:
        print(key, words[key])
