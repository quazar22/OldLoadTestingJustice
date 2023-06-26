# this program creates a bunch of sql statements that can be used in SSMS to create test users for centralisation
# each name starts with the the name inside the variable (gtlt) and appends an iterated number onto it (eg. automatedtestuser1, automatedtestuser2, etc.)
# The output for inserting the users is located in [[insert_test_users.sql]] (for inserting the users and encrypted user passwords) 
# The output for deleting the users is located in [[delete_test_users.sql]] (for deleting all of those users and passwords just created)
# The passwords themselves are output to an easily parseable file called [[user_password_pairs.txt]]

# a lot of ideas from this could be made better, but it's an okay start

from binascii import b2a_base64
import hashlib
import os
import string
import random

gtlt = "automatedtestuser"

user_insert = 'INSERT [dbo].[User] ([Title], [FirstName], [LastName], [Username], [Email], [ContactNumber], [LastLoginDate], [FailedLogins], [LocalAuthorityId], [Deleted], [SecurityRoleId], [PasswordResetToken], [PasswordResetTokenExpiry]) VALUES '
password_insert = 'INSERT [dbo].[UserPassword] ([UserId], [Password], [Salt], [ChangedDate], [ChangedRequired]) VALUES '

user_delete = "DELETE FROM [User] WHERE Username = N'%s'"
user_password_delete = "DELETE FROM [UserPassword] WHERE (SELECT TOP 1 FROM [User] WHERE Username = N'%s')"

user_password_dict = {}

class User():
    def __init__(self, username, number):
        self.title = "Mr"
        self.firstname = "test" + str(number)
        self.lastname = "test" + str(number)
        self.email = username + str(number) + "@test.com"
        self.username = username + str(number) + "@test.com"
        self.contactnumber = "123456789"
        self.laid = 16
        self.failedlogins = 0
        self.deleted = False
        self.securityroleid = 3
    
    def get_insert_string(self):
        return user_insert + f"(N'{self.title}', N'{self.firstname}', N'{self.lastname}', N'{self.username}', N'{self.email}', N'{self.contactnumber}', NULL, 0, {self.laid}, 0, {self.securityroleid}, NULL, NULL)"

    def get_delete_string(self):
        return f"DELETE FROM [User] WHERE Username = N'{self.username}'"


class Password():
    def __init__(self, username):
        self.password = Password.get_random_password()
        self.salt = os.urandom(16)
        self.key = hashlib.pbkdf2_hmac('sha512', password=bytes(self.password, encoding='utf8'), salt=self.salt, iterations=10000, dklen=32)
        self.salt = b2a_base64(self.salt).strip().decode('ascii')
        self.key = b2a_base64(self.key).strip().decode('ascii')
        self.username = username

    def get_random_password():
        password = ''
        i = 0
        while i < 16:
            password += random.choice(string.ascii_letters) if random.random() > 0.5 else random.choice(string.digits)
            i += 1

        return password

    def get_insert_string(self):
        return password_insert + f"((SELECT TOP 1 Id FROM [User] WHERE Username = '{self.username}'), N'{self.key}', N'{self.salt}', getdate(), 0)"

    def get_delete_string(self):
        return f"DELETE FROM [UserPassword] WHERE [UserId] = (SELECT TOP 1 Id FROM [User] WHERE Username = N'{self.username}')"
        

for i in range(0, 128):
    user = User(gtlt, i)
    password = Password(user.username)
    user_password_dict[user] = password

with open('insert_test_users.sql', 'w') as passfile, open('delete_test_users.sql', 'w') as deletefile, open('user_password_pairs.txt', 'w') as passpairs:    
    for i in user_password_dict:
        passfile.write(i.get_insert_string() + '\n')
        deletefile.write(user_password_dict[i].get_delete_string() + '\n')
        passpairs.write(i.username + " : " + user_password_dict[i].password + '\n')

    passfile.write('GO\n\n')
    deletefile.write('GO\n\n')

    for i in user_password_dict:
        passfile.write(user_password_dict[i].get_insert_string() + '\n')
        deletefile.write(i.get_delete_string() + '\n')

    passfile.write('GO\n\n')
    deletefile.write('GO\n\n')

