import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def run_agent(prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def main():
    print("AI Exhibition Design Agent")
    user_input = input("请输入设计需求：\n")

    brief = run_agent(load_prompt("prompts/brief_parser.txt"), user_input)
    concept = run_agent(load_prompt("prompts/concept_generator.txt"), brief)
    spatial = run_agent(load_prompt("prompts/spatial_planner.txt"), concept)
    render = run_agent(load_prompt("prompts/render_prompt.txt"), spatial)

    print("\n=== OUTPUT ===\n")
    print(concept)
    print(spatial)
    print(render)

if __name__ == "__main__":
    main()
