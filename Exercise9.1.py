def sum(f1,f2):
    result = {}
    result["s"] = (f1["s"] * f2["m"]) + (f2["s"]  * f1["m"])
    result["m"] = f1["m"] * f2 ["m"]
    return result

def multiply(f1,f2):
        result = {}
        result["s"] = f1["s"] * f2["s"]
        result["m"] = f1["m"] * f2["m"]
        return result
def subtract(f1,f2):
        result = {}
        result["s"] = (f1["s"] * f2["m"]) - (f2["s"]  * f1["m"])
        result["m"] = f1["m"] * f2 ["m"]
        return result
def divide(f1,f2):
      result = {}
      result["s"] = f1["s"] * f2["m"]
      result["s"] = f1["m"] * f2["s"]
      return result


def show(r):
    print(f"{r['s']} / {r['m']}")
s1 = float(input("Enter the number: "))
s2 = float(input("Enter the number: "))
m1 = float(input("Enter the number: "))
m2 = float(input("Enter the number: "))

f1 = {"s": s1, "m": m1}
f2 = {"s": s2, "m": m2}
  
result_s = sum(f1,f2)
show(result_s)

result_m = multiply(f1,f2)
show(result_m)

result_sub = subtract(f1,f2)
show(result_sub)

result_d = divide(f1,f2)
show(result_d)