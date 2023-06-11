from par import par

def main():
    while True:
        print('ВЫ ----------- ')
        num  = input().lower()
        rezult = par(num)
        if rezult == False:
            break
   
if __name__ == '__main__':
    main()


# принимаем номер телефона только вида +xx(xxx)-xxx-xxxx +38(096)-289-3087