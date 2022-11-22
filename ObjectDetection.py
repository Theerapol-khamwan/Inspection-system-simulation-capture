import cv2

def colorProfiles(n):
    if n == 0 :
        name = "Pepsi"
        flavor = "Cola flavor"
        color = "color blue"
        hsv_lower = ( 95,100,100)
        hsv_upper = (115,255,255)
        return (name,flavor,color,hsv_lower,hsv_upper)
    elif n == 1 :
        name = "Sprite"
        flavor = "lemon lime flavor"
        color = "color green"
        hsv_lower = ( 57,72,0)
        hsv_upper = (83,255,255)
        return (name,flavor,color,hsv_lower,hsv_upper)
    elif n == 2 :
        name = "Coke"
        flavor = "Cola flavor"
        color = "color red"
        hsv_lower = ( 142,92,0)
        hsv_upper = (179,255,255)
        return (name,flavor,color,hsv_lower,hsv_upper)
    elif n == 3 :
        name = "Root Beer"
        flavor = "Root Beer Cola flavor"
        color = "color Brown"
        hsv_lower = ( 0,10,30)
        hsv_upper = (20,255,150)
        return (name,flavor,color,hsv_lower,hsv_upper)
    
    

frame = cv2.imread("test1.png")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
rects = {}

for i in range(4):
    name,flavor,color, hsv_lower, hsv_upper = colorProfiles(i)
    mask = cv2.inRange(hsv,hsv_lower,hsv_upper)
    conts, herirarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = sorted(conts,key = cv2.contourArea,reverse=True)[0]
    rect = cv2.boundingRect(biggest)
    x,y,w,h = rect
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.putText(frame, name, (x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.putText(frame, flavor, (x,y+30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.putText(frame, color, (x,y+60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Image",frame)
#cv2.imshow("MASK",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()