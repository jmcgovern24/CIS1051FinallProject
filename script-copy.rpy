# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#character directory:
define batman = Character("Batman", color = "#FF0000")

define alfred = Character("Alfred", color = "#0000FF")

#JOKER CHARACTERS:
define joker = Character("Joker", color = "#800080")

define charlie = Character("Charlie Collins", color = "#808080")

define gordon = Character("Commisioner Gordon", color = "#0000FF")

define bullock = Character("Harvey Bullock", color = "#0000FF")

#CLAYFACE CHARACTERS:
define clayface = Character("Clayface", color = "#964B00")

define stella = Character("Stella Bates", color = "#964B00")

define scientist = Character("Scientist", color = "#0000FF")

define thomas = Character("Thomas Elliot", color = "#0000FF")

define gaurd = Character("Gaurd", color = "#0000FF")

define bruce = Character("Bruce Wayne", color = "#FF0000")

#TWO-FACE CHARACTERS:
define twoface = Character("Two-Face", color = "#FFFFFF")

define tim = Character("Tim Drake", color = "#FF0000")

define thug1 = Character("Thug1", color = "#FFFFFF")

define thug2 = Character("Thug2", color = "#FFFFFF")

define janet = Character("Janet Van Dorn", color = "#0000FF" )

define harley = Character("Harley Quinn", color = "#800080")

define ivy = Character("Poison Ivy", color = "#008000")

define scarecrow = Character("Scarecrow", color = "#FFA500")

define crock = Character("Killer Croc", color = "#808080")

define hatter = Character("Mad Hatter", color = "#008000")



#image batmobile = Movie(play="images/Clips", size=(1280, 720), loop = False, xaling = 0, yaling = 0)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene batcave
    "In the deep dark layer of the batman..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show batman neutral
    # These display lines of dialogue.

    batman "I am batman"

    "Alfred appears from the lit stairwell to the cave"

    show batman neutral at left

    show alfred at right
    
    alfred "Sir, there seems to be trouble brewing in Gotham." 
    alfred "Someone called in an anonymous tip from Falcone Plaza." 
    alfred "A silent alarm was tripped at Tarnower Financial." 
    alfred "There was a reported break in at the lower west side"

    batman "It will be a long night for me."

    alfred "Where will you go first?"
     
    menu:
        "Falcone plaza":
            jump Joker #jokers favor

        "Tarnower Financial":
            jump ClayFace #mudslide

        "Elliot apartment complex":
            jump TwoFace #Sins of the father/the trial

    label Joker: 
        alfred "Be caredul sir, you do not know what might be ahead of you."
        batman "I always am."
        jump joker_scene_1
      
    label ClayFace:
        alfred "Do not understimate the situation even if it may just be a simple robbery."
        batman "Don't worry I am prepared for everything."
        jump clayface_scene_1

    label TwoFace:
        batman "I'll investigate the break in"
        alfred "SOunds good sir"
        jump twoface_scene_1


