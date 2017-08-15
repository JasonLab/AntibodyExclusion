"""
User can add their own panel cells here which is pretty straightforward. The code should not have issues as long as
any added cells also include  "": "" and "Always0":'0' which prevent errors. Then they would have to copy the code for
each cell and sub in their cell name. As well as add their own cell counter such as Cell1,Cell2.etc

Adding entire antigens to the panel is a little more difficult. They just need to be sure to add it to the
Antigen_Dict if it has a counterpart antigen while inputting all that correctly. Adding it to the Antigen_List would be
a good idea, but isn't necessary for the program to function.

"""
TMQ_1 = {'D': '+', 'C': '+', 'c': '0', 'E': '0', 'e': '+', 'f': '0', 'V': '0', 'Cw': '+', 'K': '0', 'k': '+',
         'Fya': '0', 'Fyb': '+', 'Jka': '+', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '0', 'M': '0', 'N': '+',
         'S': '0', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '0', "": "","Always0":'0'}
TMQ_2 = {'D': '+', 'C': '+', 'c': '0', 'E': '0', 'e': '+', 'f': '0', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '0', 'Fyb': '+', 'Jka': '0', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '+', 'N': '0',
         'S': '+', 's': '0', 'Lua': '0', 'Lub': '+', 'Xg': '+', "": "","Always0":"0"}
TMQ_3 = {'D': '+', 'C': '0', 'c': '+', 'E': '+', 'e': '0', 'f': '0', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '+', 'Fyb': '+', 'Jka': '+', 'Jkb': '0', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '0', 'N': '+',
         'S': '0', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '+', "": "","Always0":"0"}
TMQ_4 = {'D': '0', 'C': '0', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '+', 'k': '+',
         'Fya': '+', 'Fyb': '+', 'Jka': '+', 'Jkb': '0', "Lea": '+', 'Leb': '0', 'P1': '0', 'M': '+', 'N': '+',
         'S': '+', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '0', "": "","Always0":"0"}
TMQ_5 = {'D': '+', 'C': '0', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '0', 'Fyb': '0', 'Jka': '+', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '0', 'N': '+',
         'S': '0', 's': '0', 'Lua': '0', 'Lub': '+', 'Xg': '0', "": "","Always0":"0"}
TMQ_6 = {'D': '0', 'C': '0', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '0', 'Fyb': '0', 'Jka': '+', 'Jkb': '0', "Lea": '+', 'Leb': '0', 'P1': '0', 'M': '0', 'N': '+',
         'S': '0', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '0', "": "","Always0":"0"}
TMQ_7 = {'D': '0', 'C': '0', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '+', 'Fyb': '0', 'Jka': '+', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '+', 'N': '0',
         'S': '+', 's': '+', 'Lua': '+', 'Lub': '+', 'Xg': '0', "": "","Always0":"0"}
TMQ_8 = {'D': '0', 'C': '0', 'c': '+', 'E': '+', 'e': '+', 'f': '+', 'V': '+', 'Cw': '0', 'K': '0', 'k': '+',
         'Fya': '0', 'Fyb': '+', 'Jka': '0', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '+', 'N': '0',
         'S': '+', 's': '0', 'Lua': '0', 'Lub': '+', 'Xg': '0', "": "","Always0":"0"}
TMQ_9 = {'D': '0', 'C': '0', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '+', 'k': '0',
         'Fya': '+', 'Fyb': '0', 'Jka': '0', 'Jkb': '+', "Lea": '0', 'Leb': '+', 'P1': '0', 'M': '+', 'N': '+',
         'S': '0', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '+', "": "","Always0":"0"}
TMQ_10 = {'D': '0', 'C': '+', 'c': '+', 'E': '0', 'e': '+', 'f': '+', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
          'Fya': '+', 'Fyb': '+', 'Jka': '+', 'Jkb': '0', "Lea": '0', 'Leb': '0', 'P1': '0', 'M': '0', 'N': '+',
          'S': '0', 's': '+', 'Lua': '0', 'Lub': '+', 'Xg': '+', "": "","Always0":'0'}
