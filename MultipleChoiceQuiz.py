from Question import Question

questions_prompts=[
    "What color are apples?\na.Red\nb.Purple\nc.Pink\n\n",
    "What color are bananas?\na.Blue\nb.Red\nc.Yellow\n\n",
    "What color is the sky?\na.Purple\nb.Black\nc.Blue\n\n"
]
questions=[
    Question(questions_prompts[0],"a"),
    Question(questions_prompts[1],"c"),
    Question(questions_prompts[2],"c"),
]

def RunTest(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer ==question.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+" right")

RunTest(questions)