# - https: // openai.com / pricing
# - https: // platform.openai.com / docs / models
# - https: // www.anthropic.com / pricing

def calculate_cost(model_name, in_tokens, out_tokens):
    if model_name not in MODEL_CONFIG:
        raise ValueError("Unknown model name")
    input_cost_per_token, output_cost_per_token = MODEL_CONFIG[model_name]['pricing']
    total_request_cost = in_tokens * input_cost_per_token + out_tokens * output_cost_per_token
    return total_request_cost

MODEL_CONFIG = {
    # pricing format is like this: (input_cost_per_token, output_cost_per_token),
    # OpenAI pricing:
    'gpt-4-1106-preview': {'max_tokens': 128000, 'pricing': (0.01 / 1000, 0.03 / 1000)},
    'gpt-4-1106-vision-preview': {'max_tokens': 128000, 'pricing': (0.01 / 1000, 0.03 / 1000)},
    'gpt-4': {'max_tokens': 8192, 'pricing': (0.03 / 1000, 0.06 / 1000)},
    'gpt-4-32k': {'max_tokens': 32768, 'pricing': (0.06 / 1000, 0.12 / 1000)},
    'gpt-3.5-turbo-1106': {'max_tokens': 16385, 'pricing': (0.0010 / 1000, 0.0020 / 1000)},
    # OpenAI other models:
    'text-davinci-003': {'max_tokens': 4097, 'pricing': (0.02 / 1000, 0.02 / 1000)},
    'text-embedding-ada-002': {'max_tokens': 4097, 'pricing': (0.0001 / 1000, 0 / 1000)},
    # OpenAI finetuned models
    # training is 0.008 / 1000 tokens as of 11-2023 but not accounted for here
    'ft:gpt-3.5-turbo': {'max_tokens': 4097, 'pricing': (0.0030 / 1000, 0.0060 / 1000)},
    # Anthropic pricing:
    'claude-2': {'max_tokens': 100000, 'pricing': (11.02 / 1000000, 32.68 / 1000000)},
    'claude-instant': {'max_tokens': 100000, 'pricing': (1.63 / 1000000, 5.51 / 1000000)},
}