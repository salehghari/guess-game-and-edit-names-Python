import pyfiglet
list_of_names = []
answer = input("do you want to edit your list of names?yes or no?")
answer_2 ='add'
if answer == 'no':
    print(pyfiglet.figlet_format(': ('))
elif answer == 'yes':
    while answer_2 == 'add' or answer_2 == 'remove' or answer_2 == 'display':
        answer_2 = input("well.what do you want to do with this list?add,remove or display names?")
        if answer_2 == 'add':
            a = input("now,what name do you want to add?")
            list_of_names.append(a)
            print(list_of_names)

        if answer_2 == 'remove':
            b = input("now,what name do you want to remove?")
            try:
                list_of_names.remove(b)
            except ValueError:
                print("name not defind in the list!")
            print(list_of_names)

        if answer_2 == 'display':
            print(list_of_names)
# while answer != 'yes' and answer != 'no':
#     print("please say yes or no!")