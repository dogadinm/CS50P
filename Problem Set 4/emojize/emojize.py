import emoji

smile = input('Input: ')
emoji = emoji.emojize(smile, language='alias')
print('Output: ', emoji)