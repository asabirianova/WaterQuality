# Finding DEP ineffiencies through analysis of 311's water quality complaints 

## *Introduction*
New York City is known for its high-quality tap water that is safe to drink. However, the DEP (Department of Environmental Protection) still receives over 800 complaints per year from New York residents regarding their water quality. Initial analyses are done to look into general trends and then  further investigation is conducted to look for possible agency ineffiencies.

The dataset used comes from [NYC OpenData](https://data.cityofnewyork.us/Environment/Water-Quality-complaints/qfe3-6dkn/data). This data shows complaints placed via 311 from 2010 until today. The data includes information on when and where the complaint was made, along with a description of the complaint and its resolution status. 

The data pulled had information regarding complaints ranging from 2010 up until Oct of 2018. However, the analyses done excluded 2018 due to its incomplete data. The focus was placed on data that's complete and available in order to evaluate the agency’s possible inefficiencies.

## *Analyses*
The following are questions the analyses attemps to answer:

**1. How is the number of complaints changing over time?**<br/>
Despite the small dip in 2011, there is a general upward trend in the number of complaints placed per year. This general trend can also be explained away by NY's poulation growth over the years.  

**2. Is the agency getting better at closing complaints?**<br/>
  Here, a look was taken into the number of complaints closed per year to see how well the DEP is doing in terms of their resolution rate. Though there is a dip in closed complaints from 2010 to 2011, the general trend is upward in the number of resolved complaints per year.<br/>
To put this trend into context, the ratio of closed to unresolved complaints by year was calculated. At least 98% of all complaints received per year have a closed status. The year 2016 saw the most complaints left unresolved, but those still only made up 1% of all complaints that year, which is negligible. Years 2011, 2013, and 2015 all had 100% rate of closed complaints. From this angle, the DEP is running fairly efficiently.

<a href="https://imgbb.com/"><img src="https://image.ibb.co/jA54cf/statusofcomp.jpg" alt="statusofcomp" border="0"></a>

**3. Finding zipcodes with the highest unresolved complaints**<br/>
From 2010-2017, zipcode 11374 has had the highest rate of unresolved cases, which is just three. This zipcode is located in Rego Park of Queens, NY. However, after looking into the portion these unresolved cases make up of all its zipcode's complaints, it only came out to 5%. Looking into which zipcode historically had the highest percentage of unresolved cases, 10% of zipcode 11370's cases are unresolved. Again, this is a misleading statistic since zipcode 11370 has had only ten complaints, one of which is still open. This analysis does not seem to indicate any structural inefficiencies at the DEP.

**4. What is the agency’s average resolution time per year?**<br/>
Though it appears that most complaints eventually get closed, it would be helpful to see how long it takes for these complaints to get resolved. Year 2011 saw the most efficient average resolution time of about 17 days. Since 2014, the resolution times has been on the rise which could point to possible inefficency within the DEP. Earlier findings show that the number of complaints has also been on the rise, so this could be a potential explanation for this. However, looking further into DEP funding and how many workers are allocated to handle complaints would give a better idea into whether misuse is taking place. 

<a href="https://imgbb.com/"><img src="https://image.ibb.co/mO1f00/avgrestime.jpg" alt="avgrestime" border="0"></a>

**5. Which zip codes have the longest resolution times?**<br/>
Digging further, a dive into the breakdown of the resolution times per zip code was taken to see if there are any areas that have longer resolution times than others. There are a number of zipcodes which have longer resolution times than the median time across all zipcodes. Some zipcodes have resolution times that are at least twice as long than the median. Zipcode 10004, in perticular, has a very high resolution time of 327 days, which seems like an outlier. Having the number of complaints placed per zipcode became helpful to see which zipcodes had enough data to point to a trend. Since the range in number of complaints is from 1-100, a threshold of 50 complaints for a zipcode is a good starting point. Zipcodes 11222, 11231 11230, and 11234 are excellent candidates for zipcodes with enough complaints and a well above median resolution time to warrent an investigation. Moreover, all these zipcodes are in Brooklyn and relatively close to each other. 

**6. Does the type of complaint placed affect the resolution time?**<br/>
After finding that certain Brooklyn zipcodes have longer resoluation times than the median time across all boroughs, the next analysis involved seeing if this is maybe due to the complaint types. Perhaps there are certain complaints that take a longer time to be resolved due to the nature of the complaint. Most water quality complaints took about 22-26 days to resolve despite its type. The only true outliers are the complaints QSS, QG2, and QB1. Both QSS and QG2 are the only complaints that deal with water sampling issues so those are probably quick to get resolved. QB1 is a complaint regarding Cloudy or Milky Water. This is also the most common complaint, making about 13% of all complaints placed by all boroughs. This complaint is likely to also get resolved quickly since it’s so [common](https://water.usgs.gov/edu/qa-chemical-cloudy.html). Furthermore, DEP claims that this complaint is a [harmless one that often occurs during the colder months](http://www.nyc.gov/html/dep/pdf/wsstate16.pdf). Concluding from this analysis, complaint type should not have that much of an impact on resolution time so there must be other factors at play when it comes to zipcodes having above median resolution times. 

## *Conclusion*

•	The number of water quality complaints has been on the rise since 2010, however, this could be attributed to NYC population growth or the awareness of global environmental concerns.<br/> 
•	It would appear from findings, that there is a high resolution rate in terms of the amount of complaints that are closed amongst the DEP’s water quality ccomplaints, which is a sign of efficiency. Though some zipcodes have a higher number of unresolved complaints than others, the number of these is statistically insignificant compared to those that are closed.<br/>
•	It looks like the resolution time for all complaints has been increasing in the last couple of years. Looking further into DEP funding and how many workers are currently allocated to handle complaints would give us a better idea into the possible misuse taking place. Furthermore, some zipcodes have a notably higher average resolution times than others, despite complaint volume and complaint types. This should be investigated further.

Further analysis could include supplementing the data with zipcode population to see the ratio in the number of complaints per zipcode to its population. Are there any zipcodes where the population is small compared to how many complaints are placed? This could also point to agency problem areas. Examing the income and census date for each zipcode could point to possible biases in terms of DEP's response rate per neighborhood. 















