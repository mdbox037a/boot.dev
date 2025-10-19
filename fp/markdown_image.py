def create_markdown_image(alt_text):
    enclosed_text = f"![{alt_text}]"

    def handle_url(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        formatted_text = f"{enclosed_text}({escaped_url})"

        def add_title(title=None):
            if title is not None:
                enclosed_title = f'"{title}"'
                with_title = f"{formatted_text.replace(')', '')} {enclosed_title})"
                return with_title
            return formatted_text

        return add_title

    return handle_url
