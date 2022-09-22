def arithmetic_arranger(problems, showResult=False):
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
    lineOne = ''
    lineTwo = ''
    lineThree = ''
    lineResult = ''

    for problem in problems:

        piece = problem.split()
        longestNum = len(piece[0]) > len(piece[2])
        longestLength = max(len(piece[0]), len(piece[2]))

        if longestNum is True:
            diff = len(piece[0]) - len(piece[2])
            numOneSrt = ' ' * 2 + piece[0]
            numTwoSrt = (' ' * (diff + 1)) + piece[2]
        else:
            diff = len(piece[2]) - len(piece[0])
            numOneSrt = ' ' * (diff + 2) + piece[0]
            numTwoSrt = ' ' + piece[2]

        lineOne += numOneSrt
        lineTwo += piece[1] + numTwoSrt
        lineThree += '-' * (longestLength + 2)

        # calculating result
        if showResult is True:
            operandOne = int(piece[0])
            operandTwo = int(piece[2])

            if piece[1] == '-':
                result = operandOne - operandTwo
            else:
                result = operandOne + operandTwo

            lineResult += str(' ' * ((longestLength + 2) - len(str(result))) + str(result))

        # only add 4 spaces if it is not the last arithmetic problem
        if problem != problems[-1]:
            lineOne += '    '
            lineTwo += '    '
            lineThree += '    '
            lineResult += '    '

    if showResult is True:
        return lineOne + '\n' + lineTwo + '\n' + lineThree + '\n' + lineResult
    else:
        return lineOne + '\n' + lineTwo + '\n' + lineThree
