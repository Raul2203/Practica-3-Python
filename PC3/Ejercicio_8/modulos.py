import random
def generate_number():
    list=[]
    for i in range(20):
        list.append(random.randint(0,100))
    return list


def show_list(list):
    print(list)    

def sort_list(list):
    return list.sort()



