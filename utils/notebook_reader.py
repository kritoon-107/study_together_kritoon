import json
import streamlit as st


def display_notebook(file_path):
    """
    Read a .ipynb file and display its content
    without using nbformat or nbconvert.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            notebook = json.load(file)

        cells = notebook.get("cells", [])

        for cell in cells:

            cell_type = cell.get("cell_type")
            source = "".join(cell.get("source", []))

            # Markdown cells
            if cell_type == "markdown":
                st.markdown(source)

            # Code cells
            elif cell_type == "code":
                st.code(source, language="python")


    except FileNotFoundError:
        st.error("Notebook file not found.")

    except Exception as e:
        st.error(f"Error loading notebook: {e}")