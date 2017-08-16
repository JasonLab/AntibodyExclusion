# AntibodyExclusion
Given a database of Antibody Panels it can provide cells that are adequate given the parameters provided by the user.

Guide to adding your own Screening Cells.

The easy way is just entering your data into the TMQ dictionnaries already there. I recommend this method. 

Step 1

Creating a dictionnary with your cell. Name it something like the Panel then cell number like VRA257_1
Fill it as shown in the other dicts so {'Antigen':'expression'} If it is Positive expression is '+', else expression is '0'

Step 2

You're going to take the following code and basically replace the TMQ_1 with your dictionnary name from above. You can use microsoft word and the
Replace All function on there to make it quick and errorless. Then you're going to paste it with all the other code that looks like this while
making sure it is tabbed the same. 

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

Now you're going to go back to the code you pasted and change all the instances it says TMQ Cell 1 to whatever cell you called it. Then you're going
to rename Cell 1 to something to do with your cell name. So if your cell name was VRA257_1 just do like VRA257Cell_1. Then you're going to copy paste
VRA257Cell_1 = 1 up near the top with all the other Cell = 0. Remember to change the value of your cell to 0. so VRA257Cell_1 = 0.

Step 3

Delete all the cells that don't matter to you, so this includes their code, their dict and the cell1=0 counter for that specific cell. 
If you really want to keep them then just comment them out with
--->    """ code """
