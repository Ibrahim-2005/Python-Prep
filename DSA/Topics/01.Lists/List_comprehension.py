word="Hello python"
wordlist=[i for i in word]
print(wordlist)


num=20
numberlist=[i for i in range(num+1)]
print(numberlist)

evenlist=[i for i in range(num+1) if i%2==0]
print(evenlist)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
singleline=[num for row in matrix for num in row]
print(singleline)