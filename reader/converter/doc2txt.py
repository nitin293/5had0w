import textract
from gtts import gTTS
import os

text = textract.process("../pdf.pdf")

# text = text.decode('ascii')
# text =  text.split("\\n")
text = text.decode('utf-8')


def text_to_voice(text):
    try:
        convert = gTTS(text, lang="en", slow=False)
        convert.save("../output/speak.mp3")
        os.system("mpg321 ../output/speak.mp3 -quiet")
        print(text)
        os.system("rm ../output/speak.mp3")
    except AssertionError:
        pass

