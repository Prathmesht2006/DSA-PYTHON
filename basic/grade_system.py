# Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.



class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print("Grade A")
            return
        if marks>=70:
            print("Grade B")
            return
        if marks>=50:
            print("Grade C")
            return
        if marks>=35:
            print("Grade D")
            return
        else:
            print("Fail")