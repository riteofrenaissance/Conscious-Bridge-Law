"""
Arabic Context Demo for Conscious Bridge Law
Author: Samir Baladi
Date: December 2025
"""

from engine.conscious_law import ConsciousBridgeLaw


def run_demo():
    """Demo: Strong Arabic context with adaptive temperature."""
    print("\n" + "🔵" * 30)
    print("DEMO: Arabic Context")
    print("🔵" * 30 + "\n")

    model = ConsciousBridgeLaw()

    output, phi, components = model.generate_with_awareness(
        input_text="الذكاء الاصطناعي يتطور بسرعة كبيرة",
        base_temperature=0.7,
        max_new_tokens=30,
        adaptive_temp=True,
        verbose=True
    )

    print("📝 Generated Text:")
    print(output)
    print("\n")
    print(f"φ (Phi): {phi}")
    print(f"Components: {components}")
    print("\n")


if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                 ARABIC CONTEXT DEMO (CBL)                 ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    run_demo()

    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                        DEMO FINISHED                       ║
    ╚═══════════════════════════════════════════════════════════╝
    """)