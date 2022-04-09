from question import Question

test = [

    "1+4=?\n(a) 2\n(b) 4\n(c) 5\n\n "
    "1公尺幾公分?\n(a) 1\n(b) 10\n(c)100\n\n"
    "蘋果是啥顏色?\n(a) 黑色\n(b) 紅色\n(c) 黃色\n\n"
]

questions = [
    Question(test[0], "c" ),
    Question(test[1], "c" ),
    Question(test[0], "b" ),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    print ("你得到" + str(score) + "分,共" + str(len(questions)) +"題" )

run_test(questions)