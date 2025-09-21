
def Highest_Frequency_Calculator(SampleArray):
    

    Highest = 1 
    FirstTripleCounter = 1 
    MostCommonNum = 0 
    output = {"HighestFrequency":0, "MostCommonNum":0}

    for index in range(0,5):
        if SampleArray[index] == SampleArray[index + 1]:
            FirstTripleCounter = FirstTripleCounter + 1
            if  FirstTripleCounter > Highest:
                Highest = FirstTripleCounter
                MostCommonNum = SampleArray[index]
        else: 
            if  FirstTripleCounter > Highest:
                Highest = FirstTripleCounter
                MostCommonNum = SampleArray[index]
            FirstTripleCounter = 1

    output["HighestFrequency"] = Highest
    output["MostCommonNum"] = MostCommonNum
    
    return output 


def No_Points_Flag_Calculator(SampleArray,HighestFrequency):

    NoPointsFlag = True 
    Fuffa = (2,3,4,6)

    #checks if there are any 1s or 5s 
    for i in range(6):
        if SampleArray[i] not in Fuffa: 
            NoPointsFlag = False     

    #checks if there are any triples or quads etc etc 
    if HighestFrequency >= 3:
        NoPointsFlag = False   
    
    return NoPointsFlag


def Scala_Checker(HighestFrequency):
    ScalaCheck = False 

    if HighestFrequency == 1:
        ScalaCheck = True
    
    return ScalaCheck




def ReRollChecker(SampleArray,HighestFrequency,MostCommonNum,ScalaCheck):

    ReRollCheck = False 

    if ScalaCheck == True:
        ReRollCheck = True 

    #removes the triples/quads from the array, so that 1 and 5s can be looked at 

    elif HighestFrequency >= 3: 
        Counter = 0 
        for i in range(len(SampleArray)):
            if SampleArray[i] == MostCommonNum: 
                while HighestFrequency > Counter:
                    SampleArray.pop(i)
                    Counter = Counter + 1 
            break 

        #checks the case where there are two sets of triples     
        if len(SampleArray) == 3:
            if ( SampleArray[0] == SampleArray[1] ) and ( SampleArray[1] == SampleArray[2] ):
                ReRollCheck = True 

        #removes remaining 1s or 5s from the array 
        EmptyCheck = True

        for i in range (len(SampleArray)):
            if SampleArray[i] == 1 or SampleArray[i] == 5:
                SampleArray[i] = 0 

        for i in range(len(SampleArray)):
            if SampleArray[i] != 0:
                EmptyCheck = False
                break 
        
        if EmptyCheck == True:
            ReRollCheck = True


    return ReRollCheck
        
def Max_Point_Calculator(SampleArray,HighestFrequency,MostCommonNum,NoPointsCheck,ScalaCheck):
    MaxPoints = 0 
    
    if NoPointsCheck == True:
        MaxPoints = 0

    elif ScalaCheck == True:
        MaxPoints = 2500 

    elif HighestFrequency >= 3: 
        Counter = 1
        for i in range(len(SampleArray)):
            if SampleArray[i] == MostCommonNum:     

                #checks the case of a list of 1s 
                if SampleArray[i] == 1:                   
                    MaxPoints = 1000
                    while (HighestFrequency - 3) >= Counter:
                        MaxPoints = MaxPoints**2
                        SampleArray.pop(i)
                        Counter = Counter + 1

                #checks the case of a list of 5s
                elif SampleArray[i] == 5:
                    MaxPoints = 500
                    while HighestFrequency > Counter:
                        MaxPoints = 500
                        MaxPoints = MaxPoints**2
                        SampleArray.pop(i)
                        Counter = Counter + 1

                #checks the case of a list of 2s,3s,4s or 6s 
                else:
                    MaxPoints = MostCommonNum * 100
                    while HighestFrequency > Counter:
                        MaxPoints = MaxPoints * 2 
                        SampleArray.pop(i)
                        Counter = Counter + 1 
            break 

    #adds the points from the remaining 1s and 5s 
    for i in range(len(SampleArray)):
        if SampleArray[i] == 1:
            MaxPoints = MaxPoints + 100
        elif SampleArray[i] == 5:
            MaxPoints = MaxPoints + 50

    return MaxPoints




SampleArray = [2,2,2,4,4,5]
HighestFrequency = 5
MostCommonNum = 2
ScalaCheck = False



def main():
    TestingFHand = open("testing.txt","w")
    Counter = 1


    TestingFHand.write("Counter" + "\t\t" + "i"    + "\t"  + "j"   + "\t" + "k"     + "\t" + "l"    + "\t" + "m"    + "\t" + "n"    + "\t\t"  + "NoPointsFlag" + "\t" + "Highest" + "\t" + "ScalaCheck" + "\t" + "MostCommonNum" + "\t" "ReRollCheck" + "\n\n")

    for i in range(1,7): 
        for j in range(1,7):
            for k in range(1,7):
                for l in range(1,7):
                    for m in range(1,7):
                        for n in range(1,7): 

                            #highest calculator
                            TempArray = [i,j,k,l,m,n]
                            TempArray = sorted(TempArray)


                            DictFrequency = Highest_Frequency_Calculator(TempArray)
                            HighestFrequency = DictFrequency["HighestFrequency"]

                            MostCommonNum = DictFrequency["MostCommonNum"]
                            
                            #No points checker  
                            NoPointsCheck = No_Points_Flag_Calculator(TempArray,HighestFrequency)

                            #Scala checker 
                            ScalaCheck = Scala_Checker(HighestFrequency)

                            #ReRoll Check
                            ReRollCheck = ReRollChecker(TempArray,HighestFrequency,MostCommonNum,ScalaCheck)
                            
                    
                            TestingFHand.write(str(Counter) + "\t\t\t" + str(i) + "\t" + str(j) + "\t" + str(k)  + "\t" + str(l) + "\t" + str(m) + "\t" + str(n) + "\t \t" + str(NoPointsCheck) + "\t\t\t" + str(HighestFrequency) + "\t\t" + str(ScalaCheck) + "\t\t" + str(MostCommonNum) + "\t" + str(ReRollCheck) + "\n")
                            Counter = Counter + 1

main()




#go through and filter out all the commbinations that roll a new hand and then you can calculate a mean value for points from one roll, 
#then go back and add this mean value to the number of points created from that roll e.g 666444 would be 1000 + mean found earlier 


# test = [1,1,1,1,1,5]


# MostCommonNum = 1
# HighestFrequency = 5 
# Counter = 0

# for i in range(6):
#     if test[i] == MostCommonNum:
#         test.pop(i)
#         counter = counter + 1 
#         i = i -1 
#         if counter >= HighestFrequency:
#             break 






# SampleArray = [1,1,5]

# EmptyCheck = True

# for i in range (len(SampleArray)):
#     if SampleArray[i] == 1 or SampleArray[i] == 5:
#         SampleArray[i] = 0 

# for i in range(len(SampleArray)):
#     if SampleArray[i] != 0:
#         EmptyCheck = False
#         break 

# print(EmptyCheck)

# if EmptyCheck == True:
#     ReRoll = True 


for i in range(0):
    print("hello world")