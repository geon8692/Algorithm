def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        tmp = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                tmp += char.upper()
            else:
                tmp += char.lower()
        answer.append(tmp)
    return " ".join(answer)