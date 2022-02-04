# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def main():
    tea_chosen = False
    coffee_chosen = True

    if tea_chosen ^ coffee_chosen:
        print("Your drink is being processed")
    else:
        print("Choose either tea or coffee but not both")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()