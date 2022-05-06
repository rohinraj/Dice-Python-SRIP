from PIL import Image, ImageDraw
import cv2                                                                         # Importing all the related libraries

Total_Dice = 0


#For black dice
##color ="black"           
##bg_color = "white"


#For White dice
color = "white"
bg_color ="black"           

im = Image.new('RGB', (5000, 5000), (bg_color))

    # The screen of 5000*5000 will be displayed with black background color
draw = ImageDraw.Draw(im)                                                          # This line is used to get the drawing screen 
v=20
precision = 1
def click_event (i,j):                                                             #Function which is used to get the pixel values and convert them to get greyscale value where the range we are using is being sent from the part of the code where the function is being called

 global Total_Dice

 summ=0

 
 for x in range(o,a):             
     for y in range (i,j):                                                         # The bgr values will be calculated and then using the varible gg we are converting it to get the greyscale
                (x,' ',y)                                                          # Here we get  the value of x and y in the specifies range
                b=img[y,x,0] 
                g=img[y,x,1]
                r=img[y,x,2]
                #print(b,g,r)
                gg=(0.299*r)+ (0.587*g)+ (0.114*b)                                 
                #print(gg)
                summ=summ+gg                                                       # Here the greyscale of respective columns and rows are added to get a value gray which is further used to make a dice in the drawing screen 
                                                    
 #print(summ)
 gray=(summ)/(precision*precision)
 #print("the gray scale value for at index","[",x,",",y,"]is:",gray)

 #For Black Dice
 #gray = 255 - gray 

 if(gray<43):                                                                      # if the value of gray is less than 43 a dice with one dot would be drawn on the screen
    draw.rectangle((q,l,q1,l1), fill=(color), outline=(bg_color))
    r=2
    aa=(q+q1)/2
    bb=(l+l1)/2
    cc=(q+aa)/2
    dd=(l+bb)/2
    ee=(q1+aa)/2
    ff=(l1+bb)/2
    gg=(aa+q1)/2
    hh=(l+bb)/2
    ii=(q+aa)/2
    jj=(l1+bb)/2
    draw.ellipse((cc-r,dd-r,cc+r, dd+r), fill=(bg_color))
    draw.ellipse((ee-r,ff-r,ee+r, ff+r), fill=(bg_color))
    draw.ellipse((gg-r,hh-r,gg+r, hh+r), fill=(bg_color))
    draw.ellipse((ii-r,jj-r,ii+r, jj+r), fill=(bg_color))
    draw.ellipse((cc-r,bb-r,cc+r, bb+r), fill=(bg_color))
    draw.ellipse((gg-r,bb-r,gg+r, bb+r), fill=(bg_color))

    Total_Dice = Total_Dice + 1

     
 elif(gray<85):                                                                    # The same procedure is repeated for dice with two dots 

    draw.rectangle((q,l,q1,l1), fill=(color), outline=(bg_color))
    r=2
    aa=(q+q1)/2
    bb=(l+l1)/2
    cc=(q+aa)/2
    dd=(l+bb)/2
    ee=(q1+aa)/2
    ff=(l1+bb)/2
    gg=(aa+q1)/2
    hh=(l+bb)/2
    ii=(q+aa)/2
    jj=(l1+bb)/2
    draw.ellipse((cc-r,dd-r,cc+r, dd+r), fill=(bg_color))
    draw.ellipse((ee-r,ff-r,ee+r, ff+r), fill=(bg_color))
    draw.ellipse((gg-r,hh-r,gg+r, hh+r), fill=(bg_color))
    draw.ellipse((ii-r,jj-r,ii+r, jj+r), fill=(bg_color))
    draw.ellipse((aa-r,bb-r,aa+r, bb+r), fill=(bg_color))

    Total_Dice = Total_Dice + 1
     

 elif(gray<127):                                                                    # The same procedure is repeated for dice with three dots 
   
     draw.rectangle((q,l,q1,l1), fill=(color), outline=(bg_color))
     r=2
     aa=(q+q1)/2
     bb=(l+l1)/2
     cc=(q+aa)/2
     dd=(l+bb)/2
     ee=(q1+aa)/2
     ff=(l1+bb)/2
     gg=(aa+q1)/2
     hh=(l+bb)/2
     ii=(q+aa)/2
     jj=(l1+bb)/2
     draw.ellipse((cc-r,dd-r,cc+r, dd+r), fill=(bg_color))
     draw.ellipse((ee-r,ff-r,ee+r, ff+r), fill=(bg_color))
     draw.ellipse((gg-r,hh-r,gg+r, hh+r), fill=(bg_color))
     draw.ellipse((ii-r,jj-r,ii+r, jj+r), fill=(bg_color))

     Total_Dice = Total_Dice + 1
     
 
 elif(gray<170):                                                                     # The same procedure is repeated for dice with four dots 

    draw.rectangle((q,l,q1,l1), fill=(color), outline=(bg_color)) 
    r=2
    aa=(q+q1)/2
    bb=(l+l1)/2
    cc=(q+aa)/2
    dd=(l+bb)/2
    ee=(q1+aa)/2
    ff=(l1+bb)/2
    draw.ellipse((cc-r,dd-r,cc+r, dd+r), fill=(bg_color))
    draw.ellipse((ee-r,ff-r,ee+r, ff+r), fill=(bg_color))
    draw.ellipse((aa-r,bb-r,aa+r, bb+r), fill=(bg_color))

    Total_Dice = Total_Dice + 1
  
  
 elif(gray<213):                                                                      # The same procedure is repeated for dice with five dots 
      
    draw.rectangle((q,l,q1,l1), fill=(color), outline=(bg_color))
    r=2
    aa=(q+q1)/2
    bb=(l+l1)/2
    cc=(q+aa)/2                                                                    # Here first we are making use of the centre of original  coordinates and then using theese centre value and original value (i.e either q or q1 and l or l1 ) we are again making a dot at a specific location 
    dd=(l+bb)/2
    ee=(q1+aa)/2
    ff=(l1+bb)/2
    draw.ellipse((cc-r,dd-r,cc+r, dd+r), fill=(bg_color))                           # a dot with white color at the specified position will be made   
    draw.ellipse((ee-r,ff-r,ee+r, ff+r), fill=(bg_color))

    Total_Dice = Total_Dice + 1


 elif(gray<256):                                                                            # The same procedure is repeated for dice with six dots 
             
    draw.rectangle((q,l,q1,l1), fill=(color), outline=(color))                                 # Using the pil lib's function first we are drawing a rectangle using the value of coordinates represented by q and l 
    r=2                                       
    aa=(q+q1)/2                                                                    # used to calculate the mid point of coordinated denoted by q and q1
    bb=(l+l1)/2                                                                    # used to calculate the mid point of coordinated denoted by 1 and l1

    #draw.ellipse((aa-r,bb-r,aa+r, bb+r), fill=(bg_color))                           # This function is used to make a dot at the desired coordinate or we can say centre 

    #Total_Dice = Total_Dice + 1

