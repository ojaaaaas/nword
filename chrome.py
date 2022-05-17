import webbrowser



id_pool = [1,2,3,4]

enter_id = int(input("Enter your id: "))

if enter_id == 1:
    webbrowser.open("https://www.google.com")

elif enter_id == 2:
    webbrowser.open("https://www.youtube.com")

else:
    webbrowser.open("https://amazon.in")

