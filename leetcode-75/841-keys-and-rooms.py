class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.keys = [False for _ in range(len(rooms))]
        self.keys[0] = True

        def visit(keys):
            for key in keys:
                if not self.keys[key]:
                    self.keys[key] = True
                    visit(rooms[key])

        visit(rooms[0])

        for i in self.keys:
            if not i:
                return False      
        return True
