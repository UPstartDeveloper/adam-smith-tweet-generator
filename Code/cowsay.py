def get_input():
    """Prompt user to inout message to display."""
    pass


def draw_speech(message):
    """Given a message, draws a speech bubble for the cow to use.
       Param: message(str)
       Return: speech_bubble(str)
    """
    pass


def draw_cow(speech_bubble):
    """Draws the ASCII cow to speak the message.
       Param: speech_bubble(str)
       Return: cow(str)"""
    pass


def cowsay():
    """Implements the cowsay program"""
    message = get_input()
    speech_bubble = draw_speech(message)
    print(draw_cow(speech_bubble))


if __name__ == "__main__":
    cowsay()
