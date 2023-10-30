from package_import import *
from API import *


if __name__ == "__main__":
    greetings()
    while True:
        try:
            while True:
                user_input = str(Telegrammer.get_message())
                print(user_input)
                result = process_user_input(user_input)
                if result is not None:
                    print(result)
                continue
        except Exception as e:
            print(Telegrammer.send_message(f"Error: {e}"))
            continue