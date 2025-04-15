# script.rpy

define asel = Character("Asel", color="#ffffff")  
define emir = Character("Emir", color="#ffffff")
define adil = Character("Adil", color="#ffffff")
define landlord = Character("Landlord", color="#ffffff")
define mother = Character("Mother", color="#ffffff")
define adilmom = Character("Adil's mother", color="#ffffff")
define nurgul = Character("Nurgul", color="#ffffff")
define gul = Character("Gul", color="#ffffff")
define samira = Character("Samira", color="#ffffff")
define police1 = Character("Police 1", color="#ffffff")
define police2 = Character("Police 2", color="#ffffff")
define friend1 = Character("Friend 1", color="#ffffff")
define friend2 = Character("Friend 2", color="#ffffff")
define uncle = Character("Uncle", color="#ffffff")
define father = Character("Father", color="#ffffff")
define attacker = Character("Attacker", color="#ffffff")

label start:

    # Set background to black
    scene black with fade

    # Show text with typewriter effect (speed controlled by window size)
    window hide
    window show

    "Ala Kachuu: Gran & Run."
    "Ala Kachuu, the most common marriage custom in Kyrgyzstan, literally means 'grab and run.' In English, it translates to 'bride kidnapping.'"
    "Bride kidnapping is divided into 'real kidnapping' and 'fake kidnapping.' 'Real kidnapping' refers to a practice in conservative Islamic societies where a couple, already in love, arranges for the groom’s side to abduct the bride and stage a forced marriage. In contrast, 'fake kidnapping' refers to the actual abduction of a woman, where methods such as threats and violence are used to force her into marriage."

    # Move to the next label or end (if it's the end of the intro)
    jump episode_1


