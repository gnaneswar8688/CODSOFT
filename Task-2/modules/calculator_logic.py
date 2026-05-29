def calculate_expression(expression):

    try:
        result = eval(expression)
        return str(result)

    except:
        return "Error"