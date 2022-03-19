class TrafficLight:
    def __init__(self, light_state, traffic):
        self.light_state = light_state
        self.traffic = traffic

    def get_light_state(self):
        return self.light_state

    def get_traffic(self):
        return self.traffic

    def set_light_state(self, light_state):
        self.light_state = light_state

    def set_traffic(self, traffic):
        self.traffic = traffic


l_1 = TrafficLight(0,0)

print(l_1.get_light_state())
print(l_1.get_traffic())

l_1.set_light_state(2)
l_1.set_traffic(13)

print(l_1.get_light_state())
print(l_1.get_traffic())

