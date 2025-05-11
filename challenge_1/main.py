from graph_config import graph


if __name__ == "__main__":
    initial_state = {
        "user_query": "What are the temperature limits mentioned?",
        "documents": [
            "docs/spec_sheet.pdf",
            "docs/parameters.csv",
            "docs/notes.docx",
            "docs/diagram.png",
            "docs/summary.txt"
        ]
    }

    result = graph.invoke(initial_state)
    print("Final Agent State:")
    print(result["reasoning"])

# if __name__ == "__main__":
#     initial_state = {
#         "user_query": "Can I use aluminum for this 80°C application?",
#         "documents": ["docs/spec_sheet.pdf"]
#     }

#     result = graph.invoke(initial_state)
#     print("Final Agent State:")
#     print(result)
