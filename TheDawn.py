import random
import string
import turtle
import time


def unlock_vault(clues):#TheDawn
    check = 1
    print("hello:) this is your last challenge\nnow go to exit")
    TheDawn = ["T", "H", "E", "D", "A", "W", "N"]
    for i in range(7):
        if TheDawn[i] in clues:
            print(TheDawn[i])
        else:
            check = 0
    return (check)


def calculate_magic_numbers(start, end):
    dawn = int(time.time())
    for i in range(7):
        dawn = (dawn * 1351045125 + 12345) & 0x7fffffff
        random_number = dawn % (max(start, end) - min(start, end) + 1) + min(start, end)
        print(random_number)


def lataraji():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("TheDawn")   #la
    Dawn = turtle.Turtle()
    Dawn.color("black")
    Dawn.forward(300)
    Dawn.left(90)
    Dawn.forward(200)
    Dawn.right(90)
    Dawn.color("white")
    Dawn.pensize(3)
    Dawn.left(270)
    Dawn.forward(260)
    Dawn.right(90)
    Dawn.forward(90)
    Dawn.right(90)
    Dawn.forward(260)
    Dawn.left(90)
    Dawn.color("black")
    Dawn.forward(50)
    Dawn.left(90)
    Dawn.forward(160)
    #tar
    Dawn.color("white")
    Dawn.forward(2)
    Dawn.right(90)
    Dawn.forward(40)
    Dawn.color("black")
    Dawn.left(90)
    Dawn.forward(20)
    Dawn.left(90)
    Dawn.forward(20)
    Dawn.color("white")
    for i in range(2):
        Dawn.right(90)
        Dawn.forward(85)
    Dawn.left(45)
    Dawn.forward(130)
    Dawn.color("black")
    Dawn.left(225)
    Dawn.forward(130)
    Dawn.left(90)
    Dawn.forward(90)
    #ji
    Dawn.color("white")
    Dawn.left(220)
    Dawn.forward(90)
    Dawn.right(90)
    Dawn.forward(110)
    Dawn.right(128)
    Dawn.forward(180)
    Dawn.color("white")
    Dawn.left(90)
    Dawn.forward(80)
    Dawn.left(90)
    Dawn.forward(80)
    Dawn.right(90)
    Dawn.forward(80)
    Dawn.right(90)
    Dawn.forward(200)
    Dawn.right(90)
    Dawn.forward(105)
    Dawn.color("black")
    Dawn.right(90)
    Dawn.forward(225)
    Dawn.color("white")
    Dawn.pensize(15)
    Dawn.forward(4)
    Dawn.right(90)
    Dawn.forward(1)
    Dawn.right(90)
    Dawn.forward(4)
    wn.mainloop()


def check_pass():
    standard_passwords = []
    usernames = [
        "wili324", "mohammad_sprint",
        "sina.1386", "amirhossein333",
        "paria.butterfly1", "hadi_fanny", "mohaddeseh$$$",
        "davoodsprint2", "gameofthrones123", "moonlight1384"]
    passwords = [
        "Alireza#123", "sprint666", "Sina138202$", "123456789",
        "mamax99655", "Fannybazi$$1", "hadis",
        "ali", "johnsnow11", "Bmwz123#$"]
    for i in range(10):
        if len(passwords[i]) >= 8:
            if passwords[i].upper() != passwords[i].lower():
                if any(c in string.punctuation for c in passwords[i]):
                    standard_passwords.append(usernames[i])
    print(standard_passwords)
    return (standard_passwords)


