import random
import time
from tkinter import messagebox, ttk

# Globale Variablen

name = ""from tkinter import simpledialog, messagebox, ttk

alter = 0

farbe = ""import tkinter as tkimport tkinter as tk

energie = 100

hunger = 0# Globale Variablen

glücklichkeit = 50

runde = name = ""from tkinter import simpledialog, messagebox, ttkfrom tkinter import simpledialog, messagebox, ttk



def schnurren():alter = 0

    """Katze schnurrt wenn sie glücklich ist"""

    laute = ["brrr...", "purr purr...", "prrrrrr!", "schnurrrr...", "mrrr mrrr"]farbe = ""

    return f"🎵 {random.choice(laute)}"

energie = 100

def gebe_infos_aus():

    """Zeigt alle Informationen der Katze an"""hunger = 0# Globale Variablen# Globale Variablen

    return f"""🐱 {name.upper()} - Status Report

════════════════════════════════════════glücklichkeit = 50

Alter: {alter} Jahre

Farbe: {farbe}runde = 0name = ""name = ""

Glücklichkeit: {glücklichkeit}/100

Energie: {energie}/100

Hunger: {hunger}/100

Runde: {runde}def schnurren():alter = 0alter = 0

════════════════════════════════════════"""

    """Katze schnurrt wenn sie glücklich ist"""

