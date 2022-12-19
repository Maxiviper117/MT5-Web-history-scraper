import pandas as pd

# match table that is within div with class = page-block frame bottom

from bs4 import BeautifulSoup
# use beautiful soup to parse html
soup = BeautifulSoup(open('ttt-firefox.html'), 'html5lib')
# print(soup.prettify())
tables = pd.read_html(
	# io='mt5_web_html.html',
	io='ttt-firefox.html',
	# io=soup,
	match='Deal',
	header=0,
	index_col=0,
	# flavor='bs4',
	)

print(tables[0])



df = tables[0]

# print the second last row index value
print(df.index[-2])

# loop through each row of the dataframe and if index contains 'Profit:' remove row.
for index, row in df.iterrows():
	print(index)
	if 'Profit:' in str(index) or 'nan' in str(index).lower():
		df = df.drop(index)



print(df)

# print each row of the dataframe
for index, row in df.iterrows():
	print(type(row['Deal']))
	# if row['Deal'] is not type integer, remove row
	if not isinstance(row['Deal'], int):
		df = df.drop(index)



# remove last 2 rows
# df = df[:-2]
# remove duplicate values based on Ticket column
# df = df.drop_duplicates(subset=['Ticket'], keep='first')
print(df)