label episode_1:
    # Introduction
    scene bg room with fade
    asel "Hi, let me introduce myself."
    asel "My name is Asel. I live with my mother on the outskirts of Bishkek, the capital of Kyrgyzstan. I’m nineteen, and I work as a nurse at a hospital in the city."
    asel "Well, and also..."

    # Landlord knocks
    scene bg living_room with fade
    landlord "Is anyone there?"
    asel "Ugh..."
    mother "The landlord’s here. Not surprising... The rent’s been overdue for a few months."

    player "Yes, I’m coming!" (exits the screen)

    # Argument with landlord
    landlord "I’ve been patient because of Nazira’s face, but if the rent’s not paid this month, things will get serious. We’re not exactly well off either."
    asel "I’m really, really sorry. But my paycheck will come in three days, and I’ll pay as soon as I can."
    landlord "You’d better!"

    mother "Sigh... There’s nothing we can do, Asel. I’m sorry for putting all this on you."
    asel "It’s fine." 

    asel "Actually… there’s something I haven’t told you, Mother, but I’m worried about something."

    # Choice 1: What should Asel say?
    menu:
        "What’s going on?":
            asel "For the past few days, I’ve been feeling like someone’s been following me after work... and on my way to work. It’s kind of scary."
        "I haven’t asked.":
            asel "Ah... it’s nothing. Just... someone might be stalking me. But it could be my imagination."
            asel "So, it’s nothing. I was just wondering whether I should go to work today or not."

    # Choice 2: What should Asel do?
    menu:
        "I need the money, so I should go to work.":
            asel "Yeah, I guess I have to, right?"
        "I feel uneasy. I should tell my family and friends just in case.":
            asel "Yeah, it’s probably safer that way."
        "I shouldn’t go to work today.":
            asel "Should I? I want to stay home... But if I don’t go, Mom and I will lose the house."

    # Adil knocks on the window
    scene bg window with fade
    sound "knock_knock.ogg"
    adil "Knock, knock."
    asel "Huh?!"
    adil "It’s me, Adil."
    asel "Adil!!"

    # Reveal Adil
    scene bg outside_window with fade
    adil "Hey, babe. How’ve you been?"
    asel "(looks sideways with a frown) Adil’s my boyfriend. We had a bit of a fight yesterday."

    # Choice 3: What should Asel do?
    menu:
        "Tell Adil everything.":
            adil "What? That doesn’t feel right... I have a bad feeling about this."
        "Tell him to get lost.":
            adil "Hey, why are you being like this? I already apologized!"
        "I don’t want to worry him. I’ll stay silent.":
            adil "…"

    # Scene transition to hospital
    scene bg hospital with fade
    asel "Phew, it’s finally over. Time to head home."

    # Scene transition to way home
    scene bg street_night with fade
    sound "van_approaching.ogg"
    attacker "That’s her! Grab her!"

    # The kidnapping scene
    scene bg street_night_van with fade
    ###  sound "struggling.ogg"
    attacker "Let’s go!"
    asel "Help! Somebody, please help!"
    friend1 "It’s okay, it’s okay."
    friend2 "Grab her legs. I’ll hold her arms."
    friend1 "Wow, she’s really strong."
    asel "Mom!!!! Help! Let me go!!!"
    uncle "It’s okay, sweetie. You’ll be happy. Just calm down."
    father "Yes, our son is a good man. You’ll be happy."
    friend1 "No, she’s crying because she’s happy. These are happy tears."
    friend2 "Yeah, when women get married, they cry because they’re happy. Come on, step on it!"

    # Choice 4: What should Asel do?
    menu:
        "Lie about having a boyfriend and losing her virginity to make them stop.":
            asel "I have a boyfriend! I’ve already lost my virginity!"
            friend1 "What? You’ve lost your virginity?"
            friend2 "You brought a whore as your bride."
            uncle1 "Calm down. She’s just lying because she wants to go back."
            friend1 "What if she really has lost her virginity? Emir will be furious."
            father "If that’s the case... I guess we’ll just have to deal with it. No need to send a gift to her parents. It’s already too late."
        "Resist as much as possible. Fight with all your might.":
            asel "Get off me, you bastards!!!"
            friend1 "Why are you struggling so much? Just stay still!"
            friend2 "Ouch! She scratched me!"
            asel "I’ll kill you! Let me go now!"
            friend1 "I told you to stay still!"
            window hide
            "friend1 beats Asel. friend1 breaks Asel’s arm."
            window show
            asel "Ugh... I feel dizzy..."
            window hide
            "Asel faints from pain."
            window show
            jump episode_2
        "Try to convince them that her family and boyfriend will find her and come to rescue her.":
            asel "Don’t you think my mom will come looking for me? Once she notices I’m gone, she’ll call the police! My boyfriend’s coming for me! It’s only a matter of time before they know I’m missing. And my family won’t let you get away with this."
            friend1 "But once your boyfriend and family know, you’ll already have lost your virginity."
            asel "I don’t care. This is illegal."
            friend2 "You’re hilarious. Who would want a woman who’s lost her virginity? Do you think we’re criminals? This is a celebrated traditional marriage!"
            uncle "Yes, this is a proud tradition passed down through our bloodline."
        "Stay calm, because they might have weapons.":
            friend1 "Okay, I see you’re accepting your fate. You’ll be happy."
            friend2 "Yeah, who would want a woman who’s lost her virginity? Do you think we’re criminals? This is a celebrated traditional marriage!"
            uncle "Yes, this is a proud tradition passed down through our bloodline."

    jump episode_2


