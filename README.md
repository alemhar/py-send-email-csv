# py-send-email-csv
Send email to list of emails on CSV file

python sendemail.py -i <input-file.csv> -m <message.txt> -s <subject>'


- CSV file as list of name and email. Column names must spell "name" and "email" respectively.
- TEXT file as message body.
- SMTP credentials, server and port must be provided and set on the variables just after this notes.
- USAGE: python sendemail.py -i <input-file.csv> -m <message.txt> -s <subject>
- Enclose EMAIL SUBJECT with doubel quotes if it has more that one word as such "My Email Subject"

Important: 
Edit and set your email address or user name, password, smtp server and smtp port number.


