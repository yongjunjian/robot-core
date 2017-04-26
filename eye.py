#encoding=utf8
#ear:读取视频流，处理后压入图像帧队列
import threading
class Eye:
    #video_stream: 音频输入队列
    #frame_stream:音频输出片断队列
    def __init__(self, video_stream, frame_seq):
        self.video_stream = video_stream
        self.frame_seq = frame_seq
    def start_watch(self):
        threading.Thread(target=self.echo).start()
    def echo(self):
        while(True):
            if(not self.video_stream.empty()):
                video =  self.video_stream.get_nowait()
                print "video",video
                self.frame_seq.put(video)
 