label joker_scene_1: #The first scene where batman goes to the GCPD policemen's ball
    scene perched building
    "Batman arrives at Falcone plaza"
    alfred "\"Alfred in Batman's earpiece\" A tip was called in about suspicious activity at the Policemen's ball."
    batman "The policemen's ball! That would be ludicrous, the place would be swarming with armed GCPD officers. Who would ever want to cause chaos there?"
    alfred "\"Alfred in Batman's earpiece\" The tip said they spotted a woman with a Red and Black jester's Outfit."
    batman "\"Batman says to himself\" The Joker, what could he be planning."

    menu:
        "Wait to investigate":
            jump joker_Choice_1

        "Go down and investigate":
            jump joker_Choice_2

    label joker_Choice_1:
        batman "What could the Joker be planning hmmm..."
        menu:
            "Keep waiting":
                jump joker_Choice_3

            "Go down and investigate":
                jump joker_Choice_2

    label joker_Choice_3:
        batman "If only I could find a way to figure what he's doing"
        menu:
            "Keep waiting":
                jump joker_ending_1

            "Go down and investigate":
                jump joker_Choice_2

    label joker_ending_1: #ending 1 where the building explodes
        scene perched building with vpunch
        "The ground shakes violently"
        batman "What could that be?"
        "A bright ornage ball can be seen from inside Falcone Plaza, as the glass cieling above the ball room bursts open from the explosion"
        batman "What have I done."
        scene end card
        "ENDING 1/17"
        return

    label joker_Choice_2:
        batman "Hmmm... I do not see anyone, what could he be up to?"
        batman "Wait who is that!"
        scene intersection
        "Charlie Collins appears out of the shadows of the alley drenched in sweat"
        show charlie collins nuetral at right
        show batman neutral at left
        hide charlie neutral at right
        show charlie scared at right
        charlie "Oh... oh hi-hi Batman, my name is Ch-ch-ch Charlie Collins what seems to be the  officer problem?"
        "Batman obviously noticing the amount of durress Charlie is under"
        
        menu:
            "Question Charlie":
                jump joker_scene_2

            "Go inside and investigate":
                jump joker_ending_3

        label joker_scene_2: #continue through ending 2 which is the episode
            batman "Charlie have you seen The Joker or Harley Quinn?"
            charlie "N-n-n no of course not!"
            batman "Are you lying to me?"
            charlie "Okay fine yes, he kidnapped me and he is forcing me to work with him"
            batman "And you decided to not notfiy any of the GCPD officers inside?"
            charlie "It's not that simple you see. He has been tormenting me for the past two years!"
            charlie "You see, I kind of owed him a favor after he cornered me one night. We struck a deal because he was going to kill me!"
            charlie "I swear I'm not a bad guy you have to believe me. If he is caught he said hell kill my family!"
            batman "You say he has been tormenting you for 2 years?"
            charlie "Yes he knows my address, my family's names, and everything. He knows my whole life!"
            batman "Alright Charlei it'll be okay calm down. We'll figure out something."

            jump joker_scene_3
        

        label joker_ending_3: #go to ending 3 where batman is hit with nerve gas out and the building explodes
            scene black screen
            batman "Jeez it is dark in here, I wish I packed my bat-flashlight today"
            batman "What is that smell"
            batman "\"cough\" \"cough\" What is going on"
            batman "It must be \"cough\" nerve gas"
            "In that moment Batman becomes frozen in place, before passing out"
            "Suddenly, a blinding light fills the room"
            scene end card
            "ENDING 2/17"
            return

    label joker_scene_3:
        scene manor inside
        show commisioner gordon at left
        show harvey bullock at right
        "Music plays as people celebrate themselves at the Policemen's ball"
        gordon "Geez bullock I wish I could get out of here"
        bullock "Relax will ya. We have hard job's we need to unwind, especially your self commish"
        "Just then smoke starts to fill the room"
        gordon "Oh what! \"cough\" \"cough\" what is this? \"cough\"."
        bullock "I dont know but we need to get out of here!"
        "Just then, everyone in the hall freeze up"
        "Charlie opens the door as the smoke clears the hall. The Joker enters the hall, with a sadistic smile cackling maniacly"
        show joker at center
        joker "Good evening ladies and gentlemen. I hope everyone is havinga wonderful night and is not too frozen with joy!"
        joker "I hope you are all enjoying the party favors I brought along. It will surely strike a nerve with some of you."
        joker "Now to the matter at hand. I know you are celebrating tonight, but I am quite hurt and upset, especially at you JIMBO."
        joker "All of my hard work year around to go unnoticed, and not a single thank you for keeping your paychecks coming, I am truly hurt."
        joker "But I have grown a lot this year, and because of this I will take the higher road. No need to apologize. It is your night"
        joker "But I will leaving you with a parting gift, it will surely leave you {u}exploding{/u} with laughter"
        "Joker places a bomb to the floor"
        joker "Please enjoy the rest of your night everyone, while you still can."
        hide joker at center
        "Joker walks out laughing wildly."
        "Everyone stares in horror as they bear witness to their own demise."
        "Suddenly-Glass shatters."
        "Batman comes gliding in from the glass cieling above."
        show batman active at center
        show batman neutral at center
        "Batman rushes over and picks up the bomb."
        "The bomb displaying 10 seconds left"
        batman "Only 10 seconds what can I do?"

        menu:
            "Throw the bomb into the air":
                jump joker_Choice_4

            "Defuse the bomb":
                jump joker_Choice_5

            "Run":
                jump joker_Choice_6

        label joker_Choice_4:
            "Batman ties the bomb to his grapnle gun and shoots the bomb through the hole he came in"
            "The bomb explodes in the air with a glorious blaze of light, shaking the whole building"
            jump joker_ending_2 

        label joker_Choice_5: #Defuse
            "Batman lifts the front panel off the bomb revealing a mess of brighlty colored wires and a message drawn in lipstick"
            "Have fun batsy"
            batman "Blast there's barely enough time, time to act!"
            
            menu:
                "Cut Green wire":
                    jump joker_ending_5

                "Cut Red wire":
                    jump joker_ending_4

                "Cut Yellow wire":
                    jump joker_ending_6

        label joker_ending_5:
            "A small snip is heard as Batman precedes to cut the green wire"
            "The timer stops with 2 seconds left"
            batman "Good"
            "Suddenly, the timer counts to zero"
            batman "Dear god"
            "A blinding light fills the room as Batman shields himself with his cape"
            "It is too late"
            scene end card
            "ENDING 3/17"
            return

        label joker_ending_6:
            "A small snip is heard as Batman precedes to cut the yellow wire"
            "The timer stops with 2 seconds left"
            batman "Good"
            "Suddenly, the timer counts to zero"
            batman "Dear god"
            "A blinding light fills the room as Batman shields himself with his cape"
            "It is too late"
            scene end card
            "ENDING 4/17"
            return

        label joker_Choice_6: #Run
            "Batman picks up the bomb holding it over his head in an almost cartoonishly bombastic way"
            "With all his might BAtman runs for the exit"
            batman "I can make it."
            "Sharp beeps tick bye as he makes his way to the entryway"
            "Suddnely Batman trips falling over dropping the bomb"
            "With a shocked look Batman reaches out"
            batman "Nooooo!!"
            "A blinding light fills the room"
            "He saved the GCPD, but at what cost"
            jump joker_ending_7
            
    label joker_ending_2: #the ending of the actual episode
        scene intersection
        show joker at right
        "Joker strutting outside knowing he has bested the GCPD"
        "Suddenly the ground shakes underneath him"
        joker "That explosion came from outside! Whatttt!"
        "Suddenly Charlie grabs Joker by the colar and throws him into the alley."
        scene alley way
        show charlie neutral at left
        show joker at right
        charlie "You know Joker my life was not great when you came along and you still had to mess it up."
        "Charlie punches joker sending him into the trash cans next to the alley wall."
        joker "Oh bucko your life was meaningless until I came along, I gave you purpose"
        "Joker stands towering over charlie, holding him by his colar"
        joker "You didnt think I would let you leave alive?"
        charlie "Why not both of us"
        scene charlie bomb1
        "Charlie reaches into his coat pocket and holds a bomb"
        "Joker looking scared"
        scene charlie bomb2
        joker "Now Charlie I feel that this is quite undeserved, I feel I have treated you quite well these past two years"
        charlie "My life has been a misereable wreck, lets both go out together!" 
        "Batman appears"
        scene alley way
        show charlie scared at center
        show batman neutral at left
        show joker at right
        batman "Charlie put the bomb down it doesnt have to be like this"
        joker "\"Huddling in the corner\" yeah Charlie why don't we just put the bomb down and go our seperate ways"
        charlie "I've had enough of my life being meaningless, now I'll be known as the man who took the Joker down"
        "The bomb ticks down to 5"
        batman "No Charlie dont!"
        "The Joker cowering in fear"
        "4, 3, 2, 1"
        "The bomb explodes and fantastic dislpay of streamers and ribbons"
        joker "Oh fooey. You really had me going there Charlie"
        batman "Alright Joker lets get to Arkahm Asylum, and Charlie you better go home"
        charlie "Yeah that sounds really nice"
        scene end card
        "ENDING 5/17"
        return

    label joker_ending_4: #slightly altered ending of the episode
        scene intersection
        show joker at right
        "Joker strutting outside knowing he has bested the GCPD"
        "But no explosion comes"
        joker "We must have a bat infestation then!"
        "Suddenly Charlie grabs Joker by the colar and throws him into the alley."
        scene alley way
        show joker at right
        show charlie neutral at left
        charlie "You know Joker my life was not great when you came along and you still had to mess it up."
        "Charlie punches joker sending him into the trash cans next to the alley wall."
        joker "Oh bucko your life was meaningless until I came along, I gave you purpose"
        "Joker stands towering over charlie, holding him by his colar"
        joker "You didnt think I would let you leave alive?"
        charlie "Why not both of us"
        scene charlie bomb1
        scene charlie bomb2
        "Charlie reaches into his coat pocket and holds a bomb"
        "Joker looking scared"
        joker "Now Charlie I feel that this is quite undeserved, I feel I have treated you quite well these past two years"
        charlie "My life has been a misereable wreck, lets both go out together!" 
        "Batman appears"
        scene alley way
        show charlie neutral at center
        show batman neutral at left
        show joker at right
        show charlie neutral at center
        show batman neutral at left
        batman "Charlie put the bomb down it doesnt have to be like this"
        joker "\"Huddling in the corner\" yeah Charlie why don't we just put the bomb down and go our seperate ways"
        charlie "I've had enough of my life being meaningless, now I'll be known as the man who took the Joker down"
        "The bomb ticks down to 5"
        batman "No Charlie dont!"
        "The Joker cowering in fear"
        "4, 3, 2, 1"
        "The bomb explodes and fantastic dislpay of streamers and ribbons"
        joker "Oh fooey. You really had me going there Charlie"
        batman "Alright Joker lets get to Arkahm Asylum, and Charlie you better go home"
        charlie "Yeah that sounds really nice"
        scene end card
        "ENDING 6/17"
        return

    label joker_ending_7:
        show intersection
        show joker at right
        "Joker strutting outside knowing he has bested the GCPD"
        "Suddenly the ground shakes underneath him"
        joker "Ah the clown prince of crime finally won."
        "Suddenly Charlie grabs Joker by the colar and throws him into the alley."
        show charlie neutral at left
        charlie "You know Joker my life was not great when you came along and you still had to mess it up."
        "Charlie punches joker sending him into the trash cans next to the alley wall."
        joker "Oh bucko your life was meaningless until I came along, I gave you purpose"
        "Joker stands towering over charlie, holding him by his colar"
        "Joker grabs his knife out of his pocket and plunges it into Charlies side."
        "Charlie steps back taken aback by what has just happened"
        joker "You didnt think I would let you leave alive?"
        "Charlie falls to the ground, the Joker towering over him laughing widly"
        charlie "Why not both of us"
        scene charlie bomb1
        "Charlie reaches into his coat pocket and holds a bomb"
        "Joker's laughing stops has his face switchs from a sadistic grin to shock and horror."
        scene charlie bomb2
        joker "Now Charlie I feel that this is quite undeserved, I feel I have treated you quite well these past two years"
        charlie "My life has been a misereable wreck, lets both go out together!" 
        charlie "I've had enough of my life being meaningless, now I'll be known as the man who took the Joker down"
        "The bomb ticks down to 5"
        "The Joker cowering in fear"
        "4, 3, 2, 1"
        "The bomb explodes and fantastic dislpay of light and smoke"
        scene end card
        "ENDING 7/17"
        return   