def exam_numbers():
    correct = 0
    incorrect = 0
    binary_numbers = []
    int_binary = []
    for i in range(7):
        numbers = 0
        for j in range(4):
            numbers = numbers * 10 + (random.randint(0, 1))
        binary_numbers.append(numbers)
    binary_numbers = list(map(str, binary_numbers))
    for i in range(7):
        inteager = 0
        number = int(binary_numbers[i])
        for j in range(4):
            remain = number % 10
            number = number // 10
            if remain == 1:
                inteager = inteager + (2 ** j)
        int_binary.append(inteager)

    for k in range(7):
        gusses = int(input(f"please enter int {binary_numbers[k]}: "))
        if gusses == (int_binary[k]):
            print('correct')
            correct = correct + 1
        else:
            print("incorrect")
            incorrect = incorrect + 1
    print(f"correct = {correct}\nincorrect = {incorrect}")
    if correct > incorrect:
        return 1
    else:
        return 0


def slove_puzzles(puzzles):
    list_bool = []
    for i in range(48):
        list_bool.append(bool(puzzles[i]))
    print(list_bool)
    return list_bool


def decrypt_clue(text):
    allKeyWords = []
    key_words = [
        'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif',
        'else', 'except', 'False', 'finally', 'for', 'from', 'global',
        'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'True', 'try',
        'while', 'with', 'yield']
    for i in range(31):
        if key_words[i] in text:
            allKeyWords.append(key_words[i])
    print(allKeyWords)
    return (allKeyWords)


The_Python_Way = """
    ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbr
    eakclasscontinueexceptfinallyforfromglobalimportnonlocalpassrai
    sereturntrywhilewithandorasassertbreakclasscontinuedefdelelifel
    seexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorp
    assprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasync
    awaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatil
    eabstractenumintfloatdoublebyteboolcharstructvectorlistdictiona
    ryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsex
    tendspublicprotectedprivatefinalstaticvoidmainStringargsSystemo
    utprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContai
    nsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinu
    eiteratoriterablecollectionsframeworksynchronizedtransientvolat
    ilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencege
    nericswildcardstypeerasurereflectionproxydecoratorfactorysingle
    tonprototypebuildercompositeadapterbridgechainofresponsibilityc
    ommandstateobservermementointerpreteriteratorvisitorstrategytem
    platemethodflyweightmediatorproxymultithreadingconcurrencyasync
    hronousprogrammingeventdrivenarchitecturefunctionalprogrammingi
    mmutables...
quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsSho
rsGroverquantumcryptographyquantumteleportationartificialintelligen
ceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepth
firstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulat
edannealingparticlewarmoptimizationantcolonyoptimizationmachinelear
ningdeeplearningunsupervisedlearningreinforcementlearningneuralnetw
orksconvolutionalneuralnetworksrecurrentneuralnetworkslongshortterm
memorynetworksgenerativeadversar...

blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWork
proofOfStakeByzantineFaultTolerancepeer-to-peerP2Pnetworkscryptogra
phyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigit
alcertificatesdigital signaturesmartcontractsdecentralizedapplicati
onsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNF
Tsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesD
EXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypools
oraclesDAOsdecentralizedautonomousorganizati..."""

puzzles = ["ali", 1233, 0, "", [], {}, 'False', '0',
           'None', None, -1, [1, 2, 3], {'key': 'value'},
           True, ' ', '[]', '[1, 2, 3]', '{}', {'a': 1},
           'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ',
           '[]', '[1, 2, 3]', '{}', {'a': 1}, 'True',
           'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]',
           '[1, 2, 3]', '{}', {'a': 1}, 'True', 'ali',
           '1234', 1, 0.1, -0.1]
clues = []
python = []
magic1 = decrypt_clue(The_Python_Way)
time.sleep(3)
clues1 = [word.capitalize()[0] for word in magic1]
magic2 = slove_puzzles(puzzles)
time.sleep(3)
number1 = int(input("please enter num1"))
number2 = int(input("please enter num2"))
calculate_magic_numbers(number1, number2)
time.sleep(3)
p = exam_numbers()
time.sleep(3)
clues2 = magic2
magic3 = check_pass()
time.sleep(3)
clues3 = [word.capitalize()[0] for word in magic3]
lataraji()
clues = clues1 + clues2 + clues3
time.sleep(3)
check = unlock_vault(clues)
if p == 1 & check == 1:
    print("you win")
else:
    print("you lose")