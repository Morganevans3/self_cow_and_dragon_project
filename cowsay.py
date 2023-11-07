import sys
from heifer_generator import HeiferGenerator

if __name__ == '__main__':
    all_list = HeiferGenerator.get_cows()
    cow_list = HeiferGenerator.cow_names
    dragon_list = HeiferGenerator.dragon_names
    all_names = cow_list + dragon_list
    args = sys.argv
    '''
    for cow in all_list:
        print(cow.get_name())
        print(cow.get_image())

    print(args)
    '''

    def list_cows():
        # displays available cows from a Python list of Cow objects
        available = 'Cows available: '
        available += ' '.join(cow_list)
        available += ' '
        available += ' '.join(dragon_list)
        return available

    def find_cow(name, cows):
        # Given a name and a python list of cow objects, return the
        # Cow object with the specified name. If no such Cow object
        # can be found, return None
        # if i in
        for index, cow in enumerate(cows):
            if cow == name:
                return all_list[index]
        return None

    if args[1] == '-l':
        # lists available cows
        print(list_cows())

    elif args[1] == '-n':
        # prints out the message using specified cow
        cow_print = find_cow(args[2], cow_list)
        if cow_print == None:
            dragon_print = find_cow(args[2], all_names)
            if dragon_print == None:
                print(f'Could not find {args[2]} cow!')
            else:
                print(' '.join(args[3:]))
                print(dragon_print.get_image())
                fire = dragon_print.can_breathe_fire()
                if fire == True:
                    print('This dragon can breathe fire.')
                else:
                    print('This dragon cannot breathe fire.')
        else:
            print(' '.join(args[3:]))
            print(cow_print.get_image())

    else:
        # prints out the message using default cow (heifer)
        print(' '.join(args[1:]))
        print(all_list[0].get_image())

