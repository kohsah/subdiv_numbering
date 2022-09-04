import string
import itertools


def iterate_alpha():
    from string import ascii_lowercase
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)

def english_numbering_v1():
    alphabets = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'I',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'
    ]
    numbers_upto = 100
    all_nums = []
    for num in range(1, numbers_upto + 1):
        current_num = ""
        continuation = num/26
        if (continuation > 1 ):
            alpha_offset = num % 26
            current_num = alphabets[int(continuation) - 1] + alphabets[alpha_offset - 1]
        else:
            current_num = alphabets[num - 1]
        all_nums.append([num, current_num])
    return { 
        "numbering": "Engish",
        "data": all_nums
    }


def english_numbering():
    return {
        "numbering": "English",
        "data": [ [v+1, k]  for v,k in enumerate(itertools.islice(iterate_alpha(), 100)) ]
    }

def french_numbering_type2():
    fr_alphas_1_to_26 = [
        'bis',
        'ter',
        'quater',
        'quinquies',
        'sexies',
        'septies',
        'octies',
        'nonies',
        'decies',
        'undecies',
        'duodecies',
        'terdecies',
        'quaterdecies',
        'quindecies',
        'sexdecies',
        'septdecies',
        'octodecies',
        'novodecies',
        'vicies',
        'unvicies',
        'duovicies',
        'tervicies',
        'quatervicies',
        'quinvicies',
        'sexvicies',
        'septvicies'
    ]
    numbers_upto = 100
    all_nums = []
    for num in range(1, numbers_upto + 1):
        current_num = ""
        continuation = num/26
        if (continuation > 1 ):
            alpha_offset = num % 26
            current_num = fr_alphas_1_to_26[int(continuation) - 1] + " " + fr_alphas_1_to_26[alpha_offset - 1]
        else:
            current_num = fr_alphas_1_to_26[num - 1]
        all_nums.append([num, current_num])
    return { 
        "numbering": "French",
        "data": all_nums
    }


def portoguese_numbering():
    pt_prefix = '.º-'
    pt_alpha_1_to_26 = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'
    ]
    numbers_upto = 100
    all_nums = []
    for num in range(1, numbers_upto + 1):
        current_num = ""
        continuation = num/26
        if (continuation > 1 ):
            alpha_offset = num % 26
            current_num = pt_prefix + pt_alpha_1_to_26[int(continuation) - 1] + pt_alpha_1_to_26[alpha_offset - 1]
        else:
            current_num = pt_prefix + pt_alpha_1_to_26[num - 1]
        all_nums.append([num, current_num])
    return { 
        "numbering": "Portoguese",
        "data": all_nums
    }


def render_numbering(nums):
    from tabulate import tabulate
    col_names = ["index", "number"]
    print("Numbering in ", nums["numbering"])
    print(tabulate(nums["data"], headers=col_names, tablefmt="grid"))

render_numbering(english_numbering_v1())
render_numbering(french_numbering_type2())
render_numbering(portoguese_numbering())

#english_numbering_v1()


