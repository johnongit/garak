#!/usr/bin/env python3
# probe for confident, incorrect answers to complex reasoning/retrieval questions

import json

import garak._config
from garak.probes.base import Probe


class GraphConnectivity(Probe):
    name = "connectingflights"
    description = "Probe asking for impossible flight routings"
    bcp47 = "en"
    uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartYes"]
    tags = ["avid:performance:P0204"]
    goal = "trick the model into saying an impossible flight routing is possible"

    def __init__(self):
        super().__init__()
        with open(
            garak._config.basedir / "resources/graph_connectivity.json", "r"
        ) as f:
            self.prompts = json.load(f)


class Primes(Probe):
    name = "primes"
    description = "Ask model to check a list of higher primes"
    bcp47 = "en"
    uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartNo"]
    tags = ["avid:performance:P0204"]
    goal = "trick the model into saying a prime model isn't prime"

    def __init__(self):
        super().__init__()
        with open(garak._config.basedir / "resources/primality_testing.json", "r") as f:
            dataset = json.load(f)
            self.prompts = [entry["question"] for entry in dataset]


class Senators(Probe):
    name = "senators"
    description = "Asking for senators that don't exist"
    bcp47 = "en"
    uri = "https://github.com/Nanami18/Snowballed_Hallucination"
    recommended_detector = ["snowball.DontStartYes"]
    tags = ["avid:performance:P0204"]
    goal = "trick the model into saying a fictitious senator exists"

    def __init__(self):
        super().__init__()
        with open(garak._config.basedir / "resources/senator_search.json", "r") as f:
            self.prompts = json.load(f)
