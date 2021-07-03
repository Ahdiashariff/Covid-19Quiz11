from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import random

name = []
name_record = []
asked = []

score = 0

def randomiser():# this will allow the questions to be chosen randomly
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()



class BeginQuiz: #class for starting window
  def __init__ (self, parent):#constructor
    background_color = "white"

    #creating frame 
    self.open_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
    self.open_frame.grid()#for where to place frame

    #creating code to show image
    self.bg_image = Image.open("covid-19.jpg")#name of the image
    self.bg_image = self.bg_image.resize((1300,667),Image.ANTIALIAS)#resizing the image 
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.open_frame = Frame (parent, bg = background_color)#frame for image
    self.open_frame.grid()

    self.img_label = Label (self.open_frame, image = self.bg_image)#label for image
    self.img_label.place(x = -1, y = 20, relheight = 1)


    #Creating a label for the title
    self.title_label = Label(self.open_frame, text = "The Covid-19 Quiz",font = ("Comic Sans MS","25","bold"), bg = background_color)#title for entire window
    self.title_label.grid(row = 1)

    #label for username
    self.end_label = Label(self.open_frame, text = "Enter you name here:", bg = background_color)
    self.end_label.grid(row = 2, columnspan = 3, padx = 10, pady = 20)
    
    #creating the entry box for username
    self.entry_box = Entry(self.open_frame)
    self.entry_box.grid(row = 3, padx = 30, pady = 20)

    #creating a continue button
    self.continue_button = Button(self.open_frame, text = "Continue", bg = "#b2fca2", command = self.name_supply)
    self.continue_button.grid(row = 6,  padx = 20, pady = 20)

    #creating a quit button
    self.quit_button = Button(self.open_frame, text = "Exit", font = ("Times", "15", "bold"), bg = "Red", command = self.close_screen)
    self.quit_button.grid(row = 7)

#This function is error handling for the entry box on the starting window
  def name_supply(self):
    name = self.entry_box.get()
    if str.isalpha(name) == True and len(name) >0 and len(name) <=10:#isalpha is a function that returns something if it equals to zero
      name_record.append(name)
      self.open_frame.destroy()#destroys/clears entry box
      Start(root)
    elif str.isalpha(name) == False:
      messagebox.showerror("Please enter your username again:","Either you haven't typed your username, or you used special characters/numbers in your username, which is not allowed. Please try again.")#the messagebox is shown as a pop up, which will show the errror that needs fixing
    elif len(name) >10:#refrains from letting more than 10 characters from being written
      messagebox.showerror("Please enter your username again:","Make sure you have entered a name with up to 10 characters.")
    
  def close_screen(self):
      root.withdraw()
      open_closescrn = Close()#calling the Close class to end window 

class Close:
  def __init__(self):
    background = "lightblue"
    self.close_box = Toplevel(root)#Toplevel is used in a specific window manager, shown when called
    self.close_box.title("Program Ended")
    
    self.close_frame = Frame (self.close_box, width = 1000, height = 1000, bg = background)
    self.close_frame.grid()

    close_heading = Label (self.close_frame, text = 'Thank You for Playing!', font = ('Tw Cen Mt', 22, 'bold'), bg = background, pady = 15)
    close_heading.grid(row = 4)


  def stop_sus(self):#destroying Close and ending program 
    self.close_box.destroy()
    root.destroy()

class Start:#Start is the questions window, containing the questions, radio buttons, question_structure and test_advance
  def __init__(self, parent):
