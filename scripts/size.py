from audiocraft.models import MusicGen
import matplotlib.pyplot as plt
import torch.nn as nn

def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def count_musicgen_parameters(name: str) -> int:
    model = MusicGen.get_pretrained(name)
    params = count_parameters(model.compression_model)
    params += count_parameters(model.lm)
    del model

    return params


def main():
    params_micro = count_musicgen_parameters('pharoAIsanders420/micro-musicgen-jungle') / 1e6
    params_small = count_musicgen_parameters('facebook/musicgen-small') / 1e6

    model_names = ['micro-musicgen', 'musicgen-small']
    params_counts = [params_micro, params_small]

    plt.figure(figsize=(8, 6))
    plt.bar(model_names, params_counts, color=['green', 'blue'])
    plt.ylabel('Number of Parameters in Millions (Encodec + LM)')
    plt.title('Comparison of Model Parameters')
    plt.show()


if __name__=="__main__":
    main()
