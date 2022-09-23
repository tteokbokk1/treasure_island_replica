#A simple text based adventure game

print('''                      _
                           ,--.\`-. __
                         _,.`. \:/,"  `-._
                     ,-*" _,.-;-*`-.+"*._ )
                    ( ,."* ,-" / `.  \.  `.
                   ,"   ,;"  ,"\../\  \:   |
                  (   ,"/   / \.,' :   ))  /
                   \  |/   / \.,'  /  // ,'
                    \_)\ ,' \.,'  (  / )/
                        `  \._,'   `"
                           \../
                           \../
                 ~        ~\../           ~~
          ~~          ~~   \../   ~~   ~      ~~
     ~~    ~   ~~  __...---\../-...__ ~~~     ~~
       ~~~~  ~_,--'        \../      `--.__ ~~    ~~
   ~~~  __,--'              `"             `--.__   ~~~
~~  ,--'                                         `--.
   '------......______             ______......------` ~~
 ~~~   ~    ~~      ~ `````---"""""  ~~   ~     ~~
        ~~~~    ~~  ~~~~       ~~~~~~  ~ ~~   ~~ ~~~  ~
     ~~   ~   ~~~     ~~~ ~         ~~       ~~   SSt
              ~        ~~       ~~~       ~
''')

print("Welcome to Treausure Island!")

start_game = input("Would you like to play? Yes or No?\n")

if start_game.lower() == "no":
    print("Goodbye.")
    exit()
else:
    print("Your mission is to find treasure.")

first_prompt = "You're standing in a forest. Which way would you like to go?"
print(first_prompt)
first_move = input("Left, Right, or Forward?\n")

invalid_input = "That's not an allowed move. Game Over."

#if player slects any move other than forward then game over.
if first_move.lower() == "left":
    print("You've stepped on a land mine and blown up. You're dead.")
    print("Game Over")
elif first_move.lower() == "right":
    print("You've encountered a venomous snake.")
    snake_attack = input("What do you do?\nGo around the snake, Grab a stick and push it away, or step on it?\n")
    if snake_attack.lower() == "go around the snake":
        print("You've fallen into quicksand and are sinking. The snake slithers towards you and bites you. You're dead.")
        print("Game Over")
    elif snake_attack.lower() == "grab a stick and push it away":
        print("You are now past the snake and are facing a fork in the road.")
        fallen_tree = input("Which direction do you go? Left or Right?\n")
        if fallen_tree.lower() == "left":
            print("You've fallen into a pit. You're dead.")
            print("Game Over")
        else:
            print("A gust of wind picks up and the tree next to you falls on top of you. You're dead.")
            print("Game Over")
    else:
        print("The snake is now angry and bites you. You're dead.")
        print("Game Over")
elif first_move.lower() == "forward":
    print("You walk through the forest.")
else:
    print(invalid_input)
    exit()

second_prompt = "You stumble onto a lake with an island in the middle. What do you do?"
second_move = input("Swim across the lake or wait and think?\n")

#if player waits they will notice a raft
#if player uses raft they pass the lake
if second_move.lower() == "swim across the lake":
    print("A trout swims towards you and attacks you. You're dead.")
    print("Game Over")
    exit()
elif second_move.lower() == "wait and think":
    print("You notice a raft to the left.")
    use_raft = input("Do you use the raft? Yes or No?\n")
    if use_raft.lower() == "yes":
        print("You get on the raft and safely cross the lake to the other side.")
    else:
        print("You die of hunger while waiting. You're dead.")
        print("Game Over")
        exit()
else:
    print(invalid_input)
    exit()

third_prompt = "You get off the raft and encounter a red door, a yellow door, and a blue door."
print(third_prompt)
third_move = input("Which door do you open? Red, Yellow, or Blue?\n")

#if player selects red door they win
if third_move.lower() == "red":
    print("You open the red door and walk through it. You enter into an airport lobby with a ticket home.")
    print("Congratulations. You've escaped the island.")
    print("You win!")
    exit()
elif third_move.lower() == "yellow":
    print("You open the yellow door and walk through it. You fall into a blazing inferno. You're dead.")
    print("Game Over")
    exit()
elif third_move.lower() == "blue":
    print("You open the blue door and walk through it. You get mauled by wolves. You're dead.")
    print("Game Over")
    exit()
else:
    print(invalid_input)
    exit()