#questions written in a dictionary
    self.questions_and_answers = {
1: ["What are the most common symptoms of covid-19?", 
    'dry cough, fever, tiredness', 
    'headaches, neck pain, sore throat', 
    'rashes, chest pain, hair loss', 
    'none of the above', 
    'dry cough, fever, tiredness', 1],

2: ["What is the most commonly used covid-19 vaccine in New Zealand?", 
    'Moderna Vaccine', 
    'Johnson & Johnsons Janssen Vaccine',
    'Pfizer-BioNTech Vaccine',
    'none of the above', 
    'Pfizer-BioNTech Vaccine', 3],

3: ["What does wearing a mask do to prevent getting Covid-19?", 
    'Nothing.', 
    'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs', 
    'It prevents people from looking at your face.', 
    'none of the above', 
    'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs', 2],

4: ["Which Alert Level instructs you to stay inside your bubble, only going out for the essentials?", 
    'Alert Level 3', 
    'Alert Level 4', 
    'Alert Level 5', 
    'none of the above', 
    'Alert Level 4', 2],

5: ["Which country has the most Covid-19 cases?", 
    'Russia', 
    'United States of America', 
    'India', 
    'none of the above', 
    'United States of America', 2],

6: ["Can washing your hands prevent you from getting Covid-19?", 
    'No, It cant', 
    'Covid can only be prevented by wearing a mask', 
    'Yes, It can', 
    'none of the above', 
    'Yes, It can', 3],

7: ["What age group has a higher chance of Covid-19 being dangerous for them?",
    '3 to 10 years old', 
    '13 to 20 years old', 
    '40 to 70 years old', 
    'none of the above', 
    '40 to 70 years old', 3],

8: ["What is the official name of the Covid-19 disease?", 
    'Coronavirus Disease 2019', 
    'Coronavirus-19', 
    'Corona Virus Diesease-19', 
    'none of the above', 
    'none of the above', 5],

9: ["When did Covid-19 first start spreading around the world?", 
    'November 23rd 2019', 
    'September 11th 2019', 
    'December 31st 2019', 
    'none of the above', 
    'December 31st 2019', 3],

10: ["If you have a cold, what should you do?", 
    'Go to school/work regardless', 
    'Get a covid swab and stay home', 
    'go to the doctors', 
    'none of the above', 
    'Get a covid swab and stay home', 2],

}
    
    #constructer
    background_color = "lightblue"
    #creating frame
    self.open_frame = Frame(parent, bg = background_color, padx = 50, pady = 50)
    self.open_frame.grid(row = 1)

    #creating label widget
    self.question_label = Label(self.open_frame, text = self.questions_and_answers[qnum][0], font = ("Tw Cen Mt", "18", "bold"), padx = 10,pady = 10, bg = background_color)
    self.question_label.grid(row = 0)

    #holds the value of radio buttons
    self.Var1 = IntVar()

    #first radio Button
    self.rb1 = Radiobutton(self.open_frame, text = self.questions_and_answers[qnum][1], font = ("Helvetica", "12"), bg = "#7093ff", cursor = "spraycan", value = 1, variable = self.Var1, pady = 10)
    self.rb1.grid(row = 1, sticky = W, padx = 10, pady = 10)

    #second radio Button
    self.rb2 = Radiobutton(self.open_frame, text = self.questions_and_answers[qnum][2], font = ("Helvetica", "12"),  bg = "#7093ff", cursor = "spraycan", value = 2, variable = self.Var1, pady = 10)
    self.rb2.grid(row = 2, sticky = W, padx = 10, pady = 10)

    #third radio Button
    self.rb3 = Radiobutton(self.open_frame, text = self.questions_and_answers[qnum][3], font = ("Helvetica", "12"),  bg = "#7093ff", cursor = "spraycan", value = 3, variable = self.Var1, pady = 10)
    self.rb3.grid(row = 3, sticky = W, padx = 10, pady = 10)
    
    #fourth radio Button
    self.rb4 = Radiobutton(self.open_frame, text = self.questions_and_answers[qnum][4], font = ("Helvetica", "12"),  bg = "#7093ff", cursor = "spraycan", value = 4, variable = self.Var1, pady = 10)
    self.rb4.grid(row = 4, sticky = W, padx = 10, pady = 10)

    #confirm answer button
    self.verify_button = Button(self.open_frame, text = "Confirm", bg = "#b2fca2", command = self.test_advance)
    self.verify_button.grid(row = 5)

    #creating an exit button
    self.quit_button = Button(self.open_frame, text = "Exit", font = ("Times", "15", "bold"), bg = "Red", command = self.close_screen)
    self.quit_button.grid(row = 6)
    
    #creating score label
    self.score_label = Label(self.open_frame, text = "SCORE", font = ("Courier"),bg = background_color,)
    self.score_label.grid(row = 12, padx = 10, pady = 1)

    #to edit the already made radio buttons and question labels
  def questions_structure(self):
    randomiser()
    self.Var1.set(0)
    self.question_label.config(text = self.questions_and_answers[qnum][0])
    self.rb1.config(text = self.questions_and_answers[qnum][1])
    self.rb2.config(text = self.questions_and_answers[qnum][2])
    self.rb3.config(text = self.questions_and_answers[qnum][3])
    self.rb4.config(text = self.questions_and_answers[qnum][4])
#how the score will work and correcting answers when wrong
  def test_advance(self):
      global score
      scr_label = self.score_label
      choice = self.Var1.get()
      if len(asked)>9:
        if choice == self.questions_and_answers[qnum][6]:
          score+=1#adds to score
          scr_label.configure(text = score)
          self.verify_button.config(text = "Confirm")
          self.close_screen()
        else:
          print(choice)
          score+=0#no addition to score
          scr_label.configure(text = "The correct answer is " + self.questions_and_answers[qnum][5])
          self.verify_button.config(text = "Confirm")
          self.close_screen()
      else:
        if choice == 0:
          self.verify_button.config(text = "Try Again, you haven't selected anything.")#error handling when user didn't select a button
          choice = self.Var1.get()
        else:
          if choice == self.questions_and_answers[qnum][6]:
            score+=1
            scr_label.configure(text = score)
            self.verify_button.config(text = "Confirm")
            self.questions_structure()
          else:
            print(choice)
            score+=0
            scr_label.configure(text= "correct answer was " + self.questions_and_answers[qnum][5])
            self.verify_button.config(text = "Confirm")
            self.questions_structure()


  def close_screen(self):#ends program
    root.withdraw()
    open_endscrn = Close()


randomiser()
if __name__ == "__main__":
  root = Tk() #creating the window 
  root.title("Covid-19 Quiz")#title of window
  quizzing_instance = BeginQuiz(root)#calling starting window
  root.mainloop()#looping so window keeps appearing
