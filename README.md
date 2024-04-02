# AirBnB MongoDB Analysis

## Data set details:

\- The origin of your data set - what is it and where does it come from. Include a link to the URL of the source.

This dataset "listings.csv.gz" was downloaded from the website [insideairbnb.com](http://data.insideairbnb.com/canada/bc/vancouver/2023-12-13/data/listings.csv.gz), updated on December 13, 2023, and contains detailed listing data for Airbnb properties in Vancouver.

\- What format the original data file was in (CSV, JSON, or other).

The original data file is in CSV format.

\- Display some of the raw data from the original data file (the first 20 rows is enough - feel free to clip the text in fields to prevent line-wrapping). Use Markdown's ability to display tables - see the examples in the Markdown guide linked above.

| id                 | listing_url | scrape_id     | last_scraped | source   | name    | description | neighborhood_overview       | picture_url | host_id  | host_url  | host_name   | host_since | host_location | host_about  | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost  | host_thumbnail_url | host_picture_url | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed   | neighbourhood_group_cleansed | latitude    | longitude    | property_type | room_type | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities | price   | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
| ------------------ | ----------- | ------------- | ------------ | -------- | ------- | ----------- | --------------------------- | ----------- | -------- | --------- | ----------- | ---------- | ------------- | ----------- | ------------------ | ------------------ | -------------------- | ------------------ | ------------------ | ---------------- | ------------------ | ------------------- | ------------------------- | ------------------ | -------------------- | ---------------------- | ------------- | ------------------------ | ---------------------------- | ----------- | ------------ | ------------- | --------- | ------------ | --------- | -------------- | -------- | ---- | --------- | ------- | -------------- | -------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------- | ---------------- | --------------- | --------------- | --------------- | ---------------- | --------------------- | ----------------- | --------------------- | ---------------------- | ------------ | ----------- | -------------------- | ---------------------- | ------------------------- | --------------------- | --------------------------- | ---------------------- | ------------------- | ------- | ---------------- | ------------------------------ | ------------------------------------------- | -------------------------------------------- | ------------------------------------------- | ----------------- |
| 13188              | https://w   | 2.02312E+13   | 2023/12/14   | city     | Rental  |             | The uber hip Main street    | https://a0. | 51466    | https://  | Ian And     | 2009/11/4  | Vancouver,    | We are a    |                    |                    |                      |                    |                    |                  |                    |                     |                           |                    |                      |                        |               |                          |                              |             |              |               |           |              |           |                |          |      |           |         |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| Bon Voyage !!"     | within an   | 100%          | 100%         | f        | https:/ | https://a0. | Riley Park                  | 1           | 3        | ['email', | t           | t          | Vancouver,    | Riley Park  |                    | 49.24773           | -123.10509           | Entire rental unit | Entire home/apt    | 4                |                    | 1 bath              |                           | 2                  | []                   | $150.00                | 2             | 180                      | 1                            | 2           | 1125         | 1125          | 2         | 1125         |           | t              | 0        | 0    | 0         | 0       | 2023/12/14     | 283            | 30                     | 1                      | 2010/2/21              | 2023/11/28             | 4.84                   | 4.88                   | 4.84             | 4.86             | 4.92            | 4.88            | 4.8             | 23-156488        | t                     | 1                 | 1                     | 0                      | 0            | 1.68        |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| 13221              | https://w   | 2.02312E+13   | 2023/12/14   | city     | Rental  |             | The Mount Pleasant          | https://a0. | 51634    | https://  | Amanda      | 2009/11/5  | Vancouver,    | Hi! I'm a   | within a day       | 100%               | 0%                   | f                  | https://a0.muscach | https://a0.musca | Riley Park         | 1                   | 4                         | ['email', 'phone'] | t                    | t                      | Vancouver,    | Riley Park               |                              | 49.25489    | -123.09708   | Entire rental | Entire    | 4            |           | 1 bath         |          | 2    | []        | $120.00 | 31             | 730            | 31                     | 31                     | 730                    | 730                    | 31                     | 730                    |                  | t                | 30              | 59              | 89              | 363              | 2023/12/14            | 15                | 0                     | 0                      | 2015/8/12    | 2017/12/19  | 4.73                 | 4.73                   | 4.67                      | 5                     | 4.8                         | 4.87                   | 4.6                 |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.15              |
| 13358              | https://w   | 2.02312E+13   | 2023/12/14   | city     | Condo   |             | 2 blocks away from the      | https://a0. | 52116    | https://  | Lynn        | 2009/11/7  | Vancouver,    | I am from   | within an hour     | 100%               | 99%                  | f                  | https://a0.muscach | https://a0.musca | Downtown Vancouver | 1                   | 1                         | ['email', 'phone'] | t                    | t                      | Vancouver,    | Downtown                 |                              | 49.28117371 | -123.1259308 | Entire condo  | Entire    | 2            |           | 1 bath         |          | 1    | []        | $165.00 | 1              | 1125           | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 0               | 0               | 0               | 0                | 2023/12/14            | 493               | 55                    | 3                      | 2010/6/22    | 2023/12/11  | 4.68                 | 4.75                   | 4.8                       | 4.83                  | 4.79                        | 4.91                   | 4.65                | 22      | f                | 1                              | 1                                           | 0                                            | 0                                           | 3                 |
| 13490              | https://w   | 2.02312E+13   | 2023/12/13   | city     | Rental  |             | In the heart of Vancouver,  | https://a0. | 52467    | https://  | Iris        | 2009/11/8  | Vancouver,    | Hello! My   | within an hour     | 100%               | 97%                  | t                  | https://a0.muscach | https://a0.musca | Kensington-Cedar   | 3                   | 4                         | ['email', 'phone'] | t                    | t                      | Vancouver,    | Kensington-Cedar Cottage |                              | 49.25622    | -123.06607   | Entire rental | Entire    | 2            |           | 1 bath         |          | 1    | []        | $150.00 | 30             | 180            | 30                     | 30                     | 180                    | 180                    | 30                     | 180                    |                  | t                | 10              | 25              | 25              | 92               | 2023/12/13            | 101               | 5                     | 1                      | 2011/6/2     | 2023/11/16  | 4.93                 | 4.93                   | 4.96                      | 4.96                  | 4.97                        | 4.79                   | 4.89                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.66              |
| 14267              | https://w   | 2.02312E+13   | 2023/12/13   | city     | Home    |             | We live in the centre of    | https://a0. | 56030    | https://  | Peter &     | 2009/11/20 | Vancouver,    | We moved    |                    |                    |                      |                    |                    |                  |                    |                     |                           |                    |                      |                        |               |                          |                              |             |              |               |           |              |           |                |          |      |           |         |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| We welcome         | relocate    | visit family  | who find a   |          |         |             |                             |             |          |           |             |            |               |             |                    |                    |                      |                    |                    |                  |                    |                     |                           |                    |                      |                        |               |                          |                              |             |              |               |           |              |           |                |          |      |           |         |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| Craftsman/designer | Public      | we find our   | slow and     | simple   | within  | 100%        | 0%                          | f           | https:// | https://a | Kensington- | 1          | 1             | ['email',   | t                  | t                  | Vancouver, British   | Kensington-Cedar   |                    | 49.24922         | -123.08139         | Entire home         | Entire home/apt           | 4                  |                      | 1 bath                 |               | 2                        | []                           | $150.00     | 3            | 7             | 3         | 3            | 1125      | 1125           | 3        | 1125 |           | t       | 0              | 0              | 0                      | 17                     | 2023/12/13             | 33                     | 0                      | 0                      | 2010/10/3        | 2021/7/14        | 4.76            | 4.84            | 4.68            | 4.9              | 4.68                  | 4.77              | 4.71                  | 21-156500              | t            | 1           | 1                    | 0                      | 0                         | 0.21                  |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| 16254              | https://w   | 2.02312E+13   | 2023/12/14   | city     | Guest   |             | Good Eats, Cute Shops       | https://a0. | 63238    | https://  | Jason       | 2009/12/15 | Vancouver,    | Enjoys:     | N/A                | N/A                | N/A                  | f                  | https://a0.muscach | https://a0.musca | Hastings-Sunrise   | 1                   | 1                         | ['phone']          | t                    | t                      | Vancouver,    | Hastings-Sunrise         |                              | 49.27721    | -123.04086   | Entire guest  | Entire    | 4            |           | 1 bath         |          | 3    | []        | $800.00 | 5              | 31             | 5                      | 5                      | 1125                   | 1125                   | 5                      | 1125                   |                  | t                | 0               | 0               | 0               | 0                | 2023/12/14            | 7                 | 0                     | 0                      | 2018/8/4     | 2022/7/30   | 4.57                 | 4.86                   | 4.57                      | 4.86                  | 5                           | 4.86                   | 4.29                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.11              |
| 16611              | https://w   | 2.02312E+13   | 2023/12/14   | previous | Home    |             | Next block to               | https://a0. | 58512    | https://  | Q           | 2009/11/29 |               |             | a few days or more | 0%                 | 0%                   | f                  | https://a0.muscach | https://a0.musca | Commercial Drive   | 6                   | 7                         | ['email', 'phone'] | t                    | t                      | Vancouver,    | Grandview-Woodland       |                              | 49.26339    | -123.07145   | Entire home   | Entire    | 6            |           | 1 bath         |          | 4    | []        | $100.00 | 365            | 365            | 365                    | 365                    | 365                    | 365                    | 365                    | 365                    |                  | t                | 30              | 60              | 89              | 89               | 2023/12/14            | 3                 | 0                     | 0                      | 2017/12/24   | 2018/2/16   | 4                    | 4                      | 3                         | 4                     | 4.33                        | 5                      | 3.67                |         | f                | 5                              | 5                                           | 0                                            | 0                                           | 0.04              |
| 17765              | https://w   | 2.02312E+13   | 2023/12/14   | previous | Rental  |             | It is central to everything | https://a0. | 68672    | https://  | James       | 2010/1/7   | Vancouver,    | I'm a       | N/A                | N/A                | N/A                  | f                  | https://a0.muscach | https://a0.musca | Mount Pleasant     | 1                   | 1                         | ['phone']          | t                    | t                      | Vancouver,    | Mount Pleasant           |                              | 49.26132    | -123.10845   | Entire rental | Entire    | 2            |           | 1 bath         |          | 1    | []        |         | 5              | 60             | 5                      | 5                      | 60                     | 60                     | 5                      | 60                     |                  |                  | 0               | 0               | 0               | 0                | 2023/12/14            | 203               | 0                     | 0                      | 2012/10/1    | 2021/10/1   | 4.6                  | 4.75                   | 4.5                       | 4.85                  | 4.85                        | 4.88                   | 4.66                | 21-     | f                | 1                              | 1                                           | 0                                            | 0                                           | 1.49              |
| 18024              | https://w   | 2.02312E+13   | 2023/12/14   | previous | Home    |             | This beautiful, friendly,   | https://a0. | 69472    | https://  | Raine       | 2010/1/10  | Vancouver,    |             | N/A                | N/A                | N/A                  | f                  | https://a0.muscach | https://a0.musca | Kensington-Cedar   | 1                   | 1                         | ['phone']          | t                    | t                      | Vancouver,    | Kensington-Cedar Cottage |                              | 49.24781    | -123.07241   | Private room  | Private   | 6            |           | 1 private bath |          | 3    | []        |         | 30             | 365            | 30                     | 30                     | 365                    | 365                    | 30                     | 365                    |                  |                  | 0               | 0               | 0               | 0                | 2023/12/14            | 0                 | 0                     | 0                      |              |             |                      |                        |                           |                       |                             |                        |                     |         | f                | 1                              | 0                                           | 1                                            | 0                                           |                   |
| 18270              | https://w   | 2.02312E+13   | 2023/12/14   | previous | Condo   |             | Lots of restaurants,        | https://a0. | 70437    | https://  | Ran         | 2010/1/14  | Vancouver,    | In my spare |                    |                    |                      |                    |                    |                  |                    |                     |                           |                    |                      |                        |               |                          |                              |             |              |               |           |              |           |                |          |      |           |         |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| I also enjoy       | reading     | foreign films | and          |          |         |             |                             |             |          |           |             |            |               |             |                    |                    |                      |                    |                    |                  |                    |                     |                           |                    |                      |                        |               |                          |                              |             |              |               |           |              |           |                |          |      |           |         |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |
| I am often busy    | but         | N/A           | N/A          | N/A      | f       | https://a0. | https://a0.muscache.co      | Mount       | 1        | 4         | ['email',   | t          | t             | Vancouver,  | Mount Pleasant     |                    | 49.26557             | -123.096           | Private room in    | Private room     | 2                  |                     | 1 shared bath             |                    | 1                    | []                     | $51.00        | 30                       | 1125                         | 30          | 30           | 1125          | 1125      | 30           | 1125      |                | t        | 19   | 39        | 57      | 234            | 2023/12/14     | 118                    | 0                      | 0                      | 2011/3/17              | 2019/12/31             | 4.54                   | 4.5              | 3.98             | 4.75            | 4.73            | 4.69            | 4.49             |                       | f                 | 1                     | 0                      | 1            | 0           | 0.76                 |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             |                   |

\- Describe any problems that were present in the data and the scrubbing tasks that were necessary to prepare your data set for import - include any scrubbing done in Python, a text editor, or any other tool. Be specific with examples of the problems in the original data and the way in which those were solved. Feel free to show small snippets of relevant code - see the examples of code "syntax highlighting" in the Markdown guide linked above.

There is missing data in the original dataset. From a security perspective, I believe documents with missing data may pose a security risk. Therefore, I have decided to only use documents that contain all the data. The specific operation involves loading the listings.csv file with pandas, selecting some essential fields, and deleting documents that contain null values in these fields. Specifically, I selected 'host_id', 'name', 'price', 'host_is_superhost', 'neighbourhood', 'host_name', 'beds', 'review_scores_rating'.

```python
import pandas as pd

file_path = 'listings.csv'
data = pd.read_csv(file_path)
l = ['host_id', 'name', 'price', 'host_is_superhost','neighbourhood', 'host_name', 'beds', 'review_scores_rating']
data = data.dropna(subset= l)  
data = data[l]

output_file_path = 'listings_clean.csv'
data.to_csv(output_file_path, index=False)
```

## Analysis:

1. show exactly two documents from the `listings` collection in any order

   ```sql
   db.listings.find().limit(2)
   ```

   ```json
   [
     {
       _id: ObjectId('6607996f90769e963dfcc07e'),
       host_id: 51466,
       name: 'Rental unit in Vancouver · ★4.84 · Studio · 2 beds · 1 bath',
       price: '$150.00',
       host_is_superhost: 'f',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Ian And Emma',
       beds: 2,
       review_scores_rating: 4.84
     },
     {
       _id: ObjectId('6607996f90769e963dfcc07f'),
       host_id: 51634,
       name: 'Rental unit in Vancouver · ★4.73 · 1 bedroom · 2 beds · 1 bath',
       price: '$120.00',
       host_is_superhost: 'f',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Amanda',
       beds: 2,
       review_scores_rating: 4.73
     }
   ]
   ```

   Insights: First, there appears to be a correlation between a listing's price and its rating, with a higher rating potentially leading to a higher price, though the difference between them is not large. Second, even though neither listing is offered by a superhost, this suggests that attaining superhost status could be an opportunity to attract more guests. Lastly, the configurations of these two listings are similar, both providing 2 beds and 1 bathroom, which points to a specific market demand likely targeting small families or groups.

1. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

   ```sql
   db.listings.find().limit(10).pretty()
   ```

   ```json
   [
     {
       _id: ObjectId('6607996f90769e963dfcc07e'),
       host_id: 51466,
       name: 'Rental unit in Vancouver · ★4.84 · Studio · 2 beds · 1 bath',
       price: '$150.00',
       host_is_superhost: 'f',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Ian And Emma',
       beds: 2,
       review_scores_rating: 4.84
     },
     {
       _id: ObjectId('6607996f90769e963dfcc07f'),
       host_id: 51634,
       name: 'Rental unit in Vancouver · ★4.73 · 1 bedroom · 2 beds · 1 bath',
       price: '$120.00',
       host_is_superhost: 'f',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Amanda',
       beds: 2,
       review_scores_rating: 4.73
     },
     {
       _id: ObjectId('6607996f90769e963dfcc080'),
       host_id: 52467,
       name: 'Rental unit in Vancouver · ★4.93 · 1 bedroom · 1 bed · 1 bath',
       price: '$150.00',
       host_is_superhost: 't',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Iris',
       beds: 1,
       review_scores_rating: 4.93
     }
   ]
   ```

   Insights: First, listings hosted by superhosts typically receive higher ratings, suggesting that the superhost status may enhance guest satisfaction and could even make guests willing to pay extra for better service. Second, there is a correlation between the price of a listing and its ratings, with higher-rated listings often being more expensive, reflecting the possibility that guests may view price as an indicator of quality. Lastly, the number of beds in a listing is not the sole determinant of its price; the quality of the listing and the superhost status are also important considerations.

1. choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts

   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

   ```sql
   db.listings.find(
       { "host_is_superhost": "t", "host_id": { "$in": [52467, 71508] } },
       { "_id":0, "name": 1, "price": 1, "neighbourhood": 1, "host_name": 1, "host_is_superhost": 1 }
   )
   ```

   ```json
   [
     {
       name: 'Rental unit in Vancouver · ★4.93 · 1 bedroom · 1 bed · 1 bath',
       price: '$150.00',
       host_is_superhost: 't',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Iris'
     },
     {
       name: 'Home in Vancouver · ★4.98 · 1 bedroom · 1 bed · 1 private bath',
       price: '$99.00',
       host_is_superhost: 't',
       neighbourhood: 'Vancouver, British Columbia, Canada',
       host_name: 'Sylvain & Alexis'
     }
   ]
   ```

   Insights: Firstly, the status of superhosts indeed reflects on the quality of their listings and guest satisfaction. For instance, Iris's listing is priced at $150 with a rating of 4.93, while Sylvain & Alexis's listing, despite being lower-priced at just $99, boasts a high rating of 4.98. This demonstrates that high-quality accommodation experiences can be offered even at more budget-friendly price points. Secondly, both listings are located in Vancouver, which not only shows the popularity of the area as a travel destination but also reflects how superhosts in competitive markets attract guests by providing high standards of service and accommodation.

1. find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))

   ```sql
   db.listings.distinct("host_name")
   ```

   ```json
   [
     'A', 'Aaron', 'Aaron & Anna'
   ]
   ```

   Insights: The range of names from a single letter (e.g., “A”) to full individual names (e.g., “Aaron”) and combined names (e.g., “Aaron & Anna”) indicates the presence of various hosting arrangements. A single letter might be used for branding or anonymity, while combined names suggest a joint hosting situation, potentially offering more comprehensive support for guests. This diversity could meet different guests' expectations regarding the way they interact with hosts, the level of personalized service, and the type of hospitality offered.

