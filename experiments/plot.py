
import pickle
import matplotlib.pyplot as plt

read_file=open('./learning_curves/retest_rewards.pkl','rb')
rewards=pickle.load(read_file)
read_file.close()
plt.plot(rewards)
plt.savefig("1.png")
