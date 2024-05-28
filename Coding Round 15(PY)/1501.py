# Python Project - 01 
# Build a Eye Controllable Gesture Mouse 
# REQUIREMENT 
# 1. Modules - openCV, mediapipe, pyautogui 
# 2. Version - Any Version above 3.3.1 


# import the opencv library 
import cv2  
import mediapipe as mp
import pyautogui as py

# define a video capture object q
vid = cv2.VideoCapture(0)  

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

screen_w, screen_h = py.size()

while(True): 

    rt, frame = vid.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB )
    output = face_mesh.process(rgb_frame)

    frame_h, frame_w, _ = frame.shape
    landmark_points = output.multi_face_landmarks
    # print(landmark_points)
    # This step prints the landmark points onto the console 

    if landmark_points:

        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):

            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,0))
            
            if id == 1:
                
                screen_x = screen_w/ frame_w * x
                screen_y = screen_h/ frame_h *y
                py.moveTo(screen_x,screen_y)


        left = [landmarks[145], landmarks[159]]

        for landmark in left:

            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,255))
            
        if(left[0].y - left[1].y < 0.004):

            py.click()
            py.sleep(1)
            

    cv2.imshow("Eye Controllable Mouse", frame)
	
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

