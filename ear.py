#ecoding=utf8
#ear:读取音频流，识别出非静音片断，并输出到队列
import threading
class Ear:
    #audio_stream: 音频输入队列
    #audio_slice:音频输出片断队列
    def __init__(self, audio_stream, audio_slice):
        self.audio_stream = audio_stream
        self.audio_slice = audio_slice
    def start_listen(self):
        threading.Thread(target=self.echo).start()
    def echo(self):
        while(True):
            if(not self.audio_stream.empty()):
                audio =  self.audio_stream.get_nowait()
                print "audio",audio
                self.audio_slice.put(audio)
    
