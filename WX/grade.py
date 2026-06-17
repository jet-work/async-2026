grade = int(input("Enter ="))

def evaluate_grade(score):

    if score < 0 or score > 100:
        print("กรุณากรอกใหม่")
    elif score >= 80:
        return  "Excellent"  
    elif 50 <= score < 80:
        return "pass" 
    elif 0 <= score < 50:
        return "fail"     