label clayface_scene_1:
    scene perched building
    batman "What could be going on?"
    scene tarnower_financial
    batman "I guess I must investigate"
    jump clayface_scene_2

    label clayface_scene_2:
        scene building-interior
        show batman neutral 2 at right
        show security gaurd at left
        gaurd "Oh batman you need to help a terrible creature broke in and stole so much you gotta help!"
        batman "It's alright, which way did he go?"
        hide security gaurd
        show clayface at left
        clayface "Behing you!"
        "Clayface forms his fist into a giant cinderblock and strikes Batman, sending him to the ground!"
        batman "Oof"
        clayface "See you later bat-brain, next time dont get in my way"

        menu:
            "Shoot grapnle gun":
                jump clayface_Choice1

            "Thrown explosive batarang":
                    jump clayface_Choice2


        label clayface_Choice1:
            "Just before Clayface leaves, Batman shoots him with his grapnle gun, and the claw goes right through withoout sticking"   
            batman "\"Batman thinks to himself\" Huh?"
            "clayface departs in a white van."
            jump clayface_scene_3

        label clayface_Choice2:
            "As Clayface walks out of Tarnower Financial, he deploys one of his explosive batarangs."
            batman "This'll stop you."
            "Batman throws the batarang at Clayface chest, suddenly, instead of sticking in, it passes right through him."
            batman "Huh."
            "Just then the skie lights up with a small explosion."
            clayface "Nice try, now stay down next time."
            jump clayface_scene_9

    label clayface_scene_3:
        "Back at the Bat-Cave"
        scene batcave
        show batman neutral at left
        batman "Hmm I wonder what Clayface was up to, and why did my claw pass right through him"
        batman "Hmmm..."
        "Alfred appears"
        show alfred at right
        alfred "Sir, Thomas Elliot is on line one, he wants to know about the new shipment at Wayne Biotech"
        batman "Not now Alfred, I am working"
        alfred "Sir If I do recall, Bruce wayne still has a public appearance."
        batman "\"Grunt\""
        alfred "Is that a sample of Mr. Hagen."
        batman "Yes. it was peculiar my bat-claw right through him, usually he is rock solid."
        batman "Also during my encounter, whatever he was doing, he needed a lot of money for it."
        alfred "How peculiar, how will you precede?"

        menu:
            "Check a sample from the Bat-claw":
                jump clayface_Choice4

            "Find cctv of the van":
                jump clayface_Choice5

        label clayface_Choice4:
            scene batcomputer 2
            batman "Computer, run an analysis on the sample."
            alfred "Now is Bruce wayne avialable?"
            batman "Yes Alfred, get the blue coupe running, I'll meet him in the city."
            jump clayface_scene_4

        label clayface_Choice5:
            scene batcomputer 2
            batman "Computer pull up the CCTV footage."
            "Beeping can be heard from the computer screen as the screen shows \"System processing\""
            "The computer pulls up a video from the event."
            "As the video plays, the screen displays a white van driving by, as Clayface hops in the back of the van."
            batman "Slow down and pause."
            "As the video whirs, the van drives by slower displayign the white van flashing by."
            batman "Computer pause and zoom in."
            "The computer zooms in displaying a women driving the van."
            batman "Computer run facial recognition on the driver."
            "The computer whirs, processing the command."
            "..."
            "..."
            "..."
            "The computer beeps and displays the name \"Stella Bates, Age 38, Place of work: Wayne Bio Tech\""
            batman "How could she be related to Clayface?"
            alfred "Maybe you should visit her and find out."
            batman "Way ahead of you, Batmmobile start up."
            alfred "Will you be arriving as Batman or Bruce."
            batman "Bruce will be paying them a visit."
            jump clayface_scene_10

    label clayface_scene_9:
        "Back at the Batcave"
        scene batcave
        show batman neutral at left
        batman "Hmmm what is wrong with Clayface? Why did my batarang go right through him."
        show alfred at right
        alfred "Sir due to your escapade last night, the library you caused damage too from your \"Toy\", is asking for a donation from anyone."
        batman "Set up an anonymous donation of $5000."
        alfred "Right sir."
        batman "Alfred, the batarang passed right through."
        alfred "You know, sir, that reminds me of a story sir, form my time in the army."
        alfred "Sometimes in the war, when the whether was quite dismal, the bullets could pass through thin layers of mud."
        batman "That's it, his body is turning into mud!"
        batman "He must be trying to get treatment for his condition, thats what the money is for!"
        batman "Alfred I am heading to the lab, tell any incoming call that I am unavailable."
        alfred "Right sir, is Bruce or Batman going?"
        batman "Bruce."
        jump clayface_scene_10

    label clayface_scene_4:
        "In an undisclosed location"
        scene clayface-lab
        show clayface2 at right
        show stella bates at left
        clayface "I gave you the money, now can you fix me?"
        stella "Not yet I require one more ingrediant."
        clayface "You promised me that if I got the money I would be fine."
        stella "Patience these things take time"
        clayface "I DON'T HAVE TIME! NOW WHERE IS MY CURE!"
        clayface "Sorry, I did not mean to yell."
        stella "It'll be here soon, you just have to pick up this new isotope from Wayne Bio-tech."
        clayface "And after that, you'll have what you need to make my cure?"
        stella "Yes, it'll all be over soon darling"
        jump clayface_scene_5

    label clayface_scene_5:
        scene resturant
        show bruce wayne at left
        show reeves neutral at right
        "As Bruce finishes his meal with Wayne Bio Tech representative Thomas Elliot"
        batman "Ah what a wonderful meal, and you can handle everything with your division"
        thomas "Yes everything should be secure"
        batman "excellent"
        "Incoming message from Alfred"
        alfred "Sir, the computer has completed it's analysis of the sampel you took off of Clayface"
        alfred "There also seems to be reports of something bad occuring at the lab"

        menu:

            "Check out the lab":
                jump clayface_ending_2

            "Head back to the Batcave":
                jump clayface_scene_6

    label clayface_ending_2:
        "Batman heads over to the lab"
        scene wayne labs
        "Batman sees the lab covered in mud, strewn with the incopasated bodies of scientists"
        show batman neutral 2 at right
        show clayface at left
        batman "Hagen stop I can help you we can figure this out!"
        "Batman shouts as Clayface grasps a scientist."
        clayface "Why won't you just quit Batman!"
        "Clayface drops the scientist"
        batman "We don't have to fight Hagen!"
        clayface "You did this not me!"
        "Batman lunges at Clayface sliding under him"
        clayface "Oh no you don't."
        "Clayface jumps back slamming his body on Batman, submerging him in mud"
        clayface "You can't stop me anymore Batman."
        "Clayface moves Batman up through his body and exits him onto his hands, Batman's hands bound by clay"
        batman "\"Muffled sounds\""
        clayface "Maybe you should've listened to me the first time."
        "Clayface raises Batman over his head, before he slams Batman's back over his suddenly rock solid knee."
        "A loud crack is heard, as Batman folds over his knee."
        batman "Ahhhhhhhhh"
        clayface "I'm sorry Batman, but you left me no choice."
        "Batman lays motionless, eyes wide, unable to move."
        scene end card
        "ENDING 8/17"
        return

    label clayface_scene_10:
        scene wayne labs
        show bruce wayne2 at right
        show scientist at left
        scientist "Oh Mr. Wayne, we weren't expecting you, I apologize for the state of things."
        bruce "Oh nonsense, I like to pop from time to time, to see how my paren'ts legacy is doing."
        scientist "So what did you want to see today."
        bruce "I wanted to check in on your research on material dynamics?"
        scientist "Right, we just got a shipment, of our new isotope, MP40."
        bruce "I see, how does it improve your research."
        scientist "Its quite an exciting new discovery, it repairs semi-fluids molecular structure, bringing it back together."
        "Bruce make's a mental note."
        bruce "\"In Bruce's mind\" Clayface must be after this isotope."
        bruce "So who is the head researcher on this?"
        scientist "Oh Dr. Stella Bates, but she is not in the lab today."
        bruce "Oh I see-"
        "Just then, a sudden boom comes from outside the lab."
        bruce "What the-"
        "Suddenly Clayface stops in thrashing the doors around"
        show clayface at right
        show bruce wayne at center
        clayface "Where is the MP40?!"
        "Suddenly Bruce dissapears"
        hide bruce wayne
        scientist "Y-y-y yes it's rig- right, where did Mr. Wayne go?"
        clayface "Who?!"
        scientist "It's right here, please don't hurt me, I have nothing to do with this!"
        "Suddenly Batman appears in the mangled doorway."
        hide scientist at left
        show clayface at left 
        show batman neutral at right
        batman "Hagen stop this."
        clayface "I thought I told you to stay down!"
        "Clayface slaps Batman to the side, sneding him flying ot the other side of the room"
        clayface "I warn you, don't get back up!"
        "As clayface exits the lab, Batman runs and hops on the back of clayface"
        batman "Hagen you have to stop!"
        "In that moment, Batman pulls out a small bottle of pepper spray"
        clayface "What is that gonna do?!"
        "As Batman sprays it, it coats him in liquid nitrogen freezing him"
        clayface "Ahhhh"
        "Just then Clayface, pushes himself with his last bit of mobility out of the window falling multiple stories, Batman watching from the window"
        clayface "See you later Bats!"
        "Clayface shouts as he falls onto the bed of a moving dumpster, clutching the MP40"
        jump clayface_scene_8
        

    label clayface_scene_6:
        "Back at the Batcave"
        scene batcomputer 2
        batman "It appears that CLayface's molecular structure is disintegrating, that explains why he is so maleable."
        batman "The money he stole must be for a treament."
        alfred "Clayface is at Wayne Biotech!"
        batman "I'm on my way"
        batman "\"Thinking to himself\" I wish Karlo wasn't going down this path, we could have worked somehting out with Arkkahm."
        jump clayface_scene_7

