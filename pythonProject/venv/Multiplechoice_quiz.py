from question import Ask

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) purple\n(c) Orange\n\n"
    "What color are bananas?\n(a)Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

testing = [
    Ask(question_prompts[0], "a"),
    Ask(question_prompts[1], "c"),
    Ask(question_prompts[2], "b"),
]


def run_test(testing):   # not sure what is wrong here.
    score = 0
    for Ask in testing:
        answer = input(Ask.prompts)
        if answer == Ask.answer:
            score = + 1
    print("You got " + str(score) + "/" + str(len(testing)) + " Correct")


run_test(testing)