1. find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending

   - only show the `name`, `beds`, `review_scores_rating`, and `price`
   - if your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.

   ```sql
   db.listings.find(
       { 
           "neighbourhood": "Vancouver, British Columbia, Canada", 
           "beds": { "$gt": 2 }, 
           "review_scores_rating": { "$ne": null }  
       },
       {
           "_id": 0,
     			"name": 1, 
           "beds": 1, 
           "review_scores_rating": 1, 
           "price": 1
       }
   ).sort({ "review_scores_rating": -1 })
   ```

   ```json
   [
     {
       name: 'Rental unit in Vancouver · ★5.0 · 2 bedrooms · 3 beds · 1 bath',
       price: '$150.00',
       beds: 3,
       review_scores_rating: 5
     },
     {
       name: 'Home in Vancouver · ★5.0 · 2 bedrooms · 4 beds · 1 bath',
       price: '$145.00',
       beds: 4,
       review_scores_rating: 5
     },
     {
       name: 'Guest suite in Vancouver · ★5.0 · 2 bedrooms · 3 beds · 2 baths',
       price: '$125.00',
       beds: 3,
       review_scores_rating: 5
     }
   ]
   ```

   Insights: All listed properties received the highest rating of 5.0, indicating that large accommodations in Vancouver are not only available but also highly rated by guests. These listings showcase a variety of bed arrangements, with combinations of 3 to 4 beds, catering to the needs of groups of different sizes. The price range varies from $125 to $150, reflecting a competitive pricing strategy among hosts. These high-rated listings demonstrate a significant demand for accommodations that can host more people while maintaining high quality standards.

