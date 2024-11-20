from abc import ABC, abstractmethod

class FileSystemComponent(ABC):

    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemComponent):

    def __init__(self, name:str, size: int):
        self.name = name
        self.size = size

    def show_details(self):
        print(f"File: {self.name}, Size: {self.size}")

    def get_size(self) -> int:
        return self.size


class Directory(FileSystemComponent):

    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.cached_size = None # with caching

    def add(self, component: FileSystemComponent):
        self.children.append(component)
        self.cached_size = None

    def show_details(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_details()

    def get_size(self) -> int:
        if self.cached_size is None:
            total_size = sum(child.get_size() for child in self.children)
            self.cached_size = total_size
        return self.cached_size


# Create individual files
file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)
file3 = File("file3.txt", 300)

# Create directories
dir1 = Directory("Documents")
dir2 = Directory("Pictures")

# Add files to directories
dir1.add(file1)
dir1.add(file2)
dir2.add(file3)

# Create a subdirectory and add it to a directory
subdir = Directory("Subfolder")
subdir.add(file2)
dir2.add(subdir)

# Show details of the directories (and their files)
print("Directory 1 Details:")
dir1.show_details()  # Should show files file1.txt and file2.txt

print("\nDirectory 2 Details:")
dir2.show_details()  # Should show file3.txt and subfolder (file2.txt)

# Get and print size of directories
print("\nSize of Directory 1:", dir1.get_size())  # Should calculate size of file1 + file2
print("Size of Directory 2:", dir2.get_size())  # Should calculate size of file3 + subfolder (file2)
