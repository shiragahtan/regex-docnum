import sys
# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))
# print("argv2" , str(sys.argv[1]))

"""
def starting_regex(list_of_docnum):
    reg = []
    big_length = 0
    for docnum in list_of_docnum:
        if len(docnum) > big_length:
            big_length = len(docnum)
    min_length = big_length
    for docnum in list_of_docnum:
        if len(docnum) < min_length:
            min_length = len(docnum)
    for i in range(big_length):
        reg.append([])
        add_question = False
        if i >= min_length:
            add_question = True
        for docnum in list_of_docnum:
            if len(docnum) > i:
                if docnum[i] not in reg[i]:
                    reg[i] += docnum[i]
        if add_question:
            reg[i] = ''.join(reg[i]) + "?"
        else:
            reg[i] = ''.join(reg[i])
    #final_regex = ''.join(str(obj) for obj in reg)
    #return "^(" + final_regex + ")$"
    print(reg)
    return reg

def organize_regex(final_regex):
    list_regex = final_regex.split(',')
    organize = []
    last_one = ""
    num_last = 0
    for i in list_regex:
        if i == last_one:
            num_last += 1
        else:
            if num_last > 1 :
                organize += "(" + last_one + ")"
                organize += "{" + str(num_last) + "}"
            else:
                organize += last_one
            last_one = i
            num_last = 1
    if num_last > 1:
        organize += "(" + last_one + ")"
        organize += "{" + str(num_last) + "}"
    else:
        organize += last_one
    organize = "".join(organize)
    print(organize)
    return "(" + organize + ")"

def final_regex(regex_start):
    regex_start = starting_regex(regex_start)
    final = []
    for i in regex_start:
        add_to_final = []
        add_question = False
        if len(i) < 5:
            for char in i:
                if char == "?":
                    add_question = True
                    continue
                if char == "*":
                    char = "\*"
                elif char == ".":
                    char = "\."
                add_to_final += char
            if add_question:
                if len(i) < 3:
                    final += ''.join(add_to_final) + "?,"
                else:
                    final += "[" + ''.join(add_to_final) + "]?,"
            else:
                if len(i) == 1:
                    final += ''.join(add_to_final) + ","
                else:
                    final += "[" + ''.join(add_to_final) + "],"
            continue
        for char in i:
            if char.isdigit():
                if "0-9" not in add_to_final:
                    if len(add_to_final) == 0 :
                        add_to_final.append("[")
                    add_to_final.append("0-9")
            elif char.isalpha():
                if char.islower():
                    if "a-z" not in add_to_final:
                        if len(add_to_final) == 0:
                            add_to_final.append("[")
                        add_to_final.append('a-z')
                elif char.isupper:
                    if "A-Z" not in add_to_final:
                        if len(add_to_final) == 0:
                            add_to_final.append("[")
                        add_to_final.append('A-Z')
            elif char == "?":
                add_question = True
            elif char == "*" or char == ".":
                if char not in add_to_final:
                    if len(add_to_final) == 0:
                        add_to_final.append("[")
                    if char == "*":
                        add_to_final.append("\*")
                    elif char == ".":
                        add_to_final.append("\.")
            else:
                if char not in add_to_final:
                    if len(add_to_final) == 0:
                        add_to_final.append('[')
                    add_to_final.append(char)
        with_options = False
        for i in add_to_final:
            if i== "|":
                with_options = True
        if with_options :
            if add_question:
                final += "(" + ''.join(add_to_final) + ")?,"
            else:
                final += "(" + ''.join(add_to_final) + "),"
        else:
            if add_question:
                final += "[" + ''.join(add_to_final) + "]?,"
            else:
                final += "[" + ''.join(add_to_final) + "],"
    final_regex = ''.join(str(obj) for obj in final)
    final_regex = final_regex.replace("[[","[")
    final_regex = final_regex.replace("]]", "]")
    final_regex = final_regex[:-1]
    most_final = organize_regex(final_regex)
    most_final
    return most_final
    #organize_regex(final_regex)
    #organize_regex(final)

def get_regex():
    user_input = input("please enter the string that you want for the regex:")
    list_of_docnum = list(user_input.split('\n'))
    print(list_of_docnum)
    #final_regex(list_of_docnum)
#print(starting_regex(["3rs","3s","3ef","345","3edf","3dv","3y","rrrrt","DF"]))
#print(final_regex(["3rs","3s","3ef","345","3edf","3dv","3y","rrrrt","DF"]))

#print(get_regex())

organize_string = '[YFBD][[0-9]][[0-9]][[0-9]][[0-9]][[0-9]][[0-9]][[0-9]]'
#print(organize_regex(organize_string))"""


def starting_regex(list_of_docnum):
    reg = []
    big_length = 0
    for docnum in list_of_docnum:
        if len(docnum) > big_length:
            big_length = len(docnum)
    min_length = big_length
    for docnum in list_of_docnum:
        if len(docnum) < min_length:
            min_length = len(docnum)
    for i in range(big_length):
        reg.append([])
        add_question = False
        if i >= min_length:
            add_question = True
        for docnum in list_of_docnum:
            if len(docnum) > i:
                if docnum[i] not in reg[i]:
                    reg[i] += docnum[i]
        if add_question:
            reg[i] = ''.join(reg[i]) + "?"
        else:
            reg[i] = ''.join(reg[i])
    return reg

def organize_regex(final_regex):
    list_regex = final_regex.split(',')
    organize = []
    last_one = ""
    num_last = 0
    for i in list_regex:
        if i == last_one:
            num_last += 1
        else:
            if num_last > 1 :
                organize += "(" + last_one + ")"
                organize += "{" + str(num_last) + "}"
            else:
                organize += last_one
            last_one = i
            num_last = 1
    if num_last > 1:
        organize += "(" + last_one + ")"
        organize += "{" + str(num_last) + "}"
    else:
        organize += last_one
    organize = "".join(organize)
    return "(" + organize + ")"

