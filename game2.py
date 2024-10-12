print(''' _,.
    ,` -.)
   ( _/-\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /   _______ ________  _     _   ____
 __,-<_     )`-/  `./  /   / ___  / \  ___ /  \|   |/  / __ \
'  \   `---'   \   /  /    ``  / /   ||   `   ||   || | <__``
    |           |./  /       _/ /   < |==|    ||   ||  \__ `\
    /           //  /       / /`     ||       ||   ||     `\ |
\_/' \         |/  /       / /___,,  ||___,   \ \_/ / |\___/ /
 |    |   _,^-'/  /       /_______/ /______\   \___/  \_____/
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
       ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you wanna go? Type "left" or "right". ').lower()

if choice1 == "left":
    print('''
                          Now I am ready for that dragon!
                      I have a horse and armour!
             ,      ,  /
        ____/~\    ~O
    ,;~( )_  )'' /~()'-{---
       )/  |(     /~)
       ~    ~     ~ ~
    ''')
    print("You found a Horse! You named it Roach. Check his saddlebag!")
    print("Inside the saddlebag you found an old green Sword and a Shield made of iron")
    choice2 = input(
        "You've come to a cave. The cave is dark and you can't see well. Will you ENTER? type \"yes\" or 'no'. ").lower()
    if choice2 == 'no':
        print('''               
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
jgs \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_''')
        print("You thought its better to wait for the sunrise so you took a rest by the trees")
        print('''          |
     \     |     /
       \       /
         ,d8b,           .,
 (')-")_ 88888 ---   ;';'  ';'.
('-  (. ')98P'      ';.,;    ,;
 '-.(PjP)'     \       '.';.' 
           |     \
           |''')
        print("The sun rised and you decied to enter the cave with Roach")
        print("Inside the cave, you encouter a sleeping red dragon guarding a chest of treasure!")
        choice3 = input("Will you fight it? run away? or look for a hidden path around the dragon?").lower()
        print("CHOOSE:\nA for fight\nB for run\nC for hidden path")
        if choice3 == "a":
            print('''
                                                                      _   __,----'~~~~~~~~~`-----.__
                                   .  .    `//====-              ____,-'~`
                   -.            \_|// .   /||\\  `~~~~`---.___./
             ______-==.       _-~o  `\/    |||  \\           _,'`
       __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
    _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
  .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
 / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
          '         `-|      /|    )-'\~'      _,--"'
                      '-~^\_/ |    |   `\_   ,^             /\
                           /  \     \__   \/~               `\__
                       _,-' _/'\ ,-'~____-'`-/                 ``===\
                      ((->/'    \|||' `.     `\.  ,                _||
        ./                       \_     `\      `~---|__i__i__\--~'_/
       <_n_                     __-^-_    `)  \-.______________,-~'
        `B'\)                  ///,-'~`__--^-  |-------~~~~^'
        /^>                           ///,--~`-\\
       `  `

         ''')
            print("You tried to fight it but your sword broke! The dragon Killed you and Roach ran away. GAME OVER")
        elif choice3 == "c":
            print('''
                                       _.--.
                        _.-'_:-'|| 
                    _.-'_.-::::'|| 
               _.-:'_.-::::::'  || 
             .'`-.-:::::::'     || 
            /.'`;|:::::::'      ||_ 
           ||   ||::::::'     _.;._'-._ 
           ||   ||:::::'  _.-!oo @.!-._'-. 
           \'.  ||:::::.-!()oo @!()@.-'_.| 
            '.'-;|:.-'.&$@.& ()$%-'o.'\U|| 
              `>'-.!@%()@'@_%-'_.-o _.|'|| 
               ||-._'-.@.-'_.-' _.-o  |'|| 
               ||=[ '-._.-\U/.-'    o |'|| 
               || '-.]=|| |'|      o  |'|| 
               ||      || |'|        _| '; 
               ||      || |'|    _.-'_.-' 
               |'-._   || |'|_.-'_.-' 
            jgs '-._'-.|| |' `_.-' 
                    '-.||_/.-'

       ''')

            print("The dragon was asleep and he didn't notice you! You stole the treasure!!!")
        else:
            print('''
                     /^\                   /^\
        /     \     )   (     /     \
      /         \ )\(-+-)/( /         \
    /            )-/ 0:0 \-(            \
  /         ____ )--\~-~/--( ____        \
 (/)  +*****\/\/****(o:o)****\/\/****+  (\)
  / /)*              \-/             *(\ \
 (/   *                              *   \)
      *             GAME OVER        *
      *                              *
      *                              *
      +******************************+''')
            print("You ran away without the treasure. GAME OVER.")


    else:
        print('''        _  _
  ___ (~ )( ~)
 /   \_\ \/ /
|   D_ ]\ \/
|   D _]/\ \
 \___/ / /\ \
      (_ )( _)''')
        print("You tripped on a skull and died. GAME OVER.")
        print("TIP: wait for SUNRISE.")


else:
    print('''    
               ____ __
          { --.\\  |          .)%%%)%%
           '-._\\ | (\\___   %)%%(%%(%%%
               `\\|{/ ^ _)-%(%%%%)%%;%%%
           .'^^^^^^^  /`    %%)%%%%)%%%'
  jgs     //\\   ) ,  /       '%%%%(%%'
    ,  _.'/  `\\<-- \\
     `^^^`     ^^   ^^

''')
    print("You encounter a dragon and he killed you. GAME OVER.")
    print("TIP: don't be alone!")


