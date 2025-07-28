from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import time
import os
import sys


class Vasiki():
    def __init__(self, root):
        self.root = root
        self.frame = Frame(root)
        self.center_window(root)
         
    def center_window(self, window, width=1300, height=700):
        '''κεντραρισμα οθόνης '''
        #παίρνει τις διαστάσεις της οθόνης σε mm
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        #υπολογίζει τις συντεταγμένες του πάνω αριστερού μέρους του παραθύρου
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        window.geometry(f'{width}x{height}+{position_left}+{position_top}')
    
    def show(self):
        self.frame.pack(side="top", fill="both", expand=1)
        self.frame.lift()

    def hide(self):
        self.frame.pack_forget()
        
    def create_popwindow(self, title, message):
        '''δημιουργεί ένα παράθυρο ειδοποίησης με ένα μήνυμα και το κλείνει μετά από ένα χρονικό διάστημα'''
        try:
            self.pop_win = Tk()
            self.pop_win.title(title)
            self.pop_win.iconbitmap('C:/Users/User/Pictures/Saved Pictures/millionaire.ico')
            self.center_window(self.pop_win, 500, 350)        
            self.pop_label = Label(self.pop_win, text=message, font=("TimesNewRoman", 16), wraplength=300, fg="purple", bg="orange")
            self.pop_label.pack(pady=40)
            return self.pop_win
        except:
            print("Unable to create popwindow")
        
    def resource_path(self, arxeio):
        '''Συνάρτηση για την εύρεση διαδρομής(root) και χρήση αρχείων(εικόνες. αρχεία κειμένου)'''
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            #όταν τρέχει μέσα από το pyinstaller(.exe)
            #η διαδρομή (root) που έχει τα αρχεία βρίσκεται πάντα στο sys._MEIPASS
            #που είναι μια προσωρινή διαδρομή (temp) που δημιουργείται κατά την εκτέλεση
            base_path = sys._MEIPASS
        else:
            #όταν τρέχει σε python(.py)
            #η διαδρομή (root) όπου βρίσκεται και το .py αρχείο είναι (".")
            #με την os.path.abspath(".") εκχωρούμε όλη τη διαδρομή(C:\\...)
            base_path = os.path.abspath(".")
        #επιστρέφεται η διαδρομή (root) του αρχείου μαζί με το όνομα του("sample.png")
        #για να μπορέσουμε να το χρησιμοποιήσουμε(open,write κτλ.)
        return os.path.join(base_path, arxeio)
    
    def data_path(self, apothiki):
        '''Συνάρτηση για την αποθήκευση της βάσης δεδομένων στον ίδιο φάκελο με το exe'''
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            #όταν τρέχει μέσα από το pyinstaller(.exe)
            #η διαδρομή (root) να είναι ίδια με του .exe
            base_path = os.path.dirname(sys.executable)
        else:
            #όταν τρέχει σε python(.py)
            #η διαδρομή (root) όπου βρίσκεται και το .py αρχείο είναι (".")
            #με την os.path.abspath(".") εκχωρούμε όλη τη διαδρομή(C:\\...)
            base_path = os.path.abspath(".")
        #επιστρέφεται η διαδρομή (root) του αρχείου μαζί με το όνομα του("sample.txt")
        #για να μπορέσουμε να το χρησιμοποιήσουμε(open,write κτλ.)
        return os.path.join(base_path, apothiki)
    
    def read_q(self, filename):
        '''συνάρτηση που διαβάζει τα αρχεία ερωτήσεων'''
        questions = []
        try:
            #το encoding χρειάζεται για να αναγνωρίσει τους χαρακτήρες
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(0, (len(lines)-1), 2):
                    #κάνουμε strip για να μη συμπεριληφθούν τυχόν κενά στην αρχή και στο τέλος κάθε γραμμής
                    question = lines[i].strip()
                    #με το split χωρίζουμε κάθε γραμμή στο σημείο \t με το οποίο χωρίζονται οι απαντήσεις μεταξύ τους
                    answers = lines[i+1].strip().split('\t')
                    #εκχωρούμε μια πλειάδα (ερώτηση, απαντήσεις) σε κάθε στοιχείο της λίστας
                    questions.append((question, answers))
            return questions
        except:
            print("Unable to read file")

class MainMenu(Vasiki):
    def __init__(self, root):
        super().__init__(root)
        self.label = Label(self.frame, text="Main Menu", font=("TimesNewRoman", 32), fg="red")
        self.label.pack(pady=30)
        self.play_btn = Button(self.frame, text="Play Game", command=self.play_game, font=("TimesNewRoman", 14), padx=80, pady=40, fg="black", bg="green" )
        self.play_btn.pack(pady=30)
        self.top_scores_btn = Button(self.frame, text="Top Scores", command=self.top_scores, font=("TimesNewRoman", 14), padx=76, pady=40, fg="orange", bg="blue")
        self.top_scores_btn.pack(pady=20)
        self.escape_btn = Button(self.frame, text="Exit Game", font=("TimesNewRoman", 14), command=self.exit_game, padx=83, pady=40, fg="blue", bg="red")
        self.escape_btn.pack(pady=20)

    def play_game(self):
        self.hide()
        self.play_game = PlayGame(root)
        self.play_game.show()

    def top_scores(self):
        self.hide()
        self.top_scores = TopScores(root)
        self.top_scores.show()
    
    def exit_game(self):
        '''εξοδος από το πρόγραμμα με μήνυμα επιβεβαίωσης'''
        response = messagebox.askyesno("Exiting Game", "Are you sure you want to exit the game?")
        if response == True:
            root.quit()

