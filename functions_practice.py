def hello():
    print("hello , user")


def pack(x,y,z):
    return print(f("x:{x},y:{y},z:{z}"))

def eat_lunch(list_food):
    if len(list_food)==0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {list_food[0]}")
        for food in list_food[1:]:
            print(f"Next I eat, {food}")
            

