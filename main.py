from tkinter import*
#from tkinter import messagebox
from PIL import Image, ImageTk
import random
#geometry(), for window dimensions
#messagebox.showinfo(), error handling

global questions_and_answers
names = []
asked = []

score = 0

questions_and_answers = {
1:["What are the most common symptoms of covid-19?",'dry cough, fever, tiredness','headaches, neck pain, sore throat', 'chest pain, conjunctivitis, sneezing', 'rashes, chest pain, hair loss',1],
2:["What is the most commonly used covid-19 vaccine in New Zealand?",'Moderna Vaccine', 'Johnson & Johnsons Janssen Vaccine', 'Pfizer-BioNTech Vaccine',3],
3:["What does wearing a mask do to prevent getting covid-19?",'Nothing.', 'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs' , 'It prevents people from looking at your face.',2],
4:["Which Alert Level instructs you to stay inside your bubble, only going out for the essentials?",'Alert Level 3','Alert Level 4', 'Alert Level 5',2],
5:["Which country has the most Covid-19 cases?",'Russia', 'United States of America', 'India',2],
6:["Can washing your hands prevent you from getting covid-19?", 'No, It cant', 'Covid can only be prevented by wearing a mask', 'Yes, It can',3],
7:["What age group has a higher chance of Covid-19 being dangerous for them?", '3-10 years old', '13-20 years old', '40-70 years old',3],
8:["What is Covid-19 short for?", 'Coronavirus Disease 2019', 'Coronavirus-19', 'Corona Virus Diesease-19',1],
9:["When did Covid-19 first start spreading around the world?", 'November 23rd 2019', 'September 11th 2019', 'December 31st 2019',3],
10:["If you have a cold, what should you do?", 'Go to school/work regardless', 'Get a covid swab and stay home', 'go to the doctors',2]
}

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class BeginQuiz:
  def __init__(self, parent):#constructor
    background_color = "PeachPuff"

    #frame set up 
    self.quiz_frame = Frame(parent, bg = background_color, padx = 50, pady = 50)
    self.quiz_frame.grid()

    #image set up
    self.bg_image = Image.open("covid-19.jpg")
    self.bg_image = self.bg_image.resize((1200,667),Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.quiz_frame = Frame (parent, bg = background_color)
    self.quiz_frame.grid()

    self.image_label = Label (self.quiz_frame, image = self.bg_image)
    self.image_label.place(x = -1, y = 70, relheight = 1)


    #Create a label widget for the title
    self.title_label = Label(self.quiz_frame, text = "The Covid-19 Quiz",font = ("Comic Sans MS","25","bold"), bg = background_color)
    self.title_label.grid(row = 0)

    #label for the user Name
    self.end_label = Label(self.quiz_frame, text ="Enter you name here:", bg = background_color)
    self.end_label.grid(row = 1, columnspan = 3, padx = 20, pady = 20)

  #  name_var = tk.StringVar()
   # age_var = tk.StringVar()
   
    #create the entry box
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 2, padx = 20, pady = 20)
    #asking for age
    self.number_label = Label(self.quiz_frame, text = "Enter your age here:", bg = background_color)
    self.number_label.grid(row = 4, columnspan = 3, padx = 20, pady = 20)

    #create the entry box
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 5, padx = 20, pady = 20)

    #def handle():
    #  name = name_var.get()
    #  age = age_var.get()
     # if name == '' or age == '':
       # messagebox.showerror(title = "ERRor")
    #  else:
       # try:
        #  age = int(age)
       # except ValueError:
         # messagebox.showerror(title = "ERRor")

    #creating a continue button
    self.continue_button = Button(self.quiz_frame, text = "Continue", bg = "#C5CAE9", command = self.name_collection)
    self.continue_button.grid(row=6,  padx=20, pady=20)

    #creating an exit button
    self.quit_button = Button (self.quiz_frame, text = "Exit", font = ("Times", "15", "bold"), bg = "Red", command = self.closescreen)
    self.quit_button.grid(row = 8)


  def name_collection(self):
    name = self.entry_box.get()
    names.append(name)
    self.quiz_frame.grid_forget()
    Start(root)

  #For please try again pop up
  def closescreen(self):
    root.withdraw()
    open_closescrn = Close()


