#!/usr/bin/env python
# coding: utf-8

# import the necessary libraries
import json
from unity_simulator.comm_unity import UnityCommunication
import sys
import re

sys.path.append("../simulation")

# establish a link with VirtualHome
comm = UnityCommunication()
print("Starting scene...")
comm.reset()
comm.add_character("Chars/Female1")

# make the agent do somethings
script = ["<char0> [Walk] <KITCHEN> (4)"]
comm.render_script(script, recording=True, find_solution=True)

script = ["<char0> [TurnLeft] (4)"]
comm.render_script(script, recording=True, find_solution=True)

# # get a list of the objects visible to the agent
# comm.get_visible_objects(2)
# comm.add_character_camera()

x = comm.environment_graph()  # x[1] is the environment graph
# print(type(x[1]))


# with open("asd.json", "w") as f:
#     json.dump(x[1], f, indent=4)

# get the items in each of the four rooms
items = {}
present_class = None
for idx, node in enumerate(x[1]["nodes"]):
    if "ROO_" in node["prefab_name"]:
        present_class = node["class_name"]
        items[present_class] = [idx, 0]
    else:
        if present_class is None:
            continue
        if items[present_class] is not None:
            items[present_class][1] = idx


bathroom_objects = x[1]["nodes"][items["bathroom"]
                                 [0] + 1: items["bathroom"][1]]
bedroom_objects = x[1]["nodes"][items["bedroom"][0] + 1: items["bedroom"][1]]
kitchen_objects = x[1]["nodes"][items["kitchen"][0] + 1: items["kitchen"][1]]
livingroom_objects = x[1]["nodes"][items["livingroom"]
                                   [0] + 1: items["livingroom"][1]]

objs_bathroom = {}
objs_bedroom = {}
objs_kitchen = {}
objs_livingroom = {}

for i in x[1]["nodes"][items["bathroom"][0]: items["bathroom"][1]]:
    objs_bathroom[i["class_name"]] = i["id"]
for i in x[1]["nodes"][items["bedroom"][0]: items["bedroom"][1]]:
    objs_bedroom[i["class_name"]] = i["id"]
for i in x[1]["nodes"][items["kitchen"][0]: items["kitchen"][1]]:
    objs_kitchen[i["class_name"]] = i["id"]
for i in x[1]["nodes"][items["livingroom"][0]: items["livingroom"][1]]:
    objs_livingroom[i["class_name"]] = i["id"]
