class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def process_data(data):
    try:
        if not isinstance(data, int):
            raise InvalidDataException("Invalid data type. Integer expected.")
        elif data < 0:
            raise ProcessingException("Negative number not allowed.")
    except InvalidDataException as e:
        print(f"InvalidDataException: {e}")
    except ProcessingException as e:
        print(f"ProcessingException: {e}")
    else:
        print("Data processing successful.")
    finally:
        print("Data processing finished.")


def main():
    try:
        data = input("Enter a number: ")
        process_data(int(data))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except InvalidDataException as e:
        print(f"InvalidDataException: {e}")
    except ProcessingException as e:
        print(f"ProcessingException: {e}")


if __name__ == "__main__":
    main()