class Close:
  def __init__(self):
    background = "Oldlace"
    self.close_box = Toplevel(root)
    self.close_box.title("Close box")

    self.close_frame = Frame (self.close_box, width=1000, height = 1000, bg = background)
    self.close_frame.grid()

    close_heading = Label (self.close_frame, text = 'Well Done', font = ('Tw Cen Mt',22, 'bold'), bg = background, pady = 15)
    close_heading.grid(row = 4, pady = 20)


    leave_button = Button (self.close_frame, text = 'Exit', width = 10, bg = "IndianRed1",font = ('Tw Cen Mt',12,'bold'),command = self.stop_sus)
    leave_button.grid(row = 4,pady = 20)
    
    self.listLabel = Label (self.end_frame, text = "1st place Available", font = ('Tw Cen MT',18), width = 40, bg = background, padx = 10, pady = 10)
    self.listLabel.grid(column = 0,row = 2)

  def stop_sus(self):
    self.close_box.destroy()
    root.withdraw()


class Start:
  def __init__(self, parent):#constructer
    background_color = "PeachPuff"
    #frame set-up 
    self.quiz_frame = Frame(parent, bg = background_color, padx = 50, pady = 50)
    self.quiz_frame.grid()

    #label widget heading set-up
    self.question_label = Label (self.quiz_frame, text = questions_and_answers[qnum][0], font = ("Tw Cen Mt", "18", "bold"), padx = 10,pady = 10, bg = background_color)
    self.question_label.grid(row = 0)

    #holds value of radio buttons
    self.Var1 = IntVar()


    #first radio Button
    self.rb1 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][1], font = ("Helvetica", "12"), bg = background_color, value = 1, variable = self.Var1, pady=10)
    self.rb1.grid(row = 1, sticky = W, padx = 10,pady = 10)

    #second radio Button
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][2], font = ("Helvetica", "12"), bg = background_color, cursor = "spraycan", value = 2, variable = self.Var1, pady = 10)
    self.rb2.grid(row = 2, sticky = W, padx = 10,pady = 10)

    #third radio Button
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][3], font = ("Helvetica", "12"), bg = background_color, value = 3, variable = self.Var1, pady = 10)
    self.rb3.grid(row = 3, sticky = W, padx = 10,pady = 10)

    #confirm answer button
    self.confirm_button = Button(self.quiz_frame, text = "Confirm", bg = "blue", command = self.test_progress)
    self.confirm_button.grid(row = 4)
    
    #score label
    self.score_label = Label (self.quiz_frame,text = "SCORE", font = ("Courier"),bg = background_color,)
    self.score_label.grid(row = 12,padx = 10,pady = 1)

    #editing radio button and question label's to show next question's data
  def questions_setup(self):
    randomiser()
    self.Var1.set(0)
    self.question_label.config(text = questions_and_answers[qnum][0])
    self.rb1.config(text = questions_and_answers[qnum][1])
    self.rb2.config(text = questions_and_answers[qnum][2])
    self.rb3.config(text = questions_and_answers[qnum][3])

  def test_progress(self):
      global score
      scr_label = self.score_label
      choice = self.Var1.get()
      if len(asked)>9:
        if choice == questions_and_answers[qnum][1]:
          score+=1
          scr_label.configure(text = score)
          self.confirm_button.config(text = "confirm")
        else:
          score+=0
          scr_label.configure(text = "The correct answer was" + questions_and_answers[qnum][2])
          self.confirm_button.config(text = "Confirm")
      else:
        if choice == 0:
          self.confirm_button.config(text = "Try Again, you haven't selected anything.")
          choice = self.Var1.get()
        else:
          if choice == questions_and_answers[qnum][2]:
            score+=1
            scr_label.configure(text = score)
            self.confirm_button(text = "Confirm")
            self.questions_setup( )
          else:
            score+=0
            scr_label.configure(text = "The correct answer was:" + questions_and_answers[qnum][3])
            self.confirm_button.configure(text = "confirm")
            self.questions_setup()


  def close_screen(self):
    root.withdraw()
    open_endscrn = End()       
    
def finalscreen(self):
    root.withdraw()
    name = names[0]
    file = open("leaderboard.txt","a")
    file.write(str(score))
    file.write(name+"\n")
    file.close
    
    input.File = open("leaderboard.txt","r")
    lineList = inputFile.readlines()
    lineList.sort()
    top = []
    top5 = (lineList[-5:])
    for line in top5:
        point = line.split(" - ")
        top.append((int(point[0]), point[1]))
    file.close()
    top.sort
    top.reverse()
    return_string = ""
    for i in range(len(top)):
        return_string += "{} - {}\n".format(top[i][0], top[i][1])
    print(return_string)
      
    open_finalscrn = Close()
    open_finalscrn.listLabel.config(text = return_string)

randomiser()
if __name__ =="__main__":
  root = Tk()  #creating the window 
  root.title("NZ Covid-19 Quiz")   #title
  quiz_instance = BeginQuiz(root)
  root.mainloop()