1. show the number of listings per host

   ```sql
   db.listings.aggregate([
       {
           $group: {
               _id: "$host_name",  
               number_of_listings: { $sum: 1 }
           }
       }
   ])
   ```

   ```json
   [
     { _id: 'Derek', number_of_listings: 1 },
     { _id: 'Serey', number_of_listings: 1 },
     { _id: 'Gian', number_of_listings: 1 }
   ]
   ```

   Insights: Individual hosts rather than commercial hosts with multiple listings dominate the market. This situation suggests that the market might be more inclined towards or more accessible for individual hosts, potentially offering guests more personalized and unique accommodation experiences. At the same time, this also means that hosts have the opportunity to focus on niche marketing strategies, targeting specific types of travelers or experiences, which could lead to higher guest satisfaction.

1. find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))

   - if your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.

   ```sql
   db.listings.aggregate([
       {
           $group: {
               _id: "$neighbourhood",  
               average_rating: { $avg: "$review_scores_rating" }  
           }
       },
       {
           $match: {
               average_rating: { $gte: 4 }  
           }
       },
       {
           $sort: { average_rating: -1 }  
       }
   ])
   ```

   ```json
   [
     {
       _id: 'Vancouver , British Columbia, Canada',
       average_rating: 4.904999999999999
     },
     {
       _id: 'Vancouver bc, British Columbia, Canada',
       average_rating: 4.88
     },
     {
       _id: 'Vancouver, British Columbia (BC), Canada',
       average_rating: 4.82
     }
   ]
   ```

   Insights: Firstly, all listed neighborhoods have high average ratings, with the lowest being 4.82, indicating that accommodations in these areas generally meet or exceed guests' expectations. Secondly, the slight variations in ratings, ranging from 4.82 to 4.905, could reflect differences in the quality of accommodations, availability of amenities, or the overall guest experience in each neighborhood. These high average ratings may also indicate the attractiveness of these neighborhoods as places to stay, including factors such as convenience of location, scenic beauty, proximity to attractions, or safety. Moreover, the slight differences in neighborhood names could suggest inconsistencies in how hosts list their properties, potentially affecting guests' perceptions and choices.

