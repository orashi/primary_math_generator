import random


def generator(num, type):
    question, answer = [], []
    for i in range(num):
        q, a = type()
        question.append(q)
        answer.append(a)
    return question, answer


def sum_sub_2():
    if random.random() > 0.5:  # sum
        a = random.randint(0, 8) * 10 + random.randint(2, 9)
        b = random.randint(0, 8 - a // 10) * 10 + random.randint(11 - a % 10, 9)
        ques = str(a) + ' + ' + str(b) + ' = \n'
        ans = a + b

    else:
        a = random.randint(1, 9) * 10 + random.randint(1, 8)
        b = random.randint(0, a // 10 - 1) * 10 + random.randint(a % 10 + 1, 9)
        ques = str(a) + ' - ' + str(b) + ' = \n'
        ans = a - b
    return ques, ans


def sum_sub_3():
    if random.random() > 0.5:  # sum
        a = random.randint(0, 8) * 10 + random.randint(2, 9)
        b = random.randint(0, 8 - a // 10) * 10 + random.randint(11 - a % 10, 9)
        ans = a + b
        c = random.randint(0, ans // 10 - 1) * 10 + random.randint(ans % 10, 9)
        ques = str(a) + ' + ' + str(b) + ' - ' + str(c) + ' = \n'
        ans = a + b - c
    else:
        a = random.randint(1, 9) * 10 + random.randint(1, 8)
        b = random.randint(0, a // 10 - 1) * 10 + random.randint(a % 10 + 1, 9)
        ans = a - b
        c = random.randint(0, 8 - ans // 10) * 10 + random.randint(10 - a % 10, 9)
        ques = str(a) + ' - ' + str(b) + ' + ' + str(c) + ' = \n'
        ans = a - b + c
    return ques, ans

if __name__ == '__main__':
	ansfile = open('math_2_answer.txt', 'w')
	for i in range(20):
	    ques, ans = generator(52, sum_sub_2)
	    file = open('math_2_' + str(i) + '.txt', 'w')
	    file.writelines(ques)
	    ansfile.write('math' + str(i) + ' answer: ' + str(ans) + '\n')
