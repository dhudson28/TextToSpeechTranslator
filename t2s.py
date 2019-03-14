import googletrans
import sys
from PyQt4 import QtCore, QtGui, uic
from gtts import gTTS
from playsound import playsound

translator = googletrans.Translator()

qtCreatorFile = "t2s.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def lang_select(langSEL):
        if langSEL == 'Dutch':
            lang = 'de'
        elif langSEL == 'Spanish':
            lang = 'es'
        elif langSEL == 'French':
            lang = 'fr'
        elif langSEL == 'Russian':
            lang = 'ru'
        elif langSEL == 'Korean':
            lang = 'ko'
        elif langSEL == 'Japanese':
            lang = 'ja'
        elif langSEL == 'Chinese':
            lang = 'zh-CN'
        else:
            lang = 'en'
        return lang
    
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def text_to_speech(self):
        
        lang = lang_select(self.LangCombo.currentText())    
        talkIn = translator.translate(str(self.text_input.toPlainText()), dest=lang).text
        #talkIn = str(self.LangCombo.currentText())
        speech = gTTS(talkIn, lang)
        speech.save('speech.mp3')
        playsound('speech.mp3')
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.speech_button.clicked.connect(self.text_to_speech)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
