def begin():
    #size(400,600)
    fill (30,90,100)
    rect(100,100,50,50)
def middle():
    
    
    background(0,0,0)
    noStroke()
    fill(100,100,100)
    ellipse(50,90,50,50)
    rect(mouseX,500,30,30)
    stroke(205,205,0)
    noFill()
    ellipse(mouseX,mouseY,10,10)

if mousePressed and mouseX > 400:
         line(pmouseX,pmouseY,mouseX,mouseY)
if mouseX> 300:
         stroke(255,0,0)
         line(mouseX,mouseY,100,100)
    
else mouseX< 400:
         stroke(255,0,0)
         line(mouseX,mouseY,150,100)


    
  
