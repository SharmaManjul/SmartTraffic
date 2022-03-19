class TrafficLight:
    def __init__(self, light_state, traffic, r_time, y_time, g_time):
        self.light_state = light_state
        self.traffic = traffic
        self.r_time = r_time
        self.y_time = y_time
        self.g_time = g_time

    def get_light_state(self):
        return self.light_state

    def get_traffic(self):
        return self.traffic

    def get_r_time(self):
        return self.r_time

    def get_y_time(self):
        return self.y_time

    def get_g_time(self):
        return self.g_time

    def set_light_state(self, light_state):
        self.light_state = light_state

    def set_traffic(self, traffic):
        self.traffic = traffic

    def set_r_time(self, r_time):
        self.r_time = r_time

    def set_y_time(self, y_time):
        self.y_time = y_time

    def set_g_time(self, g_time):
        self.g_time = g_time


l_1 = TrafficLight(0, 0, 0, 0, 0)

print(l_1.get_light_state())
print(l_1.get_traffic())

l_1.set_light_state(2)
l_1.set_traffic(13)

print(l_1.get_light_state())
print(l_1.get_traffic())

