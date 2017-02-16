from social_auth.facebook.authentication import login

username = raw_input("enter username")
password = raw_input("enter password")

login(username,password)