class PlayGame(Vasiki):
    def __init__(self, root):
        super().__init__(root)
        self.label = Label(self.frame, text="Play Game", font=("TimesNewRoman", 24))
        self.label.pack(pady=30)
        self.name_label = Label(self.frame, text="Enter Player's name", font=("TimesNewRoman", 24), fg="red")
        self.name_label.pack(pady=50)
        self.name_frame = LabelFrame(self.frame, padx=5, pady=5)
        self.name_frame.pack()
        self.name_entry = Entry(self.name_frame, width=40, font=("TimesNewRoman", 24), fg="blue", bg="orange", borderwidth=10)
        self.name_entry.pack(ipady=30)
        self.name_entry.insert(0, "Type your name")    
        #σύνδεση της συνάρτησης με το συμβάν <FocusIn> (αν γίνει κλικ με ποντίκι)
        self.name_entry.bind("<FocusIn>", lambda event: self.focus_entry(event, self.name_entry))
        self.submit_btn = Button(self.frame, text="Submit name", command = self.submit, font=("TimesNewRoman", 24),padx=40, pady=20, fg="black", bg="lightgreen")
        self.submit_btn.pack(pady=30)
        self.back_btn = Button(self.frame, text="Back to Main Menu", command=self.back_to_main_menu, font=("TimesNewRoman", 14), padx=40, pady=20, fg="black", bg="grey")
        self.back_btn.pack(pady=30)
        #το όνομα του παίχτη
        self.given_name = None
    
    def focus_entry(self, event, entry):
        '''η συνάρτηση εξαφανίζει το βοηθητικό κείμενο όταν ο χρήστης πατήσει στο πλαίσιο εισαγωγής ονόματος'''
        if entry.get() == "Type your name":
            #διαγραφή του βοηθητικού κειμένου 
            entry.delete(0, END)
            entry.config(fg="black")
            
    def submit(self):
        '''διαχείριση του πλαισίου εισαγωγής ονόματος'''
        name = self.name_entry.get()
        if (self.name_entry.get()=="Type your name" or name.strip()==""):
            messagebox.showwarning("Be Careful", "Please enter your name")
        else:
        #μήνυμα καλωσορίσματος και μεταβαίνει στην έναρξη του παιχνιδιού
            self.given_name = name
            response = messagebox.askyesno("Hello " + self.given_name, "Enter the game?")
            if response == True:
                self.hide()
                #εδω θα ξεκινήσει ο κώδικας για το κυρίως παιχνίδι
                game = Game(self.given_name, root)
                game.show()
        
    def back_to_main_menu(self):
        self.hide()
        self.main_menu = MainMenu(root)
        self.main_menu.show()

class TopScores(Vasiki):
    def __init__(self, root):
        super().__init__(root)
        self.label = Label(self.frame, text="Top Scores", font=("TimesNewRoman", 24))
        self.label.pack(pady=30)
        self.scores = LabelFrame(self.frame, fg="black", bg="Wheat")
        self.scores.pack(pady=20)
        self.back_btn = Button(self.frame, text="Back to Main Menu", command=self.back_to_main_menu, font=("TimesNewRoman", 14), padx=40, pady=20, fg="black", bg="grey")
        self.back_btn.pack(pady=10)
        self.show_ranking()
    
    def show_ranking(self):
        '''κώδικας για εμφάνιση του πίνακα κατάταξης'''
        #δημιουργία υπο-πλαισίων για τις στήλες
        self.columns = []  # Λίστα για τα υπο-πλαίσια
        titloi = ["A/A", "Player's name", "Prize earned", "Total time", "Avg time/question", "DAEP"]
        for i in range(6):
            #Δημιουργία υπο-πλαισίου με στρογγυλεμένο πλαίσιο
            frame = LabelFrame(self.scores, borderwidth=2, relief="ridge")
            frame.grid(row=0, column=i, padx=5, pady=5)
            #προσθήκη του υπο-πλαισίου στη λίστα
            self.columns.append(frame)  

        #Προσθήκη labels στα υπο-πλαίσια
        #να καθορίσω τα statsss να παίρνει από κάθε γραμμή του αρχείου το αντιστοιχο split
        for column, statsss in zip(self.columns, titloi):
            label = Label(column, text=statsss, padx=10, pady=5, font=("TimesNewRoman", 18))
            label.pack()  # Τοποθέτηση label στο υπο-πλαίσιο
    
        try:
            file_path = self.data_path("data/ranking.txt")
            with open(file_path, "r") as file:
                lines = file.readlines()
                sorted_lines = sorted(lines, key=lambda x: float(x.split('\t')[4]), reverse=True)
                for aa, line in enumerate(sorted_lines):
                 #εμφανίζουμε μόνο τους πρώτους 10 
                    if aa >= 10:
                        break
                    pleiada = line.strip().split('\t')
                    for i in range(6):
                        if i == 0:
                            label = Label(self.columns[i], text=(aa+1), padx=10, pady=5, font=("TimesNewRoman", 16))
                            label.pack()
                        else:
                            label = Label(self.columns[i], text=pleiada[i-1], padx=10, pady=5, font=("TimesNewRoman", 16))  
                            # Τοποθέτηση label στο υπο-πλαίσιο
                            label.pack()
                    
        except:
            labelexcept = Label(self.scores, text=f"No ranking available", padx=30, pady=30, bg="orange", fg="lightgrey",font=("TimesNewRoman", 18))
            labelexcept.grid(row=1, column=0, columnspan=6, padx=5, pady=5)
                    

    def back_to_main_menu(self):
        self.hide()
        self.main_menu = MainMenu(root)
        self.main_menu.show()


