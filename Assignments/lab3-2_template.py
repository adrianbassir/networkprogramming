"""Don't forget your docstrings!
"""
import socket


def build_list():
    """Collect input from the user and return it as a list.

    Only numeric input will be included; strings are rejected.
    """
    #Create a list to store our numbers
    unsorted_list = []

    # Create a variable for input
    user_input = ""

    while user_input != "done":
        # Prompt the user for input
        user_input = input("Please enter a number, or 'done' to stop.")

        # Validate our input, and add it to out list
        # if it's a number
        try:
            # Were we given an integer?
            unsorted_list.append(int(user_input))
        except ValueError:
            try:
                # Were we given a floating-point number?
                unsorted_list.append(float(user_input))
            except ValueError:
                # Non-numeric input - if it's not "done",
                # reject it and move on
                if (user_input != "done"):
                    print ("ERROR: Non-numeric input provided.")
                continue

    # Once we get here, we're done - return the list
    return unsorted_list

def sort_list(unsorted_list):
    """Sorts a list of numbers by sending it to a remote server.

    Args:
        unsorted_list (list): A list of numeric values to be sorted.

    Prints:
        The sorted list received from the server or an error message.
    """
    server_ip = "159.203.166.188"
    server_port = 7778
    list_str = "LIST " + " ".join(map(str, unsorted_list))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((server_ip, server_port))

        s.sendall(list_str.encode('ascii'))

        response = s.recv(1024)

        print(response.decode('ascii'))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()


def main():
    """Call the build_list and sort_list functions, and print the result."""
    number_list = build_list()
    sort_list(number_list)

if __name__ == "__main__":
    main()

