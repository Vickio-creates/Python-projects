results = []

while True:
    subject = input("\nEnter subject name (or 'quit' to finish): ")
    if subject.lower() == "quit":
        break

    score = float(input(f"Enter score for {subject}: "))
    results.append({"Subject": subject, "Score": score})
    print(f"{subject} added!")

print("\n=== STUDY RESULTS ===") 
for result in results:
    print(f"{result['Subject']}: {result['Score']}")

total_score = 0
for result in results:
    total_score += result['Score']

average = total_score / len(results)
print(f"\nAverage score: {average:.1f}%")

if average >= 90:
    print("Performance: 🌟 Excellent!")
elif average >= 60:
    print("Performance: ✅ Pass")
else:
    print("Performance: ❌ Fail - keep studying!")  