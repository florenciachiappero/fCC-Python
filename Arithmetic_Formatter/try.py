def main():
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))


def arithmetic_arranger(problems, solver = False):

    # Principal Variables
    #arranged_problems = []
    first = ""
    second = ""
    line = ""
    total_sol = ""

    # First error check.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Loop through "problems"
    for problem in problems:
        firstNumber = problem.split()[0]
        operator = problem.split()[1]
        secondNumber = problem.split()[2]

        if firstNumber.isdigit() and secondNumber.isdigit():
            # Second error check.
            if len(firstNumber) > 4 or len(secondNumber) > 4:
                return "Error: Numbers cannot be more than four digits."
        # Third error check.
        else:
            return "Error: Numbers must only contain digits."

        # Forth error check.
        if operator == "+":
            operation = int(firstNumber) + int(secondNumber)
        elif operator == "-":
            operation = int(firstNumber) - int(secondNumber)
        else:
            return "Error: Operator must be '+' or '-'."


        long_value = max(len(firstNumber), len(secondNumber))
        width = long_value + 2

        top = str(firstNumber).rjust(width)
        bottom = operator + str(secondNumber).rjust(width - 1)
        lines = "-" * width
        solution = str(operation).rjust(width)

        # Add to the string to print it
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            line += lines + '    '
            total_sol += solution + '    '
        else:
            first += top
            second += bottom
            line += lines
            total_sol += solution
        
    if solver:
        arranged_problems = first + "\n" + second + "\n" + line + "\n" + total_sol
    else:
        arranged_problems = first + '\n' + second + '\n' + line
    return arranged_problems


if __name__ == "__main__":
    main()