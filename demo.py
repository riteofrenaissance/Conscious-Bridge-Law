"""
demo.py
Conscious Bridge Transformer Demo
"""

from conscious_transformer import ConsciousBridgeTransformer

def demo_strong_context():
    print("\n" + "🔵"*30)
    print("DEMO 1: Strong English Context")
    print("🔵"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "Artificial intelligence is rapidly evolving in the field of natural language processing, with major applications in"
    
    output, phi, components = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=0.7,
        max_new_tokens=30,
        adaptive_temp=True,
        verbose=True
    )
    
    print("📝 Generated Text:")
    print(output)
    print("\n")

def demo_weak_context():
    print("\n" + "🔴"*30)
    print("DEMO 2: Weak/Mixed Context")
    print("🔴"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "Artificial intelligence AI is"
    
    output, phi, components = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=0.7,
        max_new_tokens=20,
        adaptive_temp=True,
        verbose=True
    )
    
    print("📝 Generated Text:")
    print(output)
    print("\n")

def demo_short_context():
    print("\n" + "🟡"*30)
    print("DEMO 3: Very Short Context")
    print("🟡"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "AI"
    
    output, phi, components = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=0.7,
        max_new_tokens=25,
        adaptive_temp=True,
        verbose=True
    )
    
    print("📝 Generated Text:")
    print(output)
    print("\n")

def demo_comparison():
    print("\n" + "🟢"*30)
    print("DEMO 4: Adaptive vs Non-Adaptive Temperature")
    print("🟢"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "Neural language programming is used in"
    
    print("--- WITH Adaptive Temperature ---")
    output1, phi1, _ = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=0.7,
        max_new_tokens=25,
        adaptive_temp=True,
        verbose=True
    )
    print(f"Output: {output1}\n")
    
    print("\n--- WITHOUT Adaptive Temperature ---")
    output2, phi2, _ = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=0.7,
        max_new_tokens=25,
        adaptive_temp=False,
        verbose=True
    )
    print(f"Output: {output2}\n")

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        🌉 CONSCIOUS BRIDGE TRANSFORMER DEMO 🌉           ║
    ║                                                           ║
    ║              Conscious Bridge Theory                       ║
    ║              Founder: Samir Baladi                        ║
    ║              Date: December 3, 2025                        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    demo_strong_context()
    demo_weak_context()
    demo_short_context()
    demo_comparison()
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    DEMO COMPLETED                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)