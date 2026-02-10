from models.property import PropertyModel
from models.review import ReviewModel
# from models.request import RequestModel

property_list = [
    PropertyModel(title="Apartment", price= 40, numOfRooms=5,numOfBathrooms=4,location='Manama',user_id=1),
    PropertyModel(title="House", price= 100000, numOfRooms=15,numOfBathrooms=6,location='Manama',user_id=1),
    PropertyModel(title="Villa", price= 500000, numOfRooms=15,numOfBathrooms=14,location='Manama',user_id=1)   
]


reviews_list = [
    ReviewModel(content="This is a great apartment", property_id=1),
    ReviewModel(content="This house is expensive", property_id=2),
    ReviewModel(content="I liked this villa", property_id=3)
]