def final_regex(regex_start):
    regex_start = starting_regex(regex_start)
    final = []
    delim = ".,\\*|$^-[]()"
    for i in regex_start:
        add_to_final = []
        add_question = False
        if len(i) < 5:
            for char in i:
                if char == "?":
                    add_question = True
                    continue
                if char == "*":
                    char = "\*"
                elif char == ".":
                    char = "\."
                add_to_final += char
            if add_question:
                if len(i) < 3:
                    final += ''.join(add_to_final) + "?,"
                else:
                    final += "[" + ''.join(add_to_final) + "]?,"
            else:
                """if len(i) == 1:
                    final += ''.join(add_to_final) + ","
                else:
                    final += "[" + ''.join(add_to_final) + "],""""
                final += (char + ',') if len(i) == 1 else add_parentheses(char,'[' , ']')
            continue
        for char in i:
            if char.isdigit():
                if "0-9" not in add_to_final:
                    if len(add_to_final) == 0 :
                        add_to_final.append("[")
                    add_to_final.append("0-9")
            elif char.isalpha():
                if char.islower():
                    if "a-z" not in add_to_final:
                        if len(add_to_final) == 0:
                            add_to_final.append("[")
                        add_to_final.append('a-z')
                elif char.isupper:
                    if "A-Z" not in add_to_final:
                        if len(add_to_final) == 0:
                            add_to_final.append("[")
                        add_to_final.append('A-Z')
            elif char == "?":
                add_question = True
            elif char == "*" or char == ".":
                if char not in add_to_final:
                    if len(add_to_final) == 0:
                        add_to_final.append("[")
                    if delim.__contains__(char):
                        add_to_final.append("\\")
                        add_to_final.append(char)
                    """if char == "*":
                        add_to_final.append("\*")
                    elif char == ".":
                        add_to_final.append("\.")"""
            else:
                if char not in add_to_final:
                    if len(add_to_final) == 0:
                        add_to_final.append('[')
                    add_to_final.append(char)
        with_options = False
        for i in add_to_final:
            if i== "|":
                with_options = True
        if with_options :
            if add_question:
                final += "(" + ''.join(add_to_final) + ")?,"
            else:
                final += "(" + ''.join(add_to_final) + "),"
        else:
            if add_question:
                final += "[" + ''.join(add_to_final) + "]?,"
            else:
                final += "[" + ''.join(add_to_final) + "],"
    final_regex = ''.join(str(obj) for obj in final)
    final_regex = final_regex.replace("[[","[")
    final_regex = final_regex.replace("]]", "]")
    final_regex = final_regex[:-1]
    most_final = organize_regex(final_regex)
    return most_final

def add_parentheses(string, parentheses_s, parentheses_e):
    return parentheses_s + string + parentheses_e + ","


list = """---
!!!
@@@
###
|||
..."""

string_of_list = list.split("\n")

#list = list("9STO998423SJ12808aE68NYZ\r\n0GOM001046GA12808iE70NYZ\r\n0NOR022403NI52714hE70NYZ\r\n0JAC020457JJ12802iE71NYZ\r\n0TWI037799TS52726dE63NYZ\r\n0LEN011642LS52806bE63NYZ\r\n9BUR981979BM12302aE72NYZ\r\n0HOS020907HC12408hE69NYZ\r\n0LIT026389LE52922aE64NYZ\r\n0MCK033830MS52629fE60NYZ\r\n0TUR027832TJ12821IE69NYZ\r\n0ARR025108AI12808jE72NYZ\r\n0BRI019605BK52810kE65NYZ\r\n3BOU031091BV52909cE65NYZ\r\n0HEL034493HA52803bE62NYZ\r\n0GRA022979GT52706fE59NYZ\r\n9LEO999035LA12520kE75NYZ\r\n0ROC025062RA52619dE60NYZ\r\n0HER021094HM52326fE59NYZ\r\n0VIV003212VD52609cE63NYZ\r\n0MOC012431MS52524dE61NYZ\r\n0AHM037331AA12826jE67NYZ\r\n0FIN025394FM52704iE61NYZ\r\n0KAN044399KK52802cE62NYZ\r\n9ROM972948RN52308gE64NYZ\r\n9DAV997214DK12709gE72NYZ\r\n0ROB023467RD52821IE64NYZ\r\n9ROD998582RV52508fE62NYZ\r\n0LIT006165LA52816jE64NYZ\r\n0SCH026003SR52829IE67NYZ\r\n0BOY024076BM12830IE60NYZ\r\n0ROD027957RR12420IE69NYZ\r\n0ABN037839AJ52730gE65NYZ\r\n0YEL043924YM12620IE67NYZ\r\n0POS005401PA12516eE73NYZ\r\n9URU998719UY52608fE64NYZ\r\n0PHE003927PA52629fE61NYZ\r\n9WAL998954WT52624iE65NYZ\r\n0SOT003768SR52628fE59NYZ\r\n0HIL023952HS52421fE66NYZ\r\n9FER981547FS12521bE69NYZ\r\n0AYU032718AG52704fE62NYZ\r\n0SER026241SM52701gE69NYZ\r\n0GRI029207GX12822hE77NYZ\r\n0HER021094HM52326fE59NYZ\r\n0MAR002620MH12811IE72NYZ\r\n0GBI007321GJ52826jE64NYZ\r\n0YOU014189YM12714fE66NYZ\r\n".split('\r\n'))
ans = final_regex(string_of_list)
print(ans, end="")

