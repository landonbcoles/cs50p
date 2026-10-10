def convert(time):
    x, y = time.split(":")
    z = int(x + y)
    return z

time = input("What time is it? ")

if 700 <= convert(time) < 800:
    print("Breakfast Time")
elif 1200 <= convert(time) < 1300:
    print("Lunch Time")
elif 1800 <= convert(time) < 1900:
    print("Dinner Time")


