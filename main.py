from tkinter import *


class BeginQuiz:
    def __init__(self, parent):#constructer
      background_color="PeachPuff"

      #frame set up 
      self.quiz_frame= Frame(parent, bg= background_color, padx=50, pady=50)
      self.quiz_frame.grid()


      #Create a label widget for the title
      self.title_label = Label(self.quiz_frame, text= "Welcome to the Covid-19 Quiz!",font=("Comic Sans MS","39","bold"), bg=background_color)
      self.title_label.grid(row=0)

      #label for the user Name
      self.end_label= Label(self.quiz_frame, text="Please enter your name:", bg=background_color)
      self.end_label.grid(row=1, columnspan=3, padx=20, pady=20)


      #create the entry box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=20, pady=20)


      #creating a continue button
      self.continue_button = Button(self.quiz_frame, text="Continue", bg="#C5CAE9", command=self.name_collection)
      self.continue_button.grid(row=3,  padx=20, pady=20)        
        

    def name_collection(self):
      name=self.entry_box.get()
      names_list.append(name)#add name to names list declared at the beginning
      self.quiz_frame.destroy()#destroy the starter
      Quiz(root)#we will create a new class Quiz and create an instance of it after we get the name,
      #we destroy starter the quiz_frame and open the question quiz_frame instead which will be part of the Quiz object




if __name__ =="__main__":
    root = Tk()  #create the window 
    root.title("NZ Covid-19 Quiz")   #title of the window
    quiz_instance = BeginQuiz(root)
    root.mainloop()  #so the window doesn't disappear 