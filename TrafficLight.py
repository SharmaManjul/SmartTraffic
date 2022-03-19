class TrafficLight:
    def __init__(self, light_state, traffic):
        self.light_state = light_state
        self.traffic = traffic

    def get_light_state(self):
        return self.light_state

    def get_traffic(self):
        return self.traffic


l_1 = TrafficLight(1, 23)
print(l_1.get_light_state())
print(l_1.get_traffic())

