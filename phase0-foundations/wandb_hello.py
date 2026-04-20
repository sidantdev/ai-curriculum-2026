import wandb
import random
import time

run = wandb.init(
    project="phase0-foundations",
    name="hello-world",
    config={
        "learning_rate": 0.01,
        "epochs": 10,
        "notes": "First wandb run in the 24-week curriculum"
    }
)

for epoch in range(10):
    fake_loss = 1.0 / (epoch + 1) + random.random() * 0.1
    fake_acc = 1.0 - fake_loss + random.random() * 0.05
    wandb.log({
        "loss": fake_loss,
        "accuracy": fake_acc,
        "epoch": epoch
    })
    time.sleep(0.3)
    print(f"Epoch {epoch}: loss={fake_loss:.3f}, acc={fake_acc:.3f}")

run.finish()
print(f"\nView run: {run.url}")
