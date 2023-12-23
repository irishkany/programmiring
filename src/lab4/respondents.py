from typing import List

class Respondent:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class AgeGroup:
    def __init__(self, lower_bound: int, upper_bound: int) -> None:
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents: List[Respondent] = []

    def add_respondent(self, respondent: Respondent) -> None:
        self.respondents.append(respondent)

    def __repr__(self) -> str:
        sorted_respondents = sorted(self.respondents, key=lambda x: (x.age, x.name))
        return f"{self.lower_bound}{'+' if self.upper_bound == float('inf') else f'-{self.upper_bound}'}: " + ", ".join(
            [f"{respondent.name} ({respondent.age})" for respondent in sorted_respondents]
        )




def main() -> None:
    try:
        group_boundaries = list(map(int, input().split()))
        divider = AgeGroupDivider(group_boundaries)

        while True:
            input_data = input().strip()
            if input_data == "END":
                break

            name, age = input_data.split(",")
            age = int(age)

            if age < 0 or age > 123:
                print("Error: Invalid age.")
                continue

            respondent = Respondent(name, age)
            divider.add_respondent(respondent)

        print(divider)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
