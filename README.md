# enm5310-project
My final project for the ENM 5310 class: Data-driven Modelling and Probabilistic Scientific Computing

Questions for Prof. Paris:
- 'A100 with 80 GB' in the finetuning part of Aurora
- AuroraSmallPretrained apparently is only good for debugging, nothing else. They say we don't recommend any other use. Should I still fine-tune this ? I have no other choice do I.
- maybe theme the project: 'how good can we predict rainfall after finetuning with an 8gb gpu'


Questions for me later:
- Be able to define what is the ERA5 Reanalysis dataset. Okay I know the big lines etc. But what is it, how big is it, what format is it, etc.
- When we say 'Foundation model has a pre-training phase then a fine tuning phase on a smaller set of specialized data, this data is not seen in the pre-training phase right ? Hence, if I want to fine-tune Aurora, I would have to find exactly what data was used in the training of Aurora (ERA5 reanalysis) and know what NOT to use, mahek ?
- Understand encoders and decoders better. I kinda do, but need more
- Understand what HuggingFace is, intimately
- Understand LoRA intimately

when I say understand I mean intimately

- What the heck is a docker image



Resources and links:
- https://microsoft.github.io/aurora/finetuning.html#basic-fine-tuning-environment
- ARCCA ? Is this an HPC resources for penn students
https://www.arcca.upenn.edu/getting-started/
hpc-help@arcca.upenn.edu
- Microsoft Azure for Students — $100 credit with your Penn email (https://azure.microsoft.com/en-us/free/students/
)
- https://jupyterhub.seas.upenn.edu/
- https://github.com/microsoft/aurora/issues/155 about precipiations !


To do:
- find a way to run the examples on your laptop. Convert to less precise floating points etc, idk but find a way. If you can't do that, then we're in trouble maybe. 
- To do the above, try running on the Aurora Smaller model, with far less parameters.
- So we've established the only model that is going to run on my computer is AuroraSmallPretrained. Find out how to download some real ERA5 data with the correct dimensions and feed it to it.

- Maybe come up with a function to pretty print a Batch into a dataframe or tabular data of some sort. Is that feasible ? Memory-wise ? Is it already done ? Check the Batch.py file

- Come up with a loss !

- 

Observations:
- loading data into a batch takes forever haha
- So with my meager RTX 4070 gpu, I'm gonna have to freeze most model parameters, using something like this:
for p in model.parameters():
    p.requires_grad = False

then, I'll unfreeze the lightweight parts,

