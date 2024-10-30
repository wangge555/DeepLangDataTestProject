import gradio as gr
import traceback
import re

def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("html parser"):
            raw_input = gr.Textbox(lines=1, placeholder="html", label="")
            pack_output = gr.Textbox(label="输出")

            btn = gr.Button("开始转换")
            btn.click(
                fn=extract_text,
                inputs=raw_input,
                outputs=pack_output,
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )

def extract_text(html):
    p_texts = re.findall("(?s)(?<=<p>).*?(?=</p>)", html)
    res = []
    for text in p_texts:
        text = re.sub("(?s)<.*?>.*?<.*?>", "", text)
        res.append(text.strip())
    return "\n".join(res)


if __name__ == "__main__":
    main()
#     html = """"<a>
#    111
#    <b>222</b>
#    <p>
#       333
#       <c>444</c>
#    </p>
#    <p>555</p>
# </a>"""
#     print(extract_text(html))
