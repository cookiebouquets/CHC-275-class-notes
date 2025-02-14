def getMean(userList):
    """
    Function Name: getMean
    Parameters: List
    Return Type: Float
    Description: Calculates the mean for the list and returns the value 
    """
    return sum(userList)/len(userList)


def getMedian(userList):
    tempUserList = []
    tempUserList = userList
    tempUserList.sort()
    if len(tempUserList)%2 == 1:
        median = tempUserList[(len(tempUserList)//2)]
    elif len(tempUserList)%2 == 0:
        num1 = tempUserList[len(tempUserList)//2]
        num2 = tempUserList[(len(tempUserList)//2)-1]
        sum = num1 + num2
        median = sum/2
    return median


def getMin(userList):
    min = userList[0]
    for i in range(1,len(userList)):
        if min > userList[i]:
            min = userList[i]
    return min

def getMax(userList):
    max = userList[0]
    for i in range(1,len(userList)):
        if max < userList[i]:
               max = userList[i]
    return max

