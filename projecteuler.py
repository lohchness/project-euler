import math
from re import L

from numpy import true_divide

def problem1():
    total = 0
    for x in range(1000):
        if x%3 == 0 or x%5 == 0:
            total += x
    return total

def problem2():
    x, y = 1, 2
    total = 0
    limit = 4000000
    while x <= limit:
        x, y = y, x+y
        if x%2==0:
            total += x
    return total



def problem3():
    num = 600851475143
    for x in range(1, num, 2):
        if num%x == 0:
            if isprime(num/x):
                return num/x

def isPalindrome(i):
    return i == i[::-1]

def problem4():
    largest = 0
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            if isPalindrome(str(x*y)):
                if x*y > largest:
                    largest = x*y
    return largest

def twentyfactors(n):
    for possible_factor in range(2, 20):
        if n%possible_factor != 0:
            return False
    return True

def problem5():
    num = 20
    while True:
        if twentyfactors(num):
            return num
        num += 20
        
def sumsquare(limit):
    total = 0
    for i in range(limit+1):
        total += (i**2)
    return total

def squaresum(limit):
    total = 0
    for x in range(limit+1):
        total += x
    return total**2

def problem6():
    return sumsquare(100)-squaresum(100)

def problem7():  
    count = 0
    target = 10001
    current_prime = 0
    for number in range(2, 1000000000000000):
        if count == target:
            return current_prime
        if isprime(number):
            current_prime = number
            count += 1

digits = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n","")

def problem8():
    largest13 = 0
    left_index = 0
    for x in range(987):
        total = 1
        numbers = []
        for index in range(left_index, left_index+13):
            numbers.append(digits[index])
        for number in numbers:
            total *= int(number)
        if total > largest13:
            largest13 = total
        left_index += 1
    return largest13

