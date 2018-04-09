"""
1. Define terminology:
    1) plan: a plan is an instance of a Plan class. Each plan has the following attributes: Time(a Time instance which has 2 attributes, Departure time and Landing time), Location(a Location instance which has 2 attributes: Departure place and the Landing place), Price-range(also a instance with attribute of lowest and highest), Largest Stop number(int).
    2) flight: a flight is an instance of a Flight class. Each flight has the following attributes:
        Flight Number,
        Price,
        Departure time,
        Landing time,
        Company name,
        URL,
    3) tank: an instance who store the latest information of the flight.
       Attributes:
           1.pool: a dictionary whose label is the flight's unique(like CZ1900) and the value is an flight object.
       Method:
           1. update: After everytime using a clawer, update the flight objects collected.
           2. min: takes an plan and return the flight objects whose sum has the min price of all other conbinations.
                   * the stop number is limited by the Largest_Stop_Number attribute of a plan.

           3. is_alter: keep track the pool and everytime it's updated, call the min method on the tank. If the result is different from previous, return True; Otherwise, return False and update the function.
           4. alter: send the email if the is_alter return True.

2. Workflow:
    1) user input their plans (including: Departure_time, Landing_time, Departure_place, Landing_place, Price_range, Maxium_acceptable_stop)
    2) use the information user input to build instances:
        flight_price_range = Range(lowest, hightest)
        flight_time = Time(Departure_time=None, Landing_time=None) # if one of the time information is missing, seprate the case in the tank.min() method
        flight_place = Place(Departure_place, Landing_place)
        flight_plan = Plan(flight_time, flight_place, Maxium_acceptable_stop)
    3) use the clawer to get the information of the flight evey 6 hours, including:
        Flight Number,
        Price,
        Departure time,
        Landing time,
        Company name,
        URL,
    4) create the flight instance each time we get the information from the clawer and update them in to the tank's pool attribute using the update method.
    5) Every time updated, call the tank.is_alter method to decide whether or not to send the email.

3. Engineer Checklist:
    1) Class:
        Plan(flight_time, flight_place, flight_range, max_stops)
        Place(departure_place, landing_place)
        Time(departure_time, landing_time)
        CostRange(lowest_price, highest_price)
        Flight(flight_num, flight_price(fixed int), flight_place, company, flight_url)
        Tank(plan, pool)
    2) Method:
        Tank.update(self, {dictionary of the updated flight})
        Tank.min(self)
        Tank.is_alter(self)
        Tank.alter(self)
4. Dark Zone: (the part we still don't know how to write)
    1) tank.min():
        the algorithm that find the smallest combination of the flight that makes the total smallest under the constrains of the stop limit. May find some theroey in Graph therory useful.
    2) How to clawer the information from the web where some of them may have the tech of anti-cralwer.
    3) How to send the email using a script.
"""
class Plan:
    def __init__(self, flight_time, flight_place, flight_range, max_stops):
        self.flight_time = flight_time
        self.flight_place = flight_place
        self.max_stop = max_stop
        self.flight_range = self.flight_range

class Place:
    def __init__(self, departure_place, landing_place):
        self.departure_place = departure_place
        self.landing_place = landing_place

class Time:
    def __init__(self, departure_time, landing_time):
        self.departure_time = departure_time
        self.landing_time = landing_time
class CostRange:
    def __init__(self, lowest_price, highest_price):
        self.lowest_price = lowest_price
        self.highest_price = highest_price

class Flight:
    def __init__(self, flight_num, flight_price, flight_place, company, flight_url):
        self.flight_num = flight_nim
        self.price = flight_price
        self.company = company
        self.flight_url = flight_url

class Combination:
    def __init__(self, flight_place, *args):
        self.flight_place = flight_place # flight_place is an istance of Place which contains the info of departure and landing place.
        self.flights = [*args] # a list contains all the transit flights

class Tank:
    def __init__(self, plan, pool={}, lowest=None):
        self.plan = plan
        self.pool = pool
        self.lowest = lowest

    def update(self, update_info):
        self.pool.update(update_info)

    def min(self):
        """ Return a Combination instance which is the shortest combination in the pool that make the sum of the cost the lowest"""

    def is_alter(self):
        lowest_now = self.min(self)
        if self.lowest is lowest_now:
            return False
        self.lowest = lowest_now
        return True
    def alter(self):
        if self.is_alter():
            self.send()
    def send(self):
        """ A method of Tank which can send email using the info of tank.lowest."""



