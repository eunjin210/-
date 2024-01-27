import sys
cr_sum = 0
sc_sum = 0
dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    sub, credit, score = sys.stdin.readline().split()
    if score =='P':
        continue
    else:
        cr_sum += float(credit)
        sc_sum +=dic[score]*float(credit)
print(sc_sum/cr_sum)