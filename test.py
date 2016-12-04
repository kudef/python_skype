import sys
from datetime import datetime
import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype(Transport='x11')

# Connect the Skype object to the Skype client.
skype.Attach()

if sys.argv[1] == '-i':
    print 'Your full name:', skype.CurrentUser.FullName
    print 'Your contacts:'
    for user in skype.Friends:
        print 'userId', user.Handle, '    name', user.FullName
else:
    cl = []
    message = ''
    message_found = False
    f = open(sys.argv[1], 'r')
    for line in f:
        if not message_found:
            if line.strip() == 'message:':
                message_found = True
                continue
            cl.append(line.strip())
        else:
            message = message + line

    print 'contact list', cl
    print 'message:'
    print  message
    print

    for contact in cl:
        print 'sending message to', contact
        skype.SendMessage(contact, str(datetime.now()) + ' message: ' + message)

#print 'Groups:'
#for group in skype.CustomGroups:
#    print '    ', group.DisplayName
#    for gUser in group.Users:
#        print '    DisplayName:', user.DisplayName, 'FullName:', user.FullName
