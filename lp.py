def main(n):
    print('food item number', n)


    def loop():
        n = int(input('How many food items do you have'))
        for i in range(n):
            main()


loop()