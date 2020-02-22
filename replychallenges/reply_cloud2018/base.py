
class Provider():
    def __init__(self, name, no_of_regions, regions):
        self.name = name
        self.no_of_regions = no_of_regions
        self.regions = regions

class Region():
    def __init__(self, name, no_of_service_units_avail, cost_of_package, no_of_units_avial_in_each_pack):
        self.name = name
        self.no_of_service_units_avail = no_of_service_units_avail
        self.cost_of_package = cost_of_package
        self.no_of_units_avial_in_each_pack = no_of_units_avial_in_each_pack

class Project():
    def __init__(self, penalty, country, amount_of_service_needed_for_each_serv_pack):
        self.penalty = penalty
        self.country = country
        self.amount_of_service_needed_for_each_serv_pack = amount_of_service_needed_for_each_serv_pack