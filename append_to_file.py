app_text = "\nHere i've put the appended text!"

saveFile = open('exampleFile.txt', 'a')

saveFile.write(app_text)
saveFile.close()
