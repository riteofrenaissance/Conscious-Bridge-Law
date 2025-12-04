"""
demo.py
تطبيق تجريبي لنظام الجسر الواعي
"""

from conscious_transformer import ConsciousBridgeTransformer

def demo_strong_context():
    """
    مثال 1: سياق عربي قوي (φ متوقع: ~0.8)
    """
    print("\n" + "🔵"*30)
    print("DEMO 1: Strong Arabic Context")
    print("🔵"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "الذكاء الاصطناعي يتطور بسرعة كبيرة في مجال معالجة اللغة الطبيعية، ومن أهم التطبيقات"
    
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
    """
    مثال 2: سياق ضعيف/مختلط (φ متوقع: ~0.3)
    """
    print("\n" + "🔴"*30)
    print("DEMO 2: Weak/Mixed Context")
    print("🔴"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    # سياق مختلط (عربي + إنجليزي)
    input_text = "الذكاء artificial intelligence هو"
    
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
    """
    مثال 3: سياق قصير جداً (φ_context منخفض)
    """
    print("\n" + "🟡"*30)
    print("DEMO 3: Very Short Context")
    print("🟡"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "الذكاء"
    
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
    """
    مثال 4: مقارنة adaptive vs. non-adaptive
    """
    print("\n" + "🟢"*30)
    print("DEMO 4: Adaptive vs Non-Adaptive Temperature")
    print("🟢"*30 + "\n")
    
    model = ConsciousBridgeTransformer()
    
    input_text = "البرمجة اللغوية العصبية تستخدم في"
    
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
    ║              نظرية الجسر الواعي                         ║
    ║           المؤسس: سمير بلدي                             ║
    ║           التاريخ: 3 ديسمبر 2025                        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # تشغيل الأمثلة
    demo_strong_context()
    demo_weak_context()
    demo_short_context()
    demo_comparison()
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    DEMO COMPLETED                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)