label clayface_scene_7:
    scene wayne labs
    "The labratory in disoray with mud stains everywhere."
    show batman neutral
    batman "No, I have came to late."
    batman "What could Hagen have been looking for?"

    menu:
        "Check storage":
            jump clayface_ChoiceStorg
            
        "Check lab equipment":
            jump clayface_ChoiceEquip

        "Check documents":
            jump clayface_ChoiceDoc

    label clayface_ChoiceStorg:
        "Batman checks the lab storage"
        batman "Hmmm"
        batman "Wait the filing cabinet was broken into."
        batman "I should look for the missing documents."
        jump clayface_ChoiceDoc

    label clayface_ChoiceEquip:
        "Batman checks the lab equipment."
        batman "Hmmm, nothing but broken lb equipment and mud stains everywhere."

        menu:
            "Check storage":
                jump clayface_ChoiceStorg
            
            "Check documents":
                jump clayface_ChoiceDoc

    label clayface_ChoiceDoc:
        "Batman picks up the mud covered lab sheets."
        batman "Hmmm MP40, recombines molecular structures and strengthening their bonds. Of course!"
        batman "Clayface has come here to grab the enzyme to cure himself"
        batman "He can't do this himself who is helping him?"
        batman "Huh? Who is this?"
        "Batman looks at the top of the chart, seeing the author of the paper."
        batman "Stella Bates? Of course Clayface approached her to help him fix himself."
        jump clayface_scene_8

