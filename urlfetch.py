import imaplib#internet message access protocol-provides various methods for connecting
#to an IMAP server, authenticating with a username and password,
import email#framework for parsing, creating, and manipulating email messages
import re#regular expression-match & manipulate text
import sqlite3#database

# Connect to email server
imap_server = 'imap.gmail.com'  # Replace with your email server hostname
imap_username = 'your-email@gmail.com'  # Replace with your email address
imap_password = 'password'  # Replace with your email password

mail = imaplib.IMAP4_SSL(imap_server)#IMAP4_SSL is a Python class in the imaplib
mail.login(imap_username, imap_password)#imaplib.IMAP4_SSL-used to connect to an IMAP email server
mail.select('inbox')

# Search for email messages with URLs in the subject or body
search_criteria = 'BODY "http" OR SUBJECT "http"'
status, email_ids = mail.search(None, search_criteria)

# Initialize regular expression pattern to match URLs
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|( ?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Connect to SQLite database and create URL table if not exists
conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (url text)''')

# Loop through email messages and extract URLs
for email_id in email_ids[0].split():
    status, email_data = mail.fetch(email_id, '(RFC822)')
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract URLs from email message subject and body
    urls = []
    urls.extend(re.findall(url_pattern, email_message['subject']))
    urls.extend(re.findall(url_pattern, email_message.get_payload()))

    # Insert URLs into database
    for url in urls:
        c.execute("INSERT INTO urls (url) VALUES (?)", (url,))

# Commit changes to database and close connection
conn.commit()
conn.close()

# Logout from email server
mail.logout()
z