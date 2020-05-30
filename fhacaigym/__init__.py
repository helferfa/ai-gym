from gym.envs.registration import register

register(
        id='Fuzzy-CartPole-v0',
        entry_point='fhacaigym.cartpole:FuzzyCartEnv',
        )

register(
        id='Wumpus-v0',
        entry_point='fhacaigym.wumpus:WumpusWorldEnv',
        )

