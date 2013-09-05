import random
import pickle

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

def final_question(obj):
    if get_answer('Is it %s?' % obj):
        print 'Success'
    else:
        interogation(obj)

def interogation(obj):
    print 'Give me a question which differentiate between ' + obj + ' and your answer'
    question = raw_input()
    print 'Now tell me what it is'
    obj = raw_input()
    ans = get_answer('And would you have answered yes or no')
    db[(question, obj)] = ans
    for q, a in answers.items():
        db[(q, obj)] = a
    print db
    pickle.dump(db, open('db.dojo', 'w'))

# not eval
db = pickle.load(open('db.dojo'))

qs = {q for (q, obj) in db}
objs = {obj for (q, obj) in db}
answers = {}

for i, question in enumerate(qs):
    answer = get_answer(question)
    answers[question] = answer
    not_objs = [obj for (q, obj), ans in db.items() if q==question and ans!=answer]
    for obj in not_objs:
        objs.remove(obj)

    if len(objs) == 1 or i==19:
        final_question(obj)
        # print 'IT IS ' + obj
        break
    print 'it could be', objs
else:
    print "I ran out of questions"
    if objs:
        for obj in objs:
            interogation(obj)
    else:
        print "And I also ran out of objects :( I've failed"
        interogation(random.choice([obj for (q, obj) in db]))







db[(q, obj)]
# 0: 'Y'
temp_db = db
# number of question and

# for q in QUESTIONS:
#     for obj in OBJECTS:
#         db[(q, obj)] = get_answer(q)

# print db

def pick_qestion():
    return
