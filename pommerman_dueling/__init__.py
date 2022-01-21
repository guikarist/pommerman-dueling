from gym.envs.registration import register

register(
    id='PommermanDuelingSimple-v0',
    entry_point='pommerman_dueling.envs:PommermanDuelingSimple',
)

register(
    id='PommermanDuelingRandom-v0',
    entry_point='pommerman_dueling.envs:PommermanDuelingRandom',
)
