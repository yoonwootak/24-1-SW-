class TravelDestination:
    def __init__(self, destinationID, name, description):
        self.destinationID = destinationID
        self.name = name
        self.description = description

    @staticmethod
    def searchByKeyword(keyword):
        destinations = []
        with open("keyword_travel_destinations.txt", "r", encoding="utf-8") as file:
            for line in file:
                destinationID, name, description, keywords = line.strip().split("|")
                if keyword in keywords.split(","):
                    destinations.append(TravelDestination(destinationID, name, description))
        return destinations

    @staticmethod
    def searchByMonth(month):
        destinations = []
        with open("month_travel_destinations.txt", "r", encoding="utf-8") as file:
            for line in file:
                destinationID, name, description, months = line.strip().split("|")
                if str(month) in months.split(","):
                    destinations.append(TravelDestination(destinationID, name, description))
        return destinations
