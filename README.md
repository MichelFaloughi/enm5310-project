# enm5310-project
My final project for the ENM 5310 class: Data-driven Modelling and Probabilistic Scientific Computing

Questions for Prof. Paris:
- Should we consider wind instead of precipitations ? Can we, given that one of Aurora's 4 tasks was hurricane tracking I believe, can we still fine-tune it to predict wind speeds ?
- 'A100 with 80 GB' in the finetuning part of Aurora
- AuroraSmallPretrained apparently is only good for debugging, nothing else. They say we don't recommend any other use. Should I still fine-tune this ? I have no other choice do I.



Questions for me later:
- Be able to define what is the ERA5 Reanalysis dataset. Okay I know the big lines etc. But what is it, how big is it, what format is it, etc.
- When we say 'Foundation model has a pre-training phase then a fine tuning phase on a smaller set of specialized data, this data is not seen in the pre-training phase right ? Hence, if I want to fine-tune Aurora, I would have to find exactly what data was used in the training of Aurora (ERA5 reanalysis) and know what NOT to use, mahek ?
- Understand what this does: model.load_checkpoint("microsoft/aurora", "aurora-0.25-small-pretrained.ckpt")
- Understand how to make a batch !!
- Understand the difference between surface, atmospheric, and static variables, and Metadata.


Resources and links:
- https://microsoft.github.io/aurora/finetuning.html#basic-fine-tuning-environment
- ARCCA ? Is this an HPC resources for penn students
https://www.arcca.upenn.edu/getting-started/
hpc-help@arcca.upenn.edu
- Microsoft Azure for Students — $100 credit with your Penn email (https://azure.microsoft.com/en-us/free/students/
)
- https://jupyterhub.seas.upenn.edu/



To do:
- find a way to run the examples on your laptop. Convert to less precise floating points etc, idk but find a way. If you can't do that, then we're in trouble maybe. 
- To do the above, try running on the Aurora Smaller model, with far less parameters.

