import os

# minecraft damage calculator made by splars#1252 for helix souppvp

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout -1 >nul" if os.name == "nt" else time.sleep(5))
os.system("title Helix Minecraft Damage Calculator" if os.name == "nt" else "pass")
os.system("color c" if os.name == "nt" else "pass")
cls()

swords = {
    "NETHERITE_SWORD": 9,
    "DIAMOND_SWORD": 8,
    "IRON_SWORD": 7,
    "STONE_SWORD": 6,
    "GOLD_SWORD": 5,
    "WOOD_SWORD": 5
}

armour = {
    "NETHERITE_HELMET": 5,
    "NETHERITE_CHESTPLATE": 9,
    "NETHERITE_LEGGINGS": 7,
    "NETHERITE_BOOTS": 4,

    "DIAMOND_HELMET": 3,
    "DIAMOND_CHESTPLATE": 8,
    "DIAMOND_LEGGINGS": 6,
    "DIAMOND_BOOTS": 3,

    "IRON_HELMET": 2,
    "IRON_CHESTPLATE": 6,
    "IRON_LEGGINGS": 5,
    "IRON_BOOTS": 2,

    "CHAINMAIL_HELMET": 2,
    "CHAINMAIL_CHESTPLATE": 5,
    "CHAINMAIL_LEGGINGS": 4,
    "CHAINMAIL_BOOTS": 1,

    "GOLD_HELMET": 2,
    "GOLD_CHESTPLATE": 5,
    "GOLD_LEGGINGS": 3,
    "GOLD_BOOTS": 1,

    "LEATHER_HELMET": 1,
    "LEATHER_CHESTPLATE": 3,
    "LEATHER_LEGGINGS": 2,
    "LEATHER_BOOTS": 1,
}

effects = {
    "vanilla": {
        "strength": 1.3,
        "weakness": -0.5
    },

    "helix": {
        "strength": 0.8,
        "weakness": -1.0
    }
}

# default settings
maxhp = 20
hp = 20
sword = swords["IRON_SWORD"]
helmet = armour["IRON_HELMET"]
chestplate = armour["IRON_CHESTPLATE"]
leggings = armour["IRON_LEGGINGS"]
boots = armour["IRON_BOOTS"]
strength = 0
weakness = 0
sharpness = 0
formula = effects["helix"]
hits = 1
prot_helmet = 0
prot_chestplate = 0
prot_leggings = 0
prot_boots = 0
seconds = 1
LAST = 0

