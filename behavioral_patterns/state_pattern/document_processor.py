class DocumentProcessor:

    def __init__(self):
        self._state = "init"

    def change_state(self, state: str):
        self._state = state
        self.process()

    def process(self):
        if self._state == "init":
            print("Starting document processing.")
        elif self._state == "uploading":
            print("Uploading document.")
        elif self._state == "completed":
            print("Document processing completed.")
        else:
            print("Unknown state.")

processor = DocumentProcessor()
processor.process()
processor.change_state("uploading")
processor.change_state("completed")
processor.change_state("invalid")