img=cv2.imread('MOELogo90.jpg')                                                  # The image is being read or loaded through this statement 
cv2.imshow('image',img)
#print('enter the starting value of i and j')                                 


                                                                              # All the values that we are using in the function for defining the range or coordinates are being initialed here only

o=0                                                                           # The value of a and o and j and i would be according to the precision that we want i.e suppose if we want that for " x=0 to x=2 and y=0 to y=2 " we want to make a dice then the value would be 2 of a and o , j and i too.
a=precision                                                                         
l=0
q=0                                                                           # q and q1 are the coordinates for x axis   and according to the value of v a dice of that pixel will be made i.e suppose if v is 20 then in the drawing screen a dice of 20*20 will be made
q1=v
l1=v                                                                          # l and 11 are the coordinates for y axis 
i=0                                                                           # the  value of i and j basically is used as a range for getting the y'values
j=precision
print("Enter the width and height of image")                               
print(img.shape)
width=int(input())                                                          #In the output screen the  the image width , height , and dimension will be shown and an an input we need to give those during the runtime 
height=int(input())



                                                                               # This loop keeps on changing the initialed position and calls the function again and again which results in the automatic formation of portrait using the dice in the output file

while(a<=height):
    if(a==height):
        o=(a-precision)
        a=height
    while(j<width):
         q=q
         l=l
         click_event(i,j)
         i=j        
         j=j+precision
         q=q
         q1=q1
         l=l1
         l1=l+v
            
         if(j==width):
           i=width-precision
           j=width
           click_event(i,j)
    o=a
    a=a+precision                                                                # As mentioned above the values keep on chaning , So here the value of a is being transferres to o  and a is being incremented by 5
    i=0
    j=precision
    q=q+v
    q1=q+v                                                                # Here the value of  q1 and l1 gets incremented according to the value of v so that the next dice is drawn at a value of v away from the last position
    l=0
    l1=l+v                                                     

print("Total Number of Dice:",Total_Dice)                               


im.save('ProfJain_output.jpg', quality=95)                                           # The output is saved in the file so named here 
cv2.waitKey(0)
cv2.destroyAllWindows()                                                   # Here all the functions so used are basically terminated or stopped
