import sys, getopt
from string import Template
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


__author__ = "Alemhar Salihuddin"
__pyversion__ = "3"
__version__ = "1.0.1"
__email__ = "alemhar@gmail.com"

"""
Notes: 
- CSV file as list of name and email. Column names must spell "name" and "email" respectively.
- TEXT file as message body.
- SMTP credentials, server and port must be provided and set on the variables just after this notes.
- USAGE: python sendemail.py -i <input-file.csv> -m <message.txt> -s <subject>
- Enclose EMAIL SUBJECT with doubel quotes if it has more that one word as such "My Email Subject"
"""

MY_ADDRESS = 'hello@example.com'
PASSWORD = 'yourpassword'
SMTP_SERVER = 'smtp.server.com'
SMTP_PORT = 587


s = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def sendmail(inputfile, header_exist, templatefile, subject):
    
    message_template = read_template(templatefile)
    with open(inputfile,'r') as source_file:
        reader = csv.DictReader(source_file)
        for row in reader:
            print(row['email'])
            if not row['email']:
                continue
            message = message_template.substitute(PERSON_NAME=row['name'].title())
            msg = MIMEMultipart() 
            
            msg['From']= MY_ADDRESS
            msg['To']= row['email']
            msg['Subject']=subject
            msg.attach(MIMEText(message, 'plain'))
            s.send_message(msg)
            del msg

def usage():
    print('USAGE: >>> python sendemail.py -i <input-file.csv> -m <message.txt> -s <subject>')


def main(argv):
    inputfile = ''
    templatefile = 'message.txt'
    subject = ''
    header_exist = True

    try:
        opts,args = getopt.getopt(argv,"hi:s:m:",["ifile=","subject="])
    except getopt.GetoptError:
        usage() 
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage() 
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-m", "--message"):
            templatefile = arg    
        elif opt in ("-s", "--subject"):
            if not arg:
                subject = 'NO SUBJECT'
            else:     
                subject = arg
                
    sendmail(inputfile, header_exist, templatefile, subject)


if __name__ == "__main__":
    main(sys.argv[1:])