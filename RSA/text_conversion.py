def string_to_list_of_char(input_string: str):
    """
  string to charater converter
  """
    output = None
    if isinstance(input_string, str):
        output = list(input_string)
        output = ''
        for i in input_string:
            output += i
    else:
        print('incorrect input type')
    return output


#character-ASCII converter
def char_to_ascii(input_list: list):
    output = []
    if isinstance(input_list[0], str):
        for i in input_list:
            output.append(ord(i))
    elif isinstance(input_list[0], int):
        for i in input_list:
            output.append(chr(i))
    else:
        print('incorrect input type')
    return output
