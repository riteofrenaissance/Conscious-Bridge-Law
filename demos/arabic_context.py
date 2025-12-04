"""
arabic_context.py
Demo: strong Arabic context.
"""

from engine.conscious_transformer import ConsciousBridgeTransformer

def demo_arabic(tokenizer=None):
    model = ConsciousBridgeTransformer()
    input_text = "الذكاء الاصطناعي يتطور بسرعة"
    output, phi, components = model.generate_with_awareness(input_text, tokenizer)
    print("Output:", output)
    print("Phi:", phi)
    print("Components:", components)