def main():
    global maxhp, hp, sword, helmet, chestplate, leggings, boots, strength, weakness, sharpness, formula, hits, prot_helmet, prot_chestplate, prot_leggings, prot_boots, LAST, seconds
    AR = helmet + chestplate + leggings + boots
    PROT = prot_helmet + prot_chestplate + prot_leggings + prot_boots

    print(f"Max Health: {round(maxhp, 2)}")
    print(f"Health: {round(hp, 2)}")
    print(f"Missing health: {round(maxhp, 2)-round(hp, 2)}\n")

    if sharpness > 0:
        print(f"Sword: {sword} | Sharpness level: {sharpness}")
    else:
        print(f"Sword: {sword}")
    print(f"Helmet: {helmet}")
    print(f"Chestplate: {chestplate}")
    print(f"Leggings: {leggings}")
    print(f"Boots: {boots}")
    print(f"Total AR: {AR}")
    print(f"Total PROT: {PROT}")
    if formula == effects["vanilla"]:
        print("Formula: Vanilla Calculations")
    elif formula == effects["helix"]:
        print("Formula: Helix Calculations")
    print(f"Strength level: {strength}")
    print(f"Weakness level: {weakness}")
    print(f"Hits: {hits}")
    print(f"Damage: {LAST} | Seconds: {seconds} | DPS: {LAST / seconds}\n")

    print("Type help to display available commands.\n")
    try:
        choice = input(">> ").lower()
        if choice == "help":
            print("help : Shows available commands.")
            print("reset : Restore all options to DEFAULT.")
            print("armour : Displays available armour.")
            print("swords : Displays available swords.")
            print("effects : Displays available effects.")
            print("resethp / reset hp : Sets current health to maximum health.")
            print("hp : Display current Health.")
            print("set : Change variables and options.")
            print("start : Starts the process.")

        if choice == "reset":
            maxhp = 20
            hp = 20
            sword = 7
            helmet = 2
            chestplate = 6
            leggings = 5
            boots = 2
            strength = 0
            weakness = 0
            sharpness = 0
            formula = effects["helix"]
            hits = 1
            prot_helmet = 0
            prot_chestplate = 0
            prot_leggings = 0
            prot_boots = 0
            LAST = 0
            seconds = 1
            print(f"Successfully reset stats to DEFAULT.")

        if choice == "armour":
            print(f"{armour}")

        if choice == "swords":
            print(f"{swords}")

        if choice == "effects":
            print(f"{effects}")

        if choice == "hp":
            print(f"Health: {round(hp, 2)}/{round(maxhp, 2)}")
        
        if choice == "resethp" or choice == "reset hp":
            hp = maxhp
            print(f"Successfully set health to {round(hp, 2)}.")

        if choice == "set":
            print("Armour: set full iron | set boots diamond | set naked / set full naked")
            print("Sword: set sword stone | set sword air")
            print("Health: set hp | set maxhp")
            print("Protection: set prot chestplate | set full prot 4")
            print("Sharpness: set sharpness | set sharpness 3 | set sharpness 0")
            print("Effects: set effect strength | set effect weakness 2 | set effect strength 0 | set effect clear")
            print("Other: set hits | set formula | set formula VANILLA/HELIX | set seconds (USED FOR CALCULATING DPS)")


        # set health options
        if choice == "set hp":
            hp = float(input("Set health: "))
            if hp > maxhp:
                maxhp = hp
            print(f"Successfully set health to {round(hp, 2)}.")

        if choice == "set maxhp":
            hp = float(input("Set maximum health: "))
            print(f"Successfully set maximum health to {round(maxhp, 2)}.")


        # set hits options
        if choice == "set hits":
            hits = int(input("Set amount of hits that will be simulated: "))
            print(f"Successfully set hits to {hits}")


        # set formula options
        if choice == "set formula":
            print("Choose between the Vanilla Formula or the Helix Formula.")
            choice = input("V / H: ").lower()

            if choice == "v" or choice == "vanilla":
                formula = effects["vanilla"]
                print("Successfully set formula to Vanilla Calculations.")

            elif choice == "h" or choice == "helix":
                formula = effects["helix"]
                print("Successfully set formula to Helix Calculations.")

        if choice == "set formula vanilla":
            formula = effects["vanilla"]
            print("Successfully set formula to Vanilla Calculations.")

        if choice == "set formula helix":
            formula = effects["helix"]
            print("Successfully set formula to Helix Calculations.")


        # set sword options
        if choice == "set sword diamond":
            sword = swords["DIAMOND_SWORD"]
            print("Successfully set sword to DIAMOND_SWORD.")

        if choice == "set sword iron":
            sword = swords["IRON_SWORD"]
            print("Successfully set sword to IRON_SWORD.")

        if choice == "set sword stone":
            sword = swords["STONE_SWORD"]
            print("Successfully set sword to STONE_SWORD.")

        if choice == "set sword gold":
            sword = swords["GOLD_SWORD"]
            print("Successfully set sword to GOLD_SWORD.")

        if choice == "set sword wood":
            sword = swords["WOOD_SWORD"]
            print("Successfully set sword to WOOD_SWORD.")

        if choice == "set sword air":
            sword = 1
            print("Successfully set sword to barefist.")


        # set sharpness options
        if choice == "set sharpness":
            sharpness = int(input("Set Sharpness on Sword: "))
            print(f"Successfully set sharpness {sharpness} on Sword.")

        if choice == "set sharpness 0":
            sharpness = 0
            print(f"Successfully cleared sharpness on Sword.")

        if choice == "set sharpness 1":
            sharpness = 1
            print(f"Successfully set sharpness {sharpness} on Sword.")

        if choice == "set sharpness 2":
            sharpness = 2
            print(f"Successfully set sharpness {sharpness} on Sword.")

        if choice == "set sharpness 3":
            sharpness = 3
            print(f"Successfully set sharpness {sharpness} on Sword.")

        if choice == "set sharpness 4":
            sharpness = 4
            print(f"Successfully set sharpness {sharpness} on Sword.")

        if choice == "set sharpness 5":
            sharpness = 5
            print(f"Successfully set sharpness {sharpness} on Sword.")


        # set effects options
        if choice == "set effect strength":
            strength = int(input("Set strength level: "))
            print(f"Successfully set strength level to {strength}.")

        if choice == "set effect weakness":
            weakness = int(input("Set weakness level: "))
            print(f"Successfully set weakness level to {weakness}.")

        if choice == "set effect clear" or choice == "set effects clear":
            strength = 0
            weakness = 0
            print(f"Successfully cleared strength and weakness.")

        if choice == "set effect strength 0":
            strength = 0
            print(f"Successfully set strength level to 0.")

        if choice == "set effect strength 1":
            strength = 1
            print(f"Successfully set strength level to 1.")

        if choice == "set effect strength 2":
            strength = 2
            print(f"Successfully set strength level to 2.")

        if choice == "set effect weakness 0":
            weakness = 0
            print(f"Successfully set weakness level to 0.")

        if choice == "set effect weakness 1":
            weakness = 1
            print(f"Successfully set weakness level to 1.")

        if choice == "set effect weakness 2":
            weakness = 2
            print(f"Successfully set weakness level to 2.")


        # set prot options
        if choice == "set prot helmet":
            prot_helmet = int(input("Set Protection on Helmet: "))
            print(f"Successfully set protection {prot_helmet} on Helmet.")

        if choice == "set prot chestplate":
            prot_chestplate = int(input("Set Protection on Chestplate: "))
            print(f"Successfully set protection {prot_chestplate} on Chestplate.")

        if choice == "set prot leggings":
            prot_leggings = int(input("Set Protection on Leggings: "))
            print(f"Successfully set protection {prot_leggings} on Leggings.")

        if choice == "set prot boots":
            prot_boots = int(input("Set Protection on Boots: "))
            print(f"Successfully set protection {prot_boots} on Helmet.")

        if choice == "set full prot 0":
            prot_helmet = 0
            prot_chestplate = 0
            prot_leggings = 0
            prot_boots = 0
            print("Successfully cleared protection on all armour.")

        if choice == "set full prot 1":
            prot_helmet = 1
            prot_chestplate = 1
            prot_leggings = 1
            prot_boots = 1
            print("Successfully set all armour to protection 1.")

        if choice == "set full prot 2":
            prot_helmet = 2
            prot_chestplate = 2
            prot_leggings = 2
            prot_boots = 2
            print("Successfully set all armour to protection 2.")

        if choice == "set full prot 3":
            prot_helmet = 3
            prot_chestplate = 3
            prot_leggings = 3
            prot_boots = 3
            print("Successfully set all armour to protection 3.")

        if choice == "set full prot 4":
            prot_helmet = 4
            prot_chestplate = 4
            prot_leggings = 4
            prot_boots = 4
            print("Successfully set all armour to protection 4.")


        # set armour options
        if choice == "set full diamond":
            helmet = armour["DIAMOND_HELMET"]
            chestplate = armour["DIAMOND_CHESTPLATE"]
            leggings = armour["DIAMOND_LEGGINGS"]
            boots = armour["DIAMOND_BOOTS"]
            print("Successfully set all armour to Diamond.")

        if choice == "set full iron":
            helmet = armour["IRON_HELMET"]
            chestplate = armour["IRON_CHESTPLATE"]
            leggings = armour["IRON_LEGGINGS"]
            boots = armour["IRON_BOOTS"]
            print("Successfully set all armour to Iron.")

        if choice == "set full chainmail":
            helmet = armour["CHAINMAIL_HELMET"]
            chestplate = armour["CHAINMAIL_CHESTPLATE"]
            leggings = armour["CHAINMAIL_LEGGINGS"]
            boots = armour["CHAINMAIL_BOOTS"]
            print("Successfully set all armour to Chainmail.")

        if choice == "set full gold":
            helmet = armour["GOLD_HELMET"]
            chestplate = armour["GOLD_CHESTPLATE"]
            leggings = armour["GOLD_LEGGINGS"]
            boots = armour["GOLD_BOOTS"]
            print("Successfully set all armour to Gold.")

        if choice == "set full leather":
            helmet = armour["LEATHER_HELMET"]
            chestplate = armour["LEATHER_CHESTPLATE"]
            leggings = armour["LEATHER_LEGGINGS"]
            boots = armour["LEATHER_BOOTS"]
            print("Successfully set all armour to Leather.")

        if choice == "set naked" or choice == "set full naked":
            helmet = 0
            chestplate = 0
            leggings = 0
            boots = 0
            print("Successfully set all armour to air.")


        # set armour specific options
        if choice == "set helmet diamond":
            helmet = armour["DIAMOND_HELMET"]
            print("Successfully set Helmet to DIAMOND_HELMET.")

        if choice == "set helmet iron":
            helmet = armour["IRON_HELMET"]
            print("Successfully set Helmet to IRON_HELMET.")

        if choice == "set helmet chainmail":
            helmet = armour["CHAINMAIL_HELMET"]
            print("Successfully set Helmet to CHAINMAIL_HELMET.")

        if choice == "set helmet gold":
            helmet = armour["GOLD_HELMET"]
            print("Successfully set Helmet to GOLD_HELMET.")

        if choice == "set helmet leather":
            helmet = armour["LEATHER_HELMET"]
            print("Successfully set Helmet to LEATHER_HELMET.")


        if choice == "set chestplate diamond":
            chestplate = armour["DIAMOND_CHESTPLATE"]
            print("Successfully set Chestplate to DIAMOND_CHESTPLATE.")

        if choice == "set chestplate iron":
            chestplate = armour["IRON_CHESTPLATE"]
            print("Successfully set Chestplate to IRON_CHESTPLATE.")

        if choice == "set chestplate chainmail":
            chestplate = armour["CHAINMAIL_CHESTPLATE"]
            print("Successfully set Chestplate to CHAINMAIL_CHESTPLATE.")

        if choice == "set chestplate gold":
            chestplate = armour["GOLD_CHESTPLATE"]
            print("Successfully set Chestplate to GOLD_CHESTPLATE.")

        if choice == "set chestplate leather":
            chestplate = armour["LEATHER_CHESTPLATE"]
            print("Successfully set Chestplate to LEATHER_CHESTPLATE.")


        if choice == "set leggings diamond":
            leggings = armour["DIAMOND_LEGGINGS"]
            print("Successfully set Leggings to DIAMOND_LEGGINGS.")

        if choice == "set leggings iron":
            leggings = armour["IRON_LEGGINGS"]
            print("Successfully set Leggings to IRON_LEGGINGS.")

        if choice == "set leggings chainmail":
            leggings = armour["CHAINMAIL_LEGGINGS"]
            print("Successfully set Leggings to CHAINMAIL_LEGGINGS.")

        if choice == "set leggings gold":
            leggings = armour["GOLD_LEGGINGS"]
            print("Successfully set Leggings to GOLD_LEGGINGS.")

        if choice == "set leggings leather":
            leggings = armour["LEATHER_LEGGINGS"]
            print("Successfully set Leggings to LEATHER_LEGGINGS.")


        if choice == "set boots diamond":
            boots = armour["DIAMOND_BOOTS"]
            print("Successfully set Boots to DIAMOND_BOOTS.")

        if choice == "set boots iron":
            boots = armour["IRON_BOOTS"]
            print("Successfully set Boots to IRON_BOOTS.")

        if choice == "set boots chainmail":
            boots = armour["CHAINMAIL_BOOTS"]
            print("Successfully set Boots to CHAINMAIL_BOOTS.")

        if choice == "set boots gold":
            boots = armour["GOLD_BOOTS"]
            print("Successfully set Boots to GOLD_BOOTS.")

        if choice == "set boots leather":
            boots = armour["LEATHER_BOOTS"]
            print("Successfully set Boots to LEATHER_BOOTS.")


        # set seconds options
        if choice == "set seconds":
            seconds = float(input("Set seconds: "))
            print(f"Successfully set seconds to {seconds}.")

        # start the simulation process
        if choice == "start":
            if formula == effects["vanilla"]:
                damage = sword
                if strength > 0:
                    damage = damage + sword * formula["strength"] * strength
                if weakness > 0:
                    damage = damage - formula["weakness"] * weakness
                if sharpness > 0:
                    damage = damage + 1.25 * sharpness

            elif formula == effects["helix"]:
                damage = sword
                if strength > 0:
                    damage = damage + sword * formula["strength"] * strength
                if weakness > 0:
                    damage = damage - -formula["weakness"] * weakness
                if sharpness > 0:
                    damage = damage + 1.25 * sharpness

            pre = damage * hits
            post = damage * (1-AR*4/100) * (1-PROT*4/100) * hits
            hp -= round(post, 2)
            LAST = round(post, 2)
            print(f"Damage pre-mitigation: {round(pre, 2)}")
            print(f"Damage post-mitigation: {round(post, 2)}")

    except:
        print("\nError in parameters, please report to splars#1252")
    sleep()
    cls()
    main()

main()