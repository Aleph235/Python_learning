def build_sandwich(*args):
    """Build a sandwich and sammarize the shosen ingredients"""
    print("We are making a sandwich with the following ingredients")
    for arg in args:
        print(f"-{arg}")
        
The_tunisian = build_sandwich('merguez', 'harissa', 'mechweya')
The_scandinavian = build_sandwich('salmon', 'mayonaise', 'salad')
