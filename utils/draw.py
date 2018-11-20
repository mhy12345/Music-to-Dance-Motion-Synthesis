import numpy as np
import cv2
import json

CANVAS_SIZE = (400,600,3)

def draw(frames):
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
        cv2.imshow('canvas',np.flip(cvs,0))
        cv2.waitKey(0)
    pass

if __name__ == '__main__':
    with open('../DANCE_C_1/skeletons.json','r') as fin:
        data = json.load(fin)
    draw(np.array(data['skeletons']))
