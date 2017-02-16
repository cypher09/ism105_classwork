import social_auth.facebook.authentication
username = raw_input("enter username:")
password = raw_input("enter password:")
login = social_auth.facebook.authentication.login(username,password)
print login