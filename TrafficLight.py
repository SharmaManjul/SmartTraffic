class TrafficLight:
    def __init__(self, light_state, traffic, r_time, y_time, g_time):
        self.light_state = light_state
        self.traffic = traffic
        self.r_time = r_time
        self.y_time = y_time
        self.g_time = g_time

    def traffic_flow(self):
        print("Light state inside traffic flow: ", self.light_state)
        if self.light_state == 1:
            self.traffic += self.r_time * 5  # 5 cars per minute getting added
        elif self.light_state == 2:
            self.traffic += self.y_time * 2
        elif self.light_state == 3:
            self.traffic -= self.g_time * 4
        else:
            print("Invalid Light State.")

    def get_light_state(self):
        return self.light_state

    def get_traffic(self):
        return self.traffic

    def get_traffic_time(self):
        return {"red":self.r_time, "yellow":self.y_time, "green": self.g_time}

    def set_light_state(self, light_state):
        self.light_state = light_state
        self.traffic_flow()

    def set_traffic(self, traffic):
        self.traffic = traffic

    def set_traffic_time(self, r_time, y_time, g_time):
        self.r_time = r_time
        self.y_time = y_time
        self.g_time = g_time


l1 = TrafficLight(0, 0, 0, 0, 0)
l1.set_traffic_time(3, 0.05, 3)
l1.set_traffic(0)

print("Initial traffic times: ", l1.get_traffic_time())

l1.set_light_state(1)
print(l1.get_light_state())
print(l1.get_traffic())

l1.set_light_state(2)
print(l1.get_light_state())
print(l1.get_traffic())

l1.set_light_state(3)
print(l1.get_light_state())
print(l1.get_traffic())
