
pooling = 'mean' #"max"

h_out = 128

import string
num_char_types = len(string.printable[:-4]) + 1

char_embed_dim = 20

column_encoding_dim = 32 #16

strLen = 100

encoder = 'dense'

num_dense_layers = 10

growth_rate = 128

button_embed_dim = 32

batchsize = 4000

train_iterations = 100000

save_path = 'robut_model_new_prelim.p' #'robut_model_larger.p' #'robut_model_conv.p' # #'robut_model.p'
load_path = 'robut_model_new_prelim.p'
#big means fatter ... 10 layers of 128 growth rate

#Vnet_save_path = 'robut_vnet.p' 

print_freq = 20

save_freq = 100

test_freq = 1000

column_enc = 'conv' #'linear' #'conv' #'linear' 
kernel_size = 5

n_rollouts = 40

n_envs_per_rollout = 50