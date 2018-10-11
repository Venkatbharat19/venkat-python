#to send a mail using smtp
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("bharath.polineni123@gmail.com", "-----------")
server.sendmail(
  "bharath.polineni123@gmail.com", 
  "vishnudeepak13@gmail.com", 
  "hello small d")
server.quit()
