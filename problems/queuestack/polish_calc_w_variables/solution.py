import string

VALID_VAR_SYMBOLS = frozenset(
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    '_'
)

BIN_OPERATORS = {
    '+': int.__add__,
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__floordiv__,  # целочисленное деление, x // y
}


def is_valid_varname(varname):
    # проверка начала имени переменной
    if varname[0] not in VALID_VAR_SYMBOLS or varname[0].isdigit():
        return False

    # проверка на вхождение запрещённых символов
    for char in varname:
        if char not in VALID_VAR_SYMBOLS:
            return False

    return True


# возвращает число переменных из выражения: корректность имён не проверяет
def count_expr_variables(polish):
    varnames = set()
    for lexem in polish.split():
        if lexem != '=' and lexem not in BIN_OPERATORS.keys():
            if is_int(lexem):
                continue
            varnames.add(lexem)
    return len(varnames)


# считывает var_count строк с переменными формата '<varname> <varval> ='
# возвращает словарь корректных переменных и флаг
# флаг == True, если все переменные из блока инициализации имеют корректное имя
def read_variables(var_count):
    variables = dict()
    isvalid = True
    for _ in range(var_count):
        varname, val, _ = input().split()
        if is_valid_varname(varname):
            val = int(val)
            variables[varname] = val
        else:
            isvalid = False
    return variables, isvalid


# проверяет, представима ли строка интом '[-]*[0-9]+'
def is_int(s):
    return s.isdecimal() or s[0] == '-' and s[1:].isdecimal()


def solve():
    polish = input()

    # подсчёт числа переменных в выражении
    var_count = count_expr_variables(polish)

    # считывание блока инициализации переменных
    init_variables, isvalid = read_variables(var_count)
    if not isvalid:
        return None

    # подсчёт выражения
    stack = []
    for lexem in polish.split():
        if lexem == '=':
            # достигли конца выражения, стек должен содержать одно значение
            return stack[0] if len(stack) == 1 else None
        else:
            if lexem in BIN_OPERATORS.keys():  # обработка бинарного оператора
                if len(stack) >= 2:
                    y, x = stack.pop(), stack.pop()
                    z = BIN_OPERATORS[lexem](x, y)
                    stack.append(z)
                else:
                    return None
            else:  # встретили число или переменную
                if is_int(lexem):
                    stack.append(int(lexem))
                else:
                    if lexem in init_variables.keys():
                        stack.append(init_variables[lexem])
                    else:  # переменной из выражения нет в списке инициализации
                        return None
    return None


if __name__ == '__main__':
    ans = solve()
    print('incorrect' if ans is None else ans)
