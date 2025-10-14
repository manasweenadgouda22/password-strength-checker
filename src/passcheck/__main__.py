import argparse, json
from .score import evaluate_password

def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker")
    parser.add_argument("password", help="Password to evaluate (avoid real credentials!)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    result = evaluate_password(args.password)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Strength: {result['strength']} (score={result['score']})")
        print(f"Entropy (adjusted): {result['entropy_bits_adjusted']:.2f} bits")
        print("Feedback:")
        for f in result["feedback"]:
            print(f" - {f}")

if __name__ == "__main__":
    main()
