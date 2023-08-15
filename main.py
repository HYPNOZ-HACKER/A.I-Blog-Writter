import openai

# Set your OpenAI API key
openai.api_key = 'YOUR API KEY'

def generate_section_prompt(title, section_title, content_so_far):
    return f"Title: {title}\n\n{section_title}:\n{content_so_far}\n"

def generate_blog_content(title, sections, max_tokens=1000):
    prompt = f"Title: {title}\n\nIntroduction:\n"
    content = ""

    for section_title in sections:
        section_prompt = generate_section_prompt(title, section_title, content)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=section_prompt,
            max_tokens=max_tokens - len(content)
        )
        content += response.choices[0].text.strip() + "\n\n"

    return content

def main():
    title = input("Enter the blog title: ")
    num_sections = int(input("Enter the number of sections: "))
    sections = []
    for i in range(num_sections):
        section_title = input(f"Enter title for section {i + 1}: ")
        sections.append(section_title)

    content = generate_blog_content(title, sections, max_tokens=2000)

    print("\nGenerated Blog Content:\n")
    print(content)

if __name__ == "__main__":
    main()