label clayface_scene_8:
    scene clayface-lab 
    "Undisclosed location."
    show clayface at left 
    show stella bates2 at right
    clayface "Okay Stella, I got you what you asked, now fix me."
    stella "OKay lay in the bed, the process will take a but, so do not move or interrupt it"
    hide clayface at left
    "Machines wir up as chemicals start infusing them in Clayface's body"
    "Suddenly glass shatters from above"
    stella "Batman, what are you doing here"
    show batman neutral at left
    clayface "Do not let Batman stop us"
    stella "You must leave now immediately, the process can't stop, it'll kill him!"
    batman "I must take you to justice Clayface"

    menu:
        "Pull the plug":
            jump clayface_Choice6

        "Add more chemicals":
            jump clayface_ending_5

    label clayface_Choice6:
        "As the process continues Batman, pulls the plug, sending sparks flying everywhere"
        batman "Alright Hagen lets head to Arkahm"
        "Stella leaps over the table, lunging for Batman."
        stella "No what have you done!"
        "Batman, grabs her, and pushes her away."
        hide stella bates2 at right
        clayface "You have intervened for the last time!"
        stella "No Matthew!"
        show clayface2 at right
        clayface "It's over, you die Batman!"

        menu:
            "Tie him up":
                jump clayface_ending_3

            "Stay in place":
                jump clayface_ending_1

            "Leap over him":
                jump clayface_ending_4

    label clayface_ending_1:
        "As Clayface charges Batman, Batman holds his ground steady"
        clayface "You are done for Batman"
        "Right before Clayface swings with his fist, now a mace, Batman pulls out a gadget, spraying Clayface with liquid nitrogen"
        clayface "Ahh, not this time"
        "Clayface swats the gadget out of Batman's hand, and before Batman can leap out of the way, he is swatted with the force of car, sending him outside the lab."
        scene clayface-fight
        batman "Uhh, Clayface you need to be stopped!"
        clayface "No Batman you are done messing up my life!"
        stella "Matthew, you are absorbign the rain, you'll melt!"
        clayface "THIS ENDS TONIGHT!"
        "Clayface lunges toward Batman, forcing them each to fall off the cliff."
        scene clayface death
        stella "Matthew no!, Batman save him!"
        batman "Hagen hold it together!"
        "Clayface's grip slipping"
        clayface "It's wraps Batman, please take care of Stella."
        "Clayface plunges into the depths of the Gotham harbor. Dissolving into nothing as the mud is absorbed by the water."
        scene end card
        "ENDING 9/17"
        return

    label clayface_ending_3:
        "As Clayface lunges for Batman, Batman shoots his Grapnle gun in hopes of restraining him."
        clayfaces "I thought you would have learned by now."
        "Clayfaces leaps on to Batman, as Batman watches in horror for the mass of clay hurtling towards him."
        clayface "This'll teach you"
        "Suddenly Clayface begins enveloping Batman in a thick mass of clay and mud."
        scene clayface-batman-death
        stella "Matthew what are you doing!"
        clayface "It's the only way, he has to be stopped."
        "As Batman struggles to get out, his muffled cries can be heard."
        clayface "Ah I feel his heartbeat slowing."
        "Slowly the moments underneath clayfaces skin slow."
        stella "Matthew i-i-i is he dead?"
        "Stella says with despair in her voice."
        clayface "Yes my dear, now we can finish this in peace."
        "Unfortunately the dark night did not make it out of this mess in time."
        "One could say he was caught in the mudslide."
        scene end card
        "ENDING 10/17"
        return

    label clayface_ending_4:
        show clayface at right
        "As Clayface charges Batman, Batman leaps over him."
        clayface "You are done for Batman"
        "Right before Clayface swings with his fist, now a mace, Batman mid-ar pulls out a gadget, spraying Clayface with liquid nitrogen"
        clayface "Ahh, not this time"
        "Clayface swats Batman out of the air sending him flying through the front window!"
        "Clayface follows Batman, yelling."
        scene clayface-fight
        clayface "Batman why do you always have to mess up everything in my life!"
        clayface "Why can't you just leave me alone."
        batman "Hagen I offered my help, but you refused, now I'm taking you to justice."
        stella "Matthew, you are absorbign the rain, you'll melt!"
        clayface "THIS ENDS TONIGHT!"
        "Clayface lunges toward Batman, but just before Batman leaps out of the way."
        batman "Here's some help from your friend Mr. Freeze."
        "Just then Batman pulls out Mr. Freeze's freeze gun firing it at Clayface."
        clayface "Noooooooo"
        "Just then, clayface is frozen into one solid mass of ice."
        stella "Batman no!"
        batman "It's alright I have a facility waiting for him under GCPD security, we can cure him, and I'd like you to join him."
        stella "Thank you Batman"
        "Stella sobs and falls to her knees, as GCPD sirens can be heard off in the distance."
        "Batman looks off into the distance over the cliff, thankful for the madness to be over."
        scene end card
        "ENDING 11/17"
        return

    label clayface_ending_5:
        "As Clayface lays in the bed on the opperating table, Batman leans over the console turning every dial and switch."
        stella"Batman no, you'll kill him"
        clayface "Nooooo"
        "Just then Clayface sits up contorting in a mess, displaiyng every past person he has every cloned. Batman with a lock of shock and horror on his face."
        hide stella bates2 at right
        show clayface 2 at right
        batman "SHUT IT OF MS. BATES!"
        stella "It can't be you have doomed him."
        "Clayface screams in agony as he body begins to melt and morph"
        clayface "Batman you son of a-"
        "Just then clayface's body melts into a puddle of mud."
        batman "I'm sorry Hagen I didnt know."
        "Batman looks in horror, as the man he was once hoping to save as died at his own hand."
        scene end card
        "ENDING 12/17"
        return

label twoface_scene_1:
    scene apartment front
    show batman neutral at left
    "Batman arrives at Elliot Apartment Complex"
    "Alfred in intercom"
    alfred "A person reported a break in from the 3rd floor."
    batman "I see, I'll keep you posted."
    "Batman enters the dilapidated run down apartment building."
    scene apartment-inside
    show batman neutral
    batman "What could've happened here."

    menu:
        "Check drawers":
            jump twoface_ChoiceDrawr

        "Check pictures":
            jump twoface_ChoicePic

        "Check clothing":
            jump twoface_ChoiceCloth

        "Check Files":
            jump twoface_ChoiceFile

    label twoface_ChoiceDrawr:
        "Batman  checks the drawers in the apartment."
        batman "Hmmm nothing but old clothing- wait the back of this drawer feels hollow."
        "Batman feels around and finds a depression in the drawer"
        batman "A false back?"
        "A soft click can be heard as Batman presses the button, as the back of the dresser opens up."
        batman "Hmmm interesting, alfred!"
        alfred "\"In Batman's earpiece\", yes, sir?"
        batman "There seems to be documents and pictures of this person's work with Two-Face?"
        batman "What is the name of the resident that lives here?"
        alfred "It is a Mr. Jack Drake."
        batman "Hmmm, interesting."
        
        menu:
            "Check pictures":
                jump twoface_ChoicePic

            "Check clothing":
                jump twoface_ChoiceCloth

            "Check Files":
                jump twoface_ChoiceFile


    label twoface_ChoicePic:
        "Batman roots around, the pictures checking behind the frames."
        batman "Theres nothing here, except he has a son. Must have left his son alone."
        batman "Deadbeat father."
        batman "His son must be the Batman fan, with all these posters everywhere."
        batman "There also seems to be what used to be a key behind one of these pictures."
        batman "Interesting."

        menu:
            "Check clothing":
                jump twoface_ChoiceCloth

            "Check Files":
                jump twoface_ChoiceFile

            "Check drawers":
                jump twoface_ChoiceDrawr


    label twoface_ChoiceCloth:
        "Batman checks the pockets of the miscellaneous clothing strewn about haphazardly"
        batman "Hmmm, just reciepts."
        batman "Groceries, Liquor, and wait whats this?"
        batman "A recipet from ACE chemicals"
        batman "What could that be for?"

        menu:
            "Check Files":
                jump twoface_ChoiceFile

            "Check pictures":
                jump twoface_ChoicePic

            "Check drawers":
                jump twoface_ChoiceDrawr


    label twoface_ChoiceFile:
        "Batman shuffles through the loose documents on the table"
        batman "Hmmm nothing but late rent, eviction noticies, and a message from Two-Face?"
        batman "\"Reading to himself\" come to the docs or the boy gets it"
        batman "Someone is in trouble"
        batman "Alfred notify the GCPD, Two-Face has kidnapped someone at the docs."
        jump twoface_scene_2

