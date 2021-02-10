message = None
while True:
    message = input("Введите возраст посетителя кинотеатра: ")
    if message =="quit": break
    try:
        message = int(message)
        if message <= 3:
            print("Билет бесплатный")
        elif message <= 12:
            print("Билет стоит 10 долларов")
        elif message > 12:
            print("Билет стоит 15 долларов")
    except:
        print("введено не число")
