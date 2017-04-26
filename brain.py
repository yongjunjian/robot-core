#encoding=utf8
import threading
class Brain:
    def __init__(self, audio_stream, video_stream, words_stream):
        self.audio_stream = audio_stream
        self.video_stream = video_stream
        self.words_stream =  words_stream
    def start_process(self):
        threading.Thread(target=self.echo).start()
    def echo(self):
        count = 0 
        while(True):
            if(not self.audio_stream.empty()):
                audio =  self.audio_stream.get_nowait()
                print "audio received by brain",audio
                self.words_stream.put("words"+str(count))
                count += 1
            if(not self.video_stream.empty()):
                video =  self.video_stream.get_nowait()
                print "video received by brain",video

