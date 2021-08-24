emailid=input('enter the mail-id:').strip()
username=emailid[:emailid.index('@')]
domain=emailid[emailid.index('@')+1:]
print(f'your username is {username} and domain is {domain}')
