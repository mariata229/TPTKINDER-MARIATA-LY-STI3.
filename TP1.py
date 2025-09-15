import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

frame1 = tk.Frame(window, bg="lightblue")
frame1.pack(expand=True, fill="both")

frame2 = tk.Frame(window, bg="lightgreen")
frame3 = tk.Frame(window, bg="orange")

lab1 = tk.Label(frame2, text="Bonsoir")
lab1.pack(anchor="w")

rep = tk.IntVar(value=-1)
questions = [
    {"question": "Qui a créé Python ?",
     "options": ["Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie"],
     "correct": 0},
    {"question": "Quelle est l’extension des fichiers Python ?",
     "options": [".java", ".cpp", ".py", ".js"],
     "correct": 2}
]

score = 0
current_question = 0
option_buttons = []  # pour stocker les boutons radio

tk.Label(frame2, text="===Bienvenue au quiz python===\n").pack(anchor="w")

def load_question():
    global option_buttons, rep
    for widget in frame2.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Radiobutton):
            widget.destroy()

    q1 = questions[current_question]
    tk.Label(frame2, text=f"Question {current_question+1}: {q1['question']}").pack(anchor="w")

    option_buttons = []
    # réinitialiser le choix
    rep.set(-1)  
    for j, option in enumerate(q1["options"]):
        rb = tk.Radiobutton(frame2, text=f"{option}", variable=rep, value=j, anchor="w")
        rb.pack(anchor="w")
        option_buttons.append(rb)

def valider():
    global score
    q1 = questions[current_question]
    if rep.get() == -1:
        return  

    if rep.get() == q1["correct"]:
        option_buttons[rep.get()].config(bg="lightgreen")
        score += 1
    else:
        option_buttons[rep.get()].config(bg="red")
        option_buttons[q1["correct"]].config(bg="lightgreen")

def suivant():
    global current_question
    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        afficher_resultats()

def afficher_resultats():
    frame2.pack_forget()
    frame3.pack(expand=True, fill="both")

    tk.Label(frame3, text=f"Résultats\nScore = {score}/{len(questions)}", font=("Arial", 14)).pack(pady=20)

    if score == len(questions):
        msg = "Excellent !"
    elif score >= len(questions) // 2:
        msg = "Bien joué "
    else:
        msg = "À revoir "

    tk.Label(frame3, text=msg, font=("Arial", 12)).pack(pady=10)

    btnRestart = tk.Button(frame3, text="Recommencer", command=recommencer)
    btnRestart.pack(pady=10)

def recommencer():
    global current_question, score
    score = 0
    current_question = 0
    frame3.pack_forget()
    frame1.pack(expand=True, fill="both")

start = tk.Label(frame1, text="Page de démarrage")
start.pack()

def demarrer():
    frame1.pack_forget()
    frame2.pack(expand=True, fill="both")
    load_question()

btStart = tk.Button(frame1, text="Demarrer", command=demarrer)
btStart.pack()

btnVal = tk.Button(frame2, text="Valider", command=valider)
btnVal.pack(anchor="w")

btnSvt = tk.Button(frame2, text="Suivant", command=suivant)
btnSvt.pack(anchor="w")

window.mainloop()