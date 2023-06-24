import pyshorteners

url =input("Enter the URL for shortenings: ")

print("URL after shortening :-",pyshorteners.Shortener().tinyurl.short(url))