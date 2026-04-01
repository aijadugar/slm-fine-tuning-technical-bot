# Fine-Tuned Technical Support SLM  
### Llama 3.2 + Unsloth + LoRA + Hugging Face Deployment

---

## Live Demo
=> https://huggingface.co/spaces/aijadugar/ft_slm  

---

## About The Project

This project demonstrates how to build a **fast, lightweight, and efficient Small Language Model (SLM)** for **technical support automation** using modern LLM optimization techniques.

Instead of training massive models, this project focuses on:
- **Speed**
- **Low memory usage**
- **Cost efficiency**

The model is based on **Llama 3.2 (3B Instruct)** and fine-tuned using:
- **Unsloth** (for fast training)
- **LoRA (Low-Rank Adaptation)** for parameter-efficient fine-tuning
- **4-bit quantization** for minimal GPU usage

---

## Use Cases

- Technical Support Chatbots  
- Customer Service Automation  
- AI Assistants for SaaS Products  
- Edge AI / Low-resource deployments  
- Internal IT Helpdesk Bots  

---

## Model Details

| Component        | Description |
|----------------|------------|
| Base Model      | `unsloth/Llama-3.2-3B-Instruct` |
| Fine-Tuning     | LoRA (PEFT) |
| Dataset         | `databricks/databricks-dolly-15k` (subset) |
| Quantization    | 4-bit (bitsandbytes) |
| Framework       | Unsloth + Transformers + TRL |
| Training Env    | Kaggle Notebook |
| Deployment      | Hugging Face Hub + Inference API |

---

## Training Pipeline

1. Load base model with **4-bit quantization**
2. Apply **LoRA adapters** to key transformer layers
3. Format dataset into **chat template**
4. Fine-tune using **SFTTrainer**
5. Merge LoRA weights into base model
6. Push final model to **Hugging Face Hub**
7. Deploy via **Inference API + Spaces UI**

---

## Prompt Format

```text
<|begin_of_text|>
<|system|>
You are a Technical Support Expert
<|user|>
User query
<|assistant|>
Response
