class Program:
    def __init__(self, name):
        self.name = name
        self.rules = {}
        # self.alias = {}

    def make_flag_rule(self, flag_rules):
        for rule in flag_rules:
            flag, arg_type = rule.split()
            flag = flag[1:]
            self.rules[flag] = arg_type
            # if self.alias.get(arg_type):
            #     self.alias[arg_type].append(flag)
            # else:
            #     self.alias[arg_type] = [flag]


class Argument_Checklist:
    def __init__(self, arg):
        self.args = arg


    def is_number(self):
        args = self.args
        if len(args) > 1:
            return 0
        return args[0].isdecimal()


    def is_numbers(self):
        args = self.args
        for a in args:
            if not a.isdecimal():
                return 0
        return 1


    def is_string(self):
        args = self.args
        if len(args) > 1:
            return 0
        return args[0].isalpha()


    def is_strings(self):
        args = self.args
        for a in args:
            if not a.isalpha():
                return 0
        return 1


    def is_null(self):
        if self.args:
            return 0
        return 1



def check_argument(flag, arg):
    args = Argument_Checklist(arg)

    if flag == 'NUMBER':
        return args.is_number()
    elif flag == 'NUMBERS':
        return args.is_numbers()
    elif flag == 'STRING':
        return args.is_string()
    elif flag == 'STRINGS':
        return args.is_strings()
    else:
        return args.is_null()


def solution(program_name, flag_rules, commands):
    answer = []

    # program 별로 flag_rule 을 만듭니다.
    program = Program(program_name)
    program.make_flag_rule(flag_rules)

    # 사용자가 입력한 명령어 별로 check_list 를 만들고 검증합니다.
    for command in commands:
        flag = False
        check_list = command.split('-')
        user_program_name = check_list.pop(0).rstrip()

        # program 이 존재하는지 확인
        if not program.name == user_program_name:
            answer.append(flag)
            continue

        program_rule = program.rules
        used_flag = {}

        for tmp in check_list:
            user_input = tmp.split()
            user_flag = user_input.pop(0)

            # flag_rules 에 존재하는 flag 인지 검증
            if not program_rule.get(user_flag):
                break

            # 이미 사용한 flag 인지 검증
            arg_type = program_rule[user_flag]
            if used_flag.get(arg_type):
                break
            else:
                used_flag[arg_type] = 1

            # flag 에 맞는 argument 를 입력하였는지 검증
            if not check_argument(arg_type, user_input):
                break
        else:
            flag = True

        answer.append(flag)

    return answer


# # 프로그램이 여러개가 될 수 있기 때문에 글로벌로 선언합니다.
# program_rules = {}

# program = 'line'
# flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]
# program, flag_rules, commands = "line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]

program = 'line'
flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]

program = 'trip'
flag_rules, commands = ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]

print(solution(program, flag_rules, commands))
