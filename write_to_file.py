text = 'This is sample text\nAnd here we come to new line!'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()