TMQ_11 = {'D': '+', 'C': '+', 'c': '0', 'E': '0', 'e': '+', 'f': '0', 'V': '0', 'Cw': '0', 'K': '0', 'k': '+',
          'Fya': '0', 'Fyb': '0', 'Jka': '+', 'Jkb': '0', "Lea": '0', 'Leb': '+', 'P1': '+', 'M': '+', 'N': '0',
          'S': '+', 's': '+', 'Lua': '0', 'Lub': '0', 'Xg': '+', "": "","Always0":"0"}
Antigen_List = ['D', 'C', 'c', 'E', 'e', 'f', 'V', 'Cw', 'K', 'k', 'Fya', 'Fyb', 'Jka', 'Jkb', 'Lea', 'Leb', 'P1', 'M',
                'N', 'S', 's', 'Lua', 'Lub', 'Xg']
Antigen_Dict = { 'C': 'c', 'c': 'C', 'E': 'e', 'e': 'E',  'K': 'k', 'k': 'K',
          'Fya': 'Fyb', 'Fyb': 'Fya', 'Jka': 'Jkb', 'Jkb': 'Jka', "Lea": 'Leb', 'Leb': 'Lea',  'M': 'N', 'N': 'M',
          'S': 's', 's': 'S', 'Lua': 'Lub', 'Lub': 'Lua',}
print("Hello. Welcome to the Antibody ExclusionBot!")
print("Antibodies from the following list are supported. Please enter exactly as listed and without the ' '.")
print(Antigen_List)
FirstAntigen = input("Enter the antibody you need to exclude from the list above: ")
HetorHomozygous = input("Does the antibody need to be homozygous? Enter Y or N")
HetorHomozygous = HetorHomozygous.lower()
FirstUndesire = input("Enter the first  suspect antibody you wish to not be present. If none press enter:")
SecondUndesire = input("Enter the second  suspect antibody you wish to not be present. If none press enter:")
ThirdUndesire = input("Enter the third suspect antibody you wish to not be present. If none press enter:")

Cell1= 0
Cell2= 0
Cell3= 0
Cell4= 0
Cell5= 0
Cell6= 0
Cell7= 0
Cell8= 0
Cell9= 0
Cell10= 0
Cell11= 0
NoCell= 0
FirstAntigenPartner = ''

# The next bit of code deals with the antibody partners...
if FirstAntigen in Antigen_Dict:
    FirstAntigenPartner = Antigen_Dict.get(FirstAntigen)
else:
    FirstAntigenPartner = 'Always0'