class KatzenSpiel:

    """Hauptspielklasse für das Katzenpflege-Spiel"""    laute = ["brrr...", "purr purr...", "prrrrrr!", "schnurrrr...", "mrrr mrrr"]farbe = ""farbe = ""

    def __init__(self, root):

        self.root = root    return f"🎵 {random.choice(laute)}"

        self.root.title("🐱 Katzenpflege-Spiel 🐱")

        self.root.geometry("900x700")energie = energie = 100

        self.root.configure(bg="#2c3e50")

        def gebe_infos_aus():

        # Titel

        titel = tk.Label(root, text="🐱 KATZENPFLEGE-SPIEL 🐱",     """Zeigt alle Informationen der Katze an"""hunger = hunger = 0

                        font=("Arial", 24, "bold"), 

                        bg="#2c3e50", fg="#ecf0f1")    return f"""🐱 {name.upper()} - Status Report

        titel.pack(pady=10)

        ════════════════════════════════════════glücklichkeit = 50glücklichkeit = 50

        # Frame für Katzenname

        info_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, bd=2)Alter: {alter} Jahre

        info_frame.pack(pady=10, padx=20, fill=tk.X)

        Farbe: {farbe}runde = 0runde = 0

        self.katze_label = tk.Label(info_frame, text="", 

                                   font=("Arial", 16, "bold"), Glücklichkeit: {glücklichkeit}/100

                                   bg="#34495e", fg="#f39c12")

        self.katze_label.pack(pady=5)Energie: {energie}/100

        

        # Frame für StatusleistenHunger: {hunger}/100

        status_frame = tk.Frame(root, bg="#34495e", relief=tk.SUNKEN, bd=2)

        status_frame.pack(pady=10, padx=20, fill=tk.X)Runde: {runde}def schnurren():def schnurren():

        

        # Glücklichkeit════════════════════════════════════════"""

        tk.Label(status_frame, text="😊 Glücklichkeit:", 

                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)    """Katze schnurrt wenn sie glücklich ist"""    """Katze schnurrt wenn sie glücklich ist"""

        self.glucklichkeit_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

                                                 maximum=100, value=50)# Hauptspielklasse

        self.glucklichkeit_bar.pack(padx=10, pady=2, fill=tk.X)

        self.glucklichkeit_label = tk.Label(status_frame, text="50%", class KatzenSpiel:    laute = ["brrr...", "purr purr...", "prrrrrr!", "schnurrrr...", "mrrr mrrr"]    laute = ["brrr...", "purr purr...", "prrrrrr!", "schnurrrr...", "mrrr mrrr"]

                                           bg="#34495e", fg="#ecf0f1")

        self.glucklichkeit_label.pack(anchor=tk.E, padx=10)    def __init__(self, root):

        

        # Energie        self.root = root    return f"🎵 {random.choice(laute)}"    return f"🎵 {random.choice(laute)}"

        tk.Label(status_frame, text="⚡ Energie:", 

                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)        self.root.title("🐱 Katzenpflege-Spiel 🐱")

        self.energie_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

                                          maximum=100, value=100)        self.root.geometry("900x700")

        self.energie_bar.pack(padx=10, pady=2, fill=tk.X)

        self.energie_label = tk.Label(status_frame, text="100%",         self.root.configure(bg="#2c3e50")

                                     bg="#34495e", fg="#ecf0f1")

        self.energie_label.pack(anchor=tk.E, padx=10)        def gebe_infos_aus():def gebe_infos_aus():

        

        # Hunger        # Titel

        tk.Label(status_frame, text="🍖 Hunger:", 

                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)        titel = tk.Label(root, text="🐱 KATZENPFLEGE-SPIEL 🐱",     """Zeigt alle Informationen der Katze an"""    """Zeigt alle Informationen der Katze an"""

        self.hunger_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

                                         maximum=100, value=0)                        font=("Arial", 24, "bold"), 

        self.hunger_bar.pack(padx=10, pady=2, fill=tk.X)

        self.hunger_label = tk.Label(status_frame, text="0%",                         bg="#2c3e50", fg="#ecf0f1")    return f""" {name.upper()} - Status Report    return f""" {name.upper()} - Status Report

                                    bg="#34495e", fg="#ecf0f1")

        self.hunger_label.pack(anchor=tk.E, padx=10)        titel.pack(pady=10)

        

        # Aktionsprotokoll        ════════════════════════════════════════════════════════════════════════════════

        self.log_frame = tk.Frame(root, bg="#1a252f", relief=tk.SUNKEN, bd=2)

        self.log_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)        # Frame für Katzenname

        

        tk.Label(self.log_frame, text="📝 Ereignisse:",         info_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, bd=2)Alter: {alter} JahreAlter: {alter} Jahre

                bg="#1a252f", fg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=10, pady=5)

                info_frame.pack(pady=10, padx=20, fill=tk.X)

        scrollbar = tk.Scrollbar(self.log_frame)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)        Farbe: {farbe}Farbe: {farbe}

        

        self.log_text = tk.Text(self.log_frame, height=8, width=80,         self.katze_label = tk.Label(info_frame, text="", 

                               bg="#2c3e50", fg="#ecf0f1", 

                               yscrollcommand=scrollbar.set, font=("Courier", 9))                                   font=("Arial", 16, "bold"), Glücklichkeit: {glücklichkeit}/: {glücklichkeit}/100

        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.log_text.yview)                                   bg="#34495e", fg="#f39c12")

        self.log_text.config(state=tk.DISABLED)

                self.katze_label.pack(pady=5)Energie: {energie}/Energie: {energie}/100

        # Button Frame

        button_frame = tk.Frame(root, bg="#2c3e50")        

        button_frame.pack(pady=10, padx=20, fill=tk.X)

                # Frame für StatusleistenHunger: {hunger}/100Hunger: {hunger}/100

        # Buttons in einem Grid anordnen

        buttons = [        status_frame = tk.Frame(root, bg="#34495e", relief=tk.SUNKEN, bd=2)

            ("🍖 Fressen", self.fressen_geben, "#e74c3c"),

            ("🤚 Streicheln", self.streicheln, "#3498db"),        status_frame.pack(pady=10, padx=20, fill=tk.X)Runde: {runde}Runde: {runde}

            ("🎾 Spielen", self.spielen, "#2ecc71"),

            ("😴 Schlafen", self.schlafen, "#9b59b6"),        

            ("🏃 Trainieren", self.trainieren, "#f39c12"),

            ("🚿 Baden", self.baden, "#1abc9c"),        # Glücklichkeit════════════════════════════════════════"""════════════════════════════════════════"""

            ("🪥 Zähne", self.zaehne_putzen, "#34495e"),

            ("🏥 Tierarzt", self.zum_tierarzt, "#c0392b"),        tk.Label(status_frame, text="😊 Glücklichkeit:", 

            ("🧸 Spielzeug", self.spielzeug_kaufen, "#d35400"),

            ("ℹ️  Infos", self.show_infos, "#8e44ad"),                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)

        ]

                self.glucklichkeit_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

        for i, (text, command, color) in enumerate(buttons):

            btn = tk.Button(button_frame, text=text, command=command,                                                 maximum=100, value=50, style="green.Horizontal.TProgressbar")# Hauptspielklassedef fressen_geben():

                          font=("Arial", 9, "bold"), bg=color, fg="white",

                          padx=10, pady=8, relief=tk.RAISED, bd=2,        self.glucklichkeit_bar.pack(padx=10, pady=2, fill=tk.X)

                          activebackground=color, activeforeground="white")

            btn.grid(row=i // 5, column=i % 5, padx=5, pady=5, sticky="ew")        self.glucklichkeit_label = tk.Label(status_frame, text="50%", class KatzenSpiel:    """Gibt der Katze Fressen"""

        

        # Configure grid weights                                           bg="#34495e", fg="#ecf0f1")

        for i in range(2):

            button_frame.grid_rowconfigure(i, weight=1)        self.glucklichkeit_label.pack(anchor=tk.E, padx=10)    def __init__(self, root):    global hunger, glücklichkeit, energie

        for i in range(5):

            button_frame.grid_columnconfigure(i, weight=1)        

        

        # Status Label        # Energie        self.root = root    hunger = max(0, hunger - 30)

        self.status_label = tk.Label(root, text="", 

                                    font=("Arial", 11, "bold"),         tk.Label(status_frame, text="⚡ Energie:", 

                                    bg="#2c3e50", fg="#2ecc71")

        self.status_label.pack(pady=5)                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)        self.root.title("🐱 Katzenpflege-Spiel 🐱")    glücklichkeit += 10

        

        # Style Setup        self.energie_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

        style = ttk.Style()

        style.theme_use('clam')                                          maximum=100, value=100, style="blue.Horizontal.TProgressbar")        self.root.geometry("900x700")    energie += 5

        

    def add_log(self, message):        self.energie_bar.pack(padx=10, pady=2, fill=tk.X)

        """Nachricht zum Log hinzufügen"""

        self.log_text.config(state=tk.NORMAL)        self.energie_label = tk.Label(status_frame, text="100%",         self.root.configure(bg="#2c3e50")    print(f"🍖 {name} frisst lecker! Hunger gesenkt, Glücklichkeit erhöht!")

        self.log_text.insert(tk.END, message + "\n")

        self.log_text.see(tk.END)                                     bg="#34495e", fg="#ecf0f1")

        self.log_text.config(state=tk.DISABLED)

            self.energie_label.pack(anchor=tk.E, padx=10)            if glücklichkeit > 85:

    def update_status(self):

        """Status aktualisieren"""        

        global energie, hunger, glücklichkeit, runde

                # Hunger        # Titel        schnurren()

        self.katze_label.config(text=f"🐱 {name} ({farbe}, {alter} Jahre)")

        self.energie_bar['value'] = energie        tk.Label(status_frame, text="🍖 Hunger:", 

        self.glucklichkeit_bar['value'] = glücklichkeit

        self.hunger_bar['value'] = hunger                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)        titel = tk.Label(root, text="🐱 KATZENPFLEGE-SPIEL 🐱", 

        

        self.energie_label.config(text=f"{energie}%")        self.hunger_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

        self.glucklichkeit_label.config(text=f"{glücklichkeit}%")

        self.hunger_label.config(text=f"{hunger}%")                                         maximum=100, value=0, style="red.Horizontal.TProgressbar")                        font=("Arial", 24, "bold"), def streicheln():

        

        self.status_label.config(text=f"Runde: {runde}")        self.hunger_bar.pack(padx=10, pady=2, fill=tk.X)

        

        # Überprüfe Spielende        self.hunger_label = tk.Label(status_frame, text="0%",                         bg="#2c3e50", fg="#ecf0f1")    """Katze streicheln"""

        if energie <= 0:

            messagebox.showwarning("Game Over", f"😴 {name} ist völlig erschöpft!\n\nGAME OVER!")                                    bg="#34495e", fg="#ecf0f1")

            self.root.quit()

        if hunger >= 100:        self.hunger_label.pack(anchor=tk.E, padx=10)        titel.pack(pady=10)    global glücklichkeit, energie

            messagebox.showwarning("Game Over", f"🍗 {name} verhungert!\n\nGAME OVER!")

            self.root.quit()        

        if glücklichkeit <= 0:

            messagebox.showwarning("Game Over", f"😿 {name} ist viel zu traurig!\n\nGAME OVER!")        # Aktionsprotokoll            glücklichkeit += 20

            self.root.quit()

        if glücklichkeit >= 100:        self.log_frame = tk.Frame(root, bg="#1a252f", relief=tk.SUNKEN, bd=2)

            messagebox.showinfo("Du hast gewonnen!", f"😻 {name} ist überglücklich!\n\nDU HAST GEWONNEN! 🎉")

            self.root.quit()        self.log_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)        # Frame für Katzenname    energie -= 5

    

    def fressen_geben(self):        

        global hunger, glücklichkeit, energie, runde

        runde += 1        tk.Label(self.log_frame, text="📝 Ereignisse:",         info_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, bd=2)    print(f"🤚 Du streichelst {name} sanft...")

        hunger = max(0, hunger - 30)

        glücklichkeit += 10                bg="#1a252f", fg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=10, pady=5)

        energie += 5

        self.add_log(f"🍖 {name} frisst lecker! Hunger: {hunger}%, Glücklichkeit: {glücklichkeit}%")                info_frame.pack(pady=10, padx=20, fill=tk.X)    schnurren()

        if glücklichkeit > 85:

            self.add_log(schnurren())        scrollbar = tk.Scrollbar(self.log_frame)

        self.zeit_verstreichen()

        self.update_status()        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)        

    

    def streicheln(self):        

        global glücklichkeit, energie, runde

        runde += 1        self.log_text = tk.Text(self.log_frame, height=8, width=80,         self.katze_label = tk.Label(info_frame, text="", def spielen():

        glücklichkeit += 20

        energie -= 5                               bg="#2c3e50", fg="#ecf0f1", 

        self.add_log(f"🤚 Du streichelst {name} sanft...")

        self.add_log(schnurren())                               yscrollcommand=scrollbar.set, font=("Courier", 9))                                   font=("Arial", 16, "bold"),     """Mit der Katze spielen"""

        self.zeit_verstreichen()

        self.update_status()        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    

    def spielen(self):        scrollbar.config(command=self.log_text.yview)                                   bg="#34495e", fg="#f39c12")    global glücklichkeit, energie, hunger

        global glücklichkeit, energie, hunger, runde

        runde += 1        self.log_text.config(state=tk.DISABLED)

        glücklichkeit += 25

        energie -= 20                self.katze_label.pack(pady=5)    glücklichkeit += 25

        hunger += 15

        self.add_log(f"🎾 {name} springt herum und spielt mit dir!")        # Button Frame

        self.add_log(f"Wow! {name} hat einen Salto gemacht!")

        self.zeit_verstreichen()        button_frame = tk.Frame(root, bg="#2c3e50")            energie -= 20

        self.update_status()

            button_frame.pack(pady=10, padx=20, fill=tk.X)

    def schlafen(self):

        global energie, glücklichkeit, runde                # Frame für Statusleisten    hunger += 15

        runde += 1

        energie = min(100, energie + 40)        # Buttons in einem Grid anordnen

        glücklichkeit += 5

        self.add_log(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")        buttons = [        status_frame = tk.Frame(root, bg="#34495e", relief=tk.SUNKEN, bd=2)    print(f"🎾 {name} springt herum und spielt mit dir!")

        self.add_log(f"💤 zzzzzz...")

        self.zeit_verstreichen()            ("🍖 Fressen", self.fressen_geben, "#e74c3c"),

        self.update_status()

                ("🤚 Streicheln", self.streicheln, "#3498db"),        status_frame.pack(pady=10, padx=20, fill=tk.X)    print(f"Wow! {name} hat einen Salto gemacht!")

    def trainieren(self):

        global energie, glücklichkeit, runde            ("🎾 Spielen", self.spielen, "#2ecc71"),

        runde += 1

        if energie < 20:            ("😴 Schlafen", self.schlafen, "#9b59b6"),        

            self.add_log(f"😴 {name} ist zu müde zum Trainieren!")

            return            ("🏃 Trainieren", self.trainieren, "#f39c12"),

        energie -= 25

        glücklichkeit += 15            ("🚿 Baden", self.baden, "#1abc9c"),        # Glücklichkeitdef schlafen():

        self.add_log(f"🏃 {name} trainiert und springt umher!")

        self.add_log(f"Gut gemacht!")            ("🪥 Zähne", self.zaehne_putzen, "#34495e"),

        self.zeit_verstreichen()

        self.update_status()            ("🏥 Tierarzt", self.zum_tierarzt, "#c0392b"),        tk.Label(status_frame, text="😊 Glücklichkeit:",     """Katze schlafen legen"""

    

    def baden(self):            ("🧸 Spielzeug", self.spielzeug_kaufen, "#d35400"),

        global glücklichkeit, energie, runde

        runde += 1            ("ℹ️  Infos", self.show_infos, "#8e44ad"),                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)    global energie, glücklichkeit

        glücklichkeit -= 15

        energie -= 10        ]

        self.add_log(f"🚿 Du versuchst {name} zu baden...")

        self.add_log(f"MIAAAAUU! 😾")                self.glucklichkeit_bar = ttk.Progressbar(status_frame, length=400, mode='determinate',     energie = min(100, energie + 40)

        self.add_log(f"{name} ist NICHT begeistert!")

        self.zeit_verstreichen()        for i, (text, command, color) in enumerate(buttons):

        self.update_status()

                btn = tk.Button(button_frame, text=text, command=command,                                                 maximum=100, value=50, style="green.Horizontal.TProgressbar")    glücklichkeit += 5

    def zaehne_putzen(self):

        global glücklichkeit, energie, runde                          font=("Arial", 9, "bold"), bg=color, fg="white",

        runde += 1

        glücklichkeit -= 10                          padx=10, pady=8, relief=tk.RAISED, bd=2,        self.glucklichkeit_bar.pack(padx=10, pady=2, fill=tk.X)    print(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")

        energie -= 5

        self.add_log(f"🪥 Du putzt {name} die Zähne...")                          activebackground=color, activeforeground="white")

        self.add_log(f"Mrrrow! 😾 {name} möchte das nicht!")

        self.zeit_verstreichen()            btn.grid(row=i // 5, column=i % 5, padx=5, pady=5, sticky="ew")        self.glucklichkeit_label = tk.Label(status_frame, text="50%",     time.sleep(1)

        self.update_status()

            

    def zum_tierarzt(self):

        global energie, glücklichkeit, runde        # Configure grid weights                                           bg="#34495e", fg="#ecf0f1")    print(f"💤 zzzzzz...")

        runde += 1

        self.add_log(f"🏥 Ihr besucht den Tierarzt...")        for i in range(2):

        self.add_log(f"Der Tierarzt untersucht {name}...")

        energiewert = random.randint(10, 30)            button_frame.grid_rowconfigure(i, weight=1)        self.glucklichkeit_label.pack(anchor=tk.E, padx=10)

        self.add_log(f"✅ {name} ist gesund! +{energiewert} Energie!")

        energie = min(100, energie + energiewert)        for i in range(5):

        glücklichkeit -= 5

        self.zeit_verstreichen()            button_frame.grid_columnconfigure(i, weight=1)        def trainieren():

        self.update_status()

            

    def spielzeug_kaufen(self):

        global glücklichkeit, runde        # Status Label        # Energie    """Mit Katze trainieren"""

        runde += 1

        glücklichkeit += 30        self.status_label = tk.Label(root, text="", 

        self.add_log(f"🧸 Du kaufst ein neues Spielzeug für {name}!")

        self.add_log(f"{name} ist begeistert und spielt damit!")                                    font=("Arial", 11, "bold"),         tk.Label(status_frame, text="⚡ Energie:",     global energie, glücklichkeit, alter

        self.add_log(schnurren())

        self.zeit_verstreichen()                                    bg="#2c3e50", fg="#2ecc71")

        self.update_status()

            self.status_label.pack(pady=5)                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)    if energie < 20:

    def zeit_verstreichen(self):

        global energie, hunger, glücklichkeit        

        energie -= 8

        hunger += 10        # Styles konfigurieren        self.energie_bar = ttk.Progressbar(status_frame, length=400, mode='determinate',         print(f"😴 {name} ist zu müde zum Trainieren!")

        glücklichkeit -= 3

        self.add_log(f"⏰ Zeit verstreicht... (-8 Energie, +10 Hunger, -3 Glücklichkeit)")        style = ttk.Style()

    

    def show_infos(self):        style.theme_use('clam')                                          maximum=100, value=100, style="blue.Horizontal.TProgressbar")        return

        messagebox.showinfo(f"Infos über {name}", gebe_infos_aus())

        style.configure("green.Horizontal.TProgressbar", background="#2ecc71", troughcolor="#34495e")



def start_game():        style.configure("blue.Horizontal.TProgressbar", background="#3498db", troughcolor="#34495e")        self.energie_bar.pack(padx=10, pady=2, fill=tk.X)    energie -= 25

    """Startet das Spiel nach Eingabe der Katzeninfos"""

    global name, alter, farbe        style.configure("red.Horizontal.TProgressbar", background="#e74c3c", troughcolor="#34495e")

    

    # Fenster für Eingabe erstellen                self.energie_label = tk.Label(status_frame, text="100%",     glücklichkeit += 15

    root_input = tk.Tk()

    root_input.title("🐱 Katzenpflege-Spiel - Einrichtung")    def add_log(self, message):

    root_input.geometry("400x300")

    root_input.configure(bg="#2c3e50")        """Nachricht zum Log hinzufügen"""                                     bg="#34495e", fg="#ecf0f1")    print(f"🏃 {name} trainiert und springt umher!")

    

    tk.Label(root_input, text="🐱 Willkommen zum Katzenpflege-Spiel! 🐱",        self.log_text.config(state=tk.NORMAL)

            font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=20)

            self.log_text.insert(tk.END, message + "\n")        self.energie_label.pack(anchor=tk.E, padx=10)    print(f"Gut gemacht!")

    # Name

    tk.Label(root_input, text="Gib den Namen deiner Katze ein:",        self.log_text.see(tk.END)

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

    name_entry = tk.Entry(root_input, font=("Arial", 12), width=30)        self.log_text.config(state=tk.DISABLED)        

    name_entry.pack(pady=5)

        

    # Alter

    tk.Label(root_input, text="Gib das Alter deiner Katze ein:",    def update_status(self):        # Hungerdef baden():

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

    alter_entry = tk.Entry(root_input, font=("Arial", 12), width=30)        """Status aktualisieren"""

    alter_entry.pack(pady=5)

            global energie, hunger, glücklichkeit, runde        tk.Label(status_frame, text="🍖 Hunger:",     """Katze baden"""

    # Farbe

    tk.Label(root_input, text="Gib die Farbe deiner Katze ein:",        

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

    farbe_entry = tk.Entry(root_input, font=("Arial", 12), width=30)        self.katze_label.config(text=f"🐱 {name} ({farbe}, {alter} Jahre)")                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)    global glücklichkeit, energie

    farbe_entry.pack(pady=5)

            self.energie_bar['value'] = energie

    def starte_spiel():

        global name, alter, farbe        self.glucklichkeit_bar['value'] = glücklichkeit        self.hunger_bar = ttk.Progressbar(status_frame, length=400, mode='determinate',     glücklichkeit -= 15

        

        try:        self.hunger_bar['value'] = hunger

            name = name_entry.get().strip()

            alter = int(alter_entry.get().strip())                                                 maximum=100, value=0, style="red.Horizontal.TProgressbar")    energie -= 10

            farbe = farbe_entry.get().strip()

                    self.energie_label.config(text=f"{energie}%")

            if not name or not farbe:

                messagebox.showerror("Fehler", "Bitte fülle alle Felder aus!")        self.glucklichkeit_label.config(text=f"{glücklichkeit}%")        self.hunger_bar.pack(padx=10, pady=2, fill=tk.X)    print(f"🚿 Du versuchst {name} zu baden...")

                return

                    self.hunger_label.config(text=f"{hunger}%")

            root_input.destroy()

                            self.hunger_label = tk.Label(status_frame, text="0%",     print(f"MIAAAAUU! 😾")

            # Hauptfenster erstellen

            root = tk.Tk()        self.status_label.config(text=f"Runde: {runde}")

            spiel = KatzenSpiel(root)

            spiel.add_log(f"✨ Willkommen {name}! Du bist eine {farbe} Katze im Alter von {alter} Jahren!")                                            bg="#34495e", fg="#ecf0f1")    print(f"{name} ist NICHT begeistert!")

            spiel.update_status()

            root.mainloop()        # Überprüfe Spielende

            

        except ValueError:        if energie <= 0:        self.hunger_label.pack(anchor=tk.E, padx=10)

            messagebox.showerror("Fehler", "Das Alter muss eine Zahl sein!")

                messagebox.showwarning("Game Over", f"😴 {name} ist völlig erschöpft!\n\nGAME OVER!")

    btn = tk.Button(root_input, text="🎮 Spiel starten!",

                   font=("Arial", 12, "bold"), command=starte_spiel,            self.root.quit()        def zaehne_putzen():

                   bg="#2ecc71", fg="white", padx=20, pady=10)

    btn.pack(pady=20)        if hunger >= 100:

    

    root_input.mainloop()            messagebox.showwarning("Game Over", f"🍗 {name} verhungert!\n\nGAME OVER!")        # Aktionsprotokoll    """Zähne der Katze putzen"""



            self.root.quit()

if __name__ == "__main__":

    start_game()        if glücklichkeit <= 0:        self.log_frame = tk.Frame(root, bg="#1a252f", relief=tk.SUNKEN, bd=2)    global glücklichkeit, energie


            messagebox.showwarning("Game Over", f"😿 {name} ist viel zu traurig!\n\nGAME OVER!")

            self.root.quit()        self.log_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)    glücklichkeit -= 10

        if glücklichkeit >= 100:

            messagebox.showinfo("Du hast gewonnen!", f"😻 {name} ist überglücklich!\n\nDU HAST GEWONNEN! 🎉")            energie -= 5

            self.root.quit()

            tk.Label(self.log_frame, text="📝 Ereignisse:",     print(f"🪥 Du putzt {name} die Zähne...")

    def fressen_geben(self):

        global hunger, glücklichkeit, energie, runde                bg="#1a252f", fg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=10, pady=5)    print(f"Mrrrow! 😾 {name} möchte das nicht!")

        runde += 1

        hunger = max(0, hunger - 30)        

        glücklichkeit += 10

        energie += 5        scrollbar = tk.Scrollbar(self.log_frame)def zum_tierarzt():

        self.add_log(f"🍖 {name} frisst lecker! Hunger: {hunger}%, Glücklichkeit: {glücklichkeit}%")

        if glücklichkeit > 85:        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    """Zum Tierarzt gehen"""

            self.add_log(schnurren())

        self.zeit_verstreichen()            global energie, glücklichkeit, hunger

        self.update_status()

            self.log_text = tk.Text(self.log_frame, height=8, width=80,     print(f"🏥 Ihr besucht den Tierarzt...")

    def streicheln(self):

        global glücklichkeit, energie, runde                               bg="#2c3e50", fg="#ecf0f1",     time.sleep(1)

        runde += 1

        glücklichkeit += 20                               yscrollcommand=scrollbar.set, font=("Courier", 9))    print(f"Der Tierarzt untersucht {name}...")

        energie -= 5

        self.add_log(f"🤚 Du streichelst {name} sanft...")        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)    time.sleep(1)

        self.add_log(schnurren())

        self.zeit_verstreichen()        scrollbar.config(command=self.log_text.yview)    energiewert = random.randint(10, 30)

        self.update_status()

            self.log_text.config(state=tk.DISABLED)    print(f"✅ {name} ist gesund! Erhalte {energiewert} Energie!")

    def spielen(self):

        global glücklichkeit, energie, hunger, runde            energie = min(100, energie + energiewert)

        runde += 1

        glücklichkeit += 25        # Button Frame    glücklichkeit -= 5

        energie -= 20

        hunger += 15        button_frame = tk.Frame(root, bg="#2c3e50")

        self.add_log(f"🎾 {name} springt herum und spielt mit dir!")

        self.add_log(f"Wow! {name} hat einen Salto gemacht!")        button_frame.pack(pady=10, padx=20, fill=tk.X)def spielzeug_kaufen():

        self.zeit_verstreichen()

        self.update_status()            """Neues Spielzeug kaufen"""

    

    def schlafen(self):        # Buttons in einem Grid anordnen    global glücklichkeit, energie

        global energie, glücklichkeit, runde

        runde += 1        buttons = [    glücklichkeit += 30

        energie = min(100, energie + 40)

        glücklichkeit += 5            ("🍖 Fressen", self.fressen_geben, "#e74c3c"),    print(f"🧸 Du kaufst ein neues Spielzeug für {name}!")

        self.add_log(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")

        self.add_log(f"💤 zzzzzz...")            ("🤚 Streicheln", self.streicheln, "#3498db"),    print(f"{name} ist begeistert und spielt damit!")

        self.zeit_verstreichen()

        self.update_status()            ("🎾 Spielen", self.spielen, "#2ecc71"),    schnurren()

    

    def trainieren(self):            ("😴 Schlafen", self.schlafen, "#9b59b6"),

        global energie, glücklichkeit, runde

        runde += 1            ("🏃 Trainieren", self.trainieren, "#f39c12"),def zeit_verstreichen():

        if energie < 20:

            self.add_log(f"😴 {name} ist zu müde zum Trainieren!")            ("🚿 Baden", self.baden, "#1abc9c"),    """Zeit verstreicht - alles verschlechtert sich"""

            return

        energie -= 25            ("🪥 Zähne", self.zaehne_putzen, "#34495e"),    global energie, hunger, glücklichkeit

        glücklichkeit += 15

        self.add_log(f"🏃 {name} trainiert und springt umher!")            ("🏥 Tierarzt", self.zum_tierarzt, "#c0392b"),    energie -= 8

        self.add_log(f"Gut gemacht!")

        self.zeit_verstreichen()            ("🧸 Spielzeug", self.spielzeug_kaufen, "#d35400"),    hunger += 10

        self.update_status()

                ("ℹ️  Infos", self.show_infos, "#8e44ad"),    glücklichkeit -= 3

    def baden(self):

        global glücklichkeit, energie, runde        ]

        runde += 1

        glücklichkeit -= 15        def start_game():

        energie -= 10

        self.add_log(f"🚿 Du versuchst {name} zu baden...")        for i, (text, command, color) in enumerate(buttons):    """Startet das Spiel nach Eingabe der Katzeninfos"""

        self.add_log(f"MIAAAAUU! 😾")

        self.add_log(f"{name} ist NICHT begeistert!")            btn = tk.Button(button_frame, text=text, command=command,    global name, alter, farbe

        self.zeit_verstreichen()

        self.update_status()                          font=("Arial", 9, "bold"), bg=color, fg="white",    

    

    def zaehne_putzen(self):                          padx=10, pady=8, relief=tk.RAISED, bd=2,    # Fenster für Eingabe erstellen

        global glücklichkeit, energie, runde

        runde += 1                          activebackground=color, activeforeground="white")    root_input = tk.Tk()

        glücklichkeit -= 10

        energie -= 5            btn.grid(row=i // 5, column=i % 5, padx=5, pady=5, sticky="ew")    root_input.title("🐱 Katzenpflege-Spiel - Einrichtung")

        self.add_log(f"🪥 Du putzt {name} die Zähne...")

        self.add_log(f"Mrrrow! 😾 {name} möchte das nicht!")            root_input.geometry("400x300")

        self.zeit_verstreichen()

        self.update_status()        # Configure grid weights    root_input.configure(bg="#2c3e50")

    

    def zum_tierarzt(self):        for i in range(2):    

        global energie, glücklichkeit, runde

        runde += 1            button_frame.grid_rowconfigure(i, weight=1)    tk.Label(root_input, text="🐱 Willkommen zum Katzenpflege-Spiel! 🐱",

        self.add_log(f"🏥 Ihr besucht den Tierarzt...")

        self.add_log(f"Der Tierarzt untersucht {name}...")        for i in range(5):            font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=20)

        energiewert = random.randint(10, 30)

        self.add_log(f"✅ {name} ist gesund! +{energiewert} Energie!")            button_frame.grid_columnconfigure(i, weight=1)    

        energie = min(100, energie + energiewert)

        glücklichkeit -= 5            # Name

        self.zeit_verstreichen()

        self.update_status()        # Status Label    tk.Label(root_input, text="Gib den Namen deiner Katze ein:",

    

    def spielzeug_kaufen(self):        self.status_label = tk.Label(root, text="",             bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

        global glücklichkeit, runde

        runde += 1                                    font=("Arial", 11, "bold"),     name_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

        glücklichkeit += 30

        self.add_log(f"🧸 Du kaufst ein neues Spielzeug für {name}!")                                    bg="#2c3e50", fg="#2ecc71")    name_entry.pack(pady=5)

        self.add_log(f"{name} ist begeistert und spielt damit!")

        self.add_log(schnurren())        self.status_label.pack(pady=5)    

        self.zeit_verstreichen()

        self.update_status()            # Alter

    

    def zeit_verstreichen(self):        # Styles konfigurieren    tk.Label(root_input, text="Gib das Alter deiner Katze ein:",

        global energie, hunger, glücklichkeit

        energie -= 8        style = ttk.Style()            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

        hunger += 10

        glücklichkeit -= 3        style.theme_use('clam')    alter_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

        self.add_log(f"⏰ Zeit verstreicht... (-8 Energie, +10 Hunger, -3 Glücklichkeit)")

            style.configure("green.Horizontal.TProgressbar", background="#2ecc71", troughcolor="#34495e")    alter_entry.pack(pady=5)

    def show_infos(self):

        messagebox.showinfo(f"Infos über {name}", gebe_infos_aus())        style.configure("blue.Horizontal.TProgressbar", background="#3498db", troughcolor="#34495e")    



        style.configure("red.Horizontal.TProgressbar", background="#e74c3c", troughcolor="#34495e")    # Farbe

def start_game():

    """Startet das Spiel nach Eingabe der Katzeninfos"""            tk.Label(root_input, text="Gib die Farbe deiner Katze ein:",

    global name, alter, farbe

        def add_log(self, message):            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

    # Fenster für Eingabe erstellen

    root_input = tk.Tk()        """Nachricht zum Log hinzufügen"""    farbe_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

    root_input.title("🐱 Katzenpflege-Spiel - Einrichtung")

    root_input.geometry("400x300")        self.log_text.config(state=tk.NORMAL)    farbe_entry.pack(pady=5)

    root_input.configure(bg="#2c3e50")

            self.log_text.insert(tk.END, message + "\n")    

    tk.Label(root_input, text="🐱 Willkommen zum Katzenpflege-Spiel! 🐱",

            font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=20)        self.log_text.see(tk.END)    def starte_spiel():

    

    # Name        self.log_text.config(state=tk.DISABLED)        global name, alter, farbe

    tk.Label(root_input, text="Gib den Namen deiner Katze ein:",

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)            

    name_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

    name_entry.pack(pady=5)    def update_status(self):        try:

    

    # Alter        """Status aktualisieren"""            name = name_entry.get().strip()

    tk.Label(root_input, text="Gib das Alter deiner Katze ein:",

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)        global energie, hunger, glücklichkeit, runde            alter = int(alter_entry.get().strip())

    alter_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

    alter_entry.pack(pady=5)                    farbe = farbe_entry.get().strip()

    

    # Farbe        self.katze_label.config(text=f"🐱 {name} ({farbe}, {alter} Jahre)")            

    tk.Label(root_input, text="Gib die Farbe deiner Katze ein:",

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)        self.energie_bar['value'] = energie            if not name or not farbe:

    farbe_entry = tk.Entry(root_input, font=("Arial", 12), width=30)

    farbe_entry.pack(pady=5)        self.glucklichkeit_bar['value'] = glücklichkeit                messagebox.showerror("Fehler", "Bitte fülle alle Felder aus!")

    

    def starte_spiel():        self.hunger_bar['value'] = hunger                return

        global name, alter, farbe

                            

        try:

            name = name_entry.get().strip()        self.energie_label.config(text=f"{energie}%")            root_input.destroy()

            alter = int(alter_entry.get().strip())

            farbe = farbe_entry.get().strip()        self.glucklichkeit_label.config(text=f"{glücklichkeit}%")            

            

            if not name or not farbe:        self.hunger_label.config(text=f"{hunger}%")            # Hauptfenster erstellen

                messagebox.showerror("Fehler", "Bitte fülle alle Felder aus!")

                return                    root = tk.Tk()

            

            root_input.destroy()        self.status_label.config(text=f"Runde: {runde}")            spiel = KatzenSpiel(root)

            

            # Hauptfenster erstellen                    spiel.add_log(f"✨ Willkommen {name}! Du bist eine {farbe} Katze im Alter von {alter} Jahren!")

            root = tk.Tk()

            spiel = KatzenSpiel(root)        # Überprüfe Spielende            spiel.update_status()

            spiel.add_log(f"✨ Willkommen {name}! Du bist eine {farbe} Katze im Alter von {alter} Jahren!")

            spiel.update_status()        if energie <= 0:            root.mainloop()

            root.mainloop()

                        messagebox.showwarning("Game Over", f"😴 {name} ist völlig erschöpft!\n\nGAME OVER!")            

        except ValueError:

            messagebox.showerror("Fehler", "Das Alter muss eine Zahl sein!")            self.root.quit()        except ValueError:

    

    btn = tk.Button(root_input, text="🎮 Spiel starten!",        if hunger >= 100:            messagebox.showerror("Fehler", "Das Alter muss eine Zahl sein!")

                   font=("Arial", 12, "bold"), command=starte_spiel,

                   bg="#2ecc71", fg="white", padx=20, pady=10)            messagebox.showwarning("Game Over", f"🍗 {name} verhungert!\n\nGAME OVER!")    

    btn.pack(pady=20)

                self.root.quit()    btn = tk.Button(root_input, text="🎮 Spiel starten!",

    root_input.mainloop()

        if glücklichkeit <= 0:                   font=("Arial", 12, "bold"), command=starte_spiel,



if __name__ == "__main__":            messagebox.showwarning("Game Over", f"😿 {name} ist viel zu traurig!\n\nGAME OVER!")                   bg="#2ecc71", fg="white", padx=20, pady=10)

    start_game()

            self.root.quit()    btn.pack(pady=20)

        if glücklichkeit >= 100:    

            messagebox.showinfo("Du hast gewonnen!", f"😻 {name} ist überglücklich!\n\nDU HAST GEWONNEN! 🎉")    root_input.mainloop()

            self.root.quit()

    if __name__ == "__main__":

    def fressen_geben(self):    start_game()

        global hunger, glücklichkeit, energie, runde

        runde += 1# Hauptspielschleife

        hunger = max(0, hunger - 30)class KatzenSpiel:

        glücklichkeit += 10    def __init__(self, root):

        energie += 5        self.root = root

        self.add_log(f"🍖 {name} frisst lecker! Hunger: {hunger}%, Glücklichkeit: {glücklichkeit}%")        self.root.title("🐱 Katzenpflege-Spiel 🐱")

        if glücklichkeit > 85:        self.root.geometry("900x700")

            self.add_log(schnurren())        self.root.configure(bg="#2c3e50")

        self.zeit_verstreichen()        

        self.update_status()        # Titel

            titel = tk.Label(root, text="🐱 KATZENPFLEGE-SPIEL 🐱", 

    def streicheln(self):                        font=("Arial", 24, "bold"), 

        global glücklichkeit, energie, runde                        bg="#2c3e50", fg="#ecf0f1")

        runde += 1        titel.pack(pady=10)

        glücklichkeit += 20        

        energie -= 5        # Frame für Katzenname

        self.add_log(f"🤚 Du streichelst {name} sanft...")        info_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, bd=2)

        self.add_log(schnurren())        info_frame.pack(pady=10, padx=20, fill=tk.X)

        self.zeit_verstreichen()        

        self.update_status()        self.katze_label = tk.Label(info_frame, text="", 

                                       font=("Arial", 16, "bold"), 

    def spielen(self):                                   bg="#34495e", fg="#f39c12")

        global glücklichkeit, energie, hunger, runde        self.katze_label.pack(pady=5)

        runde += 1        

        glücklichkeit += 25        # Frame für Statusleisten

        energie -= 20        status_frame = tk.Frame(root, bg="#34495e", relief=tk.SUNKEN, bd=2)

        hunger += 15        status_frame.pack(pady=10, padx=20, fill=tk.X)

        self.add_log(f"🎾 {name} springt herum und spielt mit dir!")        

        self.add_log(f"Wow! {name} hat einen Salto gemacht!")        # Glücklichkeit

        self.zeit_verstreichen()        tk.Label(status_frame, text="😊 Glücklichkeit:", 

        self.update_status()                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)

            self.glucklichkeit_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

    def schlafen(self):                                                 maximum=100, value=50, style="green.Horizontal.TProgressbar")

        global energie, glücklichkeit, runde        self.glucklichkeit_bar.pack(padx=10, pady=2, fill=tk.X)

        runde += 1        self.glucklichkeit_label = tk.Label(status_frame, text="50%", 

        energie = min(100, energie + 40)                                           bg="#34495e", fg="#ecf0f1")

        glücklichkeit += 5        self.glucklichkeit_label.pack(anchor=tk.E, padx=10)

        self.add_log(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")        

        self.add_log(f"💤 zzzzzz...")        # Energie

        self.zeit_verstreichen()        tk.Label(status_frame, text="⚡ Energie:", 

        self.update_status()                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)

            self.energie_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

    def trainieren(self):                                          maximum=100, value=100, style="blue.Horizontal.TProgressbar")

        global energie, glücklichkeit, runde        self.energie_bar.pack(padx=10, pady=2, fill=tk.X)

        runde += 1        self.energie_label = tk.Label(status_frame, text="100%", 

        if energie < 20:                                     bg="#34495e", fg="#ecf0f1")

            self.add_log(f"😴 {name} ist zu müde zum Trainieren!")        self.energie_label.pack(anchor=tk.E, padx=10)

            return        

        energie -= 25        # Hunger

        glücklichkeit += 15        tk.Label(status_frame, text="� Hunger:", 

        self.add_log(f"🏃 {name} trainiert und springt umher!")                bg="#34495e", fg="#ecf0f1", font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=5)

        self.add_log(f"Gut gemacht!")        self.hunger_bar = ttk.Progressbar(status_frame, length=400, mode='determinate', 

        self.zeit_verstreichen()                                         maximum=100, value=0, style="red.Horizontal.TProgressbar")

        self.update_status()        self.hunger_bar.pack(padx=10, pady=2, fill=tk.X)

            self.hunger_label = tk.Label(status_frame, text="0%", 

    def baden(self):                                    bg="#34495e", fg="#ecf0f1")

        global glücklichkeit, energie, runde        self.hunger_label.pack(anchor=tk.E, padx=10)

        runde += 1        

        glücklichkeit -= 15        # Aktionsprotokoll

        energie -= 10        self.log_frame = tk.Frame(root, bg="#1a252f", relief=tk.SUNKEN, bd=2)

        self.add_log(f"🚿 Du versuchst {name} zu baden...")        self.log_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.add_log(f"MIAAAAUU! 😾")        

        self.add_log(f"{name} ist NICHT begeistert!")        tk.Label(self.log_frame, text="📝 Ereignisse:", 

        self.zeit_verstreichen()                bg="#1a252f", fg="#ecf0f1", font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=10, pady=5)

        self.update_status()        

            scrollbar = tk.Scrollbar(self.log_frame)

    def zaehne_putzen(self):        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        global glücklichkeit, energie, runde        

        runde += 1        self.log_text = tk.Text(self.log_frame, height=8, width=80, 

        glücklichkeit -= 10                               bg="#2c3e50", fg="#ecf0f1", 

        energie -= 5                               yscrollcommand=scrollbar.set, font=("Courier", 9))

        self.add_log(f"🪥 Du putzt {name} die Zähne...")        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.add_log(f"Mrrrow! 😾 {name} möchte das nicht!")        scrollbar.config(command=self.log_text.yview)

        self.zeit_verstreichen()        self.log_text.config(state=tk.DISABLED)

        self.update_status()        

            # Button Frame

    def zum_tierarzt(self):        button_frame = tk.Frame(root, bg="#2c3e50")

        global energie, glücklichkeit, runde        button_frame.pack(pady=10, padx=20, fill=tk.X)

        runde += 1        

        self.add_log(f"🏥 Ihr besucht den Tierarzt...")        # Buttons in einem Grid anordnen

        self.add_log(f"Der Tierarzt untersucht {name}...")        buttons = [

        energiewert = random.randint(10, 30)            ("🍖 Fressen", self.fressen_geben, "#e74c3c"),

        self.add_log(f"✅ {name} ist gesund! +{energiewert} Energie!")            ("🤚 Streicheln", self.streicheln, "#3498db"),

        energie = min(100, energie + energiewert)            ("🎾 Spielen", self.spielen, "#2ecc71"),

        glücklichkeit -= 5            ("😴 Schlafen", self.schlafen, "#9b59b6"),

        self.zeit_verstreichen()            ("🏃 Trainieren", self.trainieren, "#f39c12"),

        self.update_status()            ("🚿 Baden", self.baden, "#1abc9c"),

                ("🪥 Zähne", self.zaehne_putzen, "#34495e"),

    def spielzeug_kaufen(self):            ("🏥 Tierarzt", self.zum_tierarzt, "#c0392b"),

        global glücklichkeit, runde            ("🧸 Spielzeug", self.spielzeug_kaufen, "#d35400"),

        runde += 1            ("ℹ️  Infos", self.show_infos, "#8e44ad"),

        glücklichkeit += 30        ]

        self.add_log(f"🧸 Du kaufst ein neues Spielzeug für {name}!")        

        self.add_log(f"{name} ist begeistert und spielt damit!")        for i, (text, command, color) in enumerate(buttons):

        self.add_log(schnurren())            btn = tk.Button(button_frame, text=text, command=command,

        self.zeit_verstreichen()                          font=("Arial", 9, "bold"), bg=color, fg="white",

        self.update_status()                          padx=10, pady=8, relief=tk.RAISED, bd=2,

                              activebackground=color, activeforeground="white")

    def zeit_verstreichen(self):            btn.grid(row=i // 5, column=i % 5, padx=5, pady=5, sticky="ew")

        global energie, hunger, glücklichkeit        

        energie -= 8        # Configure grid weights

        hunger += 10        for i in range(2):

        glücklichkeit -= 3            button_frame.grid_rowconfigure(i, weight=1)

        self.add_log(f"⏰ Zeit verstreicht... (-8 Energie, +10 Hunger, -3 Glücklichkeit)")        for i in range(5):

                button_frame.grid_columnconfigure(i, weight=1)

    def show_infos(self):        

        messagebox.showinfo(f"Infos über {name}", gebe_infos_aus())        # Status Label

        self.status_label = tk.Label(root, text="", 

                                    font=("Arial", 11, "bold"), 

def start_game():                                    bg="#2c3e50", fg="#2ecc71")

    """Startet das Spiel nach Eingabe der Katzeninfos"""        self.status_label.pack(pady=5)

    global name, alter, farbe        

            # Styles konfigurieren

    # Fenster für Eingabe erstellen        style = ttk.Style()

    root_input = tk.Tk()        style.theme_use('clam')

    root_input.title("🐱 Katzenpflege-Spiel - Einrichtung")        style.configure("green.Horizontal.TProgressbar", background="#2ecc71", troughcolor="#34495e")

    root_input.geometry("400x300")        style.configure("blue.Horizontal.TProgressbar", background="#3498db", troughcolor="#34495e")

    root_input.configure(bg="#2c3e50")        style.configure("red.Horizontal.TProgressbar", background="#e74c3c", troughcolor="#34495e")

            

    tk.Label(root_input, text="🐱 Willkommen zum Katzenpflege-Spiel! 🐱",    def add_log(self, message):

            font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=20)        """Nachricht zum Log hinzufügen"""

            self.log_text.config(state=tk.NORMAL)

    # Name        self.log_text.insert(tk.END, message + "\n")

    tk.Label(root_input, text="Gib den Namen deiner Katze ein:",        self.log_text.see(tk.END)

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)        self.log_text.config(state=tk.DISABLED)

    name_entry = tk.Entry(root_input, font=("Arial", 12), width=30)    

    name_entry.pack(pady=5)    def update_status(self):

            """Status aktualisieren"""

    # Alter        global energie, hunger, glücklichkeit, runde

    tk.Label(root_input, text="Gib das Alter deiner Katze ein:",        

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)        self.katze_label.config(text=f"🐱 {name} ({farbe}, {alter} Jahre)")

    alter_entry = tk.Entry(root_input, font=("Arial", 12), width=30)        self.energie_bar['value'] = energie

    alter_entry.pack(pady=5)        self.glucklichkeit_bar['value'] = glücklichkeit

            self.hunger_bar['value'] = hunger

    # Farbe        

    tk.Label(root_input, text="Gib die Farbe deiner Katze ein:",        self.energie_label.config(text=f"{energie}%")

            bg="#2c3e50", fg="#ecf0f1").pack(pady=5)        self.glucklichkeit_label.config(text=f"{glücklichkeit}%")

    farbe_entry = tk.Entry(root_input, font=("Arial", 12), width=30)        self.hunger_label.config(text=f"{hunger}%")

    farbe_entry.pack(pady=5)        

            self.status_label.config(text=f"Runde: {runde}")

    def starte_spiel():        

        global name, alter, farbe        # Überprüfe Spielende

                if energie <= 0:

        try:            messagebox.showwarning("Game Over", f"😴 {name} ist völlig erschöpft!\n\nGAME OVER!")

            name = name_entry.get().strip()            self.root.quit()

            alter = int(alter_entry.get().strip())        if hunger >= 100:

            farbe = farbe_entry.get().strip()            messagebox.showwarning("Game Over", f"🍗 {name} verhungert!\n\nGAME OVER!")

                        self.root.quit()

            if not name or not farbe:        if glücklichkeit <= 0:

                messagebox.showerror("Fehler", "Bitte fülle alle Felder aus!")            messagebox.showwarning("Game Over", f"😿 {name} ist viel zu traurig!\n\nGAME OVER!")

                return            self.root.quit()

                    if glücklichkeit >= 100:

            root_input.destroy()            messagebox.showinfo("Du hast gewonnen!", f"😻 {name} ist überglücklich!\n\nDU HAST GEWONNEN! 🎉")

                        self.root.quit()

            # Hauptfenster erstellen    

            root = tk.Tk()    def fressen_geben(self):

            spiel = KatzenSpiel(root)        global hunger, glücklichkeit, energie, runde

            spiel.add_log(f"✨ Willkommen {name}! Du bist eine {farbe} Katze im Alter von {alter} Jahren!")        runde += 1

            spiel.update_status()        hunger = max(0, hunger - 30)

            root.mainloop()        glücklichkeit += 10

                    energie += 5

        except ValueError:        self.add_log(f"🍖 {name} frisst lecker! Hunger: {hunger}%, Glücklichkeit: {glücklichkeit}%")

            messagebox.showerror("Fehler", "Das Alter muss eine Zahl sein!")        if glücklichkeit > 85:

                self.add_log(schnurren())

    btn = tk.Button(root_input, text="🎮 Spiel starten!",        self.zeit_verstreichen()

                   font=("Arial", 12, "bold"), command=starte_spiel,        self.update_status()

                   bg="#2ecc71", fg="white", padx=20, pady=10)    

    btn.pack(pady=20)    def streicheln(self):

            global glücklichkeit, energie, runde

    root_input.mainloop()        runde += 1

        glücklichkeit += 20

        energie -= 5

if __name__ == "__main__":        self.add_log(f"🤚 Du streichelst {name} sanft...")

    start_game()        self.add_log(schnurren())

        self.zeit_verstreichen()
        self.update_status()
    
    def spielen(self):
        global glücklichkeit, energie, hunger, runde
        runde += 1
        glücklichkeit += 25
        energie -= 20
        hunger += 15
        self.add_log(f"🎾 {name} springt herum und spielt mit dir!")
        self.add_log(f"Wow! {name} hat einen Salto gemacht!")
        self.zeit_verstreichen()
        self.update_status()
    
    def schlafen(self):
        global energie, glücklichkeit, runde
        runde += 1
        energie = min(100, energie + 40)
        glücklichkeit += 5
        self.add_log(f"😴 {name} kuschelt sich gemütlich zusammen und schläft ein...")
        self.add_log(f"💤 zzzzzz...")
        self.zeit_verstreichen()
        self.update_status()
    
    def trainieren(self):
        global energie, glücklichkeit, runde
        runde += 1
        if energie < 20:
            self.add_log(f"😴 {name} ist zu müde zum Trainieren!")
            return
        energie -= 25
        glücklichkeit += 15
        self.add_log(f"🏃 {name} trainiert und springt umher!")
        self.add_log(f"Gut gemacht!")
        self.zeit_verstreichen()
        self.update_status()
    
    def baden(self):
        global glücklichkeit, energie, runde
        runde += 1
        glücklichkeit -= 15
        energie -= 10
        self.add_log(f"🚿 Du versuchst {name} zu baden...")
        self.add_log(f"MIAAAAUU! 😾")
        self.add_log(f"{name} ist NICHT begeistert!")
        self.zeit_verstreichen()
        self.update_status()
    
    def zaehne_putzen(self):
        global glücklichkeit, energie, runde
        runde += 1
        glücklichkeit -= 10
        energie -= 5
        self.add_log(f"🪥 Du putzt {name} die Zähne...")
        self.add_log(f"Mrrrow! 😾 {name} möchte das nicht!")
        self.zeit_verstreichen()
        self.update_status()
    
    def zum_tierarzt(self):
        global energie, glücklichkeit, runde
        runde += 1
        self.add_log(f"🏥 Ihr besucht den Tierarzt...")
        self.add_log(f"Der Tierarzt untersucht {name}...")
        energiewert = random.randint(10, 30)
        self.add_log(f"✅ {name} ist gesund! +{energiewert} Energie!")
        energie = min(100, energie + energiewert)
        glücklichkeit -= 5
        self.zeit_verstreichen()
        self.update_status()
    
    def spielzeug_kaufen(self):
        global glücklichkeit, runde
        runde += 1
        glücklichkeit += 30
        self.add_log(f"🧸 Du kaufst ein neues Spielzeug für {name}!")
        self.add_log(f"{name} ist begeistert und spielt damit!")
        self.add_log(schnurren())
        self.zeit_verstreichen()
        self.update_status()
    
    def zeit_verstreichen(self):
        global energie, hunger, glücklichkeit
        energie -= 8
        hunger += 10
        glücklichkeit -= 3
        self.add_log(f"⏰ Zeit verstreicht... (-8 Energie, +10 Hunger, -3 Glücklichkeit)")
    
    def show_infos(self):
        messagebox.showinfo(f"Infos über {name}", gebe_infos_aus())