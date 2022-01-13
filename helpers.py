# Convert processing code to function
import json


def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
    skip_data = ["challenges", "duetInfo", "textExtra", "stickersOnItem"]
    flattened_data = {}
    for idx, value in enumerate(data):
        new_dict = {}
        keys = value.keys()
        for prop_key, prop_value in value.items():
            if prop_key in nested_values:
                for proper_key_, prop_value_ in prop_value.items():
                    new_dict[f"{prop_key}_{proper_key_}"] = prop_value_
            elif prop_key in skip_data:
                continue
            else:
                new_dict[prop_key] = prop_value
        flattened_data[idx] = new_dict

    return flattened_data
