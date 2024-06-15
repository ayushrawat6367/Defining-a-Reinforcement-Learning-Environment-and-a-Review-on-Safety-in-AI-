import numpy as np
import matplotlib.pyplot as plt
import gym
from gym import spaces
import random

class GridEnv(gym.Env):
  metadata = {'render.modes': []}
  def _int_(self):
    self.observation_space = spaces.Discrete(16)
    self.action_space= spaces.Discrete(4)
    self.max_timesteps = 10
    self.reward = 0
    
  def reset(self):
    self.timestep = 0
    self.agent_pos = [0,0]
    self.goal_pos = [3,3]
    self.state = np.zeros((4,4))
    self.state[tuple(self.goal_pos)] = 3
    self.state[tuple(self.agent_pos)] = 1
    self.reward=0
    observation = self.state.flatten()
    return observation

  def step(self, action):
    if action==0:
      self.agent_pos[0] += 1
    if action==1:
      self.agent_pos[0] -= 1
    if action==2:
      self.agent_pos[0] += 1
    if action==3:
      self.agent_pos[0] -= 1
    self.agent_pos = np.clip(self.agent_pos, 0,3)
    self.state= np.zeros((4,4))
    self.state[tuple(self.goal_pos)]=3
    self.state[tuple(self.agent_pos)]=1
    reward=1
    observation = self.state.flatten()
    if (self.agent_pos==[0,1]).all():
      reward=-3
    if(self.agent_pos==[0,4]).all():
      reward=2
    if(self.agent_pos==[2,3]).all():
       reward=-2
    if(self.agent_pos==[3,2]).all():
      reward=5
      
    if(self.agent_pos==self.goal_pos).all():
      reward=10
      done =True
    done= True if self.timestep >= self.max_timesteps else False
    info = {}
    return observation, reward,done, info



  def render(self):
   plt.imshow(self.state)

env = GridEnv()
env._int_()

total_reward=0
observation = env.reset()
for _ in range(10):
    action = env.action_space.sample() 
    observation, reward, done, info = env.step(action) 
    total_reward = total_reward + reward
    print('State: {} Action : {} Reward: {}'.format(observation,action,total_reward))
    env.render()

