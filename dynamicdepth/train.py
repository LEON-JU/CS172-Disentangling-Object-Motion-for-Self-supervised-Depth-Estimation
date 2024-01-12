import torch
import random
import numpy as np
# from .normal import Trainer
from .flow import Trainer
from .options import MonodepthOptions

def seed_all(seed):
    if not seed:
        seed = 1

    print("[ Using Seed : ", seed, " ]")

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.cuda.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.enabled = False
    torch.backends.cudnn.benchmark = False

options = MonodepthOptions()
opts = options.parse()

seed_all(opts.pytorch_random_seed)

if __name__ == "__main__":
    torch.cuda.empty_cache()
    trainer = Trainer(opts)
    trainer.train()
