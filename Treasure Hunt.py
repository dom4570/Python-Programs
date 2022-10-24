print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" : ').lower()
if direction == "left":
    print("""\
                                     8a .
                               `.  _
    ___________  s,    _____     /_/   ____________________a:f____
               .Jktbc._       _ ./
              xft#kTJ:   _.  (_)/)  -._
             cf8#6C. ,  (   ( ,-'      )
           ` `"P:'.     '-._\_\___.---'

        """)
    print("You fall into a pit! Game Over")


elif direction == "right":
    print("""\
                            %%%%
                    %%%%-(
                  _%%%%%_/                        \ ' /
                _%%%%%%%%                        - (_) -
              _%%%%%%%/ \%                        / , \
             %%%%%%%%%\\ \_
               %%%%%%   \ \\
                   )    /\_/
                 /(___. \
                 '----' (
                /       )lef
    ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
              /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
            ,'          (         ```--.._= -_= -_= _-=- -_= _=-
         ,-'            )                 ``--._=-_ =-=_-= _-= _
         '-._    '-..___(                       ``-._=_-=_- =_-=
             ``---....__)                            `-._-=_-_=-
                   )|)|                                  `-._=-_
        gnv       '-'-.\_                                    `-.
        """)
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if lake == "swim":
        print("""\
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
            """)
        print("You were attacked by crocodile! Game Over.")

    elif lake == "wait":
        print("""\
                               ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \,
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^
             """)


        color = input('You got into a boat, You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        print("""\
             ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+-+-| | |
| | |_|_|_|_| | |
| |     ___   | |
| |    /__/   | |
| |   [%==] ()| |
| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|
            """)
        if color == "red":
            print("""\
                
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
            print("It's a room full of fire. Game Over.")

        elif color == "yellow":
            print("""\
                               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
                """)
            print("You found the treasure! You Win!")

        elif color == "blue":
            print("""\
                                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                """)
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("invalid command please restart to play new game")
else:
    print("invalid command please restart to play new game")



