with open("File_request.txt") as file:
    f1 = ''.join(file.readlines())
    answer = ""
    for i in range(len(f1)):
        if f1[i].isalpha() and i<len(f1)-2 and f1[i+2].isdigit():
            answer += f1[i]*int(f1[i+1]+f1[i+2])
            i += 1
        elif f1[i].isalpha() and f1[i+1].isdigit():
            answer += f1[i]*int(f1[i+1])
file = open("File_answer.txt", 'w')
file.write(answer)
file.close()
file = open("File_answer.txt", 'r')
print(file.read())
file.close()

'''
Example:
Original .txt file is A3f10b5
Modified .txt will be AAAffffffffffbbbbb
'''