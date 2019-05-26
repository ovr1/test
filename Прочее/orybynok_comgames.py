from random import randrange

m_number = randrange(1,5)
not_bingo = True
miss_try = 1


while (not_bingo) and (miss_try <= 5):
    number = randrange(1,5)
    print(m_number,number)
    if (number == m_number):
        print("Miss_try = ", miss_try, "Win!   ")
        not_bingo = True
        break
    else:
        miss_try += 1
        print("Continue!  ")
else:
    print('Unfortunaly game not finish. Try next time!')