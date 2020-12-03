import RPi.GPIO as m
import time as t
m.setmode(m.BCM)
m.setup(21,m.OUT)
while True:
 d=str(input("enter longbell/shortbell"))
 if d=="longbell":
  m.output(21,1)
  t.sleep(15)
  m.output(21,0)
 elif d=="shortbell":
  c=int(input("count"))
  for i in range(c):
   m.output(21,1)
   t.sleep(5)
   m.output(21,0)
   t.sleep(5)



