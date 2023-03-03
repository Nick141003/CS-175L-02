#Nicholas Stevens
#CS 175L 02
#Calculate Average and Grade Fuctions

def main():
    test_score_one = int(input("Enter Test Score:"))
    test_score_two = int(input("Enter Test Score:"))
    test_score_three = int(input("Enter Test Score:"))
    test_score_four = int(input("Enter Test Score:"))
    test_score_five = int(input("Enter Test Score:"))

    def determine_grade(grades):
        if score >= 90 and score <= 100:
            print("A")
        elif score >=80 and score <= 89:
            print("B")
        elif score >=70 and score <= 79:
            print("C")
        elif score >=60 and score <= 69:
            print("D")
        else:
            print("F")
    average = (test_score_one + test_score_two + test_score_three +test_score_four + test_score_five / 5)
    print("Average Score: ", average)
main()
