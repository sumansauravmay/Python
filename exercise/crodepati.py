# create a program capable of displaying questions to the user like KBC
# use list data type to store the questions and their correct answers.
# Display the finla amount the person is taking home after playing the game



questions=[
    ["Whcih language is used most", "Python", "JS", "Java", "PHP", "None", 4],
    ["Whcih language is used most", "Python", "JS", "Java", "PHP", "None", 4],
    ["Whcih language is used most", "Python", "JS", "Java", "PHP", "None", 4],
    ["Whcih language is used most", "Python", "JS", "Java", "PHP", "None", 4],
    ["Whcih language is used most", "Python", "JS", "Java", "PHP", "None", 4]
           ];

levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]


for i in range(0, len(questions)):
    question=questions[i];
    print(f"Question for Rs. {levels[i]}");
    # print(question);
    print(f"{question[0]}");
    print(f"a. {question[1]}   b. {question[2]}   c. {question[3]}  d.{question[4]}");
    reply=int(input("enter your answer (1-4)"));
if(reply==question[-1]):
    print(f"Correct answer, You won Rs. {levels[i]}");
if(i==4):
        money=10000;
elif(i==9):
        money=320000;
elif(i==14):
        money=1000000;
else:
    print("Wrong Answer!")
    


