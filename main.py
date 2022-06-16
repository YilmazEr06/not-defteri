import sys
from PyQt5.QtWidgets import *
sekme=[]
class menubar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a=200
        self.b=150
        self.c=500
        self.d=600
        self.setGeometry(self.a, self.b,self.c, self.d)
        self.setWindowTitle("Not Defteri")
        self.bar()

        self.arayuz()
        self.show()
    def kapat(self):
        qApp.closeAllWindows()

    def ac(self):
        aUrl =QFileDialog.getOpenFileName(self,"seçiniz","","Metin Belgesi (*.txt)")
        if True:
            Url =aUrl[0]
            with open(Url,"r",encoding="utf=8") as dosya:
                icerik =dosya.read()
                sekme.append(Url)
                print(icerik)
            self.name=Url.split("/")[-1:][0]
            self.aba=Not(self.name,self,icerik)



    def bar(self):
        menu = self.menuBar()

        dosya = menu.addMenu("Dosya")
        exit = menu.addMenu("Çıkış")

        dosyaac = QAction("Dosya aç", self)
        dosyaac.setShortcut("Ctrl+O")
        kaydet = QAction("Kaydet", self)
        kaydet.setShortcut("Ctrl+S")
        kapat = QAction("Kapat", self)

        dosya.addAction(dosyaac)
        dosya.addAction(kaydet)
        exit.addAction(kapat)


        kapat.triggered.connect(self.kapat)
        dosyaac.triggered.connect(self.ac)

        kaydet.triggered.connect(self.kaydet)
    def kaydet(self):
        sekmeno=self.sekmelerbeta.currentIndex()

        with open(sekme[sekmeno],"w",encoding="utf=8") as dosya:
            dosya.write(self.aba.text)
            self.sekmelerbeta.setTabText(sekmeno,self.name.split("*")[0])

    def arayuz(self):
        anawidget=QWidget()

        self.sekmelerbeta =QTabWidget()
        self.sekmelerbeta.setTabsClosable(True)
        self.sekmelerbeta.setMovable(True)
        self.sekmelerbeta.setTabShape(1)

        self.altkisim = QStatusBar()



        dikey=QVBoxLayout()
        i=self.sekmelerbeta.count()


        self.sekmelerbeta.tabCloseRequested.connect(self.sekemkapa)
        dikey.addWidget(self.sekmelerbeta)
        dikey.addWidget(self.altkisim)
        anawidget.setLayout(dikey)
        self.setCentralWidget(anawidget)

    def sekemkapa(self,index):
        print("a")
        widget = self.sekmelerbeta.widget(index)
        widget.deleteLater()
        self.sekmelerbeta.tabRemoved(index)


class Not(QWidget):
    def __init__(self,baslik,nereye,icerik):
        super().__init__()
        self.baslik = baslik
        self.icerik=icerik
        self.metin = QTextEdit()
        self.nereye=nereye
        dikey=QVBoxLayout()

        self.metin.textChanged.connect(self.degisti)



        self.metin.setText(self.icerik)





        dikey.addWidget(self.metin)
        self.setLayout(dikey)
        nereye.sekmelerbeta.addTab(self,self.baslik)
        i=a.sekmelerbeta.count()
        a.sekmelerbeta.setCurrentIndex(i-1)

    def degisti(self):
        self.text = self.metin.toPlainText()
        harf =len(self.text)
        karaktersayisi = len(self.text.split())
        i= a.sekmelerbeta.currentIndex()
        a.sekmelerbeta.setTabText(i,self.baslik+"*")

        a.altkisim.showMessage("harf sayısı: " + str(harf) + "  karakter sayısı: " + str(karaktersayisi))








uygulama =QApplication(sys.argv)
a = menubar()
sys.exit(uygulama.exec_())