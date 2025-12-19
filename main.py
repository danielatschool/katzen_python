import random
import time

print("🐱" * 20)
print("Willkommen zum Katzenpflege-Spiel!")
print("🐱" * 20)

# Katzen infos eingeben 
name = input("\nGib den Namen deiner Katze ein: ")
alter = int(input("Gib das Alter deiner Katze ein: "))
farbe = input("Gib die Farbe deiner Katze ein: ")
energie = 100
hunger = 0
glücklichkeit = 50

print(f"\n✨ Willkommen {name}! Du bist eine {farbe} Katze im Alter von {alter} Jahren!\n")
time.sleep(1)

def schnurren():
    """Katze schnurrt wenn sie glücklich ist"""
    laute = ["brrr...", "purr purr...", "prrrrrr!", "schnurrrr...", "mrrr mrrr"]
    print(f"🎵 {random.choice(laute)}")

def gebe_infos_aus():
    """Zeigt alle Informationen der Katze an"""
    print(f"\n{'='*40}")
    print(f"🐱 {name.upper()} - Status Report")
    print(f"{'='*40}")
    print(f"Alter: {alter} Jahre")
    print(f"Farbe: {farbe}")
    print(f"Glücklichkeit: {glücklichkeit}/100 {'😸' if glücklichkeit > 70 else '😼' if glücklichkeit > 40 else '😿'}")
    print(f"Energie: {energie}/100 {'⚡' if energie > 70 else '🔋' if energie > 30 else '😴'}")
    print(f"Hunger: {hunger}/100 {'🍗' if hunger > 70 else '🍖' if hunger > 40 else '😋'}")
    print(f"{'='*40}\n")

def fressen_geben():
    """Gibt der Katze Fressen"""
    global hunger, glücklichkeit, energie
    hunger = max(0, hunger - 30)
    glücklichkeit += 10
    energie += 5
    print(f"🍖 {name} frisst lecker! Hunger gesenkt, Glücklichkeit erhöht!")
    if glücklichkeit > 85:
        schnurren()

def streicheln():
    """Katze streicheln"""
    global glücklichkeit, energie
    glücklichkeit += 20
    energie -= 5
    print(f"🤚 Du streichelst {name} sanft...")
    schnurren()

def spielen():
    """Mit der Katze spielen"""
    global glücklichkeit, energie, hunger
    glücklichkeit += 25
    energie -= 20
    hunger += 15
    print(f"🎾 {name} springt herum und spielt mit dir!")
    print(f"Wow! {name} hat einen Salto gemacht!")

