import pymongo
connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                 username="ws2406",
                                 password="sZixb45K",
                                authSource="ws2406")
collection = connection["ws2406"]["listings"]

def first_analysis():

    neighbourhood_choice = "Vancouver, British Columbia, Canada"

    result = collection.find({
        "neighbourhood": neighbourhood_choice,
        "beds": {"$gt": 2}
    }).sort("review_scores_rating", -1)

    for document in result:
        print(document)

first_analysis()

def second_analysis():
    result = collection.find(
        {},
        {"_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1}
    )

    for document in result:
        print(document)

second_analysis()
