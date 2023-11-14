# damage calculator
minecraft damage calculator made by splars#1252 for helix souppvp documentation calculations</br>
check damage pre-mitigation and post-mitigation and depending variety of variables for kitpvp

    help:
        help : Shows available commands.
        reset : Restore all options to DEFAULT.
        armour : Displays available armour.
        swords : Displays available swords.
        effects : Displays available effects.
        resethp / reset hp : Sets current health to maximum health.
        hp : Display current Health.
        set : Change variables and options.
        start : Starts the process.

    set (help):
        Armour: set full iron | set boots diamond | set naked / set full naked
        Sword: set sword stone | set sword air
        Health: set hp | set maxhp
        Protection: set prot chestplate | set full prot 4
        Sharpness: set sharpness | set sharpness 3 | set sharpness 0
        Effects: set effect strength | set effect weakness 2 | set effect strength 0 | set effect clear
        Other: set hits | set formula | set formula VANILLA/HELIX | set seconds (USED FOR CALCULATING DPS)

    Armour:
        To set a specific armour piece, enter the specified piece and the type of armour: "set helmet diamond" | "set chestplate iron" | "set leggings chainmail" | "set boots gold"
        To set all of the armour pieces, enter full instead of a specified piece: "set full iron"
        To clear armour pieces, enter: "set naked" or "set full naked"

    Sword:
        To set a specific sword, enter the specified sword: "set sword stone"
        To clear the sword, enter: "set sword air"

    Health:
        To set current health, enter: "set hp"
        To set maximum health, enter: "set maxhp"

    Protection:
        To set custom protection on a specified armour piece, enter: "set prot chestplate"
        To set a specified protection level on all armour pieces, enter: "set full prot 1" | "set full prot 2" | "set full prot 3" | "set full prot 4"
        To clear protection on all armour pieces, enter: "set full prot 0"

    Sharpness:
        To set custom sharpness on the sword, enter: "set sharpness"
        To set a specified sharpness, enter: "set sharpness 1" | "set sharpness 2" | "set sharpness 3" | "set sharpness 4" | "set sharpness 5"
        To clear sharpness from the sword, enter: "set sharpness 0"

    Effects:
        To set an custom amount of effects, enter: "set effect strength" | "set effect weakness"
        To set a specified level of effects, enter: "set effect strength 1" | "set effect strength 2" | "set effect weakness 1" | "set effect weakness 2"
        To remove one effect, enter: "set effect strength 0" | "set effect weakness 0"
        To clear both effects, enter: "set effect clear" or "set effects clear"

    Hits:
        To set the amount of hits that will be simulated, enter: "set hits"

    Formula:
        To set the calculations formula, enter: "set formula" or "set formula vanilla" or "set formula helix"

    Seconds: (This is solely used for calculating DPS.)
        To set the amount of seconds the hits will simulated in, enter: "set seconds"
