import random
attempt_lists=[]
def show_score():
    if len(attempt_lists)  <=0:
        print('THERS NO HIGE SCORE!!')
    else:
        print("the currit high_score{}".format(min(attempt_lists)))
def  start_game():
    random_number= int(random.randint(1,100))


