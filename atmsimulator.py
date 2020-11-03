from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm:
    def __init__(self,root):
        self.root=root
        blank_space=" "
        self.root.title(110*blank_space+ "ATM SYSTEM")
        self.root.geometry("800x760+280+0")
        self.root.configure(bg='gainsboro')
#=====================================Frames===============================================================
        MainFrame=Frame(self.root, bd=20, width=782, height=700, relief=RIDGE)
        MainFrame.grid()
        TopFrame1=Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1,column=0,padx=8)
        TopFrame2=Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0,column=0,padx=8)

        TopFrame2left=Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2left.grid(row=0,column=0,padx=3)

        TopFrame2Mid=Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0,column=1,padx=3)

        TopFrame2Right=Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0,column=2,padx=3)
#=====================================Function============================================================
        def enter_pin():
            PinNo=self.txtReceipt.get("1.0","end-1c")
            if((PinNo==str("0000")) or (PinNo==("5749")) or (PinNo==str("7645")) or (PinNo==str("6489"))):
                self.txtReceipt.delete("1.0",END)

                self.txtReceipt.insert(END,'\t\t ATM' +"\n\n")
                self.txtReceipt.insert(END,'withdraw\t\t\t Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END,'cash with Receipt\t\t\t Deposit'+ "\n\n\n\n")
                self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' +"\n\n\n\n")
                self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement'+ "\n\n\n")
            

#=====================================leftbuton====================================================
                self.image_arrow_left=PhotoImage(file="lArrow.png")
                self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=NORMAL,command=withdraw, image=self.image_arrow_left).grid(row=0,column=0,padx=2,pady=2)

                self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=NORMAL,command=withdraw, image=self.image_arrow_left).grid(row=1,column=0,padx=2,pady=2)

                self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=NORMAL,command=balance, image=self.image_arrow_left).grid(row=2,column=0,padx=2,pady=2)

                self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=NORMAL,command=statement, image=self.image_arrow_left).grid(row=3,column=0,padx=2,pady=2)

#=======================================rightbutton====================================================
                self.image_arrow_right=PhotoImage(file="rArrow.png")
                self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=loan, image=self.image_arrow_right).grid(row=0,column=0,padx=2,pady=2)

                self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=deposit, image=self.image_arrow_right).grid(row=1,column=0,padx=2,pady=2)

                self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=request_new_pin, image=self.image_arrow_right).grid(row=2,column=0,padx=2,pady=2)

                self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=statement, image=self.image_arrow_right).grid(row=3,column=0,padx=2,pady=2)

            else:
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"\t\t INVALID PIN")
            
#============================================================clear=================================================================================
        def clear():
            self.txtReceipt.delete("1.0",END)
            #=====================================leftbuton====================================================
            self.image_arrow_left=PhotoImage(file="lArrow.png")
            self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED, image=self.image_arrow_left).grid(row=0,column=0,padx=2,pady=2)

            self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED, image=self.image_arrow_left).grid(row=1,column=0,padx=2,pady=2)

            self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED, image=self.image_arrow_left).grid(row=2,column=0,padx=2,pady=2)

            self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED, image=self.image_arrow_left).grid(row=3,column=0,padx=2,pady=2)
            #=======================================rightbutton====================================================
            self.image_arrow_right=PhotoImage(file="rArrow.png")
            self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.image_arrow_right).grid(row=0,column=0,padx=2,pady=2)

            self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.image_arrow_right).grid(row=1,column=0,padx=2,pady=2)

            self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.image_arrow_right).grid(row=2,column=0,padx=2,pady=2)

            self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=self.image_arrow_right).grid(row=3,column=0,padx=2,pady=2)
#==============================================================================================================================================================
        def insert0():
            self.txtReceipt.insert(END,"0")

        def insert1():
            self.txtReceipt.insert(END,"1")

        def insert2():
            self.txtReceipt.insert(END,"2")

        def insert3():
            self.txtReceipt.insert(END,"3")

        def insert4():
            self.txtReceipt.insert(END,"4")

        def insert5():
            self.txtReceipt.insert(END,"5")

        def insert6():
            self.txtReceipt.insert(END,"6")

        def insert7():
            self.txtReceipt.insert(END,"7")

        def insert8():
            self.txtReceipt.insert(END,"8")

        def insert9():
            self.txtReceipt.insert(END,"9")

        def cancel():
            cancel=tkinter.messagebox.askyesno("ATM","Are You Sure to EXIT")
            if cancel>0:
                self.root.destroy()
                return

        def withdraw():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def loan():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"loan Rs.")
            self.txtReceipt.focus_set()

        def deposit():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def request_new_pin():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"\t\tWELCOME TO RBI\n")
            self.txtReceipt.insert(END,"Your New Pin will Be send to Your Home Address\n")
            self.txtReceipt.insert(END,'withdraw\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END,'cash with Receipt\t\t\t Deposit'+ "\n\n\n\n")
            self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' +"\n\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement'+ "\n\n\n")
            self.txtReceipt.insert(END,"\t\tTHANKS YOU FOR USING RBI ATM!!\n")

        def balance():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,"\t\tWELCOME TO RBI\n")
            self.txtReceipt.insert(END,'NET BALANCE Rs 3000'+"\n")
            self.txtReceipt.insert(END,'withdraw\t\t\t Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END,'cash with Receipt\t\t\t Deposit'+ "\n\n\n\n")
            self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' +"\n\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement\t\t\t Print Statement'+ "\n\n\n")
            self.txtReceipt.insert(END,"\t\tTHANKS YOU FOR USING RBI ATM!!\n")

        def statement():
            pinNo1=str(self.txtReceipt.get("1.0","end-1c"))
            pinNo2=str(pinNo1)
            pinNo3=float(pinNo2)
            pinNo4=float(3000-(pinNo3))
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\n\t'+ str(pinNo4)+"\n\n")
            self.txtReceipt.insert(END,'\t\t\t\n  NET BALANCE Rs'+ str(pinNo4)+ "\t\t\n\n")

           
            self.txtReceipt.insert(END,"\tTHANKS YOU FOR USING RBI ATM!!\n")

            
            
