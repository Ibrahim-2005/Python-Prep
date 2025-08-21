s = "A man, a plan, a canal: Panama"

answer=""
for letter in s:
    if letter.isalnum():
        answer+=letter
answer=answer.lower()
print(answer==answer[::-1])