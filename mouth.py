#encoding=utf8
import threading
#从文字流中读取文字信息，合并声音后输出
class Mouth:
    def __init__(self, words_stream, audio_stream):
        self.words_stream = words_stream;
        self.audio_stream = audio_stream
    def start_speak(self):
        threading.Thread(target=self.echo).start()
    def echo(self):
        while(True):
            if(not self.words_stream.empty()):
                words =  self.words_stream.get_nowait()
                print "words",words
                self.audio_stream.put(words)
 
