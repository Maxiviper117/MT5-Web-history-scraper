import time
import os
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

# login = "88394128"
# password = "wRQpXRG!Y583fz$"
# server = "Ava-Real 1-MT5"

login = "1006296"
password = "5dvmwece"
server = "Eightcap-Demo"

with sync_playwright() as p:
	for browser_type in [
		p.firefox,
		# p.webkit
		]:
		browser = browser_type.launch(headless=False, slow_mo=50)
		page = browser.new_page()
		page.goto('https://trade.mql5.com/trade?version=5')
		# chech if 'button[id="accept"]' is visible

		if page.is_visible('button[id="accept"]'):
			page.click('button[id="accept"]')

		page.fill(selector = 'input#login', value = login)
		page.fill(selector = 'input#password', value = password)
		page.fill(selector = 'input#server', value = server)

		time.sleep(1)
		page.click("button.input-button:nth-child(20)") # click 'ok' button to login

		############
		# print()
		# # page.evaluate("document.documentElement.outerHTML")
		# print()
		# deals_div = page.query_selector(selector = 'div.at-history-deals-table')
		# deals_table = pd.read_html(io=deals_div.inner_html(), match='Deal', header=0, index_col=0,)
		# print(deals_table[0])
		# print(deals_div.inner_html())
		# with open(f'ttt-{browser_type.name}.html', 'w') as f:
		# 	f.write(deals_div.inner_html())
		############

		# time.sleep(15)
		# Selecting history tab then right click on the table body
		history_tab_visible = False
		while history_tab_visible == False:
			history_tab_visible = page.is_visible(selector = 'div.page-tabs:nth-child(8) > a:nth-child(3)')
			print('History tab is not visible yet...waiting 1 second')
			time.sleep(1)

		if history_tab_visible:
			print('History tab is visible..waiting 10 seconds for the page to load further')
			time.sleep(10)
			History_tab_element = page.locator(selector="div.page-tabs:nth-child(8) > a:nth-child(3)")
			if 'History' in History_tab_element.inner_text():
				History_tab_element = page.locator(selector="div.page-tabs:nth-child(8) > a:nth-child(3)")
				print('History tab is clicking')
				History_tab_element.click()

		History_tab_box = History_tab_element.bounding_box() # get the bounding box of the element
		time.sleep(1)
		print('Right clicking in the deals table body, to open the context menu')
		page.mouse.click(History_tab_box['x'], History_tab_box['y'] - 20, button='right') # right click 20 pixels above the element, this should be in the table body. In order to open the context menu.

		# Selecting the deals button in the context menu
		if page.is_visible(selector = 'body > div.page-menu.context.expanded > div > div > span.box > span > div:nth-child(2)'):
			Deals_element = page.locator(selector = 'body > div.page-menu.context.expanded > div > div > span.box > span > div:nth-child(2)')
			if 'Deals' in Deals_element.inner_text():
				print('Clicking on "Deals" in the context menu')
				Deals_element.dblclick()

		time.sleep(1)
		print('Right clicking in the deals table body, to open the context menu')
		page.mouse.click(History_tab_box['x'], History_tab_box['y'] - 20, button='right')

		# Selecting the All histroy button in the context menu
		if page.is_visible(selector = 'body > div.page-menu.context.expanded > div > div > span.box > span > div:nth-child(9)'):
			All_history_element = page.locator(selector = 'body > div.page-menu.context.expanded > div > div > span.box > span > div:nth-child(9)')
			if 'All History' in All_history_element.inner_text():
				print('Clicking on "All History" in the context menu')
				All_history_element.click()

		page.mouse.click(History_tab_box['x'], History_tab_box['y'] - 20, button='left')
		time.sleep(1)
		page.mouse.click(History_tab_box['x'], History_tab_box['y'] - 20, button='left')


		html = page.evaluate("document.documentElement.outerHTML") # get the html of the page, up to date
		# save html soup to html file
		with open(f'SAMPLE-{browser_type.name}.html', 'w') as f:
			f.write(html)

		tables = pd.read_html(io="SAMPLE-firefox.html", match='Deal', header=0, index_col=0)
		print(tables)
		df1 = tables[0]
		# remove all rows from the dataframe
		df1.drop(df1.index, inplace=True)

		# print(df1)
