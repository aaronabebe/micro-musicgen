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

## considerations

goal is to allow gpu poor to train their own experimental models
the models have drawbacks and improvements that optimize for experimental workflow -> 
fast iteration speed, weird sounds, no conditioning

reduce transformer lm size inside musicgen to reduce size and increase speed
no text conditioning to reduce size and train speed
make use of encodec inherent inductive biases when generating audio
use genres that work with weird sounds/glitches and 32khz for finetuning
purposefully undertrain with small amounts of data
mono, because stereo kinda sucks with encodec
tried DAC but that fails with these small amounts of data, is way slower due to more codebooks

## features 

inference speed comparison 
cold boot inference script vs. small musicgen model
model size vs. small musicgen model



## models

explain final architecture

<p align="center">
  <img src="./assets/musicgen_arch.jpeg" width="250" alt="Nendo Core">
</p>
source: https://docs.openvino.ai/2024/notebooks/250-music-generation-with-output.html


## setup 

audiocraft setup from my fork

## training 

train command to run training
explain param choices

explain my train runs with example


## next steps

- [ ] create colab / HF space for demoing
- [ ] write custom inference script to get more optimizations 
- [ ] train more models, try smaller architectures


## extra: changes in my audiocraft fork

### fix bug in loader when no conditioner is present


### add custom lm size configs
