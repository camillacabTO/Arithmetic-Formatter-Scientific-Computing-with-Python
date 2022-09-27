def arithmetic_arranger(problems, show_result=False):
    # checking wrong format
    for problem in problems:

        if len(problems) > 5:
            return 'Error: Too many problems.'

        piece = problem.split()

        if not piece[0].isdigit() or not piece[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(piece[0]) > 4 or len(piece[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if piece[1] not in ['-', '+']:
            return 'Error: Operator must be \'+\' or \'-\'.'

    # formatting and solving arithmetic problems
    line_one = ''
    line_two = ''
    line_three = ''
    line_result = ''

    for problem in problems:

        piece = problem.split()
        longest_num = len(piece[0]) > len(piece[2])
        longest_length = max(len(piece[0]), len(piece[2]))

        if longest_num is True:
            diff = len(piece[0]) - len(piece[2])
            num_one_str= ' ' * 2 + piece[0]
            num_two_str = (' ' * (diff + 1)) + piece[2]
        else:
            diff = len(piece[2]) - len(piece[0])
            num_one_str= ' ' * (diff + 2) + piece[0]
            num_two_str = ' ' + piece[2]

        line_one += num_one_str
        line_two += piece[1] + num_two_str
        line_three += '-' * (longest_length + 2)

        # calculating result
        if show_result is True:
            operand_one= int(piece[0])
            Operand_two = int(piece[2])

            if piece[1] == '-':
                result = operand_one- Operand_two
            else:
                result = operand_one+ Operand_two

            line_result += str(' ' * ((longest_length + 2) - len(str(result))) + str(result))

        # only add 4 spaces if it is not the last arithmetic problem
        if problem != problems[-1]:
            line_one += '    '
            line_two += '    '
            line_three += '    '
            line_result += '    '

    if show_result is True:
        return line_one + '\n' + line_two + '\n' + line_three + '\n' + line_result
    else:
        return line_one + '\n' + line_two + '\n' + line_three
