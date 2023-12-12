import re # python regex module

total = 0
digitString = "one|two|three|four|five|six|seven|eight|nine"

f = open('./1/input.txt', 'r')
lines = f.readlines()

# dummy = open('./1/dummyInput.txt', 'r')
# lines = dummy.readlines()

def getCalibrationValueFromLineV1(textInput) -> str:
    tempText = ''
    first = re.search('\d',textInput)
    last = re.search('\d',textInput[::-1])

    if not first and not last:
        return('')
    
    elif first and not last:
        return(format(first.group()) * 2)
    
    elif not first and last:
        return(format(last.group()) * 2)
    
    elif first and last:
        if first == last:
            return(format(first.group()) * 2)
        else:
            return(format(first.group()) + format(last.group()))
        

def convertStrToIntIfPossible(textInput) -> int:
    strDigits = digitString.split('|')
    if strDigits.count(textInput) > 0:
        return(strDigits.index(textInput) + 1)
    else:
        return(int(textInput))
        
def getCalibrationValueFromLineV2(textInput) -> str:
    tempText = ''

    firstDig = re.search('\d',textInput)
    firstStr = re.search(digitString,textInput)

    lastDig = re.search('\d',textInput[::-1])
    lastStr = re.search(digitString[::-1],textInput[::-1])

    if not firstDig and not lastDig and not firstStr and not lastStr:
        return('')

    if firstDig and firstStr:
        if firstDig.span()[0] < firstStr.span()[0]:
            first = firstDig.group()
        else:
            first = firstStr.group()
    elif firstDig and not firstStr:
        first = firstDig.group()
    elif not firstDig and firstStr:
        first = firstStr.group()
    else:
        first = ''

    if lastDig and lastStr:
        if lastDig.span()[0] < lastStr.span()[0]:
            last = lastDig.group()
        else:
            last = lastStr.group()
    elif lastDig and not lastStr:
        last = lastDig.group()
    elif not lastDig and lastStr:
        last = lastStr.group()
    else:
        last = ''
    
    startNo = convertStrToIntIfPossible(first)
    endNo = convertStrToIntIfPossible(last[::-1])

    if first == '' and last == '':
        return('')
    
    elif first != '' and last == '':
        return(format(startNo) * 2)
    
    elif first == '' and last != '':
        return(format(endNo) * 2)
    
    elif first != '' and last != '':
        if first == last:
            return(format(startNo) * 2)
        else:
            return(format(startNo) + format(endNo))
            
for line in lines:
    text = line.strip()
    total += int(getCalibrationValueFromLineV2(text))
    # print(getCalibrationValueFromLineV2(text))

print(total)

# x = getCalibrationValueFromLineV2('one1two2blabla3three4')
# print(x)