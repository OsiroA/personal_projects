def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
        
    tops = []
    seconds = []
    dashes = []
    answers = []
    
    for problem in problems:
        left, op, right = problem.split()
        #print(left, op, right)
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        

        #to get the column width
        width = max(len(left), len(right)) + 2

        #to make the left side right aligned
        top_piece = left.rjust(width)

        second_piece = op + right.rjust(width - 1)
        dash_piece = "-" * width

        if op == "+":
            result = int(left) + int(right)
        else:
            result = int(left) - int(right)
        answer_piece = str(result).rjust(width)

        tops.append(top_piece)
        seconds.append(second_piece)
        dashes.append(dash_piece)
        if show_answers:
            answers.append(answer_piece)

    line1 = "    ".join(tops)
    line2 = "    ".join(seconds)
    line3 = "    ".join(dashes)
    if show_answers:
        line4 = "    ".join(answers)
    
    if show_answers is True:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        return line1 + "\n" + line2 + "\n" + line3
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
