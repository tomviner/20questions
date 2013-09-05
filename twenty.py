import sys
import random
import pickle

def get_answer(q):
    print q
    i = 0
    while True:
        i += 1
        if i > 5:
            print "Why you no like me??"
            raise EOFError
        try:
            ans = raw_input("y/n? ").lower()
        except KeyboardInterrupt:
            sys.exit()
        else:
            if ans and ans[0] in 'yn':
                return ans[0] == 'y'

def final_question(obj, answers):
    if get_answer('I think it\'s a %s?' % obj):
        print 'Success!!!!!'
    else:
        interrogation(obj, answers)

def interrogation(final_obj, answers):
    print 'Give me a question which differentiate between ' + final_obj + ' and your answer'
    question = raw_input()
    print 'Now tell me what it is'
    new_obj = raw_input()
    ans = get_answer('And would you have answered yes or no for %s?' % new_obj)
    db[(question, new_obj)] = ans
    db[(question, final_obj)] = not ans
    for q, a in answers.items():
        db[(q, new_obj)] = a
    print db
    pickle.dump(db, open('db.dojo', 'w'))

# not eval!
db = pickle.load(open('db.dojo'))

qs = {q for (q, obj) in db}
objs = {obj for (q, obj) in db}
answers = {}

for i, question in enumerate(qs):
    answer = get_answer(question)
    answers[question] = answer
    not_objs = [obj for (q, obj), ans in db.items() if q==question and ans!=answer]
    for obj in not_objs:
        if obj in objs:
            objs.remove(obj)

    if len(objs) == 1 or i==19:
        final_question(obj, answers)
        break
    print '\t\t\t(it could be %s things)' % len(objs)
else:
    print "\t\t\tI ran out of questions :("
    if objs:
        for obj in objs:
            interrogation(obj, answers)
    else:
        print "\t\tAnd I also ran out of objects :( I've failed"
        interrogation(final_obj, answers)(random.choice([obj for (q, obj) in db]), answers)


