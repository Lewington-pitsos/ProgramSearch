import os
from datetime import datetime

#TODO add timeout stuff so can rerun
timestamp = datetime.now().strftime('%FT%T')
timestamp += '40obj30sec'

checkpoints = [
('abs_modular', '2d_imitation_abstraction_2019-11-23T17:53:35.pickle', 'SMC'),
('abs_modular_rl' , '2d_critic_abstraction_2019-11-22T11:42:53.pickle', 'SMC'),
#('modularRLfinetune', '2d_rl_after_contrastive.pickle'),
('no_REPL', '2d_imitation_noExecution_abstraction_2019-11-07T10:50:12.pickle', 'noExecution'),
('abs_non_modular', '2d_imitation_abstraction_2019-11-28T13:21:02.pickle', 'SMC'),
('full_repl', '2d_critic_2019-11-30T01:01:12.pickle', 'SMC'),
]

for name, checkpoint, solver in checkpoints:
	os.system(f"python driver.py test --2d --train_abstraction --checkpoint checkpoints/{checkpoint} --solvers {solver} --timeout 30 --outputFolder {name}{timestamp} --maxShapes 40")

names, _, _ = zip(*checkpoints)
testResults = " ".join(f"experimentOutputs/{name}{timestamp}/testResults.pickle" for name in names)
names = " ".join(names)

cmd = f"python graphs.py {testResults} --names {names} -t 20 -e figures/graph{timestamp}.png -n testgraph"
print(cmd)
os.system(cmd)

#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --vector_loss_type norm --checkpoint AbstractContrastiveNormVecLoss.pickle --trainTime 48
#15675749
#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --vector_loss_type triplet --checkpoint AbstractContrastiveTripletVecLossAlpha05.pickle --alpha 0.05 --trainTime 48
#15675858
#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --vector_loss_type triplet --checkpoint AbstractContrastiveTripletVecLossAlpha2.pickle --alpha 0.2 --trainTime 48
#15675818
#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --vector_loss_type triplet --checkpoint AbstractContrastiveTripletVecLossAlpha1.pickle --alpha 1.0 --trainTime 48
#15675859
#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --vector_loss_type triplet --checkpoint AbstractContrastiveTripletVecLossAlpha5.pickle --alpha 5.0 --trainTime 48
#15675873

#sbatch execute_gpu_1080.sh python driver.py imitation --2d --train_abstraction --contrastive --checkpoint AbstractContrastive.pickle --trainTime 48
#15676197