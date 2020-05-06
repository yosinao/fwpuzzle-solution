# Construct the list for the 'decoder' to be used on
raw = [15, 24, 47, 106, ' ', 56, 13, 4, 6, 3, 102, 31, 10, 11, ' ', 33, 14, 5, 26, 43, 65, 40, ' ', 37, 51, 34, 74, 28, 50, ' ', 66, 63, 55, 9, ' ', 139, 42, 77, 70, ' ', 27, 87, 64, 104, 82, ' ', '&', ' ', 124, 68, 113, 179, 80, 83, 36, 49, 131, 60, 91, 69, '!', ' ', 120, 137, 'k', 78, ' ', 134, 75, 196, 92, ' ', 136, 84, ' ', 116, 103, 58, 98, 149, 189, 142, ' ', 148, 122, 140, ' ', 118, 145, 176, 174, ' ', 138, 110, 156, 182, ' ', 185, 161, 198, 206, 191, '?']

# Obtain the decoder string from Flour+Water website
about = 'Opening the doors in 2009 in the heart of the mission in San Francisco, flour and water continues to showcase a menu influenced by regional traditions throughout Italy with Northern Californian inspirations led by Executive Chef Thomas McNaughton'

# Remove spaces and commas from decoder string
about_refined = about.replace(' ','').replace(',','').lower()

# Double-check refined sentence
print(about_refined)

# Translate raw list using list comprehension
translated=[about_refined[pos-1] if pos not in [' ', '&', '!', '?', 'k'] else pos for pos in raw]

# Convert list to sentence
sentence=''.join(map(str,translated))

# Double-check final sentence
print(sentence)