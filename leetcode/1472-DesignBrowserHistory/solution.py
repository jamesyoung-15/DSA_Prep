class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        site = ListNode(url)
        site.prev = self.root
        self.root.next = site
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps-=1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps-=1
        return self.root.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)