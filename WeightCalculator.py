weight = float(input("Weight: "))

kgOrL = input("Kg:(K) Pound (L): ")

factor = 1

if (kgOrL.upper() == "K"):
    factor = 0.45
    print("Weight: " + str(weight / float(factor)) + " Lb")