def schlafen():
    """Katze schlafen legen"""
    global energie, glücklichkeit
    energie = min(100, energie + 40)
    glücklichkeit += 5
    print(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")
    time.sleep(1)
    print(f"💤 zzzzzz...")

def trainieren():
    """Mit Katze trainieren"""
    global energie, glücklichkeit, alter
    if energie < 20:
        print(f"😴 {name} ist zu müde zum Trainieren!")
        return
    energie -= 25
    glücklichkeit += 15
    print(f"🏃 {name} trainiert und springt umher!")
    print(f"Gut gemacht!")

def baden():
    """Katze baden"""
    global glücklichkeit, energie
    glücklichkeit -= 15
    energie -= 10
    print(f"🚿 Du versuchst {name} zu baden...")
    print(f"MIAAAAUU! 😾")
    print(f"{name} ist NICHT begeistert!")

def zaehne_putzen():
    """Zähne der Katze putzen"""
    global glücklichkeit, energie
    glücklichkeit -= 10
    energie -= 5
    print(f"🪥 Du putzt {name} die Zähne...")
    print(f"Mrrrow! 😾 {name} möchte das nicht!")

def zum_tierarzt():
    """Zum Tierarzt gehen"""
    global energie, glücklichkeit, hunger
    print(f"🏥 Ihr besucht den Tierarzt...")
    time.sleep(1)
    print(f"Der Tierarzt untersucht {name}...")
    time.sleep(1)
    energiewert = random.randint(10, 30)
    print(f"✅ {name} ist gesund! Erhalte {energiewert} Energie!")
    energie = min(100, energie + energiewert)
    glücklichkeit -= 5

def spielzeug_kaufen():
    """Neues Spielzeug kaufen"""
    global glücklichkeit, energie
    glücklichkeit += 30
    print(f"🧸 Du kaufst ein neues Spielzeug für {name}!")
    print(f"{name} ist begeistert und spielt damit!")
    schnurren()

def zeit_verstreichen():
    """Zeit verstreicht - alles verschlechtert sich"""
    global energie, hunger, glücklichkeit
    energie -= 8
    hunger += 10
    glücklichkeit -= 3
    print(f"\n⏰ Zeit verstreicht...")
    print(f"   Energie -8, Hunger +10, Glücklichkeit -3")

# Hauptspielschleife
def hauptspiel():
    global energie, hunger, glücklichkeit
    
    runde = 0
    while True:
        runde += 1
        
        # Statusleisten anzeigen
        print(f"\n{'='*50}")
        print(f"🎮 RUNDE {runde} - Status von {name}")
        print(f"{'='*50}")
        print(f"😊 Glücklichkeit: {'█' * (glücklichkeit // 10)}{'░' * (10 - glücklichkeit // 10)} {glücklichkeit}%")
        print(f"⚡ Energie:       {'█' * (energie // 10)}{'░' * (10 - energie // 10)} {energie}%")
        print(f"🍖 Hunger:        {'█' * (hunger // 10)}{'░' * (10 - hunger // 10)} {hunger}%")
        print(f"{'='*50}\n")
        
        # Überprüfung auf Spielende
        if energie <= 0:
            print(f"😴 {name} ist völlig erschöpft... GAME OVER!")
            break
        if hunger >= 100:
            print(f"🍗 {name} verhungert... GAME OVER!")
            break
        if glücklichkeit <= 0:
            print(f"😿 {name} ist viel zu traurig... GAME OVER!")
            break
        if glücklichkeit >= 100:
            print(f"😻 {name} ist überglücklich! DU HAST GEWONNEN! 🎉")
            break
        
        # Menü anzeigen
        print("💫 Was möchtest du mit deiner Katze tun?")
        print("────────────────────────────────────────")
        print("1. 🍖 Fressen geben")
        print("2. 🤚 Streicheln")
        print("3. 🎾 Spielen")
        print("4. 😴 Schlafen")
        print("5. 🏃 Trainieren")
        print("6. 🚿 Baden")
        print("7. 🪥 Zähne putzen")
        print("8. 🏥 Zum Tierarzt")
        print("9. 🧸 Spielzeug kaufen")
        print("10. ℹ️  Infos anzeigen")
        print("11. ❌ Spiel beenden")
        print("────────────────────────────────────────")
        
        wahl = input("Deine Wahl (1-11): ").strip()
        
        if wahl == "1":
            fressen_geben()
        elif wahl == "2":
            streicheln()
        elif wahl == "3":
            spielen()
        elif wahl == "4":
            schlafen()
        elif wahl == "5":
            trainieren()
        elif wahl == "6":
            baden()
        elif wahl == "7":
            zaehne_putzen()
        elif wahl == "8":
            zum_tierarzt()
        elif wahl == "9":
            spielzeug_kaufen()
        elif wahl == "10":
            gebe_infos_aus()
        elif wahl == "11":
            print(f"\n👋 {name} sagt: Auf Wiedersehen!")
            break
        else:
            print("❌ Ungültige Eingabe! Bitte wähle 1-11!")
            continue
        
        # Zeit verstreichen lassen
        zeit_verstreichen()
        
        time.sleep(0.5)

# Spiel starten
hauptspiel()