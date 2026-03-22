def create_user(**user):
    return user

user_info = create_user(name="danielo", email="danielojsandil@gmail.com", age=27)
print(type(user_info))



def make_greeter(greeting):
    def greet(name):
        print(f"{greeting}, {name}")
    return greet

greet_someone = make_greeter("hello")
greet_someone("danielo")



# without closure
count = 0

def increment():
    global count
    count += 1
    return count

print(increment())
print(increment())
print(increment())



# with closure - state is private
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
page_views = make_counter()
login_count = make_counter()

print(counter())
print(page_views())
print(login_count())



# without closure - repeat the config every call
def apply_tax(price, tax_rate=0.08):
    return price * (1 + tax_rate)

print (apply_tax(100))
print (apply_tax(200, 0.05))



# with closure - configure once, reuse cleanly
def make_tax_calculator(tax_rate):
    def calculate(price):
        return price * (1 + tax_rate)
    return calculate

us_tax = make_tax_calculator(0.8)
eu_tax = make_tax_calculator(0.5)
id_tax = make_tax_calculator(0.2)

print(us_tax(100), eu_tax(100), id_tax(100))

def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@log
def add(a, b, c):
    return a + b + c
@log
def multiply(a, b):
    return a * b


print(add(2, 3, 4))
print(multiply(1, 2))