class Game(Vasiki):
    '''κλάση για το κυρίως παιχνίδι'''
    prize_text = ["100€", "200€", "500€", "1.000€", "2.000€", "5.000€", "10.000€", "15.000€", "20.000€", "30.000€", "50.000€", "100.000€", "200.000€", "500.000€", "1.000.000€"]  

    def __init__(self, name, root):
        super().__init__(root)
        self.qcount = 0
        #η ιδιότητα prizecount μετράει πόσες σωστές ερωτήσεις έχουν απαντηθεί
        self.prizecount = 0
        #η ιδιότητα wronguess θα αποθηκεύει πόσες λάθος επιλογές έκανε ο χρήστης ώστε να χάνει μετά από 3 λάθος επιλογές
        self.wrong_guess = 0
        #στην ιδιότητα maksilaricount αποθηκεύεται το ποσό μαξιλαριού που έχει κερδίσει ο παίχτης
        self.maksilaricount = 0
        #η ιδιότητα main_menu είναι αντικείμενο της κλάσης MainMenu ώστε να μπορούμε να την καλέσουμε όταν χρειαστεί να επιστρέψουμε
        self.main_menu = MainMenu(root)
        self.start_game(name)
        self.name = name
    
    def started_game(self):
        '''Εμφάνιση της πρώτης ερώτησης και όλων των υπόλοιπων widget του παιχνιδιού'''
        #αφαιρούνται τα widget που δε χρειάζονται
        self.mylabel.grid_remove()
        self.start_button.grid_remove()
        self.keno_frame.grid_remove()
        #έναρξη στα χρονόμετρα       
        self.start_timer()
        #διαβάζει τις έυκολες ερωτήσεις από το αρχείο
        #δεν το χρησιμοποιώ εντός της display_question γιατί θέλω να μεταβάλω τη λίστα
        #ωστε να μην εμφανίζονται οι ίδιες ερωτήσεις
        self.questions = self.read_q(self.resource_path("data/easy.txt"))
        self.helpused1 = False
        self.helpused2 = False
        self.helpused3 = False
        self.display_question()
        self.game_running = True        
        
    def start_game(self, name):
        '''Εμφάνιση μηνύματος και κουμπιού για προβολή της 1ης ερώτησης'''
        #η game_running χρειάζεται κυρίως για να μην εκτελείται η ενέργεια από τα κουμπιά βοήθειας πριν ξεκινήσουν οι ερωτήσεις
        self.game_running = False
        self.kenolabel = Label(self.frame, text="1η Ερώτηση", font=("TimesNewRoman", 18), fg="RoyalBlue")
        self.kenolabel.grid(row=3, column=0, columnspan=5, pady=20)
        self.keno_frame = LabelFrame(self.frame)
        self.keno_frame.grid(row=6, column=0, columnspan=5, pady= 20, padx=195)        
        self.mylabel = Label(self.keno_frame, text=f"Welcome {name}.\nAre you ready for the 1st question?", font=("TimesNewRoman", 18), fg="Magenta")
        self.mylabel.grid(row=0, column=0, columnspan=2, padx=5, pady=20, ipadx=80, ipady=30)
        self.start_button = Button(self.keno_frame, text="Go", command=self.started_game, font=("TimesNewRoman", 20), fg="red", bg="green")
        self.start_button.grid(row=1, rowspan=2, column=0, columnspan=2, ipady=48, ipadx=280)        
        self.xronos()        
        self.prize_ladder()
        self.show_helpers()        
        self.heartshow()
        self.end_btn = Button(self.prizes,  text="End Game", command = self.end_game, font=("TimesNewRoman", 16), bg="red", fg="black")
        self.end_btn.grid(row=16, column=0, pady=50, ipady=20, ipadx=80)
        self.xronikhdiarkeia = "Δεν ξεκίνησε ποτέ το παιχνίδι..."
        million_img = Image.open(self.resource_path("images/million.png"))
        self.million_img = ImageTk.PhotoImage(million_img)
        self.mymillion = Label(self.frame, image=self.million_img)
        self.mymillion.grid(row=0, column=0, columnspan=5, rowspan=3)
        
    def end_game(self):
        '''Συνάρτηση για τον τερματισμό του παιχνιδιού από το κουμπί'''
        response = messagebox.askyesno("End current Game", "Are you sure you want to end this game?")
        if response == True:
            #αν έχει απαντηθεί σωστά έστω και 1 ερώτηση τερματισμός με εμφάνιση κερδισμένου ποσού
            self.nomoregame()
        
    def display_question(self):
        '''Συνάρτηση για την εμφάνιση της ερώτησης και των απαντήσεων'''
        #εξαφανίζει το frame στο οποίο εμφανίζεται η ερώτηση με τις απαντήσεις για να μη μπαίνει η 1 πάνω στην άλλη
        if self.qcount>0:
            self.question_frame.grid_remove()
        #αν δεν εχουν χρησιμοποιηθεί οι βοήθειες τις καθιστούμε ενεργές
        #απενεργοποιούνται προσωρινά όταν επιλέγεται μια απάντηση μέχρι να εμφανιστεί η επόμενη ερώτηση
        if self.helpused1 == False:
            self.helper_5050.config(state="active")
        if self.helpused2 == False:
            self.helper_prop.config(state="active")
        if self.helpused3 == False:
            self.helper_allagi.config(state="active")
        #μετρητής αρίθμησης ερώτησης
        self.qcount+=1
        self.questnumlabel = Label(self.frame, text=str(self.qcount)+"η Ερώτηση", font=("TimesNewRoman", 18), fg="RoyalBlue")
        #έχω αφήσει row=5 κενό μήπως θέλω να προσθέσω κάτι. επίσης είναι κενό και το column=2 (μόνο στις ζωές χρησιμοποιείται) για καλύτερο κεντράρισμα
        self.questnumlabel.grid(row=3, column=0, columnspan=5, pady=20)
        try:
            #τυχαίος ακέραιος αριθμός που αντιστοιχεί στην ερώτηση που θα εμφανιστεί
            random_i = random.randint(0, len(self.questions)-1)
            #το 1ο στοιχείο της πλειάδας είναι η ερώτηση και το 2ο οι απαντήσεις
            question, answers = self.questions.pop(random_i)
            #το 1ο στοιχείο του 2ου στοιχείου της πλειάδας είναι η σωστή απάντηση
            correct_answer = answers[0]
            #ανακατεύουμε τις απαντήσεις για να μην εμφανίζονται με την ίδια σειρά
            random.shuffle(answers)
            self.question_frame = LabelFrame(self.frame, bg="blue", borderwidth=2, relief="ridge")
            self.question_frame.grid(row=6, column=0, columnspan=5, pady= 20, padx=5)       
            self.questlabel = Label(self.question_frame, text=(f"{question:^100}"), borderwidth=4, relief="sunken",  font=("TimesNewRoman", 18), fg="red")
            self.questlabel.grid(row=0, column=0, columnspan=2, pady=20, padx=5, ipady=15, sticky="ew")
            self.answer_buttons=[]
            self.wrong_answers=[]
            for i in range(4):
                answer = answers[i]
                #βρίσκουμε τη θέση που μπαίνει η σωστή απάντηση για χρήση μετέποιτα
                if answer == correct_answer:
                    correct_index = i
                #προσθέτουμε αρχικό γράμμα στις απαντήσεις και ορίζουμε τη θέση κάθε απάντησης στο grid
                if i==0:
                    abcd = "Α. "
                    seira=1
                    stili=0
                elif i==1:
                    abcd = "Β. "
                    seira=1
                    stili=1
                elif i==2:
                    abcd = "Γ. "
                    seira=2
                    stili=0
                else:
                    abcd = "Δ. "
                    seira=2
                    stili=1
                #περνάμε ως παραμέτρους την text=answer και index=i στην lambda για να μπορέσει να κάνει τον έλεγχο
                answer_btn = Button(self.question_frame, text=abcd+answer, command=lambda index=i, text=answer: self.handle_answer(text == correct_answer, index, correct_index), 
                                    font=("TimesNewRoman", 16), borderwidth=2, relief="raised", fg="Salmon", bg="grey", anchor="w", padx=40)
                self.answer_buttons.append(answer_btn)
                answer_btn.grid(row=[seira], column=[stili], ipady=24, padx=5,pady=5, sticky="ew")    
            #λίστα με τις λάθος απαντήσεις για χρήση στη βοήθεια 50/50
            for btn in self.answer_buttons:
                if btn != self.answer_buttons[correct_index]:
                    self.wrong_answers.append(btn)
        except:
            print("Unable to display current question and answers")
        
    def handle_answer(self, is_correct, index, j):
        '''Συνάρτηση που καλείται όταν ο χρήστης επιλέγει μια απάντηση'''
        self.stop_timer()
        #έλεγχος της απάντησης
        if is_correct==True:
            self.flash_button(self.answer_buttons[index])
            #χρήση της θέσης σωστής απάντησης
            self.show_correct(self.answer_buttons[j])
            self.root.after(5000, self.highlight_label)

        else:
            self.flash_button(self.answer_buttons[index])
            self.show_correct(self.answer_buttons[j])
            self.wrong_guess+=1
            self.root.after(5000, lambda: self.livesimgs[self.wrong_guess-1].config(image=self.heartno_img))
        
        #απενεργοποίηση όλων των κουμπιών απάντησης όταν επιλέξει ο χρήστης μια απάντηση
        for btn in self.answer_buttons:
            btn.config(state="disabled")
        self.helper_5050.config(state="disabled")
        self.helper_prop.config(state="disabled")
        self.helper_allagi.config(state="disabled")
        #πρεπει να υπαρχει αυτός ο έλεγχος εδώ και όχι παρακάτω, για να μην προχωράει σε επόμενη ερώτηση όταν φτάσει στο μαξιλαράκι
        #καθώς εμφανίζεται popup window με κουμπιά επιλογής
        if (self.prizecount+1)%5 == 0 and self.qcount!=15:
            self.stop_timer()
        #εμφανίζουμε την επόμενη ερώτηση αν δεν εχουν τελειώσει οι 15 ή αν δεν έχει κάνει 3 φορές λάθος
        #το qcount αυξάνεται στην αρχή της εμφάνισης της ερώτησης οπότε όταν θα φτάσει στην τιμή 15 θα είναι η τελευταία ερώτηση
        #το wrongguess αρχικοποιείται στο 0 και αυξάνεται όταν ελεγχθεί η απάντηση παραπάνω, άρα όταν πάρει τιμή 3 θα έχουν τελειώσει και οι ευκαιρίες
        elif self.qcount<15 and self.wrong_guess<3 :
            self.root.after(8000, lambda: [self.display_question(), self.start_timer()])
        #αλλιώς κάνουμε τερματισμό και εμφάνιση κερδισμένου ποσού και διάρκειας αναλόγως
        else:
            self.root.after(5500, self.nomoregame)

    def save_stats(self, player_name, score, total_time, mesos_oros, daep):
        try:
            file_path = self.data_path("data/ranking.txt")
            with open(file_path, "a") as file:
                file.write(f"{player_name}\t{score}\t{total_time}\t{mesos_oros:.2f}\t{daep:.2f}\n")
        except:
            print(f"Unable to save stats: {e}")
            
    def nomoregame(self):
        '''Συνάρτηση για την εμφάνιση popup παραθύρου όταν τελειώσει το παιχνίδι για οποιονδήποτε λόγο'''
        pk = [100, 200, 500, 1000, 2000, 5000, 10000, 15000, 20000, 30000, 50000, 100000, 200000, 500000, 1000000]
        try:
            #αν ξεκινήσει το παιχνίδι και έχει απαντηθεί έστω 1 ερώτηση γίνεται υπολογισμός μ.ο. χρόνου/ερώτηση και του ΔΑΕΠ όταν τελειώσει το παιχνίδι
            if (self.game_running==True and (self.prizecount>0)):
                #εγινε αλλαγη το self.qcount
                self.mesosxronos = self.diarkeia/self.qcount
                self.daep = pk[self.prizecount-1]*(1/self.diarkeia)
            #εάν τελείωσαν οι ζωές εμφανίζεται το τυχόν εξασφαλισμένο ποσό από το μαξιλαράκι
            #αν δεν έχει εξασφαλιστεί ποσό ή δεν έχει απαντηθεί καμία ερώτηση σωστά(περιλαμβάνει  και την περίπτωση που ο χρήστης κάνει end game με 0 σωστές απαντήσεις)
            #εμφανίζεται κατάλληλο μήνυμα και επιστρέφει στο main menu
            if ((self.wrong_guess==3) or (self.prizecount == 0)) and self.game_running == True:
                if self.maksilaricount != 0:
                    pop = self.create_popwindow("The End", f"Το παιχνίδι τελείωσε...\nΚερδίσατε  {self.maksilaricount}\nΤο παιχνίδι διήρκεσε {self.xronikhdiarkeia}")
                    self.save_stats(self.name, self.maksilaricount, self.diarkeia, self.mesosxronos, self.daep)
                else:
                    pop = self.create_popwindow("The End", f"Το παιχνίδι τελείωσε...\nΔεν κερδίσατε τίποτα!!!\nΤο παιχνίδι διήρκεσε {self.xronikhdiarkeia}")
                    self.save_stats(self.name, self.maksilaricount, self.diarkeia, self.mesosxronos, self.daep)
            #αν γίνει τερματισμός πριν την εκκίνηση του παιχνιδιού δεν γινονται υπολογισμοί για τα στατιστικά (όλα είναι 0)
            elif self.game_running == False:
                pop = self.create_popwindow("The End", f"Το παιχνίδι τελείωσε πριν ακόμα ξεκινήσει...\nΔεν κερδίσατε τίποτα")
                self.save_stats(self.name, 0, 0, 0, 0)
            #σε κάθε άλλη περίπτωση εμφάνιση παραθύρου με κερδισμένο ποσό
            else:
                pop = self.create_popwindow("The End", f"Το παιχνίδι τελείωσε...\nΜπράβο!!!\nΚερδίσατε  {Game.prize_text[self.prizecount-1]}\nΤο παιχνίδι διήρκεσε {self.xronikhdiarkeia}")
                self.save_stats(self.name, Game.prize_text[self.prizecount-1], self.diarkeia, self.mesosxronos, self.daep)
            pop.after(4000, pop.destroy)
            self.stop_timer()
            self.root.after(2000, self.hide)          
            self.root.after(2000, self.main_menu.show)
        except:
            print("Unable to end current game")
    
    
    def flash_button(self, btn):
        '''Εφέ flash για suspense όταν επιλεγεί μια απάντηση πριν την εμφάνιση της σωστής'''
        btn.config(bg="yellow")
        #κάθε 500ms εναλάσσουμε το αρχικό χρώμα (γκρι) του κουμπιού με το κίτρινο
        btn.after(500, lambda: btn.config(bg="grey"))
        btn.after(1000, lambda: btn.config(bg="yellow"))
        btn.after(1500, lambda: btn.config(bg="grey"))
        btn.after(2000, lambda: btn.config(bg="yellow"))
        btn.after(2500, lambda: btn.config(bg="grey"))
        btn.after(3000, lambda: btn.config(bg="yellow"))        
        
    def show_correct(self, correct):
        '''κάνει πράσινο το φόντο του κουμπιού σωστής απάντησης'''
        correct.after(3500, lambda: correct.config(bg="green"))
    
    def heartshow(self):
        '''Εμφάνιση των εικονιδίων για εναπομείνασες προσπάθειες'''
        heartfull_img = Image.open(self.resource_path("images/heartfullr.png"))
        self.heartfull_img = ImageTk.PhotoImage(heartfull_img)
        
        heartno_img = Image.open(self.resource_path("images/heartnor.png"))
        self.heartno_img = ImageTk.PhotoImage(heartno_img)
        
        self.livesimg = Label(self.frame, image=self.heartfull_img)
        self.livesimg.grid(row=4, column=2, columnspan=3)
        self.livesimg1 = Label(self.frame, image=self.heartfull_img)
        self.livesimg1.grid(row=4, column=0, columnspan=5)
        self.livesimg2 = Label(self.frame, image=self.heartfull_img)
        self.livesimg2.grid(row=4, column=0, columnspan=3)
        self.livesimgs=[self.livesimg, self.livesimg1, self.livesimg2]
        
    def highlight_label(self):
        '''Εφαρμόζει το highlight σε ένα label με το ποσό'''
        try:
            #αφαιρούμε το highlight από το προηγούμενο widget που είχαμε κάνει highlight
            #ο έλεγχος if γίνεται για να μην πάρουμε σφάλμα στην 1η απόπερια highlight αφού δεν υπάρχει προηγούμενο
            #και να μην εφαρμοστεί αν φτάσουμε στην τελευταία ερώτηση
            if self.prizecount>0:
                self.previous_highlighted_label.config(bg="Snow")
            #εμφάνιση popup όταν φτάσει στα πρώτα 2 μαξιλαράκια. αν φτάσει στο ανώτερο βραβείο εμφανίζεται μόνο το popup κλεισίματος παιχνιδιού 
            if ((self.prizecount+1)%5 == 0 and (self.prizecount)!=14):
                #σε αυτήν θα αποθηκεύεται το ποσό του μαξιλαριού που έχει κερδίσει ο παίχτης
                self.maksilaricount = Game.prize_text[self.prizecount]
                maksilari = self.create_popwindow("Hurray!", f"Έφτασες στο {int((self.prizecount+1)/5)}ο μαξιλαράκι και έχεις εξασφαλίσει {self.maksilaricount}") 
                maksilari_label = Label (maksilari, text="Θέλετε να συνεχίσετε ή να σταματήσετε;", font=("TimesNewRoman", 16), fg="red")
                maksilari_label.pack()
                maksilari_cont_btn = Button (maksilari, text="Συνεχίζω", command = lambda: [maksilari.destroy(), self.display_question(), self.start_timer()], font=("TimesNewRoman", 24), fg="black", bg="green")
                maksilari_cont_btn.pack()
                #αν θέλει ο παίχτης να βγεί εκτελούνται διαδοχικά 3 μέθοδοι και πάει στο mainmenu
                maksilari_exit_btn = Button (maksilari, text="Φτάνει", command = lambda:[maksilari.destroy(), self.nomoregame()], font=("TimesNewRoman", 24), fg="lightgrey", bg="red")
                maksilari_exit_btn.pack()
                #αν φτάσαμε στο 1ο μαξιλαράκι, τότε διαβάζουμε ερωτήσεις από το αρχείο με τις μέτριας δυσκολίας ερωτήσεις
                if ((self.prizecount+1) == 5):
                    self.questions = self.read_q(self.resource_path("data/mid.txt"))
                #αν φτάσαμε στο 2ο μαξιλαράκι, διαβάζουμε το αρχείο με τις δύσκολες ερωτήσεις
                if ((self.prizecount+1) == 10):
                    self.questions = self.read_q(self.resource_path("data/hard.txt"))
            #κάνουμε highlight το 1ο στοιχείο της λίστας που επιστρέφει η grid_slaves (στο κατάλληλο row) που αποτελεί το label widget του ποσού
            label_to_highlight = self.prizes.grid_slaves(row=15-self.prizecount, column=0)[0]
            label_to_highlight.config(bg="green")
            #αποθηκεύουμε το νέο widget ως το προηγούμενο για μελλοντική χρήση
            self.previous_highlighted_label = label_to_highlight
        except:
            print("Unable to highlight current prize")
        #το prizecount ξεκινάει από την πρώτη θέση (0) όταν αρχικοποιείται οπότε στο τέλος της συνάρτησης
        #το αυξάνουμε κατά 1 για να είναι έτοιμο για την επόμενη σωστή ερώτηση (εφόσον υπάρξει)
        self.prizecount+=1
    def prize_ladder(self):
        '''ορίζει και εμφανίζει τη σκάλα με τα ποσά'''
        self.prizes = LabelFrame(self.frame)
        self.prizes.grid(row=0, column=5, rowspan=15, sticky="ns")
        #το πλάτος της τελευταίας στήλης στο grid να τοποθετηθεί στο δεξί άκρο του παραθύρου
        self.frame.grid_columnconfigure(5, weight=1)
        platos=20
        for i in range(15):
            bg_color="Turquoise"
            if i==4:
                platos=18
                bg_color="Wheat"
            elif i>4 and i<9:
                platos=15
            elif i==9:
                platos=13
                bg_color="Wheat"
            elif i>9 and i!=14:
                platos=10
            elif i==14:
                platos=8
                bg_color="Wheat"
            
            prize_pos = Label(self.prizes, text=Game.prize_text[i], width=platos, font=("TimesNewRoman", 16), fg="Tomato", bg=bg_color)
            prize_pos.grid(row=15-i, column=0, sticky="ns", ipady=3)
      
    def show_helpers(self):
        '''εμφανίζει τα κουμπιά βοήθειας'''
        helper5050_img = Image.open(self.resource_path("images/5050resize.png"))
        self.helper5050_img = ImageTk.PhotoImage(helper5050_img)
        
        helpercomp_img = Image.open(self.resource_path("images/compresize.png"))
        self.helpercomp_img = ImageTk.PhotoImage(helpercomp_img)
        
        helperallagi_img = Image.open(self.resource_path("images/reverseresize.png"))
        self.helperallagi_img = ImageTk.PhotoImage(helperallagi_img)
        
        self.helper_5050 = Button(self.frame, command=self.show_half, image=self.helper5050_img)
        self.helper_5050.grid(row=0, column=0, columnspan=2, sticky="w", ipadx=50)

        self.helper_prop = Button(self.frame, command=self.comp_prop, image=self.helpercomp_img)
        self.helper_prop.grid(row=1, column=0, columnspan=2, sticky="w", ipadx=50)

        self.helper_allagi = Button(self.frame, command=self.change_quest, image=self.helperallagi_img)
        self.helper_allagi.grid(row=2, column=0, columnspan=2, sticky="w", ipadx=50)
        
    def show_half(self):
        '''όταν κληθεί απενεργοποιεί τυχαία 2 από τα 3 κουμπιά των λάθος απαντήσεων'''
        if self.game_running == True:
            try:
                self.x, self.y = random.sample(self.wrong_answers, 2)
                self.x.config(state="disabled", bg="blue")
                self.y.config(state="disabled", bg="blue")
                self.x.config(disabledforeground="blue")
                self.y.config(disabledforeground="blue")
                self.helpused1 = True
                self.helper_5050.config(state="disabled")
            except:
                print("Unable to use help 50/50")
        
                    
    def comp_prop(self):
        '''όταν κληθεί προτείνει μια απάντηση στον χρήστη εξαιρώντας αυτές που τυχόν
        έχουν απενεργοποιηθεί με τη χρήση της show_half'''
        if self.game_running == True:
            try:
                while True:
                    z = random.randint(0, len(self.answer_buttons)-1)
                    try:
                        #αν η πρόταση τύχει να είναι 1 εκ των 2 αποκλεισμένων απαντήσεων της show_half
                        #εκχωρείται νέος τυχαίος αριθμός στην z
                        if (self.answer_buttons[z]==self.x or self.answer_buttons[z]==self.y):
                            continue
                        else:
                            #αλλιώς κάνει άσπρο το bg από το προτεινόμενο κουμπί
                            self.answer_buttons[z].config(bg="white")
                            break
                    #σε περίπτωση που δεν έχει χρησιμοποιηθεί η show_half βγαίνει σφάλμα καθώς δεν έχουν οριστεί ακόμα
                    #οι self.x,y οπότε σκάει ο κώδικας και πάει στο except όπου επαναλαμβάνονται οι εντολές της else πιο πάνω
                    except:
                        self.answer_buttons[z].config(bg="white")
                        break
                self.helpused2 = True
                self.helper_prop.config(state="disabled")
            except:
                print("Unable to use help proposal")
        
    def change_quest(self):
        '''όταν κληθεί μειώνεται η αρίθμηση κατά ένα για να παραμείνει στον ίδιο
        αριθμό (αφού θα γίνει +1 μέσα στην display_question) και εμφανίζει μια 
        νέα ερώτηση'''
        if self.game_running == True:
            try:
                self.qcount-=1
                self.display_question()
                self.stop_timer()
                self.helpused3 = True
                self.start_timer()
                self.helper_allagi.config(state="disabled")
            except:
                print("Unable to use help change question")
        
    def xronos(self):
        '''Εμφάνιση των χρονομέτρων'''
        self.time_head = Label(self.frame,text = "Διάρκεια:", font=("TimesNewRoman", 12), padx=70)
        self.time_head.grid(row=0, column=1, sticky="w")
        self.time_label = Label(self.frame,text = "", font=("TimesNewRoman", 12),)
        self.time_label.grid(row=0, column=1)
        self.time_qheader = Label(self.frame,text = "Χρόνος ερώτησης", font=("TimesNewRoman", 12), padx=5, pady=5)
        self.time_qheader.grid(row=0, column=4)
        self.time_qlabel = Label(self.frame,text = "", font=("TimesNewRoman", 14))
        self.time_qlabel.grid(row=1, column=4)
        self.palia_diarkeia = 0
        
    def start_timer(self):
        '''Έναρξη χρονομέτρων'''
        self.xronos_active = True
        self.start_time = time.time()
        self.update_xronos()
        self.quest_xronos()
        
    def stop_timer(self):
        '''Σταματημός των χρονομέτρων'''
        self.xronos_active = False
        #εκχώρηση της διάρκειας που έχει μετρηθεί μέχρι τη στιγμή που θα γίνει το σταμάτημα στην μεταβλητή  
        if self.game_running == True:
            self.palia_diarkeia = self.diarkeia
        
    def update_xronos(self):
        '''Συνάρτηση για τον υπολογισμό χρόνου με αφαίρεση από την αρχική χρονοσήμανση της παρούσας'''
        try:
            #αν το παιχνίδι τρέχει και δεν έχει σταματήσει ο χρόνος για κάποιο λόγο γίνεται υπολογισμός της διάρκειας του
            if self.xronos_active == True:
                self.diarkeia = self.palia_diarkeia + int(time.time() - self.start_time)
            minutes = self.diarkeia // 60
            seconds = self.diarkeia % 60
            #ενημέρωση του κειμένου του χρονόμετρου με τη νέα ώρα
            self.xronikhdiarkeia = f"{minutes:02d}:{seconds:02d}"
            self.time_label.config(text= self.xronikhdiarkeia)
            if self.xronos_active == True:
                #επαναληπτική κλήση της συνάρτησης μετά από 1 sec
                self.root.after(1000, self.update_xronos) 
        except:
            print("Unable to update time")
        
    def quest_xronos(self):
        '''Χρονόμετρο για κάθε ερώτηση'''
        try:
            self.qxronos = 60 - int(time.time() - self.start_time)
            self.time_qlabel.config(text= f"{self.qxronos} seconds")
            if self.qxronos == 0:
                self.stop_timer()
                self.time_up()            
            if self.xronos_active == True:
                self.root.after(1000, self.quest_xronos)
        except:
            print("Unable to update question timer")
            
    def time_up(self):
        '''Συνάρτηση για την περίπτωση που τελειώσει ο χρόνος χωρίς να επιλεγεί απάντηση'''
        try:
            self.wrong_guess+=1
            telos_xronou = self.create_popwindow("Be Careful", f"Τελείωσε ο χρόνος για να απαντήσεις την ερώτηση.")
            telos_xronou.after(4000, telos_xronou.destroy)
            self.livesimgs[self.wrong_guess-1].config(image=self.heartno_img)
            if self.wrong_guess==3:
                self.root.after(4500, self.nomoregame)
            else:
                self.root.after(4500, lambda: [self.display_question(), self.start_timer()])
        except:
            print("Unable to handle time up")
    
class GameApp():
    '''η κλάση αυτή χρησιμοποιείται για να δημιουργηθεί ένα στιγμιότυπο του main menu'''
    def __init__(self, root):
        self.root = root
        self.root.title("Who wants to be a millionaire")
        self.root.iconbitmap('C:/Users/User/Pictures/Saved Pictures/millionaire.ico')
        self.main_menu = MainMenu(root)
        self.main_menu.show()
       
if __name__ == "__main__":
    root = Tk()
    antikeimeno = GameApp(root)
    root.mainloop()