label twoface_scene_2:
    scene gotham docks
    "At the Gotham Harbor"
    scene twoface-docks
    tim "Hey let me go!"
    twoface "Cmon kid just tell me where your dad is, and I won't hurt you."
    tim "I don't know, my dad is never around."
    twoface "Lies, just tell me an-"
    "Suddenly Batman arrives from the shadows leaping for twoface"
    twoface "Get him boys!"
    scene twoface thugs2
    "As Batman lands, the thugs square up to Batman"
    thug1 "C'mon you can't take both of us."
    thug2 "Yeah it's over Batman."
    batman "Don't be so sure."
    "The thugs throw themselves at Batman, but he ducks and dodges their strikes"
    thug1 "Ugh why can't we hit him."
    thug2 "He must be supernatural or something!"
    "Just then Batman leaps over thug2 striking thug1 in the face with his knee, crackng his jaw"
    thug1 "OW, what the f-"
    "Just then, Batman throws a kick straight to thug1's chest, knocking him over."
    thug2 "Alright thats it, no more mister nice guy."
    "As thug2 throws a punch at Batman, Batman dodges and lands an uppercut, sending the criminal flying."
    scene gotham docks
    show batman neutral 2 at right
    show twoface at left
    batman "Alright Two-Face, you-"
    twoface "Don't move Batbrain, or the kid gets it."
    "Batman stops in his tracks, as he sees Two-Face holding the kid with a gun to his temple."
    tim "No, let me go!"
    twoface "Shut it kid you had your chance."
    batman "Two-Face, put the gun down."
    twoface "No I think I'm gonna walk away with the kid calmly and you aren't going to follow."
    "Just then Tim throws and elbow to Two-Face's stomach sending harvey backwards, and releasing his grip on him."
    twoface "Why you little."
    "At that moment, a key falls out of Tims pocket."
    twoface "Don't mind if I do."
    "Just then Batman tries to restle the gun from Two-Face, when-"
    "BLAM"
    twoface "You get what you deserve, Batman"
    "Batman steps back shocked at what has happened, his former best friend has just shot him."
    "Just then, GCPD sirens can be heard off in the distance."
    twoface "Time to go now, dont wait up Batman."
    "Batman falls backing laying in a growing pool of his own blood."
    "..."
    "..."
    "..."
    "Suddenly the boy appears."
    tim "Batman get up we need to get out of here!"
    "batman lying motionless whispering"
    batman "Call Batmobile"
    "Suddenly the Batmobile rounds the corner, humming furiouslly"
    "With the help of Tim, Batman and Tim get inside the Batmobile"
    scene tim drake batmobile
    tim "How do you drive this thing?"
    batman "Batmobile autopilot home."
    "In that moment, Batman passes out, as the Batmobile drives back to the Batcave."
    jump twoface_scene_3

label twoface_scene_3:
    scene batcave
    show batman neutral at left
    show alfred at right
    "Batman arises dreery from an unrestful slumber on a surgens table wrapped in gauze."
    batman "Alfred..."
    alfred "Yes sir?"
    batman "Did I bring home a boy?"
    alfred "Yes Master, he is standing right there."
    show tim drake at center
    tim "Thank you Batman, you know you are one of my heros."
    batman "You need to leave."
    alfred "He has already been upstairs."
    tim "Honest I can keep a secret, I promise."
    batman "Well now, what can you tell me about your father, how is he associated with Two-Face? What is he planning?"
    tim "I don't know, if I did I would tell you."
    "Batman becoming increasingly agitated"
    batman "Are you lying to me!"
    tim "I'm not, honest"
    "Tim begins to tear up."
    batman "I'm sorry, I just need to know what he's planning"
    tim "I would tell you, but he's never around. I haven't seen him for months."
    alfred "Sir you must see this."
    "Alfred brings up the news report on the Batcomputer."
    "A news broadcast begins to show"
    twoface "Well well well, I hope I didn't ruin anyone's dinner, but I have a message for Gotham City."
    twoface "Send me 2 million dollars, or I will release poision gas into the center of Gotham."
    twoface "The clock is ticking."
    "At that moment the broadcast immedieatly ends, and the Batcomputer shuts off."
    alfred "sirWhat are you gonna do?"
    batman "Batcomputer, bring up the recorded broadcast."
    "The computer whirs as the broadcast plays in reverse."
    batman "Computer scan the background where is that location."
    "It appears that it is from a wherehouse on the lower east side."
    batman "I'm gonna head there and take Harvey down."
    alfred "What about the boy."

    menu:
        "Take Tim":
            jump tim_ChoiceY

        "Do not take Tim":
            jump tim_ChoiceN

    label tim_ChoiceY:
        tim "Batman please take me with you, I have a stake in this too."
        batman "Alright Tim, get in."
        batman "But you do everything I say."
        tim "Yes sir."
        "Batman walks to the Batmobile, as Tim runs and jumps into the passenger seat of the cockpit."
        "Man this is gonna be so much fun."
        batman "I hope I don't regret this."
        jump twoface_scene_4

    label tim_ChoiceN:
        tim "Batman please take me with you, I have a steak in this too."
        batman "No it's too dangerous."
        tim "Please, my life has been only messed up because of him"
        batman "No!"
        "Batman slowly walks to the Batmobile as he enters by himself."
        jump twoface_scene_5

label twoface_scene_4:
    scene warehouse
    "Batamn enters a non descript wearhouse."
    scene warehouse2
    show batman neutral at left 
    show robin at center
    batman "Alfred, alert the GCPD."
    alfred "\"In Batman's earpiece\" on it Master Bruce."
    batman "Tim you will do everything I say."
    tim "\"Nodding silently\""
    batman "Now stay hidden and don't come out till the GCPD arrive."
    "As Batman and Tim hide, voices can be overheard."
    thug1 "You think Two-Face is really gonna do it?"
    thug2 "Do you what, release the poison?"
    thug1 "Yeah, won't it hurt alot of people?"
    thug2 "So what, we'll be safe, and a whole lot richer."
    thug1 "Yeah I just feel bad."
    thug2 "Oh don't go and grow a conscience, you had your chance years ago."
    thug1 "Yeah I guess you're right."
    "Just then Batman leaps over and smashes the thugs head's together."
    "Batman looming over the thug's"
    batman "WHERE IS TWO-FACE!"
    "Batman hold's up one of the thugs, with the intent of throwing them."
    batman "I'm not gonan ask again!"
    thug1 "Alright, alright he's in the main room."
    "Batman drops the thug to the ground, with a sharp thud."
    thug1 "Ow, you could've at least put me down gently"
    batman "Grunt"
    jump twoface_scene_6

