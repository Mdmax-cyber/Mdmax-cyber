
#.................................................................................................................
#x = input("type a number:")
#o = float(x)
#x = input("type sec number:")
#x2 = float(x)
#answer = o + x2
#round_answer = round(answer,3)
#answer = f"youre answer is here = {round_answer}"
#print(answer)
#..................................................................................................
#x = input('type a number:')
#o = float(x)
#x = input('type youre sec number:')
#o2 = float(x)
#z = input(f'chose one of them (//,%,*,/,-,+):')
#if z == '+':
#    answer = o + o2
#elif z == '-':
#    answer = o - o2
#elif z == '*':
#    answer = o * o2
#elif z == '/':
#    answer = o / o2
#elif z == '%':
#    answer = o % o2
#elif z == '//':
#    answer = o // o2
#final_answer = round(answer,4)
#print(f"youre answer is here {final_answer} ")
#..........................................................................................................
import random

q = random.randint(1,6)
chance = int(input('roll a dice (make a shot):'))
if chance == q:
    print('you win!')
elif chance > q:
    print('you lose!')
elif chance < q:
      print('you lose!')
