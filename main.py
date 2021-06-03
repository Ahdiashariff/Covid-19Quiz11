from tkinter import*
from PIL import Image, ImageTk
import random


global questions_and_answers
name_collection = []
asked = []
score = 0

questions_and_answers={
1:["What are the most common symptoms of covid-19?",'dry cough, fever, tiredness','headaches, neck pain, sore throat', 'chest pain, conjunctivitis, sneezing', 'rashes','chest pain, hair loss',1],
2:["What is the most commonly used covid-19 vaccine in New Zealand?",'Moderna Vaccine', 'Johnson & Johnson’s Janssen Vaccine', 'Pfizer-BioNTech Vaccine',3],
3:["What does wearing a mask do to prevent getting covid-19?",'Nothing.', 'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs' , 'It prevents people from looking at your face.',2],
4:["Which Alert Level instructs you to stay inside your bubble, only going out for the essentials?",'Alert Level 3','Alert Level 4', 'Alert Level 5',2],
5:["Which country has the most Covid-19 cases?",'Russia', 'United States of America', 'India',2]


}

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
    randomiser()


class BeginQuiz:
    def __init__(self, parent):#constructer
      background_color="PeachPuff"
      
      #frame set up 
      self.quiz_frame= Frame(parent, bg= background_color, padx=50, pady=50)
      self.quiz_frame.grid()

      #image set up
      self.bg_image= Image.open("covid-19.jpg")
      self.bg_image= self.bg_image.resize((300,250), Image.ANTIALIAS )
      self.bg_image= ImageTk.PhotoImage(self.bg_image)

      self.main_frame = Frame (parent, bg= background_color)
      self.main_frame.grid()

      self.image_label = Label (self.main_frame, image=self.bg_image)
      self.image_label.place(x=100, y=100, relheight=1)

      #Create a label widget for the title
      self.title_label = Label(self.quiz_frame, text= "The Covid-19 Quiz",font=("Comic Sans MS","25","bold"), bg=background_color)
      self.title_label.grid(row=0)

      #label for the user Name
      self.end_label= Label(self.quiz_frame, text="Enter you name here:", bg=background_color)
      self.end_label.grid(row=1, columnspan=3, padx=20, pady=20)


      #create the entry box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=20, pady=20)


      #creating a continue button
      self.continue_button = Button(self.quiz_frame, text="Continue", bg="#C5CAE9", command=self.name_collection)
      self.continue_button.grid(row=3,  padx=20, pady=20)   


    def name_collection(self):
      name=self.entry_box.get()
      name_collection.append(name)#add name to names list declared at the beginning
      self.quiz_frame.destroy()#destroy the starter
      Quiz(root)#we will create a new class Quiz and create an instance of it after we get the name,
      #we destroy starter the quiz_frame and open the question quiz_frame instead which will be part of the Quiz object


  def close_screen(self):
    root.withdraw()
    open_endscrn=End()

    class Close:
      def__init__(self):

     

class Quiz:
   def __init__(self, parent):#constructer
      background_color="PeachPuff"
      #frame set-up 
      self.quiz_frame= Frame(parent, bg= background_color, padx=50, pady=50)
      self.quiz_frame.grid()

      #label widget heading set-up
      self.questions_label = Label (self.quiz_frame, text = questions_and_answers[qnum][0], font=("Tw Cen Mt", "18", "bold"), padx=10,pady=10, bg=background_color)
      self.questions_label.grid(row=0)

      #holds value of radio buttons
      self.Var1=IntVar()


      #first radio Button
      self.rb1 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
      self.rb1.grid(row=1, sticky=W, padx=10,pay=10)

      #second radio Button
      self.rb2 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
      self.rb2.grid(row=2, sticky=W)

      #third radio Button
      self.rb3 = Radiobutton (self.quiz_frame, text = questions_and_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
      self.rb3.grid(row=3, sticky=W)

      #confirm answer button
      self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="blue")
      self.confirm_button.grid(row=4)

      def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])



  #randomly chooses a question from qnum
      randomiser()

if __name__ =="__main__":
    root = Tk()  #creating the window 
    root.title("NZ Covid-19 Quiz")   #title
    quiz_instance = BeginQuiz(root)
    root.mainloop()