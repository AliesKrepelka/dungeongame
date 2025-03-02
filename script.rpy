# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Dungeon Master")
define ancient_voice = Character("Ancient Voice")  # Corrected the name

# The game starts here.
screen main_menu():
    tag menu

    add "setting_bg.png"  # Background image (optional)

    vbox:
        align (0.5, 0.6)  # Adjust position if needed
        spacing 20

        textbutton "Start Game" action Start()
        textbutton "Settings" action ShowMenu("preferences")  # Opens Settings menu
        textbutton "Quit" action Quit()
        

   
    


label start:
    # Start with a black screen
    scene black
    with fade
    define dungeon_master = Character("Dungeon Master")

    "You step into the dungeon. The air is cold, and the sound of dripping water echoes in the darkness."

    # Play the door creak sound as the player enters
    play sound "door_creak.mp3"

    play music "audio/music.mp3"

    # Pause for dramatic effect
    pause 1.5

    # Fade into the dungeon scene
    scene bg class with fade

    "As your eyes adjust to the dim torchlight, a figure emerges from the shadows..."

    # Show the Dungeon Master character
    show sword with dissolve

    dungeon_master "Welcome, traveler. Few dare to enter my domain. What brings you here?"

    menu:
        "I seek power.":
            jump seek_power
        "I want to escape.":
            jump want_escape


### ***Route 1: Seeking Power***
label seek_power:
    dungeon_master "Power, you say? Power comes at a price. Are you willing to pay it?"

    menu:
        "I will do anything.":
            jump power_test
        "I will earn it through my own strength.":
            jump power_own_way

label power_test:
    dungeon_master "Very well. Step forward."

    scene ritual_chamber with fade

    "You follow the Dungeon Master to an ancient stone altar, glowing with eerie red symbols."

    dungeon_master "Kneel."

    "As you kneel, shadows rise from the ground, whispering in an unknown tongue."

    ancient_voice "To claim power, you must abandon your past. Speak your true name, and it shall be erased from time."

    menu:
        "Say your name.":
            jump lose_identity
        "Refuse.":
            jump betrayal

label lose_identity:
    "You utter your name, and a sharp pain pierces your mind. Memories fade like dust in the wind."
    
    "The Dungeon Master grins. You feel different—stronger, faster. But who are you now?"
    
    dungeon_master "Rise, my champion. You belong to the dungeon now."
    
    return

label betrayal:
    "You shake your head. 'I will not give up who I am.'"
    
    dungeon_master "Then you are of no use to me."
    
    show shadow_figure with dissolve
    
    "A shadowy figure appears behind you, a blade gleaming in the dim light."
    
    "Before you can react, darkness consumes you."
    
    return

label power_own_way:
    dungeon_master "Then prove your worth. Defeat my champion."

    show shadow_figure with dissolve
    
    "A warrior clad in black armor steps forward, sword drawn."
    
    menu:
        "Fight with all your strength.":
            jump fight_win
        "Try to reason with them.":
            jump fight_fail

label fight_win:
    "Steel clashes against steel. You dodge, counter, and finally strike the warrior down."
    
    dungeon_master "Impressive. You may yet be worthy. Follow me."
    
    return

label fight_fail:
    "You lower your weapon, trying to talk to the warrior."
    
    "The warrior hesitates... then strikes. Pain fills your vision as the world fades."
    
    return

### ***Route 2: Escaping the Dungeon***
label want_escape:
    dungeon_master "Escape? There is no escape. Only those who conquer the dungeon may leave."

    menu:
        "There must be another way.":
            jump escape_other_way
        "Then I will conquer it.":
            jump escape_fight

label escape_other_way:
    "You glance around, searching for an exit."

    scene hidden_passage with fade

    "A faint draft catches your attention. A hidden passage."

    "Do you risk taking it?"

    menu:
        "Enter the hidden passage.":
            jump passage_escape
        "Stay and fight.":
            jump escape_fight

label passage_escape:
    "You slip into the passage. The Dungeon Master’s voice echoes behind you."
    
    dungeon_master "Clever. But the dungeon does not forgive those who run."

    "The walls begin to shift. You run faster, heart pounding."

    menu:
        "Keep running.":
            jump final_escape
        "Turn back.":
            jump caught

label final_escape:
    "Light! You see an exit. You push forward and stumble into fresh air."
    
    "You've escaped... for now."
    
    return

label caught:
    "The passage closes behind you. Trapped."
    
    dungeon_master "Foolish. You should have fought."
    
    "Darkness consumes you."
    
    return

label escape_fight:
    dungeon_master "Very well. Face your fate!"

    show shadow_figure with dissolve

    "A dark warrior charges at you."

    menu:
        "Dodge and counter.":
            jump escape_win
        "Attack recklessly.":
            jump escape_fail

label escape_win:
    "You outmaneuver the warrior and strike a fatal blow."

    dungeon_master "Interesting... Perhaps you do have the strength to leave."

    "The Dungeon Master steps aside. A door creaks open."

    "Freedom is yours."

    return

label escape_fail:
    "You charge in blindly. A mistake."

    "The last thing you hear is the sound of your own heartbeat slowing."

    return