#=====================================widgets======================================================        
        self.txtReceipt= Text(TopFrame2Mid, width=42, height=17, bd=12, font=('aerial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0, padx=6)
#=====================================leftbuton====================================================
        self.image_arrow_left=PhotoImage(file="lArrow.png")
        self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED, command=withdraw,image=self.image_arrow_left).grid(row=0,column=0,padx=2,pady=2)

        self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED,command=withdraw, image=self.image_arrow_left).grid(row=1,column=0,padx=2,pady=2)

        self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED,command=balance, image=self.image_arrow_left).grid(row=2,column=0,padx=2,pady=2)

        self.btnArrowL=Button(TopFrame2left, width=160, height=60, state=DISABLED,command=statement, image=self.image_arrow_left).grid(row=3,column=0,padx=2,pady=2)
#=======================================rightbutton====================================================
        self.image_arrow_right=PhotoImage(file="rArrow.png")
        self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=loan, image=self.image_arrow_right).grid(row=0,column=0,padx=2,pady=2)

        self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=deposit, image=self.image_arrow_right).grid(row=1,column=0,padx=2,pady=2)

        self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=request_new_pin,image=self.image_arrow_right).grid(row=2,column=0,padx=2,pady=2)

        self.btnArrowR=Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=statement, image=self.image_arrow_right).grid(row=3,column=0,padx=2,pady=2)


#===============================================pin number button====================================================
        self.image1=PhotoImage(file="one.png")
        self.btn1=Button(TopFrame1, width=160, height=60,command=insert1,  image=self.image1).grid(row=2,column=0,padx=6,pady=4)

        self.image2=PhotoImage(file="two.png")
        self.btn2=Button(TopFrame1, width=160, height=60,command=insert2,  image=self.image2).grid(row=2,column=1,padx=6,pady=4)

        self.image3=PhotoImage(file="three.png")
        self.btn3=Button(TopFrame1, width=160, height=60,command=insert3, image=self.image3).grid(row=2,column=2,padx=6,pady=4)

        self.image_ce=PhotoImage(file="cancel.png")
        self.btnce=Button(TopFrame1, width=160, height=60,command=cancel, image=self.image_ce).grid(row=2,column=3,padx=6,pady=4)
#=========================================================================================================================
        self.image4=PhotoImage(file="four.png")
        self.btn4=Button(TopFrame1, width=160, height=60,command=insert4,  image=self.image4).grid(row=3,column=0,padx=6,pady=4)

        self.image5=PhotoImage(file="five.png")
        self.btn5=Button(TopFrame1, width=160, height=60,command=insert5,  image=self.image5).grid(row=3,column=1,padx=6,pady=4)

        self.image6=PhotoImage(file="six.png")
        self.btn6=Button(TopFrame1, width=160, height=60,command=insert6,  image=self.image6).grid(row=3,column=2,padx=6,pady=4)

        self.imagecr=PhotoImage(file="clear.png")
        self.btncr=Button(TopFrame1, width=160, height=60,command=clear,  image=self.imagecr).grid(row=3,column=3,padx=6,pady=4)
#==============================================================================================================================
        self.image7=PhotoImage(file="seven.png")
        self.btn4=Button(TopFrame1, width=160, height=60,command=insert7,  image=self.image7).grid(row=4,column=0,padx=6,pady=4)

        self.image8=PhotoImage(file="eight.png")
        self.btn8=Button(TopFrame1, width=160, height=60,command=insert8,  image=self.image8).grid(row=4,column=1,padx=6,pady=4)

        self.image9=PhotoImage(file="nine.png")
        self.btn9=Button(TopFrame1, width=160, height=60,command=insert9,  image=self.image9).grid(row=4,column=2,padx=6,pady=4)

        self.image_er=PhotoImage(file="enter.png")
        self.btn_er=Button(TopFrame1, width=160, height=60,command=enter_pin,  image=self.image_er).grid(row=4,column=3,padx=6,pady=4)

#==============================================================================================================================
        self.imagesp1=PhotoImage(file="empty.png")
        self.btn_sp1=Button(TopFrame1, width=160, height=60,  image=self.imagesp1).grid(row=5,column=0,padx=6,pady=4)

        self.image0=PhotoImage(file="zero.png")
        self.btn0=Button(TopFrame1, width=160, height=60,command=insert0, image=self.image0).grid(row=5,column=1,padx=6,pady=4)

        self.imagesp2=PhotoImage(file="empty.png")
        self.btnsp2=Button(TopFrame1, width=160, height=60,  image=self.imagesp2).grid(row=5,column=2,padx=6,pady=4)

        self.imagesp3=PhotoImage(file="empty.png")
        self.btnsp3=Button(TopFrame1, width=160, height=60,  image=self.imagesp3).grid(row=5,column=3,padx=6,pady=4)


if(__name__=='__main__'):
    root=Tk()
    application=atm(root)
    root.mainloop()
    
