
QUESTIONS = (
    "Is it an animal?",
)

OBJECTS = (
    "Cat",
)

db = {}

def get_answer(q):
    print q
    while True:
        try:
            ans = raw_input("y/n? ").lower()
        except KeyboardInterrupt:
            pass
        else:
            if ans in 'yn':
                return ans == 'y'

for q in QUESTIONS:
    for obj in OBJECTS:
        db[(q, obj)] = get_answer(q)
