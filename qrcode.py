
#Gerekli kütüphaneleri import ediyoruz
import qrcode
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont




class Window(QWidget):
    
 
    # Window
    def __init__(self):
        app = QApplication(sys.argv) #!!! 1
        
        super().__init__()
        
        self.setGeometry(50, 50, 470,600)  #pencerenin boyutu
        self.setWindowTitle("PyQt Basic")  #pencerenin basligi
        self.setStyleSheet("background-color: #6e7b8b;") #pencerenin arka plan rengi
        
        self.entry()      
        self.show()
        sys.exit(app.exec()) #!!! 2
    
    def entry(self):
        
        
#dosya adının yazılacağı yeri oluşturuyoruz
  
        self.textBox = QLineEdit(self)
        self.textBox.setPlaceholderText("dosya adı")
        self.textBox.move(25,25)
        self.textBox.resize(400,100)
        self.textBox.setStyleSheet("background-color :white")
        
#url nin yazılacağı yeri oluşturuyoruz        
        
        self.textBox2 = QLineEdit(self)
        self.textBox2.setPlaceholderText("URL ")
        self.textBox2.move(25,175)
        self.textBox2.resize(400,100)
        self.textBox2.setStyleSheet("background-color :#ee6363")
        #ee6363ee6363
# qr code un renginin seçileceği yeri oluşturuyoruz       
        
        self.textBox3 = QLineEdit(self)
        self.textBox3.setPlaceholderText("qr kodun rengini girin(mavi,siyah,kirmizi,sari,mor) ")
        self.textBox3.move(25,325)
        self.textBox3.resize(400,100)
        self.textBox3.setStyleSheet("background-color :#ee5c42")
        
        
#save butonunu oluşturuyoruz

        buton1 = QPushButton("Save",self)
        buton1.move(25,475)
        buton1.clicked.connect(self.QRFunction)
        buton1.resize(400,100)
        buton1.setStyleSheet("background-color :#cd919e")
        buton1.clicked.connect(self.QRFunction)
        
        
 #Qr fonksiyonunu oluşturuyoruz
        
    def QRFunction(self):
        
        url = self.textBox2.text()
        
        dosya_adi=self.textBox.text()
        
       
# kullanıcıdan aldığımız türkçe inputu ingilizceye çeviriyoru

        
        if self.textBox3.text()=="mavi": 
            renk2="blue"
            
        elif self.textBox3.text()=="siyah":
            renk2="black"
            
        elif self.textBox3.text()=="kirmizi":
            renk2="red"
            
        elif self.textBox3.text()=="sari":
            renk2="yellow"
            
        elif self.textBox3.text()=="mor":
            renk2="purple"
            
        else:
            renk2="black"
                

# aldığımız urlyi qr koda çevirecek kodu yazıyoruz 

        qr=qrcode.QRCode(version =1,                      
                         box_size=20,
                         border=2)
        qr.add_data(url)
        
        img=qr.make_image(fill_color=renk2,back_color="white")
        
        img.save(dosya_adi+".png")
    
        
       
        
window = Window()
