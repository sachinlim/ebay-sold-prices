# Ebay Sold Item Price Checker

This tool is used to provide information from [eBay's advance search](https://www.ebay.co.uk/sch/ebayadvsearch) by scraping the information available. It uses Beautiful Soup to scrape the sold prices while using the filters: Exact words, any order, Sold listings, Used, UK only. 

This project has been improved (addition of trimming) and implemented in the [Discord Bot](https://github.com/sachinlim/discord-bot) repository. It is a `!search` command that users can now use to extract information directly on Discord.

## Output

A user input is prompted so that the script can be searched on eBay's website.

![image](https://user-images.githubusercontent.com/80691974/210365167-29ff6d98-4cc8-4139-9c59-26ba178b00fe.png)

It can also be run via Terminal: 

![image](https://user-images.githubusercontent.com/80691974/210365737-d6509b37-3f31-43a1-9875-e3ee4ee868c6.png)

Timestamps would be nice, but because the user would be running this script to find out the value of their item at the current time, it was not needed. However, with it being implemented on Discord, there is now a timestamp and history available if users were to search for the item using Discord's search feature.

## Implementation 

As mentioned above, this has been implemented in a Discord bot so that a community of users can search items on eBay. The output on Discord looks like this: 

<p align="left">
  <img src="https://user-images.githubusercontent.com/80691974/208790787-ef499007-b8bd-4b16-9b9a-0dfce2b813be.png" width="550">
</p>

