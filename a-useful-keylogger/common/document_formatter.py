class Document_Formatter:
    def __init__(self, output_file="how-to.md"):
        self.output_file = output_file

    # takes a list of strings and writes them to a files
    # writes to a markdown file with the strings as a list
    # adds link to screenshot when none 

    def create_document(self, list_of_strings):

        screenshot_count = 0
        with open(self.output_file, "w") as f:

            f.write("# How to use the keylogger\n\n")
            f.write("## Steps to use the keylogger\n\n")

            for index, string in enumerate(list_of_strings):
                if string is None:
                    f.write(f"\n![screenshot_{screenshot_count}]({screenshot_count}.png)\n\n")
                    screenshot_count += 1
                else:
                    f.write(f"{index + 1}. {string}\n")
            
            f.write('\n')