for x in Antigen_List:
    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_1[x] == '+' and TMQ_1[FirstAntigenPartner] == '0' and TMQ_1[FirstUndesire] != '+' and TMQ_1[SecondUndesire] != '+' and TMQ_1[ThirdUndesire] != "+":
            print("TMQ Cell 1 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_1[x] == '+' and TMQ_1[FirstAntigenPartner] == '+' and TMQ_1[FirstUndesire] != '+' and TMQ_1[SecondUndesire] != '+' and TMQ_1[ThirdUndesire] != "+":
            print("TMQ Cell 1 is acceptable heterozygously")
            Cell1 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_1[x] == '+' and TMQ_1[FirstUndesire] != '+' and TMQ_1[SecondUndesire] != '+' and TMQ_1[ThirdUndesire] != "+" and Cell1 == 0:
            print("TMQ Cell 1 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_2[x] == '+' and TMQ_2[FirstAntigenPartner] == '0' and TMQ_2[FirstUndesire] != '+' and TMQ_2[
            SecondUndesire] != '+' and TMQ_2[ThirdUndesire] != "+":
            print("TMQ Cell 2 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_2[x] == '+' and TMQ_2[FirstAntigenPartner] == '+' and TMQ_2[FirstUndesire] != '+' and TMQ_2[
            SecondUndesire] != '+' and TMQ_2[ThirdUndesire] != "+":
            print("TMQ Cell 2 is acceptable heterozygously")
            Cell2 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_2[x] == '+' and TMQ_2[FirstUndesire] != '+' and TMQ_2[SecondUndesire] != '+' and TMQ_2[
            ThirdUndesire] != "+" and Cell2 == 0:
            print("TMQ Cell 2 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_3[x] == '+' and TMQ_3[FirstAntigenPartner] == '0' and TMQ_3[FirstUndesire] != '+' and TMQ_3[
            SecondUndesire] != '+' and TMQ_3[ThirdUndesire] != "+":
            print("TMQ Cell 3 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_3[x] == '+' and TMQ_3[FirstAntigenPartner] == '+' and TMQ_3[FirstUndesire] != '+' and TMQ_3[
            SecondUndesire] != '+' and TMQ_3[ThirdUndesire] != "+":
            print("TMQ Cell 3 is acceptable heterozygously")
            Cell3 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_3[x] == '+' and TMQ_3[FirstUndesire] != '+' and TMQ_3[SecondUndesire] != '+' and TMQ_3[
            ThirdUndesire] != "+" and Cell3 == 0:
            print("TMQ Cell 3 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_4[x] == '+' and TMQ_4[FirstAntigenPartner] == '0' and TMQ_4[FirstUndesire] != '+' and TMQ_4[
            SecondUndesire] != '+' and TMQ_4[ThirdUndesire] != "+":
            print("TMQ Cell 4 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_4[x] == '+' and TMQ_4[FirstAntigenPartner] == '+' and TMQ_4[FirstUndesire] != '+' and TMQ_4[
            SecondUndesire] != '+' and TMQ_4[ThirdUndesire] != "+":
            print("TMQ Cell 4 is acceptable heterozygously")
            Cell4 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_4[x] == '+' and TMQ_4[FirstUndesire] != '+' and TMQ_4[SecondUndesire] != '+' and TMQ_4[
            ThirdUndesire] != "+" and Cell4 == 0:
            print("TMQ Cell 4 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_5[x] == '+' and TMQ_5[FirstAntigenPartner] == '0' and TMQ_5[FirstUndesire] != '+' and TMQ_5[
            SecondUndesire] != '+' and TMQ_5[ThirdUndesire] != "+":
            print("TMQ Cell 5 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_5[x] == '+' and TMQ_5[FirstAntigenPartner] == '+' and TMQ_5[FirstUndesire] != '+' and TMQ_5[
            SecondUndesire] != '+' and TMQ_5[ThirdUndesire] != "+":
            print("TMQ Cell 5 is acceptable heterozygously")
            Cell5 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_5[x] == '+' and TMQ_5[FirstUndesire] != '+' and TMQ_5[SecondUndesire] != '+' and TMQ_5[
            ThirdUndesire] != "+" and Cell5 == 0:
            print("TMQ Cell 5 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_6[x] == '+' and TMQ_6[FirstAntigenPartner] == '0' and TMQ_6[FirstUndesire] != '+' and TMQ_6[
            SecondUndesire] != '+' and TMQ_6[ThirdUndesire] != "+":
            print("TMQ Cell 6 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_6[x] == '+' and TMQ_6[FirstAntigenPartner] == '+' and TMQ_6[FirstUndesire] != '+' and TMQ_6[
            SecondUndesire] != '+' and TMQ_6[ThirdUndesire] != "+":
            print("TMQ Cell 6 is acceptable heterozygously")
            Cell6 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_6[x] == '+' and TMQ_6[FirstUndesire] != '+' and TMQ_6[SecondUndesire] != '+' and TMQ_6[
            ThirdUndesire] != "+" and Cell6 == 0:
            print("TMQ Cell 6 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_7[x] == '+' and TMQ_7[FirstAntigenPartner] == '0' and TMQ_7[FirstUndesire] != '+' and TMQ_7[
            SecondUndesire] != '+' and TMQ_7[ThirdUndesire] != "+":
            print("TMQ Cell 7 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_7[x] == '+' and TMQ_7[FirstAntigenPartner] == '+' and TMQ_7[FirstUndesire] != '+' and TMQ_7[
            SecondUndesire] != '+' and TMQ_7[ThirdUndesire] != "+":
            print("TMQ Cell 7 is acceptable heterozygously")
            Cell7 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_7[x] == '+' and TMQ_7[FirstUndesire] != '+' and TMQ_7[SecondUndesire] != '+' and TMQ_7[
            ThirdUndesire] != "+" and Cell7 == 0:
            print("TMQ Cell 7 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_8[x] == '+' and TMQ_8[FirstAntigenPartner] == '0' and TMQ_8[FirstUndesire] != '+' and TMQ_8[
            SecondUndesire] != '+' and TMQ_8[ThirdUndesire] != "+":
            print("TMQ Cell 8 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_8[x] == '+' and TMQ_8[FirstAntigenPartner] == '+' and TMQ_8[FirstUndesire] != '+' and TMQ_8[
            SecondUndesire] != '+' and TMQ_8[ThirdUndesire] != "+":
            print("TMQ Cell 8 is acceptable heterozygously")
            Cell8 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_8[x] == '+' and TMQ_8[FirstUndesire] != '+' and TMQ_8[SecondUndesire] != '+' and TMQ_8[
            ThirdUndesire] != "+" and Cell8 == 0:
            print("TMQ Cell 8 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_9[x] == '+' and TMQ_9[FirstAntigenPartner] == '0' and TMQ_9[FirstUndesire] != '+' and TMQ_9[
            SecondUndesire] != '+' and TMQ_9[ThirdUndesire] != "+":
            print("TMQ Cell 9 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_9[x] == '+' and TMQ_9[FirstAntigenPartner] == '+' and TMQ_9[FirstUndesire] != '+' and TMQ_9[
            SecondUndesire] != '+' and TMQ_9[ThirdUndesire] != "+":
            print("TMQ Cell 9 is acceptable heterozygously")
            Cell9 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_9[x] == '+' and TMQ_9[FirstUndesire] != '+' and TMQ_9[SecondUndesire] != '+' and TMQ_9[
            ThirdUndesire] != "+" and Cell9 == 0:
            print("TMQ Cell 9 is acceptable")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_10[x] == '+' and TMQ_10[FirstAntigenPartner] == '0' and TMQ_10[FirstUndesire] != '+' and TMQ_10[SecondUndesire] != '+' and TMQ_10[ThirdUndesire] != "+":
            print("TMQ Cell 10 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_10[x] == '+' and TMQ_10[FirstAntigenPartner] == '+' and TMQ_10[FirstUndesire] != '+' and TMQ_10[SecondUndesire] != '+' and TMQ_10[ThirdUndesire] != "+":
            print("TMQ Cell 10 is acceptable heterozygously")
            Cell10 = 1
    if x == FirstAntigen and HetorHomozygous == 'n' and Cell10 != 1:
        if TMQ_10[x] == '+' and TMQ_10[FirstUndesire] != '+' and TMQ_10[SecondUndesire] != '+' and TMQ_10[ThirdUndesire] != "+" and Cell10 == 0:
            print("TMQ Cell 10 is acceptable ")

    if x == FirstAntigen and HetorHomozygous == 'y':
        if TMQ_11[x] == '+' and TMQ_11[FirstAntigenPartner] == '0' and TMQ_11[FirstUndesire] != '+' and TMQ_11[
            SecondUndesire] != '+' and TMQ_11[ThirdUndesire] != "+":
            print("TMQ Cell 11 is acceptable")
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_11[x] == '+' and TMQ_11[FirstAntigenPartner] == '+' and TMQ_11[FirstUndesire] != '+' and TMQ_11[
            SecondUndesire] != '+' and TMQ_11[ThirdUndesire] != "+":
            print("TMQ Cell 11 is acceptable heterozygously")
            Cell11 = 1
    if x == FirstAntigen and HetorHomozygous == 'n':
        if TMQ_11[x] == '+' and TMQ_11[FirstUndesire] != '+' and TMQ_11[SecondUndesire] != '+' and TMQ_11[
            ThirdUndesire] != "+" and Cell11 == 0:
            print("TMQ Cell 11 is acceptable")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("If there was is no above output indicating an acceptable cell then the available database does not contain cells that are adequate for the desired conditions")