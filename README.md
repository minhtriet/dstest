## Text classification test

### How to run
- Create a new virtual environment
- Run `pip install -r requirements.txt`
- `tr_q1.ipynb` Exploratory analysis. In the end of the notebook, there is a section called "Answer" in which I answer the questions posted
- `tr_q2.ipynb` Train
  - Hyperparams tuning: Split the training to 50-50 to tune the hyperparameters. Later use best paramenters to train on the whole training set.
  - Log experiments to Tensorboard  
  
### Error analysis
My laptop has no GPU to fintuning the whole dataset, hence I can only do a subset of it
