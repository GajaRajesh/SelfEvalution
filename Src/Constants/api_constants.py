class URL:

    @staticmethod
    def createbooking():
        post_url="https://restful-booker.herokuapp.com/booking"
        return post_url

    @staticmethod
    def getbookingids():
        URL="https://restful-booker.herokuapp.com/booking"
        return URL

    def getbooking(id):
        URL="https://restful-booker.herokuapp.com/booking/"+str(id)
        return URL

    def updatebooking(id):
        URL="https://restful-booker.herokuapp.com/booking/"+str(id)
        return URL

    def partial_update(request,id):
        URL="https://restful-booker.herokuapp.com/booking/"+str(id)
        return URL

    def delete(request,id):
        URL="https://restful-booker.herokuapp.com/booking/"+str(id)
        return URL