## Extra-credit

This assignment deserves extra credit because I set up a PyMongo environment and wrote Python connection code on the server:

```python
import pymongo
connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                 username="ws2406",
                                 password="sZixb45K",
                                authSource="ws2406")
collection = connection["ws2406"]["listings"]
```

I re-executed the following query task with the Python code below: "find all of the places that have more than 2 `beds` in a neighborhood of your choosing, ordered by `review_scores_rating` descending":

```python
def first_analysis():

    neighbourhood_choice = "Vancouver, British Columbia, Canada"

    result = collection.find({
        "neighbourhood": neighbourhood_choice,
        "beds": {"$gt": 2}
    }).sort("review_scores_rating", -1)

    for document in result:
        print(document)
```

The results are as follows:

```json
[
{'_id': ObjectId('6607996f90769e963dfcc086'), 'host_id': 1267409, 'name': 'Rental unit in Vancouver · ★5.0 · 2 bedrooms · 3 beds · 1 bath', 'price': '$150.00', 'host_is_superhost': 'f', 'neighbourhood': 'Vancouver, British Columbia, Canada', 'host_name': 'Julia', 'beds': 3.0, 'review_scores_rating': 5.0}
{'_id': ObjectId('6607996f90769e963dfcc097'), 'host_id': 1267409, 'name': 'Home in Vancouver · ★5.0 · 2 bedrooms · 4 beds · 1 bath', 'price': '$145.00', 'host_is_superhost': 'f', 'neighbourhood': 'Vancouver, British Columbia, Canada', 'host_name': 'Julia', 'beds': 4.0, 'review_scores_rating': 5.0}
{'_id': ObjectId('6607996f90769e963dfcc0b3'), 'host_id': 3211112, 'name': 'Guest suite in Vancouver · ★5.0 · 2 bedrooms · 3 beds · 2 baths', 'price': '$125.00', 'host_is_superhost': 't', 'neighbourhood': 'Vancouver, British Columbia, Canada', 'host_name': 'Rasha', 'beds': 3.0, 'review_scores_rating': 5.0}
]
```

I re-executed the following query task with the Python code below: "only show the `name`, `beds`, `review_scores_rating`, and `price`"：

```python
def second_analysis():
    result = collection.find(
        {},
        {"_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1}
    )

    for document in result:
        print(document)
```

The results are as follows:

```json
[
{'name': 'Rental unit in Vancouver · ★4.84 · Studio · 2 beds · 1 bath', 'price': '$150.00', 'beds': 2.0, 'review_scores_rating': 4.84}
{'name': 'Rental unit in Vancouver · ★4.73 · 1 bedroom · 2 beds · 1 bath', 'price': '$120.00', 'beds': 2.0, 'review_scores_rating': 4.73}
{'name': 'Rental unit in Vancouver · ★4.93 · 1 bedroom · 1 bed · 1 bath', 'price': '$150.00', 'beds': 1.0, 'review_scores_rating': 4.93}
]
```

I used Python to manipulate MongoDB has the following advantages over the command line, including automated execution of tasks, easy maintenance and reuse of code, ability to handle complex logic, robust data processing support, exception catching and error handling, cross-platform compatibility, rich community resources, and better user interaction experience. In addition, Python's asynchronous and concurrent features make database operations more efficient.
