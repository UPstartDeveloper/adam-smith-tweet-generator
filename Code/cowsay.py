def get_input():
    """Prompt user to inout message to display."""
    message = input("What would you like the cow to say?")
    return message


def split_message(message, lines):
    """Given a message to display and the number of lines to display on,
       return a list of the substrings from the message to display
       for each line.
       Param: message(str)
              lines(int)
       Return: sublines(list):
    """
    pass


def draw_speech(message):
    """Given a message, draws a speech bubble for the cow to use.
       Param: message(str)
       Return: speech_bubble(str)
    """
    bubble = ""
    bubble_top_and_bottom = "-------------------------"
    limit_line_length = len(bubble_top_and_bottom)
    # calculate number of lines the speech bubble will length-wise
    lines = len(message) // limit_line_length

    # only 1 line needed to display method
    if lines == 0:
        bubble += bubble_top_and_bottom + "\n"
        bubble += f"< {message} >\n"
        bubble += bubble_top_and_bottom + "\n"
    else:
        # split message into substring to go on each line
        sublines = split_message(message, lines)
    return bubble


def draw_cow(speech_bubble):
    """Draws the ASCII cow to speak the message.
       Param: speech_bubble(str)
       Return: cow(str)"""
    return speech_bubble


def cowsay():
    """Implements the cowsay program"""
    # message = get_input()
    message = "Hello, World!"
    speech_bubble = draw_speech(message)
    print(draw_cow(speech_bubble))


if __name__ == "__main__":
    cowsay()
