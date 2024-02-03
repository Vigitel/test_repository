
username = input("Welcome to the noncredible quiz game!! What might your name be? ")
start_prompt_condition = True

while start_prompt_condition:
    start_consent = input(f"Are you ready to play {username}? ").lower()
    if start_consent == "yes":
        print("That's great! Lets get on with it then. Remember to put the letter of your answer!")
        start_prompt_condition = False
    elif start_consent == "no":
        print("Oh ok, if you don't want to play then thats entirely fine :D, we take consent seriously here, have a great day ahead <3")
        exit()
    else:
        print("Sorry, we didn't quite get your answer. Please check your spelling and we'll ask again.")

global player_score
player_score = 0


def questions(question, answer):
    player_input = input(question).lower()
    global player_score
    if player_input == answer:
        print("Correct!")
        player_score += 1
    else:
        print("Incorrect-")

questions('''Question 1! What year did spiderman first appear in the comics? 
          a.) 1949
          b.) 1738
          c.) 1962
          d.) 1976
          ''', "c")
questions('''Question 2! What is the most consumed beverage? 
          a.) Coffee
          b.) Tea
          c.) Coca-cola
          d.) Water
          ''', "d")
questions('''Question 3! Gusto pa bang mabuhay ni Lindsay?
          a.) Yes
          b.) Maybe
          c.) No
          d.) No!🥰
          ''', "d")
questions('''Question 4! What do you get, when you cross a mentally ill loner, with a society that abandons him and treats him like trash?
          a.) Tortang Kamatis
          b.) f(x) = x^2 + 5x + 25
          c.) I dunno
          d.) YOU GET WHAT YOU F@%!+G DESEVRE! *gunshot*
          ''', "d")
questions('''Question 5! What is my alter ego?
          a.) Juan Esperanza Protacio Halberto
          b.) Anita Max Wynn
          c.) Kween Yasmin
          d.) Albus Percival Wulfric Brian Dumbledore
          ''', "b")
questions('''Question 6! What was the first capital of Assyria?
          a.) Assur
          b.) Baghdad
          c.) Tokyo
          d.) Kabul
          ''', "a")
questions('''Question 7! One plus one?
          a.) 2
          b.) 11
          c.) Magellan
          d.) 21
          ''', "a")
questions('''Question 8! Dumilim ang paligid, may tumawag sa?
          a.) Nanay mo
          b.) Abusado
          c.) Pangalan ko
          d.) Pagkabago
          ''', "c")
questions('''Kwerpo lorp 9! Gleeby plorxy iv tlarko?
          a.) Huh?
          b.) Get away from me!
          c.) ...
          d.) Blart dooq Galavit!!
          ''', "d")
questions('''Question 10! What is the airspeed velocity of an unladen swallow?
          a.) What do you mean? An African or a European swallow?
          b.) What? How am I supposed to know that?
          c.) Unfair!
          d.) 69 kilometers per hour?
          ''', "a")

point_percentage = (player_score/10)*100
print("Thanks for answering this quiz! Here are your scores!")
print(f"You scored {player_score} out of 10 points! Thats {point_percentage}% of the whole test! Great Job!")


