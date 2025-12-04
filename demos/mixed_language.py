"""
mixed_language.py
Demo: mixed Arabic-English context.
"""

from engine.conscious_transformer import ConsciousBridgeTransformer

def demo_mixed(tokenizer=None):
    model = ConsciousBridgeTransformer()
    input_text = "الذكاء artificial intelligence هو"
    output, phi, components = model.generate_with_awareness(input_text, tokenizer)
    print("Output:", output)
    print("Phi:", phi)
    print("Components:", components)