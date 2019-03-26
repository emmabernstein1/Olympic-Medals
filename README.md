# Summer Olympic Medals
By: Emma Bernstein and Mubarak Bajwa

## Goal
Our objective for this project was to scrape data from the olympics.org website, classify the data and ultimately create a dashboard to display our findings. We used our knowledge in python, pandas and the BeautifulSoup library to extract data. Then we used our knowledge of orm python and SQLAlchemy to transform our data into populated tables. We loaded our dashboard using Flask and attached the Dash app to create data visualizations. Our main focus was on gathering information on all medals over the last 10 Summer Olympic Games. With this, we were able to compare medal counts across countries, as well as the succession of scores for game events.

## Requirements

	- Flask (for the website) 
	- SQL Alchemy (for ORM) 
	- Dash (for graphing)
	- Plotly (for graphing)
	- Beautiful Soup (for scraping)
	- Requests (for making requests to http)
 
## App

Almost all of the graphs that we created are interactive.
This first graph shows the Olympic medals awarded for each sport's events. You select a sport and one of its events from the dropdown to view the medal scores from the past ten summer Olympic games. This allows you to visually track the progress that athletes are making over the years.
By hovering over the data points, you can see the country associated with the medal, as well as the score and the type of medal awarded.

![alt text](https://github.com/emmabernstein1/Project-1/blob/master/Screen%20Shot%202019-03-03%20at%207.02.54%20PM.png)


The next tab brings you to a graph that shows a country's medal count over the past ten summer Olympic games. You select a country from the dropdown menu.
By hovering over the data points, you can see the country's medal count next to the mean medal count for that Olympic game. Note that the mean medal count automatically excludes any country with zero medals that year.

![alt text](https://github.com/emmabernstein1/Project-1/blob/master/Screen%20Shot%202019-03-03%20at%206.16.43%20PM.png)


We graphed the ten countries with the highest total medal counts.
By hovering over the data points, you can see the country's total medal count from the past ten Summer Olympic games.

![alt text](https://github.com/emmabernstein1/Olympic-Medals/blob/master/Screen%20Shot%202019-03-03%20at%208.01.24%20PM.png)


While the purpose of this project was to build a dashboard to visualize the data, the relational database that we created could be utilized for further statistical analysis.

Thanks for reading!
