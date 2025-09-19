import os
path = os.path.dirname(__file__)
inputFileName = path + "/coeficienti.in"
outputFileName = path + "/coeficienti.out"

def getInput():
    with open(inputFileName, "r") as f:
        x = int(f.readline().strip())
        coefficients = [int(value) for value in f.readline().split()]
    
    return x, coefficients

def setCoefficents(coefficients, x):
    polynomial = {power: None for power in range(len(coefficients))}

    if x >= 0:
        coefficients = sorted(coefficients)
        polynomial = {power: coefficients for power, coefficients in enumerate(coefficients)}
        computedPolynomial = [x ** power * polynomial[power] for power in polynomial]
        maxSum = sum(computedPolynomial)
        return maxSum, polynomial

    if x < 0:
        # Pentru [1, -2, -3, -7, -5] si x < 0
        # Pasul I:
        # De la cea mai mare la cea mai mica putere impara, asociem cele mai mici valori negative 
        # (ex: <-7 pentru puterea 3>, <-5 pentru puterea 1>)
        # 
        # Pasul II:
        # De la cea mai mica la cea mai mare putere oarecare, asociem cele mai mici valori ramase   
        # (ex:  <-3 pentru puterea 0>, <-2 pentru puterea 2>, <1 pentru puterea 4>)

        coefficients = sorted(coefficients, reverse = True)
        polynomial = {power: None for power in range(len(coefficients))}
        
        for power in range(len(coefficients) - 1, -1, -1):
            if power % 2 != 0 and polynomial[power] is None and coefficients[-1] < 0:
                polynomial[power] = coefficients[-1]
                coefficients.pop()

        for power in polynomial:
             if polynomial[power] is None:
                 polynomial[power] = coefficients[-1]
                 coefficients.pop()
  
        computedPolynomial = [x ** power * polynomial[power] for power in polynomial]
        maxSum = sum(computedPolynomial)
        return maxSum, polynomial

    return

def writeOutput(polynomial, grade, x, maxSum):
    with open(outputFileName, "w") as g:
        for power in range(grade - 1, 0, -1):
            g.write("({}) * (({}) ** {}) + \n".format(polynomial[power], x, power))
        g.write("({}) * (({}) ** {}) = {}".format(polynomial[0], x, 0, maxSum))

    return

def main():
    x, coefficients = getInput()
    maxSum, polynomial = setCoefficents(coefficients, x)
    writeOutput(polynomial, len(coefficients), x, maxSum)
    return

if __name__ == "__main__":
    main()
    exit()