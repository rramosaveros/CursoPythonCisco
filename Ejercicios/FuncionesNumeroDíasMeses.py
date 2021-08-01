def isYearLeap(year):
    if year % 4 ==0:
        return True
    else:
        return False
#
# tu código del laboratorio anterior
#

def daysInMonth(year, month):
    mesesAñoBisiesto = [31,29,31,30,31,30,31,31,30,31,30,31]
    mesesAñoNormal = [31,28,31,30,31,30,31,31,30,31,30,31]
    isLeap = isYearLeap(year)
    if isLeap: 
        return mesesAñoBisiesto[month -1]
    else: 
        return mesesAñoNormal[month - 1]
    
#
# coloca tu código aqui
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")