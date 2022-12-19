import pandas as pd

# match table that is within div with class = page-block frame bottom

from bs4 import BeautifulSoup
# use beautiful soup to parse html
soup = BeautifulSoup(open('SAMPLE-firefox.html'), 'html5lib')
# print(soup.prettify())
tables = pd.read_html(
	# io='mt5_web_html.html',
	io='SAMPLE-firefox.html',
	# io=soup,
	match='Deal',
	header=0,
	index_col=0,
	# flavor='bs4',
	)

print(tables)

df = tables[1]

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
