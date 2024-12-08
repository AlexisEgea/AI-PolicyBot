import csv
import os
import json
import statistics
import csv


class PolicyBot():

    def __init__(self, game):

        self.game = game
        self.preprocess_data()
        policyFile = open('src/data/policy.json')
        self.policy = json.load(policyFile)
        policyFile.close()

    def preprocess_data(self):
        data = {}
        # Load data
        data_path = os.path.join(os.getcwd(), "src/data/421.csv")
        with open(data_path, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                state, action, value = tuple(line)
                value = float(value)
                if state not in data:
                    data[state] = {action: [value]}
                elif action not in data[state]:
                    data[state][action] = [value]
                else:
                    data[state][action].append(value)
        # Compute the average score for each tuple (state, action)
        average_score = {}
        for state, value in data.items():
            for action, score in value.items():
                if state not in average_score:
                    average_score[state] = {action: statistics.mean(score)}
                elif action not in average_score[state]:
                    average_score[state][action] = statistics.mean(score)

        # Select the action with the maximum score in a policy dictionary
        policy = {}
        for state, value in average_score.items():
            list_score = []
            list_action = []
            for action, score in value.items():
                list_score.append(score)
                list_action.append(action)

            max_score = max(list_score)
            index_max_score = list_score.index(max_score)

            policy[state] = list_action[index_max_score]
        # Save policy
        policy_file = open("src/data/policy.json", "w")
        json.dump(policy, policy_file, sort_keys=True, indent=2)
        policy_file.close()

    def perceive(self, game):
        pass

    def decide(self):
        state = self.game.get_state()
        action = self.policy[state]
        return action

    def sleep(self, result):
        pass



