class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.len = 1

    def visit(self, url: str) -> None:
        if self.curr == len(self.history)-1:
            self.history.append(url)
            self.curr += 1
            self.len += 1
        else:
            self.history = self.history[:self.curr+1]
            self.history.append(url)
            self.curr += 1
            self.len = self.curr+1

    def back(self, steps: int) -> str:
        if self.curr-steps >= 0:
            self.curr -= steps
        else:
            self.curr = 0
        return self.history[self.curr]


    def forward(self, steps: int) -> str:
        if self.curr+steps <= self.len-1:
            self.curr += steps
        else:
            self.curr = self.len-1
        return self.history[self.curr]