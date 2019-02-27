import numpy as np
import os
import cv2
import json
import logging
from moviepy.editor import *
logger = logging.getLogger(__name__)

CANVAS_SIZE = (400,600,3)
videoWriter = None

def draw(frames, export_to_file=False):
    global CANVAS_SIZE
    global videoWriter
    frames[:,:,0] += CANVAS_SIZE[0]//2
    frames[:,:,1] += CANVAS_SIZE[1]//2
    for i in range(len(frames)):
        cvs = np.ones(CANVAS_SIZE)
        color = (0,0,0)
        hlcolor = (255,0,0)
        dlcolor = (0,0,255)
        for points in frames[i]:
            cv2.circle(cvs,(int(points[0]),int(points[1])),radius=4,thickness=-1,color=hlcolor)
        frame = frames[i]
        cv2.line(cvs, (int(frame[0][0]), int(frame[0][1])), (int(frame[1][0]), int(frame[1][1])), color, 2)	
        cv2.line(cvs, (int((frame[0][0]+frame[1][0])/2), int((frame[0][1]+frame[1][1])/2)), (int((frame[3][0]+frame[12][0])/2), int((frame[3][1]+frame[12][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[3][0]), int(frame[3][1])), (int((frame[3][0]+frame[12][0])/2), int((frame[3][1]+frame[12][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[3][0]), int(frame[3][1])), (int(frame[4][0]), int(frame[4][1])), color, 2)
        cv2.line(cvs, (int(frame[4][0]), int(frame[4][1])), (int(frame[5][0]), int(frame[5][1])), color, 2)
        cv2.line(cvs, (int(frame[5][0]), int(frame[5][1])), (int(frame[6][0]), int(frame[6][1])), color, 2)
        cv2.line(cvs, (int(frame[12][0]), int(frame[12][1])), (int((frame[3][0]+frame[12][0])/2), int((frame[3][1]+frame[12][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[12][0]), int(frame[12][1])), (int(frame[13][0]), int(frame[13][1])), color, 2)
        cv2.line(cvs, (int(frame[13][0]), int(frame[13][1])), (int(frame[14][0]), int(frame[14][1])), color, 2)
        cv2.line(cvs, (int(frame[14][0]), int(frame[14][1])), (int(frame[15][0]), int(frame[15][1])), color, 2)
        cv2.line(cvs, (int(frame[2][0]), int(frame[2][1])), (int((frame[3][0]+frame[12][0])/2), int((frame[3][1]+frame[12][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[2][0]), int(frame[2][1])), (int(frame[7][0]), int(frame[7][1])), color, 2)
        cv2.line(cvs, (int(frame[7][0]), int(frame[7][1])), (int(frame[8][0]), int(frame[8][1])), color, 2)
        cv2.line(cvs, (int(frame[8][0]), int(frame[8][1])), (int(frame[9][0]), int(frame[9][1])), color, 2)
        cv2.line(cvs, (int(frame[9][0]), int(frame[9][1])), (int((frame[10][0]+frame[11][0])/2), int((frame[10][1]+frame[11][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[10][0]), int(frame[10][1])), (int(frame[11][0]), int(frame[11][1])), color, 2)
        cv2.line(cvs, (int(frame[2][0]), int(frame[2][1])), (int(frame[16][0]), int(frame[16][1])), color, 2)
        cv2.line(cvs, (int(frame[16][0]), int(frame[16][1])), (int(frame[17][0]), int(frame[17][1])), color, 2)
        cv2.line(cvs, (int(frame[17][0]), int(frame[17][1])), (int(frame[18][0]), int(frame[18][1])), color, 2)
        cv2.line(cvs, (int(frame[18][0]), int(frame[18][1])), (int((frame[19][0]+frame[20][0])/2), int((frame[19][1]+frame[20][1])/2)), color, 2)
        cv2.line(cvs, (int(frame[19][0]), int(frame[19][1])), (int(frame[20][0]), int(frame[20][1])), color, 2)

        '''
        for j in range(23):
            cv2.putText(cvs,str(j),(int(frame[j][0]),int(frame[j][1])),cv2.FONT_HERSHEY_SIMPLEX,.4, (155, 0, 255), 1, False)
            '''
        if export_to_file:
            img8 = (np.flip(cvs,0)*(2**8-1)).astype(np.uint8)
            videoWriter.write(img8)
        else:
            cv2.imshow('canvas',np.flip(cvs,0))
            cv2.waitKey(0)
    pass

def exportMP3(name,speed=25):
    global videoWriter
    with open('../%s/config.json'%name) as fin:
        config = json.load(fin)
    print(config)
    with open('../%s/skeletons.json'%name,'r') as fin:
        data = np.array(json.load(fin)['skeletons'])
    fourcc = cv2.VideoWriter_fourcc('I','4','2','0') #opencv3.0
    videoWriter = cv2.VideoWriter('exports/'+name+'.avi', fourcc, speed, (600, 400))
    draw(data,export_to_file=True)
    videoWriter.release()
    os.system('ffmpeg -i exports/%s.avi exports/%s.mp4'%(name,name))
    os.system('rm exports/%s.avi'%name)

    movie_dance = VideoFileClip('./exports/%s.mp4'%name,audio=False)
    movie_music = AudioFileClip('../'+name+'/audio.mp3').subclip(config['start_position']/25, config['end_position']/25)
    movie_dance = movie_dance.set_audio(movie_music)
    movie_dance.write_videofile("./exports/%s.avi"%name,fps=25,codec='libx264')

    os.system('rm exports/%s.mp4'%name)
    os.system('ffmpeg -i exports/%s.avi exports/%s.mp4'%(name,name))
    os.system('rm exports/%s.avi'%name)

    logger.info('Finish <%s>'%name)

if __name__ == '__main__':
    name = 'DANCE_W_1'
    import os
    import re
    dirs = os.listdir('../')
    for name in dirs:
        if name[:5] != 'DANCE':
            continue
        print(name)
        exportMP3(name)