label twoface_scene_6:
    scene bomb
    twoface "Cronnect the wires, dot the I's, and cross the T's"
    scene batman thugs3
    scene twoface-warehouse
    batman "Two-Face, it's over, stop this before anyone else get's hurt."
    scene clayface-lab
    show batman neutral2 at right
    show twoface at left
    twoface "Too late, bat brain. I'm gonna release the poison onto every one in Gotham and it'll be over."
    batman "I'll stop you."
    twoface "Before you stop me from blowing this kid's brains out."
    "Two-Face's thugs walk out holding tim, as he struggles to get out, squirming, handing Tim to Two-Face."
    scene twoface_holding-tim
    tim "Let me go, or you'll regret it."
    twoface "Quiet boy, and this time I won't let you get away."
    twoface "Now Batman, what'll it be, save the kid, and let the poison release or, stop me and fail to save the boy's life?"
    twoface "Maybe we should let the coin decide."
    "Two-Face flips the coin into hte air, time slows, as Batman watches the rotations slow down in air, contemplating what to do."
    
    menu:
        "Save Tim":
            jump twoface_ending_3

        "Stop Two-Face":
            jump twoface_ending_4

        "Disrupt the flip":
            jump twoface_ending_5

    label twoface_ending_3:
        "As the coin lands, Batman lunges for the thugs."
        twoface "Good move"
        "As Batman wrestles, Tim away from twoface's goons, twoface presses the button"
        scene twoface-withgun
        twoface "So long Batman"
        batman "No."
        "Batman's eyes widen as he realizes what he has done"
        "As Batman pummels the thugs away, he runs after Two-Face"
        "In a heated chase Batman manages to catch up and tackle Two-Face."
        scene batman_vs_two-face
        batman "HARVEY WHAT DID YOU DO!"
        "Batman yells with a fury that has never been seen by anyone of his villians before"
        twoface "I'm cleaning Gotham, in a way that I could never as DA"
        batman "You were one of the good ones, why?"
        twoface "The whole system is corrupt, theres no way to change it now"
        "In that moment, Two-Face stabs Batman between ribs with his switchblade."
        batman "Ahh"
        "As Two-Face continue wrestling, Batman punches his once best friend furiosly"
        batman "YOU HAVE TO BE STOPPED!"
        twoface "SHUT UP!"
        "In that moment, Batman flips on top rotating Two-Face's body when suddenly"
        twoface "AHHHH"
        "A crack can be heard, as Two-Face's back is broken"
        batman "I'm sorry Harvey I really am, but it was the only way."
        "GCPD sirens can be heard, as Batman walks away in shame for what he has done"
        tim "So Batman are we partners?"
        batman "No the GCPD will take care of you. Im sorry."
        tim "No?"
        batman "No."
        "Batman walks away back the Batmobile, in despair after he has done."
        batman "I'm sorry harvey."
        scene end card
        "ENDING 13/17"
        return        

    label twoface_ending_4:
        "As the coin lands, Batman lunges for Two-Face"
        batman "I'm taking you down"
        scene twoface_withgun
        "Batman lands on Two-Face, pummeling him to the ground"
        "Two-Face speaks as he begins coughing up blood."
        scene batman_vs_two-face
        twoface "\"Cough\" Too late \"Cough\", it's set to a timer."
        "Batman lands one final punch, with a loud crack, as Two-Face is knocked uncosious."
        "Now with Two-Face settled, Batman gets to work on the device, but what ahs been going on with Tim."
        "As the thugs begin to aim there gun at Tim, he begins to struggle harder."
        tim "No don't do this."
        "Just then, tim unfolds a bataragn and throws it, and as the batarang comes back around it strikes one of the thugs sned him crashing down."
        thug2 "Why you little brat."
        "Just then Tim gives the thug  a swift elbow to hte stomahc loosening his grip on the boy."
        tim "Ha you are done."
        "Tim, kicks the thug sneding him falling back onto the other thug."
        scene robin-victory
        tim "Another job well done."
        batman "Device is taken care of"
        "GCPD sirens can be heard as Batman and Tim tie up hte crooks."
        tim "So what is gonna happen to me now?"
        batman "Well I was thinking, how would you like to help me"
        tim "In that moment, a gleam could be seam in the young boy's eye."
        scene end card
        "ENDING 14/17"
        return

    label twoface_ending_5:
        scene twoface-coin
        "As the coin is about to land, Batman reaches in his utility belt for a handful of coins"
        scene twoface-coin2
        "As Two-Face's eyes light up waiting for the flip of the coin, Batman tosses hte extra quarters into the air."
        twoface "Noooooo!"
        "Two-Face lepas to the ground shuffling the coins around."
        scene batman thugs3
        twoface "Where is my lucky quarter, where is it, I can't make a decision without it."
        "As Two-Face, is indisposed, Batman lunges for the thugs, spereating them from Tim."
        "Making quick work of them, Batman frees Tim"
        tim "Thanks."
        batman "No time we need stop the device."
        "We some quick cuts, the device timer is shut off, and the city is saved from poison."
        "GCPD sirens can be heard as Batman and Tim tie up the crooks."
        scene robin-victory
        tim "So what is gonna happen to me now?"
        batman "Well I was thinking, how would you like to help me"
        tim "In that moment, a gleam could be seam in the young boy's eye."
        scene end card
        "ENDING 15/17"
        return        


label twoface_scene_5:
    scene warehouse
    "Batamn enters a non descript wearhouse."
    batman "Alfred, alert the GCPD."
    alfred "\"In Batman's earpiece\" on it Master Bruce."
    scene warehouse2
    show batman neutral at left
    "As Batman hides, voices can be overheard."
    thug1 "You think Two-Face is really gonna do it?"
    thug2 "Do you what, release the poison?"
    thug1 "Yeah, won't it hurt alot of people?"
    thug2 "So what, we'll be safe, and a whole lot richer."
    thug1 "Yeah I just feel bad."
    thug2 "Oh don't go and grow a conscience, you had your chance years ago."
    thug1 "Yeah I guess you're right."
    "Just then, as Batman arises to take down the crooks, a shadow can be seen over him."
    "Batman turns around but is smacked over the head with the but of a gun."
    batman "Uh Harvey, no..."
    "Batman falls unconscious."
    jump twoface_scene_7

label twoface_scene_7:
    scene black screen
    "Batman wakes up, his head pounding."
    batman "Wha... where am I."
    scene arkahm cell
    show batman neutral at left
    "Batman wakes up in a straight jacket, without his utility belt"
    "Batman looking around finds himself in a dingy stone cell, coverd in greese and mold, smelling of rot."
    batman "Oh no, its- its"
    batman "ARKAHM!"
    "Just then, the door to his cell slams open, Killer Croc and Scarecrow enter."
    scarecrow "Times up Batman, time to see if your fears set in."
    crock "RAHHHHH"
    jump twoface_scene_8

