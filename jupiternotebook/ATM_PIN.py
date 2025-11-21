import smtplib
from email.mime.text import MIMEText

# ---------------------------
# Email Notification Function
# ---------------------------
def send_notification(name, card_number):
    sender = "moniahsinom@gmail.com"  # Your email
    password = "yfcspjjvjhlydino"  # App password (not your Gmail login)
    receiver = "monimonishaofficiall17@gmail.com"  # Receiver email

    subject = "ATM Security Alert"
    body = f"""
Hello {name},

There were 3 incorrect PIN attempts on your ATM Card Number: {card_number}.

If this was NOT you, please contact customer support immediately.

Thank you,
Your Bank
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("\n📧 Notification email sent successfully!")
    except Exception as e:
        print("\n❌ Error sending email:", e)


# ---------------------------
# ATM PIN Program
# ---------------------------
print("----- ATM PIN Verification -----")

name = input("Enter your Name: ")
card_number = input("Enter your ATM Card Number: ")

correct_pin = "1234"   # Set your correct PIN here
attempts = 0

while attempts < 3:
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("\n✅ PIN Verified Successfully!")
        print(f"Welcome, {name}!")
        break
    else:
        attempts += 1
        print(f"❌ Wrong PIN! Attempts left: {3 - attempts}")

        if attempts == 3:
            print("\n❌ 3 Wrong Attempts! Your ATM Card is temporarily blocked.")
            send_notification(name, card_number)
