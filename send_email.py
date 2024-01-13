import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "nazmussakib409@gmail.com"
password = "moqw nzav phmu qbxd"

receiver = "nazmussakib409@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: hi!
Hello,
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)