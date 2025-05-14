

def hello():
    print("Hello from Python")



# function calls
hello()

def test_1():
    name = "Sergio"
    last = "Inzunza"

    print(name + " " + last)

def test_if(age):
    if age < 21:
        print("You cannot drink")
    else:
        print("Please, have a beer")


def test_for():
    nums = [2,4,3,167,34,73,74,13,67,8]
    total=0
    for num in nums:
        total += num
        print(num)

    print("Total sum is: " + str(total))


def test_dict():
    dog = { "name": "Lola",
        "age": 3}
    print(dog)
    print(dog["name"])



def test_list():
    products =[
        {"title": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
        {"title": "Yoga Mat", "price": 19.99, "category": "Fitness"},
        {"title": "Coffee Maker", "price": 49.99, "category": "Home Appliances"},
        {"title": "Bluetooth Headphones", "price": 79.99, "category": "Electronics"},
        {"title": "Running Shoes", "price": 59.99, "category": "Footwear"},
        {"title": "Desk Lamp", "price": 22.50, "category": "Office Supplies"}
        ]

    total = 0
    for prod in products:
        print(prod["title"])
        total += prod["price"]
    
    print("the sum of prices is: " + str(total))






    # function calls
hello()
test_1()


test_if(18)
test_if(30)

test_for()
test_dict()
test_list()