
#Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

#Create another list called author_last_names that only contains the last names of the poets in the provided string.

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

#First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
print(love_maybe_lines_stripped)

#.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
  
#String methods review challenge:

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

#Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems_stripped = []

#There is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.
#Start by creating a new empty list, highlighted_poems_stripped.
#Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip()) 

print(highlighted_poems_stripped)

#Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists.
#Create a new empty list called highlighted_poems_details.

highlighted_poems_details = []

#Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

#Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.
#Create three new empty lists, titles, poets, and dates.

titles = []
poets = []
dates = []

#Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

#For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])

#Finally, write a for loop that uses .format() to print out the following string for each poem:

for i in range(0, len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))





