def sum(t1, t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    if result["s"] >= 60:
        result["s"]-= 60
        result["m"]+= 1
    
    if result["m"] >= 60:
        result["m"]-= 60
        result["h"]+= 1
    return result

def subtraction(d1,d2):
    result = {}
    result["h"] = d2["h"] - d1["h"]
    result["m"] = d2["m"] - d1["m"]
    result["s"] = d2["s"] - d1["s"]
    if result["s"] < 0:
       result["m"] -= 1
       result["h"] += 60

    if result["m"] < 0:
       result["h"] -=1
       result["s"] +=60

    if result["h"] < 0:
        print("Error")

    return result


def show(result):
    print(f"{result['h']} : {result['m']} : {result['s']}")

d1 = {"h": int(input("time1: ")), "m": int(input("time1: ")) , "s": int(input("time1: "))}
d2 = {"h": int(input("time2: ")) , "m": int(input("time2: ")) , "s": int(input("time2: "))}
result_s = sum(d1, d2)
show(result_s)
result_m = subtraction(d1,d2)
show(subtraction)