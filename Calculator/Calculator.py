def calculator():
    list_operators = ["*", '/', '+', '-']
    for operator in list_operators:
        print(operator)


def calculation(number, operator):
    secondnumber = int(input("enter the second number"))

    if operator == '*':
        result = number * secondnumber
        print(f"{number} * {secondnumber} is equal to ", result)
    if operator == '/':
        result = number / secondnumber
        print(f"{number} / {secondnumber} is equal to ", result)
    if operator == '+':
        result = number + secondnumber
        print(f"{number} + {secondnumber} is equal to ", result)
    if operator == '-':
        result = number - secondnumber
        print(f"{number} - {secondnumber} is equal to ", result)
    continue_asker = str(input("press y if you want to apply more calculation on the result or press n to start new"))
    if continue_asker == 'y':

        calculation(result, input("enter the operator"))
    else:
        starters()


def starters():
    numbers1 = int(input("enter first number"))

    calculator()
    select_operator = str(input("select the operator "))
    calculation(numbers1, select_operator)

print("""
 .------------------------------------------,
| .---------------------------------------, |
| | _~_                                   | |
| |  \/  HM Developers         T I - 8 6  | |
| | .-----------------------------------, | |
| | |                                   | | |
| | | 1 + 1                             | | |
| | |                                   | | |
| | |                                2  | | |
| | |                                   | | |
| | | 6 * 8                             | | |
| | |                               14  | | |
| | |                                   | | |
| | | _                                 | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | |                                   | | |
| | `-----------------------------------' | |
| |                                       | |
| `---------------------------------------' |
|     M1      M2      M3      M4      M5    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  F1 | |  F2 | |  F3 | |  F4 | |  F5 |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|-------.________          ________,--------|
|                `--------'                 |
|                                           |
|          QUIT    MODE        _,-._        |
|  .-----, .-----, .-----,  /\ \_^_/ /\     |
|  | 2nd | | EXIT| | MORE| / /   |   \ \    |
|  `-----' `-----' `-----' |<|   O   |>|    |
|  alpha   LINK x  INS     \ \  _|_  / /    |
|  .-----, .-----, .-----,  \/ / v \ \/     |
|  |ALPHA| |x-VAR| | DEL |     -._,-        |
|  `-----' `-----' `-----'                  |
|  SOLVER  SIMULT  POLY   CATLG-VARS        |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |GRAPH| |TABLE| | PRGM| |CUSTM| |CLEAR|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  10x  A  SIN-1 B COS-1 C TAN-1 D pi   E   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LOG | | SIN | | COS | | TAN | |  ^  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ex   F  x-1  G  [    H  ]    I  CALC J   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | LN  | | EE  | |  (  | |  )  | |     |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  ./~  K  MATRX L VECTR M CPLX N  MATH O   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | X2  | |  7  | |  8  | |  9  | |  x  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  /_   P  CONS Q  CONV R  STRNG S LIST T   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  |  ,  | |  4  | |  5  | |  6  | |  -  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  RCL  =  BASE U  TEST V  MEM  W  STAT X   |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | STO>| |  1  | |  2  | |  3  | |  +  |  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  OFF     CHAR Y  :    z  ANS  _  ENTRY    |
|  .-----, .-----, .-----, .-----, .-----,  |
|  | ON  | |  0  | |  .  | | (-) | |ENTER|  |
|  `-----' `-----' `-----' `-----' `-----'  |
|  -------                                  |
`\                                         /'
  `-._                                 _.-'
      `--.__                     __.--'
            ``----.._____,,---
""")
starters()
