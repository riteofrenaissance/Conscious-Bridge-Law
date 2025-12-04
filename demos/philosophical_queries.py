"""
philosophical_queries.py
Demo: evaluate model on philosophical questions.
"""

from engine.conscious_transformer import ConsciousBridgeTransformer

def demo_philosophy(tokenizer=None):
    model = ConsciousBridgeTransformer()
    input_text = "What is consciousness in AI?"
    output, phi, components = model.generate_with_awareness(input_text, tokenizer)
    print("Output:", output)
    print("Phi:", phi)
    print("Components:", components)