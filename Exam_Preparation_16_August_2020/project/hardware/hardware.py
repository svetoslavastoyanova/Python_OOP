from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.total_capacity_used = capacity
        self.total_memory_used = memory

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        else:
            self.software_components.append(software)
            self.capacity -= software.capacity_consumption
            self.memory -= software.memory_consumption

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)