label twoface_scene_8:
    scene batman-straightjacket
    "As Batman struggles, Killer croc and Scarecrow wrestle him to the makeshift court room."
    "Batman is seated, as the reality sets in."
    batman "\'Thinking to himself\" How am I gonna get out of this one."
    "Just then, he notices his jury. His rogues gallery."
    scene arkahm-jury
    batman "Fu-"
    harley "All rise, for your beautiful and honorable, judge Joker"
    scene judge joker
    joker "Please be seated, court is now in session."
    "Batman's worst fears set in, as he realises his chance for survival is limited."
    harley "You will be judged by an unbiased jury of your peers."
    harley "Prosecuting attorny will be, Harvey Dent."
    harley "Now Batman, how will you represent yourself"

    menu:
        "Get a court appointed attorney":
            jump twoface_scene_9

        "Represent yourself":
            jump twoface_scene_10

    label twoface_scene_9:
        batman "I will take a court appointed attorney."
        "The current DA of Gotham is wheeled in, restrained to a wheelchair"
        scene batman-attorney
        harley "Please stay seated for DA Janet Van Dorn"
        janet "I'm gonna try my best"
        "Just give me time to figure things out"
        joker "Prosecuting atotrney make your opening statement"
        scene the trial2
        twoface "Today your honor we have a simple case, what does the world need with Batman."
        twoface "As I see it all of our lives were quiet and peaceful before he came along."
        twoface "So let me ask jury why should he still be ali-"
        scene batman-attorney2
        janet "OJECTION!"
        janet "Your honor that is a leading statement! He can't be allowed to state that."
        scene judge joker2
        joker "Sustained."
        scene the trial2
        twoface "I rest my opening argument, \"Two-Face whispers under his breath\" lousy bitch."
        scene judge joker2
        joker "And what is the defendants opening statement"
        scene attorney-joker
        janet "You see your honor, the way I see it, Batman is nothing more than a person."
        janet "Everyone is ordained with their own free will, and everyone has made their own choices. I rest my opening statement."
        scene judge joker2
        joker "How moving, Dent, would you like to call up your first witness."
        scene the trial2
        twoface "Yes, I would like to call Harley Quinn up to the stand."
        joker "The prosecution calls the beautiful Harley Quinn to the stand."
        scene harley-stand
        harley "Hi Pudden."
        twoface "Harley, let me ask you, what were you before Batman."
        harley "I was a Psychiatrist with a PhD."
        twoface "And what are you after Batman"
        harley "I am in love with puddin"
        "Harley blows a kiss to Joker"
        harley "I also like to kill from time to time."
        twoface "That will be all from me."
        "The jury nods in agreement, noting the effect Batman had on her."
        joker "Who would the prosecuting attorney like to call."
        scene harley-stand2
        janet "I would like to continue questioning Harley."
        janet "So Harley, let me ask you this, how did you become Harley Quinn?"
        harley "Well you see, I was treating him, when his dashing looks jsut persuaded me into loving him."
        janet "So you are saying Joker, turned you into Harley."
        harley "I suppose so."
        janet "So you let a psychopathic killer, convince you to leave your life as a PhD psychiatrist to pursue a life of crime?"
        harley "Well I wouldn't put it so bluntly but I guess so."
        janet "That'll be all."
        scene batman-attorney
        janet "\"Whispering to Batman\" I hope we can win this."
        batman "We just need a little more time."
        scene judge joker2
        joker "And who would the prosecution like to bring up as their next witness."
        scene the trial2
        twoface "I would like to bring up Pamela Isley up to the stand."
        "Poison Ivy, walks up to the stand."
        twoface "So Ivy, how did you come to be in here?"
        ivy "Well you see, I was a simple botonist that was working on my passion project, when Batman came and tried to stop me."
        twoface "So you are saying Batman led you to attck him?"
        scene batman-attorney2
        janet "Objection, your honor another leading question."
        scene judge joker2
        joker "Overruled."
        scene the trial2
        twoface "Now why don't you shut up before you steal another, thing from me."
        twoface "So Ivy, you were a plain gardner who was attacked by Batman."
        ivy "Yes."
        twoface "I am satisfied."
        scene arkahm-jury
        "The jury board nods in approval."
        joker "Defending, and you?"
        scene judge joker2
        janet "I would like to continue question miss Isley."
        scene poision ivy-stand
        janet "So Miss Isley what were you doing with this passion project."
        ivy "Well I was using certain roses to create a serum to poison well Mr. Dent"
        "Ivy looks down in approval"
        janet "So you chose to make this serum and continue this research."
        ivy "Well yes."
        janet "So why might I ask di you attack Batman?"
        ivy "Well he was stopping my research!"
        janet "Or maybe he was helping you."
        janet "You see, you have an unhealhty attachment to plants, possibly more than humans."
        ivy "Plants are plants, I have no special attachemnt to them."
        janet "So say I were to take this dead flower off Joker's lapel, already snipped and dead."
        "Ivy begins to look squeamish."
        janet "So you wouldn't care If I were to pluck pedals off."
        "Janet Van Dorn, begins to pluck the pedals off one by one"
        "Ivy begins to squirm in her chair."
        janet "Does this make you uncomfortable."
        scene poision ivy angry
        "Ivy leaps out yelling"
        "I'LL KILL YOU!!"
        "Ivy is restrained and taken back."
        scene batman-attorney2
        janet "You see jury, Ivy chooses to value plant life over human, she chose this life, Batman mearly tried to stop her."
        scene arkahm-jury
        "The jury looks in approval."
        scene judge joker
        joker "Would either the prosecution or the defendant like to bring any more witnesses to the stand."
        twoface "No"
        janet "No"
        joker "Well then, give your closiong arguments."
        "Two-face saunters to the stand."
        scene twoface-closing-argument
        twoface "It is quite clear what the Jury must decide, the only reason any of you all are in here is becausse of Batman."
        twoface "If Batman did not exist, you all would not be in here."
        twoface "I rest my case."
        scene arkahm jury angry
        "The jury begins to look angrily at Batman."
        scene batman-attorney2
        janet "I see this as a simple case of free will."
        janet "You all were villians prior to Batman, look at Harley, the only reason she is in this mess is because of Joker."
        janet "All of you made the consious choice to do this."
        janet "I rest my case."
        scene judge joker
        joker "Well then, let the jury decide."
        scene arkahm-jury
        "The jury deliberates"
        scene batman-attorney
        janet "I did my best I hope we can win."
        batman "Don't worry we just need a few minutes."
        scene arkahm-jury
        "After about five minutes, the jury came back."
        hatter "We find the defendent..."
        "..."
        "..."
        hatter "Not gulity"
        scene batman-attorney
        janet "Oh my god I did it."
        scene twoface-accusatory
        twoface "This is complete bullshit, I should've won."
        scene judge joker2
        joker "Order order order."
        joker "It seems that we have a verdict, and because of that I vot-"
        "Just in that moment, the GCPD bust in"
        scene the trial2
        gordon "Freeze, everyone put your hands up"
        joker "Well it seems the game is over."
        joker "It was fun while it lasted."
        janet "Batman how did they finds us."
        batman "The GCPD were gonna meet me before, and when I didnt show they mustve knew something was up."
        batman "I have a tracker in my suit."
        scene batman-attorney2
        janet "Thank you Batman."
        batman "Thank you DA."
        scene end card
        "ENDING 16/17"
        return

    label twoface_scene_10:
        scene judge joker
        batman "I choose to represent myself."
        joker "So be it"
        joker "Alright make your opening statements."
        scene the trial2
        twoface "You see, your lives were perfect befor Batman."
        twoface "You are only in here because of Batman."
        twoface "So let me ask you, why does Batman have to live."
        twoface "I am satisfied."
        scene batman-straightjacket2
        batman "Let me ask you this, I am only trying to help you."
        scene judge joker
        joker "By locking us up in an asylum that abuses us."
        joker "Frankly there was no helping us from the beginning."
        scene joker scary
        joker "Get him."
        "Joker says stearrner than he ever has."
        scene batman-straightjacket2
        "As Batman redies himself for what comes next. all of his rogues gallery rise up to kill him."
        scene arkahm outside
        "Hours pass by as the GCPD finally show up"
        "As they walk through the decrepit halls, they notice that everything is in order."
        gordon "Strange, what could have happened."
        "As they continue walking through the terrifiny gothic cell structure they come upon an unholy sight."
        gordon "My god..."
        "A unholy sight upon all."
        "Batman is strung up by his wrists and ankles, with his rib cage seperated and pulled out to display some sort of wings."
        "What have they done."
        "Joker from his sell"
        joker "Oh boo hoo, is little gordon's friend dead, well lets hope the rain takes the Bat away."
        "Joker laughs wildly, as the GCPD take in the horror before them."
        "How could anyone do sutch a thing."
        scene end card
        "ENDING 17/17"
        return