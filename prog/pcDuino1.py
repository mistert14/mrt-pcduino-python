from pyduino import *
import Tkinter as tk
import re
import time

class App():
    def __init__(self):
		self.setup()
		self.root = tk.Tk()
		self.label = tk.Label(text="0")
		self.label.pack()
		self.timer=0
		for i in range(8):
			tk.Button(self.root, text='False'+str(i+1), command=lambda x=i+1: self.toggle(x)).pack(padx=5, pady=5)
	        b = tk.Button(self.root, text='quit', command=self.root.quit)
	        b.pack(padx=10, pady=10)
	        b.focus_set()
		self.update_timer()
		self.root.mainloop()
    def update_timer(self):
		self.timer+=1
		self.label.configure(text=str(self.timer))
		self.root.after(1000,self.update_timer)
		return	
		
    def strip_chars(self,st):
		pat="[0-9]+$"
		prog = re.compile(pat)
		result=prog.search(st)
		if result:
			return result.group()
		else:
			return -1
    def setup(self):
		
		pinMode(8,INPUT)
		pinMode(9,INPUT)
		pinMode(10,INPUT)
		pinMode(11,INPUT)
		pinMode(12,INPUT)
		pinMode(13,INPUT)
		for i in range(8):
			pinMode(i,OUTPUT)
			digitalWrite(i,LOW)
		
    def toggle(self,x):
		
		
		theKeys=self.root.children.keys()
		for i in range(len(theKeys)):
			wdg=self.root.children[theKeys[i]]
			if (self.strip_chars(wdg['text']) == str(x)):
				
				if wdg['text'] == 'False'+str(x):
					Serial.println("sortie "+self.strip_chars(wdg['text'])+" =  1")
					wdg['text']='True'+str(x)
					digitalWrite(x-1,HIGH)
					return
				
				if wdg['text'] == 'True'+str(x):
					Serial.println("sortie "+self.strip_chars(wdg['text'])+" =  0")
					wdg['text']='False'+str(x)
					digitalWrite(x-1,LOW)

if __name__=="__main__":
	app = App()
	
	
	