def problem9():
    for a in range(1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a**2+b**2==c**2:
                    if a+b+c==1000:
                        return a, b, c, a*b*c

def problem10():
    total = 0
    for i in range(2, 2000000):
        if isprime(i):
            total += i
    return total

rows = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48""".split("\n")

table = [[int(i) for i in row.split(" ")] for row in rows]

def problem11():
    adjacent_nums = 4
    greatest = 0

    # LEFT & RIGHT
    for row in table:
        index = 0
        for shift in range(16):
            index += 1
            product = row[index]*row[index+1]*row[index+2]*row[index+3]
            if product > greatest:
                greatest = product
    # UP & DOWN
    for row in range(len(table)):
        if row >= 3: # guarantee it will start at row index 3 (4th row)
            for col in range(len(table)):
                product = table[row-3][col] * table[row-2][col] * table[row-1][col] * table[row][col]
                if product > greatest:
                    greatest = product
    # DIAGONAL TO BOTTOM RIGHT
    for row in range(16):
        for column in range(16):
            product = table[row][column]*table[row+1][column+1]*table[row+2][column+2]*table[row+3][column+3]
            if product > greatest:
                greatest = product
    # DIAGONAL TO BOTTOM LEFT
    for row in range(adjacent_nums-1, len(table)):
        for col in range(len(table)-adjacent_nums+1):
            num = table[row][col] * table[row-1][col+1] * table[row-2][col+2] * table[row-3][col+3]
            if num > greatest:
                greatest = num

    return greatest

def factor_counter(num):
    total_factors = 0
    for possible_factor in range(1, math.floor((math.sqrt(num)+1))):
        if num % possible_factor == 0:
            if possible_factor == int(math.sqrt(num)):
                total_factors += 1
            else:
                total_factors += 2
    return total_factors
    
def problem12():
    tri_num = 0
    count = 1
    while True:
        tri_num += count
        if factor_counter(tri_num) > 500:
            return tri_num
        count += 1

numbers = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690""".split("\n")

def problem13():
    return str(sum([int(i) for i in numbers]))[:10]

def collatz_counter(num):
    total = 1
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = 3*num + 1
        total += 1
    return total

def problem14():
    greatest = 0
    greatest_number = 0
    for x in range(1, 1000000):
        num = collatz_counter(x)
        if num > greatest:
            greatest = num
            greatest_number = x
    return greatest_number

from itertools import permutations, combinations

def problem15():
    length = 20
    down_move = "d"
    right_move = "r"
    movelist = [down_move for x in range(int(length))]+[right_move for x in range(int(length))]

    # perms = permutations(movelist, length*2)
    # permlist = set()
    # for perm in perms:
    #     permlist.add(perm)

    # return len(permlist)

    return math.factorial(40)/(math.factorial(20)*math.factorial(20))


def problem16():
    num = 256**125
    return sum([int(i) for i in str(num)])

# print(problem16())

def problem17():
    # DICTIONARIES
    ones = {"0":0, "1": 3, "2":3, "3":5, "4": 4, "5": 4, "6":3, "7":5, "8":5, "9":4}
    tens = {"0":0, "2":6, "3":6, "4":5, "5":5, "6":5, "7":7, "8":6, "9":6}
    # key is the value of the ones digits
    second_digit_one = {"0":3, "1": 6, "2":6, "3":8, "4": 8, "5": 7, "6":7, "7":9, "8":8, "9":8}

    total = 0
    for num in range(1, 1001):
        if num == 1000:
            total += 11
        else:
            if num > 99: # 3 digit numbers
                if num % 100 == 0: # exact multiples of 100 (do not include "and")
                    total += ones[str(num)[-3]]
                    total += 7 # hundred
                else: # not multiples of 100
                    total += ones[str(num)[-3]]
                    total += 7 # hundred
                    total += 3 # and
                    if (num//10)%10 != 1:
                        total += tens[str(num)[-2]]
                        total += ones[str(num)[-1]]
                    else:
                        total += second_digit_one[str(num)[-1]]
            else: # 1/2 digit numbers
                # numbers without 1 as second digit
                if num > 9:
                    if (num//10)%10 != 1:
                        total += tens[str(num)[-2]]
                        total += ones[str(num)[-1]]
                    # numbers with 1 as second digit
                    else:
                        total += second_digit_one[str(num)[-1]]
                else:
                    total += ones[str(num)[-1]]
            
    return total
    
    zero_to_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    # dont forget to add 3 for "and" 
    hundred = 7
    and_word = 3
    thousand = 8
    
    if num < 100:
        if num < 20:
            # Num exactly in [0,19]
            total += zero_to_19[num%100]
        else:
            # Num exactly in [20,99]
            total += ones[str(num)[-1]]
            total += tens[str(num)[-2]]
    elif num < 1000:
        # Num from [100, 999]
        if num % 100 == 0:
            total += 0
    else:
        # Num from [1000, inf]
        pass


triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")

triangle_list = [row.split() for row in triangle]

def traverse(tree, height, row, index):
    curr_num = int(triangle_list[row][index])
    if row == height:
        return curr_num
    return curr_num + max(int(traverse(tree, height, row+1, index)), int(traverse(tree, height, row+1, index+1)))

def problem18():
    return traverse(triangle_list, 14, 0, 0)



def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def problem19():
    sundays = 0
    weekday = 2
    month_days_non_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_days_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    for year in range(1901, 2000+1):
        if leap_year(year):
            for month in range(0,12):
                weekday += month_days_leap[month]
                if weekday%7 == 0:
                    sundays += 1
        else:
            for month in range(0,12):
                weekday += month_days_non_leap[month]
                if weekday%7 == 0:
                    sundays += 1
    return sundays

# print(problem19())

def problem20():
    return sum([int(i) for i in (str(math.factorial(100)))])

def sum_of_factors(n):
    total = 0
    for possible_factor in range(1, int(n/2)+1):
        if n % possible_factor == 0:
            total += possible_factor
            # if 
    return total

# from collections import defaultdict

def amicable_pair(num1, num2):
    sum = 0
    for i in range(1, int(math.sqrt(num1)) + 1):
        if num1 % i == 0:
            sum += i
    if sum == num2:
        return True
    return False

    pass

def problem21_2():
    amicable_sum = 0
    amicable_pairs = dict()
    for num in range(1, 10000+1):
        if num not in amicable_pairs:
            factor_sum = sum_of_factors(num)
            if (factor_sum <= 10000) and (factor_sum != num):
                if sum_of_factors(factor_sum) == num:
                    amicable_sum += num
                    amicable_sum += factor_sum
                    amicable_pairs[num] = factor_sum
                    amicable_pairs[factor_sum] = num
    print(amicable_sum)
    print(amicable_pairs)

def amicable_num(num):
    total = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            total += i
    return total

def problem21_1():
    total = 0
    for num in range(1, 10000+1):
        pair = amicable_num(num)
        if num != pair:
            if amicable_num(pair) == num:
                total += num

    return total


    total = 0
    iterated = []
    for i in range(1,10000+1):
        if i not in iterated:
            for j in range(1, 10000+1):
                if j not in iterated:
                    if amicable_pair(i, j):
                        total += i + j
                        iterated.append(i)
                        iterated.append(j)

    return total
    
    
    
# print(problem211())

def problem22():
    with open("p022_names.txt", "r") as names:
        name_list = str(names.read()).replace('"','').split(",")
    sortedlist = sorted(name_list)
    score = 0
    for name_indx in range(len(sortedlist)):
        name_score = 0
        for letter in sortedlist[name_indx]:
            name_score += (ord(letter)-64)
        score += (name_score*(name_indx+1))
    return score

# print(problem22())

def is_abundant(num):
    if sum_of_factors(num) > num:
        return True
    return False

def problem23():
    abundant_sum = 0
    abundant_numbers = []
    for number in range(12, 28123):
        if is_abundant(number):
            abundant_numbers.append(number)
    # print(abundant_numbers)

    # init list of 28123 zeros
    bools = [0] * (28123-1)

    # iterate through bools, if num pair is an abundant sum, set bool[num_index] to 1
    
    # iterate through bools, if value is 0 we add it to running total
    # return total

    for number in range(1, 28123):
        for abundant_idx in range(len(abundant_numbers)):
            if number-abundant_numbers[abundant_idx] in abundant_numbers:
                break
        abundant_sum += number
            
    return abundant_sum

    # for num1 in range(len(abundant_numbers)):
    #     for num2 in range(len(abundant_numbers)):
    #         if num1 > num2:


# print(problem23())

from itertools import permutations, islice

def problem24():
    digits = [0,1,2,3,4,5,6,7,8,9]
    # digits = [0,1,2]
    
    perms = permutations(digits,len(digits))
    # perms = permutations(digits, 3)
    # print([i for i in perms])
    # return next(islice(perms, 3, None), None)

    return next(islice(perms, 1000000-1, None), None)
    return next(num for ind,num in enumerate(perms) if ind==1000000-1)

# print(problem24())

def nth_fibonacci(n):
    fib_1, fib_2 = 1, 1
    for x in range(n-1):
        fib_1, fib_2 = fib_2, fib_1+fib_2
    return fib_1

def problem25():
    index = 1
    while True:
        if len(str(nth_fibonacci(index))) >= 1000:
            return index
        index += 1
        # return index if len(str(nth_fibonacci(index))) >= 1000 else index += 1

# print(problem25())

from decimal import Decimal

def exact_fraction(n): # n is the denominator in the unit fraction 
    if len(str(1/n)) < 18:
        return True
    return False

def recurring_cycle(n): # n is the denominator in the unit fraction
    if not exact_fraction(n):
        float_number = (Decimal(1)/Decimal(n))
        length = 1
        while True:
            first = int(str(float_number).split('.')[1][0:length])
            second = int(str((float_number)*(Decimal(10**length))).split('.')[1][0:length])
            if first == second:
                third = int(str((float_number)*(Decimal(10**(length*2)))).split('.')[1][0:length])
                if second == third:
                    fourth = int(str((float_number)*(Decimal(10**(length*3)))).split('.')[1][0:length])
                    if third == fourth:
                        fifth = int(str((float_number)*(Decimal(10**(length*4)))).split('.')[1][0:length])
                        if fourth == fifth:
                            return length
            print(f"Length isn't {length}")
            length += 1
            continue
    return 0

def problem26():
    return

# print(recurring_cycle(7))

def isprime(n):
    for possible_factor in range(2, int(math.sqrt(n))+1):
        if n % possible_factor == 0:
            return False
    return True

def problem27():
    maximum_consecutive = 0
    for a in range(-999, 999+1):
        for b in range(-1000, 1000+1):
            if b >= 2:
                if isprime(b): # only need to check quadratics where b is prime
                    count = 0
                    n = 0
                    while True:
                        quadratic = (n**2)+(a*n)+b
                        if quadratic >= 2: # primes have to be greater or equal to 2
                            if isprime(quadratic):
                                count += 1
                                n += 1
                            else:
                                break
                        else:
                            break
                    if count > maximum_consecutive:
                        largest_a = a
                        largest_b = b
                        maximum_consecutive = count
                        product = a*b
    return largest_a, largest_b, maximum_consecutive, product

def problem28_1():
    total = 0
    square_size = 1
    current_number = 1
    while square_size <= 1001:
        if square_size == 1:
            total += 1
        else:
            for corner in range(4):
                current_number += (square_size-1)
                total += current_number
        square_size += 2
    return total

def problem28_2():
    jump = 1
    count = 0
    total = 1
    for i in range(2, 1000+1, 2):
        for j in range(4):
            jump += i
            total += jump
    return total


def problem29():
    terms = set()
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            num = a**b
            if num not in terms:
                terms.add(num)
    return len(terms)

def problem30():
    sum = 0
    for num in range(2, 10000+1):
        pass

print(problem30())