from package_sorter import sort

def main():
    """
    Example usage of the package sorting function.
    """
    print("Package Sorting System - Thoughtful Robotic Automation Factory")
    print("=" * 60)
    
    test_packages = [
        (50, 50, 50, 10, "Standard package"),
        (100, 100, 100, 15, "Bulky by volume"),
        (150, 50, 50, 10, "Bulky by dimension"),
        (50, 50, 50, 20, "Heavy package"),
        (100, 100, 100, 20, "Both bulky and heavy"),
        (200, 200, 200, 50, "Very bulky and very heavy"),
    ]
    
    for width, height, length, mass, description in test_packages:
        stack = sort(width, height, length, mass)
        volume = width * height * length
        print(f"\n{description}:")
        print(f"  Dimensions: {width}x{height}x{length} cm (Volume: {volume:,} cm³)")
        print(f"  Mass: {mass} kg")
        print(f"  → Dispatch to: {stack}")

if __name__ == '__main__':
    main()
