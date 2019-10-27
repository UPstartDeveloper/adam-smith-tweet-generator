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
    sublines = list()
    for i in range(lines):
        speech_line = ""
        speech_line += "< "
        index = 0
        for i in range(21):
            if not len(message) == 0:
                speech_line += message[0]
                message = message[1:]
            else:
                speech_line += " "
        speech_line += " >\n"
        sublines.append(speech_line)
    return sublines


def form_message(sublines, message_divider):
    """Form the message portion of speech bubble.
       Param: sublines(list): a list of the chars to go on each line in message
       Return: bubble(str): formaatted to fit inside of a bubble
    """
    bubble = ""
    bubble += message_divider
    bubble += "".join(sublines)
    bubble += message_divider
    return bubble


def draw_speech(message):
    """Given a message, draws a speech bubble for the cow to use.
       Param: message(str)
       Return: speech_bubble(str)
    """
    bubble = ""
    message_divider = " ----------------------- \n"
    limit_line_length = len(message_divider)
    # calculate number of lines the speech bubble will need length-wise
    lines = (len(message) // limit_line_length) + 1
    # form message section of speech bubble
    bubble = form_message(split_message(message, lines), message_divider)
    # form stem section of speech bubble
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