# div.ext-table:nth-child(2) > div:nth-child(2) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1)
# html body.gecko.win.gray div.page-block.frame.bottom div.page-block div.ext-table.fixed.odd.grid.no-border.trade-table.toolbox-table.at-history-deals-table div.tables-box table thead tr th#time.sortable.sort-down
		scroll_interval = 5

		bottom_table = False
		loop_count = 0
		print('Now scrolling through the deals table to grab all the deals rows')
		print('Waiting 10 seconds for the page table to load further')
		time.sleep(30)
		time_sort = page.locator(selector = 'html body.gecko.win.gray div.page-block.frame.bottom div.page-block div.ext-table.fixed.odd.grid.no-border.trade-table.toolbox-table.at-history-deals-table div.tables-box table thead tr th#time.sortable.sort-down')
		time_sort.click()
		time_sort = page.locator(selector = 'html body.gecko.win.gray div.page-block.frame.bottom div.page-block div.ext-table.fixed.odd.grid.no-border.trade-table.toolbox-table.at-history-deals-table div.tables-box table thead tr th#time.sortable.sort-up')
		time_sort.click()

		page.mouse.click(History_tab_box['x'], History_tab_box['y'] - 20, button='left') # right click 20 pixels above the element, this should be in the table body.

		while not bottom_table:
			print(f'Scrolling the page {loop_count} times')
			if loop_count > 0:
				# Scroll the page
				page.mouse.wheel(0, scroll_interval)

			loop_count += 1

			html = page.evaluate("document.documentElement.outerHTML")

			# save html soup to html file, overwrite the file and overwrite the file

			deals_div = page.query_selector(selector = 'div.at-history-deals-table')
			deals_table = pd.read_html(io=deals_div.inner_html(), match='Deal', header=0, index_col=0,)
			df2 = deals_table[0]
			df1 = pd.concat([df1, df2]).drop_duplicates(subset=['Deal'], keep='first')

			for index, row in df2.iterrows():
				# print(index)
				if 'Profit:' in str(index):
					bottom_table = True

			for index, row in df1.iterrows(): # iterates over the rows in your dataframe
				# check if the row is not of type int
				if not (row['Deal'], int): # checks if the row is not a number, if it is not a number, it drops the row
					df1 = df1.drop(index)

			# with open(f'SAMPLE-{browser_type.name}.html', 'w') as f:
			# 	f.write(html)

			# tables = pd.read_html(io="SAMPLE-firefox.html", match='Deal', header=0, index_col=0,)
			# df2 = tables[0]
			# for index, row in df2.iterrows(): # iterates over the rows in your dataframe
			# 	# check if the row is not of type int
			# 	if not (row['Deal'], int): # checks if the row is not a number, if it is not a number, it drops the row
			# 		df2 = df2.drop(index)

			# df1 = pd.concat([df1, df2]).drop_duplicates(subset=['Deal'], keep='first')

			time.sleep(0.05)

		# delete the file
		os.remove(f'SAMPLE-{browser_type.name}.html')
		# save df1 to csv file
		print(f'Removing the last row from the dataframe: {df1.tail(1)}')
		df1 = df1.drop(df1.tail(1).index)
		# sort by index ascending
		print('Sorting the dataframe by index ascending')
		df1 = df1.sort_index(ascending=True)

		print('Converting nan values to 0 in columns [Order, Volume, Price, Commission, Fee, Swap, Profit]')
		# Converting nan values to 0 in columns [Order, Volume, Price, Commission, Fee, Swap, Profit]
		df1['Order'] = df1['Order'].fillna(0)
		df1['Volume'] = df1['Volume'].fillna(0)
		df1['Price'] = df1['Price'].fillna(0)
		df1['Commission'] = df1['Commission'].fillna(0)
		df1['Fee'] = df1['Fee'].fillna(0)
		df1['Swap'] = df1['Swap'].fillna(0)
		df1['Profit'] = df1['Profit'].fillna(0)

		print('Converting the column "Order" to int')
		df1['Order'] = df1['Order'].astype(int)
		# df1['Volume'] = df1['Volume'].astype(float)
		# df1['Price'] = df1['Price'].astype(float)
		# df1['Commission'] = df1['Commission'].astype(float)
		# df1['Fee'] = df1['Fee'].astype(float)
		# df1['Swap'] = df1['Swap'].astype(float)
		# df1['Profit'] = df1['Profit'].astype(float)

		print('Saving the dataframe to markdown file')
		df1.to_markdown(f'SAMPLE-{browser_type.name}.md', index=True)
		print(df1)

		browser.close()

	user_input = input('Enter your search: ')