label episode_2:

    # Episode 2: Persuasion
    # Scene transition. Change of player character: Asel -> Emir

    with hide
        "Episode 2. The Persuation"
        "Now is the story of the Groom, Emir."
        "One month ago. Emir's house."
    with fade

    scene bg_house with fade
        gul "Emir, it's about time you get married, don't you think?"
        father "Yes, Emir. You should get married now. I'll find a good match for you."

        # Choice 5: What should Emir say?
        menu:
            "I have a girlfriend.":
                father "Is it that damn ex-wife of yours? With a kid too? Absolutely not. You have to carry on the family line."
            "I don't want to get married yet.":
                father "Well, you don't have a choice."
            "I don't have anyone I love yet.":
                father "That's not a problem. The adults will take care of it."
            "Alright.":
                father "Good decision."

        father "So, where should we find the bride?"
        gul "We can do it the way we did when we were young."
        father "You mean Ala Kachuu?"
        gul "Exactly. It's the safest way, especially when choosing a virgin."

    # Scene transition. [One week later.]
    scene bg_village_hospital with fade
        with hide
            "One week later"
        with fade

        uncle "I found a good girl at the hospital in the next village. Let's take her."

    # Scene transition. [Morning of the wedding day]
    scene bg_wedding_day with fade
        with hide
            "Another week has passed."
            "Now is the morning of the wedding day."
        with fade

        father "Well then, I'm off. You take the driver’s role… When the car stops, quickly get her into the car and bring her inside."
        uncle "God, please help us."

        # Choice 6: What should I say?
        menu:
            "This seems wrong. Let’s reconsider.":
                uncle "Hahaha!"
            "I really don't need to get married.":
                uncle "Hahaha!"
            "I actually have someone hidden!":
                uncle "… I knew it."
            "Don’t hit me too hard if she refuses.":
                uncle "Hahaha!"
            "I’m really looking forward to this.":
                uncle "Hahaha!"

        uncle "Wait here! I'll bring the bride back when I return."

    # Scene transition. [Present day.]
    scene bg_house with fade

        "Now, back to the present. Emir's family arrives back to their house. The house is full of vibe of celebration. The only one crying and screaming is Asel, the supposed-to-be bride."
    
        father "Alright, get out! Take her straight to the house!"
        gul "They're here! They've arrived!"

        "The kidnappers pull Asel out of the car and take her inside. Inside, women – probably the bride’s family – are waiting. They hold a white veil, symbolizing 'acceptance of the marriage.'"

        asel "{i}If I wear that, it’s over for me.{/i}"

    # Scene transition. [Outside, in the yard.]
    scene bg_yard with fade

        with hide
            "Laughter and chatter can be heard from outside."
        with fade

        friend2 "Want to bet on how long this will take?"
        father "It’s all over now. Once that girl accepts our veil, and after spending the night with Emir, we’ll go to her parents’ house and apologize for taking their daughter."
        friend1 "But what if something goes wrong later? I heard they’re banning this by law now."
        uncle "Don't talk nonsense. No matter what the police say, they can't ignore our tradition."
        father "That’s right. Your mother did the same, and so did everyone else. It’s in our blood, our tradition."
        friend2 "Can’t we change the tradition?"
        father "No. There is no changing it."

    # Scene transition. [Inside Emir's house.]
    scene bg_house_interior with fade

        samira "This is how all marriages go. You're not special."

        # Choice 6-1: What should I do?
        menu:
            "Reject":
                asel "Please, let me go!"
            "Accept":
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                gul "That's enough! Darling, it’s time! Bring Emir here!"
                jump episode_3

        gul "Don't reject your fortune, child!"

        # Choice 6-2: What should I do?
        menu:
            "Reject":
                asel "No, no!"
            "Accept":
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                with hide
                "Asel collapses from exhaustion"
                with fade
                gul "That's enough! Darling, it’s time! Bring Emir here!"
                jump episode_3

        asel "I have a boyfriend!"
        gul "No, that’s not true. Put on the veil."
        nurgul "Calm down, dear. Don’t resist."
        samira "We wish for your happiness, dear. You’ll be happy now. Marriage is a woman’s greatest happiness."

        # Choice 6-3: What should I do?
        menu:
            "Reject":
                asel "Someone, please help me!"
            "Accept":
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                with hide
                "Asel collapses from exhaustion"
                with fade
                gul "That's enough! Darling, it’s time! Bring Emir here!"
                jump episode_3

        gul "Don’t resist! You won’t gain anything from this!"
        nurgul "You can’t go back now... Who would take a woman who spent the night at a man’s house?"
        samira "That’s right, you have no choice."

        # Choice 6-4: What should I do?
        menu:
            "Reject":
                asel "Someone, please help me!"
                asel "{i}I think it’s dawn now. Is it morning? Is my mom looking for me? I feel weaker…{/i}"
            "Accept":
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                with hide
                "Asel collapses from exhaustion"
                with fade
                gul "Never take it off!"
                samira "That’s enough! Darling, it’s time! Start the prayers now!"
                jump episode_3

        gul "Marriage is a woman’s happiness."
        nurgul "You won’t benefit from resisting."
        samira "Darling, all women go through this. You’re not special."

        # Choice 6-5: What should I do?
        menu:
            "Reject":
                asel "Someone, please help me!"
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                "Festive music fills the air, and the family starts reciting prayers. The family is joyfully celebrating the union of the couple."

            "Accept":
                asel "{i}My whole body hurts. It’s pointless to refuse anymore.{/i}"
                with hide
                "Asel collapses from exhaustion"
                with fade
                gul "Never take it off!"
                samira "That’s enough! Darling, it’s time! Start the prayers now!"
                jump episode_3


