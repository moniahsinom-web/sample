import smtplib
import random
 
otp = random.randint(100000, 999999)
 
sender = "moniahsinom@gmail.com"
password = "yfcs pjjv jhly dino"
receiver = "monimonishaofficiall17@gmail.com"
 
message = f"Subject: Your OTP\n\nYour OTP is {otp}"
 
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
 
print("OTP sent to email!")