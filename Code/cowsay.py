def get_input():
    """Prompt user to inout message to display."""
    message = input("What would you like the cow to say?")
    return message


def draw_speech(message):
    """Given a message, draws a speech bubble for the cow to use.
       Param: message(str)
       Return: speech_bubble(str)
    """
    bubble = ""
    bubble_top_and_bottom = "-------------------------"
    bubble += bubble_top_and_bottom
    limit_line_length = len(bubble_top_and_bottom)
    # calculate number of lines the speech bubble will length-wise
    lines = len(message) // limit_line_length
    # split message into substring to go on each line

    # only 1 line needed to display method
    if lines == 0:
        bubble += bubble_top_and_bottom
        bubble += f"< {message} >"
        bubble += bubble_top_and_bottom
    else:
        pass
    return bubble



def draw_cow(speech_bubble):
    """Draws the ASCII cow to speak the message.
       Param: speech_bubble(str)
       Return: cow(str)"""
    pass


def cowsay():
    """Implements the cowsay program"""
    # message = get_input()
    message = "Hello, World!"
    speech_bubble = draw_speech(message)
    print(draw_cow(speech_bubble))


if __name__ == "__main__":
    cowsay()
