from direct.gui.DirectGui import DirectFrame, DirectLabel
from panda3d.core import TransparencyAttrib

class Inventory:
    def __init__(self, base, max_slots=10):
        self.base = base
        self.max_slots = max_slots
        self.items = []  # List to store items

        # Simple GUI frame for inventory display
        self.frame = DirectFrame(frameColor=(0, 0, 0, 0.6),
                                 frameSize=(-0.5, 0.5, -0.7, 0.7))
        self.frame.setTransparency(TransparencyAttrib.MAlpha)
        self.frame.setPos(0, 0, 0)
        self.frame.hide()

        # Label to display inventory items
        self.label = DirectLabel(text=self.get_inventory_text(),
                                 parent=self.frame,
                                 scale=0.05,
                                 pos=(-0.45, 0, 0.6),
                                 text_align=0)  # left-align

        # Toggle inventory display with 'i' key
        self.base.accept("i", self.toggle)

    def add_item(self, item_name):
        if len(self.items) < self.max_slots:
            self.items.append(item_name)
            self.update_display()
            print(f"Added {item_name} to inventory.")
        else:
            print("Inventory full!")

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            self.update_display()
            print(f"Removed {item_name} from inventory.")
        else:
            print(f"{item_name} not in inventory.")

    def get_inventory_text(self):
        if not self.items:
            return "Inventory is empty"
        text = "Inventory:\n"
        for i, item in enumerate(self.items, start=1):
            text += f"{i}. {item}\n"
        return text

    def update_display(self):
        self.label["text"] = self.get_inventory_text()

    def toggle(self):
        if self.frame.isHidden():
            self.frame.show()
        else:
            self.frame.hide()
