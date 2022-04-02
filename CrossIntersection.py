from TrafficLight import *


def main():
    print("This is a cross inetersection.")
    light_x = TrafficLight(0, 0, 3, 0.05, 3)
    light_y = TrafficLight(0, 0, 3, 0.05, 3)

    light_x.set_light_state(1)
    light_y.set_light_state(1)
    traffic_status_logger(light_x)
    #Need to re think the idea of lights, might be better to have one function that computes everything instead of
    #specifying light states manually.

def traffic_status_logger(light):
    light_map = {1:"red", 2:"yellow", 3:"green"}
    print("The light state is: ", light_map[light.get_light_state()], "with traffic")


if __name__ == "__main__":
    main()
