import gradio as gr

try:
    from search import search_instagram_profiles 
except ImportError:
    def search_instagram_profiles(query, num_results=5):
        print("ERROR: Could not import 'search_instagram_profiles' from search.py. Is the file correct?")
        return []
    print("WARNING: 'search_instagram_profiles' function is a placeholder due to import error.")


def gradio_search_profiles(query: str):
   

    results = search_instagram_profiles(query, num_results=20)
    
    result_count = len(results)
    
    if not results:
        return (
            f"😔 **Search Complete:** Found {result_count} profiles.", 
            "No profiles found or search failed. Try another word!", 
            ""
        )
    
    output_text = f"✅ **Search Complete:** Found **{result_count}** Instagram Profiles for '{query}'! \n\n"
    output_links = []
    

    for i, res in enumerate(results):
        output_text += f"**{i+1}. {res['title']}**\n"
        
        output_text += f"   - [🔗 Profile Link]({res['url']})\n"
        
        output_text += "\n" 
        
        output_links.append(f"{res['title']}: {res['url']}")

    return (
        output_text, 
        "\n".join(output_links),
        f"Found {result_count} results." 
    )

custom_theme = gr.themes.Soft(
    primary_hue="pink",
    secondary_hue="purple",
    neutral_hue="gray",
)

def clear_fields():
    return "", "", ""


with gr.Blocks(theme=custom_theme, title="Instagram-Finder 💖") as demo:
    gr.Markdown("# 📸 Instagram-Finder Pro 💖")
    gr.Markdown("Type a name or topic below and let the Exa magic find the Instagram profile links!")

    with gr.Row():
        search_input = gr.Textbox(
            label="🔍 What are you looking for?", 
            placeholder="e.g., 'cat videos' or 'nasa official'", 
            lines=1,
            elem_id="search-input" 
        )
        
    with gr.Row():
        search_button = gr.Button("Find My Instagram! ✨", variant="primary")
        clear_button = gr.Button("Clear 🗑️", variant="secondary")
        
    with gr.Row():
        result_count_box = gr.Textbox(
            label="Result Count",
            value="Ready to search...",
            interactive=False,
            scale=1
        )
        
    output_text = gr.Markdown(label="Results Summary", elem_id="output-summary")

    link_list = gr.Textbox(
        label="Direct Links (URL: Title)", 
        lines=5, 
        interactive=False, 
        elem_id="link-list"
    )

    search_button.click(
        fn=gradio_search_profiles,
        inputs=[search_input],
        outputs=[output_text, link_list, result_count_box],
        api_name="search_profile" 
    )

    clear_button.click(
        fn=clear_fields,
        inputs=[],
        outputs=[search_input, output_text, link_list]
    )


if __name__ == '__main__':
    demo.launch()