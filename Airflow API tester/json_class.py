class Wait_time_object:
    
    def __init__(self,id,theme_park,land,ride_name,is_open,wait_time,updated):
        self.id = id
        self.theme_park = theme_park
        self.land = land
        self.ride_name = ride_name
        self.is_open = is_open
        self.wait_time = wait_time
        self.updated = updated

    def print(self):
        print(f"\nID: {self.id} \nPark: {self.theme_park} \nLand: {self.land} \nRide: {self.ride_name} \nIs open: {self.is_open} \nWait Time: {self.wait_time} \nUpdated: {self.updated}")

        