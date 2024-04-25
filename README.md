<h1 align="center">
    micro-musicgen
</h1>
<p align="center">
  <img src="./assets/micro-musicgen-post.webp" width="250" alt="Nendo Core">
</p>

<p align="center">
    A new family of super small music generation models focusing on experimental music and latent space exploration capabilities.
</p>

<p align="center">
    <a href="https://opensource.org/licenses/MIT" target="_blank">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    </a>
    <a href="https://huggingface.co/pharoAIsanders420/micro-musicgen-jungle" target="_blank">
        <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging_Face-Model_Weights-yellow?style=flat&link=https%3A%2F%2Fhuggingface.co%2FpharoAIsanders420%2Fmicro-musicgen-jungle">
    </a>
    <a href="https://twitter.com/mcaaroni" target="_blank">
        <img src="https://img.shields.io/twitter/url/https/twitter.com/mcaaroni.svg?style=social&label=Follow%20%40mcaaroni" alt="Twitter">
    </a>
</p>

---

> [!WARNING]  
> WARNING: **These models WILL sound bad to a lot of people.** The goal is not create pleasant sounding music,
> but to spark creativity by using the weird sounds of Neural Codecs for music production and sampling!

## Models 

- [micro-musicgen-jungle](https://huggingface.co/pharoAIsanders420/micro-musicgen-jungle)
- ...more coming soon

If you find these model interesting, please consider:

- following me on [Github](https://github.com/aaronabebe)
- following me on [Twitter](https://twitter.com/mcaaroni)


### Goals

My main goals for these models was to be able to train and run **from scratch** on a consumer grade GPU at home.
Based on my personal workflow with music generation models, I experimented with different configurations
and landed on this architecture which offers different advantages and drawbacks:

- 

### Architecture

<p align="center">
  <img src="./assets/musicgen_arch.jpeg" width="500" alt="Nendo Core">
</p>

image original source: [https://docs.openvino.ai/2024/notebooks/250-music-generation-with-output.html](https://docs.openvino.ai/2024/notebooks/250-music-generation-with-output.html)

My configuration in [micro.yaml](./audiocraft/config/model/lm/model_scale/micro.yaml):

```yaml
# @package _global_

transformer_lm:
  dim: 2048
  num_heads: 2
  num_layers: 2
```


goal is to allow gpu poor to train their own experimental models
the models have drawbacks and improvements that optimize for experimental workflow -> 
fast iteration speed, weird sounds, no conditioning

reduce transformer lm size inside musicgen to reduce size and increase speed
no text conditioning to reduce size and train speed
make use of encodec inherent inductive biases when generating audio
use genres that work with weird sounds/glitches and 32khz for finetuning
purposefully undertrain with small amounts of data


### Speed

I benchmarked comparing vs. `musicgen-small` via `audiocraft` and measured cold-boot start time. 
See [bench.py](./scripts/bench.py).

comparison plot

### Size 

See [size.py](./scripts/size.py).

comparison plot

## Setup 

Basically you can refer to everything from the [original docs](https://github.com/facebookresearch/audiocraft/blob/main/docs/TRAINING.md) 
or for example one of the great community writeups (e.g. [by lyra](https://github.com/lyramakesmusic/finetune-musicgen)) and follow their setup. 
Everything is the same as in the original repo and standard musicgen training except for my model configuration and run params.

## Training 

```sh
dora run solver=musicgen/musicgen_base_32khz model/lm/model_scale=micro conditioner=none dataset.batch_size=3 dset=audio/jungle dataset.valid.num_samples=1 generate.every=10000 evaluate.every=10000 optim.optimizer=adamw optim.lr=1e-4 optim.adam.weight_decay=0.01 checkpoint.save_every=5
```

explain param choices

explain my train runs with example

## FAQ

#### Are the models not just overfitting on snippets of the trainset? 
Not sure, probably yes? But doesn't really matter for this use case I'd say, still sounds cool.

#### The model I trained sounds like shit, why? 
Probably expected, I'd say it only works for more abstract stuff - don't expect it to generate your favorite hiphop beats to study to.

#### Why only 32kHz? Why no DAC? 
I tried DAC but the pretrained one somehow fails with these small amounts of data. 
I think Encodec somehow works better with the LM's but can't really say why. 
Also DAC is way slower to train and run, so I decided against it.

#### Why only mono?
Let's be real, stereo Encodec just sucks.

## Next steps

- [ ] create colab / HF space for demoing
- [ ] write custom inference script to get more optimizations 
- [ ] train more models, try smaller architectures


## Extra: Changes in my audiocraft fork
If you dont want to use my fork, below are all the changes I made. 
Since there are just a few changes it totally makes sense to just update your fork if you want to:

### fix bug in loader when no conditioner is present


### add custom lm size configs



