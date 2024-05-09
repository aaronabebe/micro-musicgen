from audiocraft.models import MusicGen
import matplotlib.pyplot as plt
import time
import torch

def bench_model(name: str) -> float:
    start_time = time.time()
    model = MusicGen.get_pretrained(name)
    model.set_generation_params(duration=10)
    _ = model.generate_unconditional(10)
    end_time = time.time()

    del model
    torch.cuda.empty_cache()

    return end_time - start_time
    


def main():
    time_micro = bench_model('pharoAIsanders420/micro-musicgen-acid')
    time_small = bench_model('facebook/musicgen-small')

    model_names = ['micro-musicgen', 'musicgen-small']
    params_counts = [time_micro, time_small]

    plt.figure(figsize=(8, 6))
    plt.bar(model_names, params_counts, color=['green', 'blue'])
    plt.ylabel('Inference speed batch size 10 (seconds)')
    plt.title('Comparison of cold inference speed')
    plt.savefig("bench.png")


if __name__=="__main__":
    main()
