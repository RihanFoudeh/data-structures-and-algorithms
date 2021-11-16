def validate_brackets(input):
    List=[]

    Round_open = input.count('(')
    Round_close = input.count(')')
    Curly_open = input.count('{')
    Curly_close = input.count('}')
    Square_open = input.count('[')
    Square_close = input.count(']')




    if Round_open == Round_close and Curly_open == Curly_close and Square_open == Square_close:
        for char in input:

            if char == '{' or char == '(' or char == '[':
                List.append(char)

            elif char == '}' or char == ')' or char == ']':
                print(List)

                element = List.pop()
                print(List)

                if not Compareing(element, char):
                    return False
        return True

    else:
        return False


def Compareing(opening, closing):

    if opening == '(' and closing == ')':
        return True

    if opening == '[' and closing == ']':
        return True

    if opening == '{' and closing == '}':
        return True

    return False



""" if __name__=='__main__':


    print(validate_brackets('')) """


